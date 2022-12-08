# total = int(input("Enter your number :-"))

# i = 1
# while 1<=total :
#     total= total+i
#     i = i+1
# print(total)


number = input("Enter your number :-")

total = 0
i = 0
while i < len(number):
    total = int(number[i]) + 1
    i = i + 1
print(total)
