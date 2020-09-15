#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:herhan

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120),
]
interface = ["merchants","consumers"]

for index,item in enumerate(interface):
    print(index,item)
interface_chioce = int(input("Choose your interface of number:"))
if interface[interface_chioce] == "consumers":
    shopping_list = []
    tag = True
    user_salary = input("your salary:")
    if user_salary.isdigit():
        user_salary = int(user_salary)
        while tag:
            for index,item in enumerate(product_list):
                print(index,item)
            user_chioce = input("Choose what you want:")
            if user_chioce.isdigit():
                user_chioce = int(user_chioce)
                if user_salary < (product_list[user_chioce][1] * num_chioce):
                    print("Your balance is insufficient!")
                user_salary -= product_list[user_chioce][1] * num_chioce
                shopping_list.append(product_list[user_chioce])
            elif user_chioce == 'q':
                print("Exit consumption now!")
                tag = False
            else:
                print("Input error, please continue")
                continue
        else:
            print("Your balance:{}".format(user_salary))
            print("shopping_list:")
            for i in shopping_list:
                print('\t{}'.format(i[0]))
elif interface[interface_chioce] == "merchants":
    funcs = ["add","alter"]
    for func in funcs:
        print(func)
    funcs_chioce = input("choose function:")
    if funcs_chioce == "add":
        product = input("Enter the item name that needs to be added:")
        price = int(input("Input the unit price that needs to be increased:"))
        product_list.append((product,price))
        print(product_list)
    elif funcs_chioce == "alter":
        tag = True
        while tag:
            for index,item in enumerate(product_list):
                print(index,item)
            user_chioce = input("Select the product to modify:")
            if user_chioce.isdigit():
                user_chioce = int(user_chioce)
                del interface_chioce[user_chioce]
                product = input("Enter the item name that needs to be added:")
                price = int(input("Input the unit price that needs to be increased:"))
                product_list.append((product, price))
                print(product_list)
            elif user_chioce == 'q':
                print("Exit consumption now!")
                tag = False
            else:
                print("Input error, please continue")
                continue
