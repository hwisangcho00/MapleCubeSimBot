
import random

# 0 index: glowing cube
# 1 index: bright cube

# first, second, third lines for outer index
legendary_weapon_120_200 = [
    {
        "STR : +12%" : [9.7562, 9.7562],
        "DEX : +12%" : [9.7562, 9.7562],
        "INT : +12%" : [9.7562, 9.7562],
        "LUK : +12%" : [9.7562, 9.7562],
        "ATT : +12%" : [4.8780, 4.8780],
        "Magic ATT : +12%" : [4.8780, 4.8780],
        "Critical Rate : +12%" : [4.8780, 4.8780],
        "Damage : +12%" : [4.8780, 4.8780],
        "All stats: +9%" : [7.3171, 7.3171],
        "ATT : +32" : [4.8780, 4.8780],
        "Magic ATT : +32" : [4.8780, 4.8780],
        "Boss Monster Damage : +35%" : [9.7561, 9.7561],
        "Boss Monster Damage : +40%" : [4.8780, 4.8780],
        "Ignore Monster DEF : +35%" : [4.8780, 4.8780],
        "Ignore Monster DEF : +40%" : [4.8780, 4.8780]
        
    },
    {
        "STR : +9%" : [10.4651, 9.3023],
        "DEX : +9%" : [10.4651, 9.3023],
        "INT : +9%" : [10.4651, 9.3023],
        "LUK : +9%" : [10.4651, 9.3023],
        "ATT : +9%" : [6.2791, 5.5814],
        "Magic ATT : +9%" : [6.2791, 5.5814],
        "Critical Rate : +9%" : [8.3721, 7.4419],
        "Damage : +9%" : [6.2791, 5.5814],
        "All stats: +6%" : [8.3721, 7.4419],
        "Boss Monster Damage : +30%" : [6.2791, 5.5814],
        "Ignore Monster DEF : +30%" : [6.2791, 5.5814],
        "STR : +12%" : [0.9756, 1.9512],
        "DEX : +12%" : [0.9756, 1.9512],
        "INT : +12%" : [0.9756, 1.9512],
        "LUK : +12%" : [0.9756, 1.9512],
        "ATT : +12%" : [0.4878, 0.9756],
        "Magic ATT : +12%" : [0.4878, 0.9756],
        "Critical Rate : +12%" : [0.4878, 0.9756],
        "Damage : +12%" : [0.4878, 0.9756],
        "All stats: +9%" : [0.7317, 1.4634],
        "ATT : +32" : [0.4878, 0.9756],
        "Magic ATT : +32" : [0.4878, 0.9756],
        "Boss Monster Damage : +35%" : [0.4878, 0.9756],
        "Boss Monster Damage : +40%" : [0.4878, 0.9756],
        "Ignore Monster DEF : +35%" : [0.9756, 1.9512],
        "Ignore Monster DEF : +40%" : [0.4878, 0.9756]
    },
    {

        "STR : +9%" : [11.5116, 11.0465],
        "DEX : +9%" : [11.5116, 11.0465],
        "INT : +9%" : [11.5116, 11.0465],
        "LUK : +9%" : [11.5116, 11.0465],
        "ATT : +9%" : [6.9070, 6.6279],
        "Magic ATT : +9%" : [6.9070, 6.6279],
        "Critical Rate : +9%" : [9.2093, 8.8372],
        "Damage : +9%" : [6.9070, 6.6279],
        "All stats: +6%" : [9.2093, 8.8372],
        "Boss Monster Damage : +30%" : [6.9070, 6.6279],
        "Ignore Monster DEF : +30%" : [6.9070, 6.6279],
        "STR : +12%" : [0.0976, 0.4878],
        "DEX : +12%" : [0.0976, 0.4878],
        "INT : +12%" : [0.0976, 0.4878],
        "LUK : +12%" : [0.0976, 0.4878],
        "ATT : +12%" : [0.0488, 0.2439],
        "Magic ATT : +12%" : [0.0488, 0.2439],
        "Critical Rate : +12%" : [0.0488, 0.2439],
        "Damage : +12%" : [0.0488, 0.2439],
        "All stats: +9%" : [0.0732, 0.3659],
        "ATT : +32" : [0.0488, 0.2439],
        "Magic ATT : +32" : [0.0488, 0.2439],
        "Boss Monster Damage : +35%" : [0.0488, 0.2439],
        "Boss Monster Damage : +40%" : [0.0488, 0.2439],
        "Ignore Monster DEF : +35%" : [0.0976, 0.4878],
        "Ignore Monster DEF : +40%" : [0.0488, 0.2439]

    }
]

rng = random.uniform(0, 100)
cur = 100.0
res = ""
sum = 0

for k, v in legendary_weapon_120_200[2].items():
    sum += v[1]

for k, v in legendary_weapon_120_200[2].items():

    if rng > cur - v[1]:
        res = k
        break
    
    cur -= v[1]


print(rng, res, sum)