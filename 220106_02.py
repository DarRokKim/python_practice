# 물품을 보여주는 함수

treasure_box = {'rope':2, 
                'apple':10, 
                'torch': 6, 
                'gold coin': 50, 
                'knife': 1, 
                'arrow': 30}

def display_stuff(treasure_box):
    print("Congraturation!! you got a treasure box")
    for k, v in treasure_box.items():
        print("you have {} {}pcs".format(k, v))
display_stuff(treasure_box)

# 물품을 통해 얻을 수 있는 은화를 보여주는 함수
# 물품의 가치

coin_per_treasure = {'rope':1,
        'apple':2,
        'torch': 2,
        'gold coin': 5, 
        'knife': 30,
        'arrow': 1}

def total_silver(treasure_box, coin_per_treasure):
    total_coin = 0
    for treasure in treasure_box:
        coin = coin_per_treasure[treasure] * treasure_box[treasure]
        print("{} : {}coins/pcs * {}pcs = {} coins".format(
          treasure, coin_per_treasure[treasure], treasure_box[treasure], coin))
        total_coin += coin
    print('total_coin : ', total_coin)
total_silver(treasure_box, coin_per_treasure)

# 딕셔너리의 딕셔너리

treasure_box = {'rope': {'coin': 1, 'pcs': 2},
                'apple': {'coin': 2, 'pcs': 10},
                'torch': {'coin': 2, 'pcs': 6},
                'gold coin': {'coin': 5, 'pcs': 50},
                'knife': {'coin': 30, 'pcs': 1},
               	'arrow': {'coin': 1, 'pcs': 30}
               }
dd = treasure_box['rope']
print(dd)

def display_stuff(treasure_box):
    print("Congraturation!! you got a treasure box!!")
    for treasure in treasure_box:
             print("You have {} {}pcs".format(treasure, treasure_box[treasure]['pcs']))
display_stuff(treasure_box)

def total_silver(treasure_box, coin_per_treasure):
    total_coin = 0
    for treasure in treasure_box:
        coin = coin_per_treasure[treasure] * treasure_box[treasure]['pcs']
        print("{} : {}coins/pcs * {}pcs = {} coins".format(
          treasure, coin_per_treasure[treasure], treasure_box[treasure]['pcs'], coin))
        total_coin += coin
    print('total_coin : ', total_coin)
total_silver(treasure_box, coin_per_treasure)

import pandas as pd
ser = pd.Series(['a','b','c',3])
print(ser)

print(ser.index)
print(ser.values)

ser2 = pd.Series(['a','b','c', 3], index=['i','j','k','h'])
print(ser2)

ser2.index = ['Jhon', 'Steve', 'Jack', "Bob"]
print(ser2)

Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swiss': 41, 'Italy': 39, 'Japan': 81, 'China': 86, 'Rusia': 7}
ser3 = pd.Series(Country_PhoneNumber)
print(ser3)

print(ser3['Korea'])
print(ser3['Italy'])

#  Series의 Name

ser3.name = "Country_PhoneNumber"
ser3.index.name = "Country_Name"
ser3


# Series와 DataFrame 비교
# Series로 변환
data = {'Region' : ['Korea', 'America', 'Chaina', 'Canada', 'Italy'],
        'Sales' : [300, 200, 500, 150, 50],
        'Amount' : [90, 80, 100, 30, 10],
        'Employee' : [20, 10, 30, 5, 3]
        }
s = pd.Series(data)
s

# DataFrame으로 변환

d = pd.DataFrame(data)
d

d.columns

d.index

d.index=['one','two','three','four','five']
d.columns = ['a','b','c','d']
d

