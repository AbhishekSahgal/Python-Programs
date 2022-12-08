def is_palendom(value):
    if value == name[::-1]:
        return "This value is Palendrom"
    return "This value is not palendrom"

name = input("Enter your string :- ")
# reverse = name[::-1]

print(is_palendom(name))