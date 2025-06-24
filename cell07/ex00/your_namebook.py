#!/usr/bin/env python3


def array_of_names(namebook):
    first_name = namebook.keys()
    name_list = []
    for i in first_name:
        fn = i.capitalize()
        ln = namebook[i].capitalize()
        fulln = f'{fn} {ln}'
        name_list.append(fulln)
    return name_list

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))
