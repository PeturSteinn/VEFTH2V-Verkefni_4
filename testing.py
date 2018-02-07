import json

with open('resources/bekkur.json', 'r', encoding='UTF-8') as f:
    bekkur = json.load(f)

n = '0201162690'
for i,nemandi in enumerate(bekkur['nemendur']):
    print(i, nemandi)

    if nemandi['kt'] == n:
        print(i, 'N á við þetta stak')


