# Sugarscape Simulation with Clustering Dynamics

This project implements a **Sugarscape** model, simulating agent movements and resource dynamics on a grid-based environment. Agents navigate the grid based on sugar levels, forming clusters around resource-rich areas. The simulation tracks clustering behavior over time.

---

## Features

### Sugarscape Environment
- **Grid**:
  - A `20x20` grid initialized with random sugar levels (`1–3`).
  - Hotspots of high sugar values (`10`) are created in random `3x3` areas to simulate resource concentration.
- **Agents**:
  - Agents are randomly initialized on the grid.
  - Agents move based on sugar levels, prioritizing high-sugar cells with some randomness.
- **Sugar Dynamics**:
  - Sugar levels gradually decrease over time, simulating resource consumption.
  - Regeneration dynamics can be added to replenish sugar levels.

### Agent Behavior
- **Movement**:
  - Agents can move to adjacent cells (up, down, left, right, or stay in place).
  - Movement prioritizes cells with higher sugar levels but includes randomness to prevent deterministic behavior.
- **Clustering**:
  - The simulation calculates a **clustering index** by evaluating agent density in local `3x3` neighborhoods.
  - Clustering occurs when more than 4 agents occupy overlapping neighborhoods.

---

## Simulation Workflow

1. **Initialization**:
   - The grid is populated with sugar values and hotspots.
   - Agents are randomly placed on the grid.
2. **Iterations**:
   - Agents move based on sugar levels.
   - Sugar levels on the grid decrease gradually.
   - Clustering index (density) is calculated for each iteration.
3. **Output**:
   - Tracks clustering behavior over 1,000 iterations.
   - Plots the clustering index over time.

---

## Code Structure

### Key Functions
- **Grid Initialization**:
  - Sets up the grid with base sugar levels and high-sugar hotspots.
- **Agent Movement**:
  - Moves agents based on sugar levels in adjacent cells.
  - Includes randomness to diversify agent behavior.
- **Grid Update**:
  - Gradually decreases sugar levels after each iteration.
- **Clustering Calculation**:
  - Evaluates clustering by counting agents in `3x3` neighborhoods.

### Main Class
- **`Sugarscape`**:
  - Manages the grid, agents, and simulation process.
  - Methods:
    - `move_agents`: Updates agent positions.
    - `update_grid`: Simulates sugar decay.
    - `calculate_density`: Calculates clustering index.
    - `run`: Runs the simulation and collects density data.

---

## How to Run

### Prerequisites
- Python 3.7 or higher.
- Required libraries:
  ```bash
  pip install matplotlib numpy
