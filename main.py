#///////////1//////////
# name = input("What's your name?: ")
# age = input("How old are you?: ")
# print(f"Привіт {name}, тобі {age}!")
#///////////2//////////
# age = int(input("How old are you?: "))
# if age >= 18:
#     print("Вхід дозволено!")
# else:
#     print("Вхід заборонено!")
#///////////3///////////
# from random import randint
# a = (randint(1,10))
# for i in range(3):
#     b = int(input("Your guess: "))
#     if b > a:
#         print("Менше")
#     elif b < a:
#         print("Більше")
#     else:
#         print("Correct!")
#//////////4/////////////
# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# for i in range(a, b + 1):
#     print(i)
#////////////5///////////
a = int(input("Введiть число: "))
for i in range(a, 0, -1):
    if i % 2 == 0:
        print(i, end=' ')