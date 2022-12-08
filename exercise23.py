name,oneChar = input("Enter your name and Enter one character :-").split(",")
print(f"User name length :-{len(name)}")
print(f"Character count :- {name.strip().upper().count(oneChar.strip().upper())}")
