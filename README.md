# Blackjack
CSCI 154 Simulation - Project
# Blackjack Monte Carlo Simulation

A Python-based Monte Carlo simulation of Blackjack to evaluate different player strategies and the impact of table composition in single-player and multiplayer environments.

## Project Overview

This project simulates millions of hands of Blackjack to:
- Compare 5 different player policies/strategies
- Measure win rates, loss rates, draw rates, and Expected Value (EV)
- Analyze how the skill level of other players at the table affects performance
- Compare results between **Infinite Deck** and **Single Deck** games

## Features

- **Single Player Mode**: Test 5 different policies
- **Multiplayer Mode**: Up to 5 players at one table
- **Deck Types**: Infinite Deck and Single Deck support
- **High-Performance Simulations**: Tested with **1,000,000+ hands** per scenario
- **Clean Object-Oriented Design**: `Hand`, `Deck`, `BlackjackGame` classes

## 📊 Results Summary (1M+ Simulations)

### Best Strategy
**Policy 5 (Dealer-Aware)** performed the best:

| Deck Type     | Win Rate | Expected Value |
|---------------|----------|----------------|
| Infinite      | 43.03%   | **-0.0462**    |
| Single        | 43.26%   | **-0.0437**    |

### Multiplayer Results (Using Policy 5)

- **Bad Table** (4 weak players): Very similar performance to single player
- **Good Table** (4 optimal players): Minimal difference observed
- Table composition had **very little impact** on optimal play

**Conclusion**: Other players’ strategies have only a marginal effect when you use a strong strategy.

## Technologies Used

- Python 3
- Object-Oriented Programming
- Monte Carlo Simulation
- Data Analysis & Visualization ready

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/jetzordaz/Blackjack.git
   cd Blackjack
