# OVERVIEW 
Welcome to the Simplified Digital Twin Prototype for a Driver repository! This project develops a simplified digital twin prototype of a driver integrated with a vehicle model, leveraging control techniques, fuzzy logic, and hybrid AI in MATLAB, SIMULINK, and Python. The prototype simulates and visualizes a driver’s behavior in a self-driving car environment, focusing on decision-making for speed, direction, and navigation under various environmental conditions such as road slope, wind, traffic lights, and distances.

The project is hosted on the feature/driver-fuzzy-model branch, which includes advanced implementations of fuzzy logic to model driver decision-making, enabling the digital twin to autonomously adjust vehicle parameters (e.g., speed) based on real-time conditions. This repository builds on the original SelfDrivingCar project by Amine Karoui, extending it with a driver model tailored for educational and research purposes.
## Self Driving Car - Fuzzy Logic

Fuzzy implementation of self driving car. The project is created with pygame, which have the capability to react to road situations and adjust its speed accordingly. The road situation can be implemented real time i.e put a rock in the middle of the game when the car is driving to test if the car stops.

--> Use of Fuzzy Logic for the Driver Model
The driver model in this project employs fuzzy logic to simulate human-like decision-making for controlling the vehicle. Fuzzy logic allows the driver digital twin to handle imprecise or uncertain inputs (e.g., “near” distance, “medium” angle, “green” traffic light) and produce smooth, intuitive outputs (e.g., “stop,” “slow,” “faster”) for vehicle speed and navigation.

### Prerequisites

Create python virtual environment. Download this github repository.

From the terminal run below command

```
pip install -r requirements.txt

(tested with Python version 3.7.2 )
```
### Demo

![Self driving car demo](https://github.com/Amine5588/SimplifiedDigitalTwinPrototypeDriver/blob/feature/driver-fuzzy-model/media/Self%20Driving%20Car%20Demo.gif)

## Run this project
- after cloning, you need to build darkflow manually, this is main repo ( as is no longer pypi included) ![DarkFlow Repo](https://github.com/thtrieu/darkflow)

- Run file **run.py** in package **main**
This launches the self-driving car simulation with the fuzzy logic driver model, displaying a graphical interface using Pygame and simulating driver decisions based on the fuzzy rules.
- Ensenbmle of Rules can be modified inside rule/fuzzy_rule.xlsx file. 

- Play with values in the fuzzification/fuzzy_dependency.py for further customization

### License
This project is licensed under the MIT License - see the LICENSE file for details (if applicable; update or add a LICENSE file if needed).
