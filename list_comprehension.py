numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers]

for num in numbers:
    doubled.append(num * 2)

friends = ['karie', 'sam', 'susan', 'mike', 'danny']
#new_array[appendThis, for item in items, if this is true]
starts_s = [friend for friend in friends if friend.lower().startswith('s') ]
print(starts_s)

friends = ['karie', 'Sam', 'susan', 'mike', 'danny']
starts_s = []
for friend in friends: 
    if friend[0].lower() == 's':
        starts_s.append(friend)
print(starts_s)

print(friends is starts_s) #false
print("friends id: ", id(friends), 'starts_s id: ', id(starts_s))