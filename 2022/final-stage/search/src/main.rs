use std::collections::HashMap;
use rayon::prelude::*;
use serde::{Serialize, Deserialize};

fn main() -> anyhow::Result<()> {
    // read mountain coordinates
    let mountains = {
        const RAW: &str = include_str!("../../mountains.json");
        serde_json::from_str::<Vec<Mountain>>(RAW)?
    };
    let cost_matrix = cost(&mountains);
    
    let (cost, path) = shortest(&cost_matrix, &mut vec![(19, 18)]);
    display(&path, cost);

    Ok(())
}

fn shortest(costs: &CostMatrix, stack: &mut Vec<Coordinate>) -> (f64, Vec<Coordinate>) {
    let current = stack.last().unwrap();
    let follow = costs.possible_next(&current, &stack);

    // base case
    if follow.len() == 0 {
        // incomplete
        if stack.len() != costs.coordinates().len() {
            return (f64::INFINITY, stack.to_vec())
        }

        // measure
        let mut total = 0.0;
        for i in 0..stack.len()-1 {
            total += costs.cost(&stack[i], &stack[i+1]);
        }
        return (total, stack.to_vec());
    }

    let (mut s_cost, mut s_path) = (f64::INFINITY, Vec::default());
    for next in follow {
        stack.push(next);

        let (cost, path) = shortest(costs, stack);
        if cost < s_cost {
            s_cost = cost;
            s_path = path;
        }

        stack.pop();
    }
    display(&s_path, s_cost);

    (s_cost, s_path)
}

#[derive(Debug, Serialize, Deserialize)]
struct Mountain {
    a: usize,
    b: usize,
    c: usize,
}

type Coordinate = (usize, usize);

impl Mountain {
    fn coords(&self) -> Coordinate {
        (self.a, self.b)
    }

    fn real_coords(&self) -> (f64, f64) {
        (self.a as f64 * 1000.0, self.b as f64 * 1000.0)
    }

    fn height(&self) -> f64 {
        self.c as f64 * 187.5 // 0.1875 * 1000.0
    }

    fn radius(&self) -> f64 {
        self.height() / 0.6
    }

    fn distance_from(&self, x: f64, y: f64) -> f64 {
        let real = self.real_coords();
        (
            (real.0 - x).powi(2) +
            (real.1 - y).powi(2)
        ).sqrt()
    }

    fn distance_to(&self, other: &Self) -> f64 {
        let loc = other.real_coords();
        self.distance_from(loc.0, loc.1)
    }

    const UPHILL_SPEED: f64 = 0.8;
    const FLAT_SPEED: f64 = 2.0;
    const DOWNHILL_SPEED: f64 = 3.2;

    fn time_to(&self, other: &Self) -> f64 {
        let (r1, r2) = (self.radius(), other.radius());
        let flat = self.distance_to(other) - r1 - r2;

        if flat >= 0.0 {
            // time
            r1/Self::DOWNHILL_SPEED +
            flat/Self::FLAT_SPEED +
            r2/Self::UPHILL_SPEED

        } else {
            // overlap
            return f64::INFINITY;
        }
    }
}

type CostMatrix = HashMap<usize, HashMap<usize, HashMap<usize, HashMap<usize, f64>>>>;

fn cost(mountains: &Vec<Mountain>) -> CostMatrix {
    let mut cost_matrix: CostMatrix = HashMap::with_capacity(mountains.len());
    
    for m1 in mountains {
        let c1 = m1.coords();

        for m2 in mountains {
            let c2 = m2.coords();

            cost_matrix
                .entry(c1.0).or_default()
                .entry(c1.1).or_default()
                .entry(c2.0).or_default()
                .insert(c2.1, m1.time_to(&m2));
        }
    }

    cost_matrix
}

type PrioQueue<T> = Vec<(T, )>

trait Possibilities {
    fn possible_next(&self, current: &Coordinate, exclude: &Vec<Coordinate>) -> Vec<Coordinate>;
    fn coordinates(&self) -> Vec<Coordinate>;
    fn cost(&self, a: &Coordinate, b: &Coordinate) -> f64;
}
impl Possibilities for CostMatrix {
    fn possible_next(&self, current: &Coordinate, exclude: &Vec<Coordinate>) -> Vec<Coordinate> {
        let mut raw = self[&current.0][&current.1].par_iter()
            
            // get coordinates
            .flat_map(|(x, ys)| {
                ys.par_iter()
                    .map(|(y, cost)| ((*x, *y), *cost))
            })
            // unvisited
            .filter(|((x, y), _)| !exclude.contains(&(*x, *y)))
            
            // possible routes
            .filter(|(_, cost)| cost.is_finite())

            // sort for min cost
            .collect::<Vec<(Coordinate, f64)>>();
        raw.par_sort_by(|(_, c1), (_, c2)| c1.partial_cmp(c2).unwrap());
        
        // filter coords only
        raw.par_iter()
            .map(|(coord, _)| *coord)
            .collect()
    }

    fn coordinates(&self) -> Vec<Coordinate> {
        self.par_iter()
            .flat_map(|(x, ys)| {
                ys.par_iter()
                    .map(|(y, _)| (*x, *y))
            })
            .collect()
    }

    fn cost(&self, a: &Coordinate, b: &Coordinate) -> f64 {
        self[&a.0][&a.1][&b.0][&b.1]
    }
}

fn display(path: &Vec<Coordinate>, cost: f64) {
    if cost.is_finite() {
        for (x, y) in path {
            println!("{x}, {y}");
        }
        println!("{cost}");
    }
}