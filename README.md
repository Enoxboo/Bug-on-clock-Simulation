![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Random Walk Clock Simulation

Small Monte Carlo experiment around a probability puzzle I saw online.
Started as a “this can’t be right” moment, ended up as code + math.

## How this started

I stumbled across a probability puzzle on Instagram:

> A ladybug starts at 12 on a clock.  
> At each step, it moves either clockwise or counter-clockwise with probability 1/2.  
> The walk continues until every other position has been visited at least once.  
> What’s the probability that position 6 is the last one visited?

The comments were full of confident answers.  
Most people said **50%** (because 6 is opposite to 12, so… symmetry, right?).

It sounded intuitive — and that’s exactly why I didn’t trust it.

I couldn’t prove anything on the spot, so I did what I usually do when intuition feels shaky:  
**I coded a simulation to see what actually happens.**

## The problem (clean version)

- Start at position 12 on a circular clock
- Each step: move ±1 with equal probability
- Positions wrap around (1 ↔ 12)
- Stop once all positions from 1 to 11 have been visited
- Record which position was visited last

Repeat this many times and look at the distribution.

## Simulation approach

No fancy math at first, just brute force:

1. Run the random walk
2. Track visited positions
3. Stop when all 11 are visited
4. Record the last one
5. Repeat a *lot*

Monte Carlo isn’t elegant, but it’s honest.

After **1,000,000 trials**, here’s what I got:

```
=== Results after 1000000 trials ===
Position  1:   9.11%
Position  2:   9.07%
Position  3:   9.07%
Position  4:   9.07%
Position  5:   9.14%
Position  6:   9.09%
Position  7:   9.12%
Position  8:   9.09%
Position  9:   9.12%
Position 10:   9.06%
Position 11:   9.07%
```

So… yeah.

**Every position has the same probability.**  
≈ **1 / 11 ≃ 9.09%**

Not 50%. Not “more likely because it’s opposite”. Just uniform.

## Why this actually makes sense

Once you step back, the result isn’t that crazy.

- The clock is perfectly symmetric
- The random walk has no bias
- There is no special position among {1,…,11}
- Starting point aside, nothing breaks rotational symmetry

Formally:
- Let P(k) be the probability that position k is visited last
- By symmetry: P(1) = P(2) = … = P(11)
- They sum to 1
- Therefore: **P(k) = 1 / 11**

The simulation just confirmed what symmetry already forces.

## How to run

```bash
# Clone the repository
git clone https://github.com/Enoxboo/bug-on-clock-simulation.git
cd bug-on-clock-simulation

# Run the simulation
python main.py
````
Requirements: Python 3.7+

## Code structure

```
bug-on-clock-simulation/
├── main.py
├── moving_bug.py
├── run_game.py
└── README.md
```


- `moving_bug.py`: handles the ladybug movement and circular wrapping
- `run_game.py`: runs trials and collects statistics
- `main.py`: entry point

Everything uses only the Python standard library.

## A fun (and painful) bug

At first, my results were *not* uniform at all.

Some positions looked clearly favored.  
I even started trying to explain it mathematically.

Turns out I had forgotten to reset the bug’s position to 12 between trials.

One missing line:
```python
bug.position = 12
```

And suddenly all my “interesting results” disappeared.

Good reminder that:

> If your data looks clever, double-check your code before inventing theory.

## What I got out of this
- Intuition is unreliable in probability
- Symmetry arguments are extremely powerful
- Monte Carlo simulations are great sanity checks
- Bugs can generate very convincing lies
- Writing things down forces real understanding

Also: a random Instagram reel can absolutely turn into a legitimate learning moment.

## Related concepts
- Random walks on graphs (cycle graph C₁₂)
- Markov chains
- Symmetry and invariance
- Coupon collector-like stopping conditions

## Author
Built out of curiosity (and mild annoyance) by a computer science student who doesn’t like accepting answers without checking.

## License

MIT License - feel free to use and adapt this code.