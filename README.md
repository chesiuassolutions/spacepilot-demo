# SpacePilot Simulator DEMO

## Overview
**SpacePilot** is the onboard controller for spacecraft. It leverages legacy algorithms that have been successfully operating in space, combined with AI-driven enhancements. This repository provides a simulator that integrates **Space Pilot**, allowing users to fly a virtual spacecraft, visualize sensor readings, and interact with actuators.

Space Pilot is designed for ARM processors, but in this repository, you can run the entire simulation on Linux.

NOTE: This is a demo version with limited capabilities!! Contact us to receive the full version.

## Repository Structure
```
space_pilot_simulator/
│── bin/                # Binaries and executable files
│   ├── space_pilot_simulator  # Executable for Linux x86_64
│   ├── space_pilot_simulator_arm  # Executable for Linux ARM
│── config/             # Configuration files
│   ├── sc_configs.json 
│   ├── actuators_configs.json 
│   ├── sc_commands.json 
│   ├── sensors_configs.json 
│   ├── sim_config.json 
│── docs/               # Documentation
│── scripts/            # Helper scripts (e.g., data_plot.py)
│── data/               # Logs and sample mission scenarios
│── tests/              # Test cases for validation
```

## Installation
Clone the repository:
```sh
git clone https://github.com/chesiuassolutions/spacepilot-demo.git
cd spacepilot-demo
```

## Running the Simulator
To run the simulator with default configurations in Linux x86_64:
```sh
./bin/space_pilot_simulator 
```

To run the simulator with default configurations on the ARM board:
```sh
./bin/space_pilot_simulator_arm
```
## Configuration
Modify the configuration files in the `config/` directory to adjust simulation parameters.
- `sc_config.json`: Defines spacecraft properties
- `actuators_config.json`: Actuators configuration parameters
- `sc_commands.json`:  Commands sent to the spacecrft during the simulation
- `sensors_configs.json`: Sensors configuration parameters
- `sim_config.json`: Simulation parameters

## Logging & Output
Simulation output is stored in the `data/` directory. Logs can be found in:
```sh
data/logs/simulation.log
```
The `data/` directory also contains the following files:
- `sc-attitude.a`: Can be used inside STK to visualize the attitude of the spacecraft during the simulation.
- `sc-orbit.e`: Can be used inside STK to visualize the orbit of the satellite.
- `sim_out.csv`: Contains parameters that can be used to display the data with the provided Python script.

## Visualizing Data with Python
To visualize the attitude and actuators' information during maneuvers, you can use the provided Python script:
```sh
python3 ./scripts/data_plot.py
```
This script will generate plots based on the `sim_out.csv` file, providing insights into spacecraft attitude dynamics and actuator performance.


## License
This DEMO is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
If you are interested in testing **Space Pilot**, contact **info@chesiuassol.com**.
