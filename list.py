l = ['bob', 'rolf','anne']  #most common
t = ('bob','rolf','anne' ) #tupple cannot be modified
s ={'bob', 'rolf', 'anne'} #no duplicates, no order

#LIST
l.append('smith')
l.remove('rolf')
l[0] = 'amy'
print(l)

#Set
s.add('some name')
friends = {'mark', 'jim', 'paul', 'derrick'}
abroad_friends = {'mark', 'jim'}
local_friends = friends.difference(abroad_friends)
print(local_friends)

all_friends = abroad_friends.union(local_friends)
print(all_friends)
smart_friends = {'kevin', 'jim', 'luke', 'vader'}
both = smart_friends.intersection(abroad_friends)
print(both)
