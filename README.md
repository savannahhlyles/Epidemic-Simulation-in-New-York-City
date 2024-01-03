# Epidemic Simulation in NYC Using Cellular Automaton Infection Model

This Python project simulates the spread of infection in a 2D grid using a cellular automaton model. The simulation consists of cells that can be in one of three states: Susceptible (S), Infected (I), or Resistant (R). The simulation progresses through discrete time steps, with cells interacting with their neighboring cells.

## Features
- **Cell States**: Cells can be susceptible, infected, or resistant.
- **Infection Spread**: Infected cells can spread the infection to neighboring susceptible cells based on a virality parameter.
- **Recovery and Death**: Infected cells have a recovery time after which they become susceptible again. There's also a probability of death for infected cells.
- **Map Visualization**: The current state of the simulation is visualized on a 2D grid.

## Code Structure

### `simulator.py`
This file contains the core logic of the cellular automaton model. It defines the `Cell` and `Map` classes, as well as functions for displaying and processing the simulation.

### Functions
- `normpdf(x, mean, sd)`: Returns the value of the normal distribution with the specified mean and standard deviation at position x.
- `pdeath(x, mean, sd)`: Calculates the probability of cell death based on a normal distribution.
- `Cell`: Class representing individual cells with methods for infection and state transition.
- `Map`: Class representing the 2D grid of cells with methods for adding cells, displaying the map, finding adjacent cells, and progressing the simulation.
- `read_map(filename)`: Reads coordinates from a file, creates Cell instances, and returns a Map instance.

## Usage
1. Import the `simulator.py` module.
2. Create a `Map` instance and add cells to it.
3. Use the `time_step` method to advance the simulation.
4. Visualize the current state using the `display` method.

```python
# Example Usage
from simulator import Map, Cell, read_map

# Create a map
nyc_map = Map()

# Add cells to the map
cell1 = Cell(10, 20)
cell2 = Cell(15, 25)
nyc_map.add_cell(cell1)
nyc_map.add_cell(cell2)

# Progress the simulation and display the map
nyc_map.time_step()
```

## Dependencies
- `random`: For generating random numbers.
- `math`: For mathematical functions.
- `matplotlib`: For visualizing the simulation.
- `numpy`: For numerical operations.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
