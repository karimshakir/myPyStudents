def mo_to_years(years):
    return years * 12


def convertAge(*args, convert):
    return convert(sum(args))

age = convertAge(12, convert=mo_to_years)
print(age)

#XXXXXXXXXX#XXXXXXXXXX#XXXXXXXXXX#XXXXXXXXXX#XXXXXXXXXX#XXXXXXXXXX

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Couldn't find an element with {expected}.") 

friends = [
    {"name": "Damen", 'age': 34},
    {"name": "Beth", 'age': 32},
    {"name": "Tracy", 'age': 23},
    {"name": "Tim", 'age': 24}
]

def get_friend_by_name(friend):
    return friend['name']

print(search(friends, "Beth", get_friend_by_name))