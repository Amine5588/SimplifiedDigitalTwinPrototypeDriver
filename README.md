# OVERVIEW 
Welcome to the Simplified Digital Twin Prototype for a Driver repository! This project develops a simplified digital twin prototype of a driver integrated with a vehicle model, leveraging control techniques, fuzzy logic, and hybrid AI in MATLAB, SIMULINK, and Python. The prototype simulates and visualizes a driver’s behavior in a self-driving car environment, focusing on decision-making for speed, direction, and navigation under various environmental conditions such as road slope, wind, traffic lights, and distances.

The project is hosted on the feature/driver-fuzzy-model branch, which includes advanced implementations of fuzzy logic to model driver decision-making, enabling the digital twin to autonomously adjust vehicle parameters (e.g., speed) based on real-time conditions. This repository builds on the original SelfDrivingCar project by Mohamed Dhameem, extending it with a driver model tailored for educational and research purposes.
## Self Driving Car - Fuzzy Logic

Fuzzy implementation of self driving car. The project is created with pygame, which have the capability to react to road situations and adjust its speed accordingly. The road situation can be implemented real time i.e put a rock in the middle of the game when the car is driving to test if the car stops.

### Prerequisites

Create python virtual environment. Download this github repository.

From the terminal run below command

```
pip install -r requirements.txt

(tested with Python version 3.7.2 )
```
### Demo

![Self driving car demo](https://github.com/mohameddhameem/SelfDrivingCar/blob/master/media/Self%20Driving%20Car%20Demo.gif)

## Run this project

- Run file **run.py** in package **main**

- Membership function values can be updated in the rule/fuzzy_rule.xlsx file. 

- Update other values with in the fuzzification/fuzzy_dependency.py for further customization

## Creators
Please check contributors section.



## Original Code
We have used original code from https://github.com/HoangNguyenHuu/fuzzy-logic-project
