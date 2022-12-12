# PO_PWR
Project is created within the Object-oriented Programming subject at [Wrocław University of Science and Technology](https://pwr.edu.pl/).
We are using Python 3.10, PyQt6 GUI library.
## Contributors:
- *Back-end Szymon Gruszecki [Simon2833](https://github.com/Simon2833)*
- *Front-endOlaf Lesiuk [olafles](https://github.com/olafles)*
- *Documentation Jakub Kęsik [Kubagf](https://github.com/Kubagf)*
## Tribes
---
### Description:
Simulation is based on behavior of people uniting into tribes. Main goal of each team basically is to survive among others.
### Basic informations:
- Quantity:
     - Amount of tribes is defined by user (cannot enter number lesser than 2).
- Map:
    - Size is defined by user (minimum dimensions are 10x10).
- Population:
    - At the begining it is defined by user. In the later stages of simulation tribe can expand or shrink based on morale and war system.
- Units:
    - Warrior - low range, moderate attack power, high defence,
    - Spearman - medium range, high attack power, medium defence,
    - Archer - high range, low attack power, low defence,
- Enviroment:
    - Monsters - they are randomly generated on the map, all stats are high except range. Basically they are hard to kill, but worth it,
    - Resources - it is randomly generated on the map, it is needed for villages to survive,
    - Village base - main structure of tribe, if it is destroyed the tribe will collapse.
### Mechanics:
- War - starts when one unit is killed by other tribe, it is lasts till one of the village base will be destroyed or global peace event occurs.
- Alliance - there is a minor chance that two passive tribes will be merged into one bigger tribe,
- Morale - it slightly decrases over time, it depends on lost units, collected food and killed monters. Dropping below 0 will cause tribe to lose one unit, if morale hit 100 tribe will gain one unit; ine every situation morale goes back to 50.
### Simulation run example:
![simulation](/documentation/simulation.gif)

##### *We reserve the right to make changes in the project.*
