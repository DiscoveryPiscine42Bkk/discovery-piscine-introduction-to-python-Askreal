#!/usr/bin/env python3 

def famous_births(name_list):
    new_nl = {}
    for key , value in name_list.items():
        new_nl[value['name']] = value['date_of_birth']

    brith_date = list(new_nl.values())
    brith_date.sort()    
    
    for i in brith_date:
        for k , v in new_nl.items():
            if v == i:
                print(f'{k} is a great scientist born in {i}.')
    return 

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
