programming_dictionary = {
    "Bug": "This is an error",
    "Function":"This is a function"
}

#extracting a key from a dictionary
print(programming_dictionary["Function"])

#adding something to a dictionary
programming_dictionary["loop"] = "Something which iterates"
print(programming_dictionary)


for thing in programming_dictionary:
    #for printing key
    print(thing)
    #for printing value
    print(programming_dictionary[thing])