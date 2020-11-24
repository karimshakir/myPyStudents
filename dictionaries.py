friend_ages = {'rolf': 24,
                'adam': 30 }
friend_ages['cathy'] = 34
print(friend_ages)


for k, v in friend_ages.items():
    print(v)

    #Destructering variables
    t = 5,11
    x,y = t
    print(x, y)