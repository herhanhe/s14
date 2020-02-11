
#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:herhan

import getpass

_names = []
_passwds = []
_lockeds = []


with open("passwd.txt","r",encoding="utf-8") as fr:
    for line in fr:
        user_list = line.strip("\n").split(":")
        _names.append(user_list[0])
        _passwds.append(user_list[1])
        _lockeds.append(user_list[2])

count = 0
m = 0
while count < 2 :
    username = input("username :")
    password = input("password :")
    if username in _names:
        m = _names.index(username)
        if _lockeds[m] == '0':
            if _passwds[m] == password:
                print("Congratulations!")
                break
            else:
                print("Incorrect password, please try again...")
                count += 1
                if count > 2:
                    _count = 5 - count
                    print("Only 5 attempts, you only have %d chances left" % _count)
        else:
            print("User was locked, Contact maintenance...")
            break
    else:
        print("Username does not exist, please try again...")
else:
    print("User was locked, Contact maintenance...")
    _lockeds[m] = '1'
    addline = _names[m]+':'+_passwds[m]+':'+_lockeds[m]+'\n'
    with open("passwd.txt","r+",encoding="utf-8") as fw:
        lines = fw.readlines()
        fw.seek(0,0)
        for line in lines:
            if _names[m] in line:
                line = addline
            fw.write(line)
