                                                    #   lucky number game 


import random
winning_number = random.randint(0,9)

user_answer = int(input("Guss what thee number is :-"))

if winning_number == user_answer:
    print("You Win")
elif winning_number > user_answer:
    print("Too low")
else:
    print("Too High")

print(f"The lucky number is :- {winning_number}")

