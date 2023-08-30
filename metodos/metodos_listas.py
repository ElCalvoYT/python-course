
# Creating a list

lista = ["hello", "world", "python"]

#----------------------------------------------------------------

# Getting the length of the list
len(lista)

#----------------------------------------------------------------

# Adding an element to the list

lista.append("Appends at the end")

#----------------------------------------------------------------

# Adding an element to the list on a specific index

lista.insert(1, "Specific index")

#----------------------------------------------------------------

# Adding multiple elements to the list at once

lista.extend(["Appends at the end", "Appends at the end", "Appends at the end"])

#----------------------------------------------------------------

# Removing an element from the list by its index

lista.pop(1)

#----------------------------------------------------------------

# Removing an element from the list by its value

lista.remove("Appends at the end")

#----------------------------------------------------------------

# Sorting the list
#! Only works for integers, floats and boolean values
#* By default the list is sorted in ascending order

lista.sort()

lista.sort(reverse=True) # This will sort the list in descending order

# Reversing the list
lista.reverse()

#----------------------------------------------------------------

# removing all elements from the list

lista.clear()

#----------------------------------------------------------------