# PO_PWR
Project is created within the Object-oriented Programming subject at [Wrocław University of Science and Technology](https://pwr.edu.pl/). We are using Python programing language and PyQ6 GUI library.
## Contributors:
- *Szymon Gruszecki [Simon2833](https://github.com/Simon2833)*
- *Olaf Lesiuk [olafles](https://github.com/olafles)*
- *Jakub Kęsik [Kubagf](https://github.com/Kubagf)*
## Tribes
---
### Description:
Simulation is based on behavior of people uniting into tribes. Main goal of each team basically is to survive among others.
### Basic informations:
- Quantity:
     - Amount is defined by user (cannot enter number lesser than 2).
- Map:
    - Size is defined by user (minimum dimensions are 10x10).
- Population:
    - At the begining it is defined by user. In the later stages of simulation tribe can expand or shrink based on collected food and killed villagers / soldiers.
- Units:
    - Warrior - low range, moderate attack power, high defence,
    - Spearman - medium range, high attack power, medium defence,
    - Archer - high range, low attack power, low defence,
    - Villager - all stats are low, unit is basically passive.
- Enviroment:
    - Monsters - they are randomly generated on the map, all stats are high except range. Basically they are hard to kill, but worth it,
    - Resources - it is randomly generated on the map, used to expand tribe,
    - Village base - main structure of tribe, if it is destroyed the tribe will fall.
### Mechanics:
- War - starts when one unit is killed by other tribe and it is going to last till one of the village base will be destroyed.
- Aliance - there is minor chance that two tribes will be united. We still consider implementating this mechanic.
- Morale - depends on the number of villagers and soldiers (garhering new units makes morale higher while killing units lowers it).
### Graphical view on project:
![Project scheme](/Schematic.png)
## Plague
---
### Description:
Simulation shows how plague spread over time and humans struggling to survive. Main goal of virus is to kill all humans before it gets fully cured.
### Basic informations:
- World population - starting value is defined by user, decrease over time (depending on lethality virus kills humans).
- Map size - defined by user, minimum dimensions are 10x10.
- Infectivity - starting value defined by user, can increase or decrease over time. Affects infection rate.
- Severity - starting value defined by user, can increase or decrease over time. Affects  rate.
- Lethality - starting value defined by user, can increase or decrease over time. Affects death rate.
### Mechanics:
- Evolution - the plague have minor chance to improve infectivity, severity and lethality.
- Cure - progressing over time remedy to the desease. When it hit 100% the plague is cured and no new cases is possible.
##### *We reserve the right to make changes to the implemented features.*