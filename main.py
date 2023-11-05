from calendar import day_abbr


users = ["Dave", "John", "Sara"]

data = ['Yohan', 42, True]

emptylist = []

print(users[0])
print(users[-2])

print(users.index('Sara')) #Tells were Sara is at the index
                           #note: the index is at proper index
                           #(it is at index 3) even though it is technically at index 2

print(users[0:2])
print(users[1:])
print(users[-3:-1]) 

print(len(data))

users.append('Elsa') #*1
print(users)

users += ['Jason'] # *1
print(users)

users.extend(['Robert', 'Jimmy']) #*1
print(users)

# users.extend(data) # Does the same thing *1
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2]