# Iterate through all elements in the (list, tuple, set)

animales = ['dog', 'cat', 'bird', 'fish']

# Creating a temporary variable for the loop,
# this variable will be change its value for every iteration.
for animal in animales:
    print(animal)
    
print(animal) #* This will print the last value of the variable.

#----------------------------------------------------------------

#Iterate trough two lists at the same time
#! This will only work if the lists are of the same length.

names = ['John', 'Jane', 'Mary']
subnames = ['Smith', 'Johnson', 'Williams']

for name, subname in zip(names, subnames):
    print(name, subname)
    
#----------------------------------------------------------------

# Iterate until a condition is met

for i in range(10):
    print(i)
    
#----------------------------------------------------------------

# Iterate through a list by index

names = ['John', 'Jane', 'Mary']

for index,value in enumerate(names):
    print(index, value)
    
#----------------------------------------------------------------

# Using else statement in a for loop
#* The else statement will always be executed.

for i in range(10):
    print(i)
else:
    print('Done')
    
#----------------------------------------------------------------

# Iterate through a diccionary

dic = {
    'name': 'John',
    'age': 30
}

for key in dic.items():
    print(key)
    
#----------------------------------------------------------------

# Skip a iteration in a for loop

for i in range(10):
    if i == 5:
        print("Numero censurado")
        continue
    print(i)
    
#----------------------------------------------------------------

# Break a iteration in a for loop

for i in range(10):
    if i == 5:
        print("Numero censurado")
        break
    print(i)
else:
    print('Done')
    #* This else statement will not be executed,
    #* because the "break" statement finishes the entire loop.