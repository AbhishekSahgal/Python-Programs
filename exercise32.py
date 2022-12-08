username,age = input("Enter your nme and age :-").split(",")
age2 =int(age)
firstletter = username[0]
if (firstletter == "a" or firstletter == "A") and age2 > 10:
    print("You can watch coco movie.")
else:
    print("sorry ! you cannt watch coco movie.")



