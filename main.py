from calendar import day_abbr


users = ["Dave", "John", "Sara"]

data = ['Yohan', 42, True]

emptylist = []

print(users[0])
print(users[-2])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

users.extend(data)
print(users)