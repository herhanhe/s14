#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:herhan

city = {
    '书籍':{
        'python书籍':{
            'python基础':{'python的基础书籍'},
            'python进阶':{'python进阶用的'},
            'python进阶到放弃':{'python开始放弃'}
        },
        '美食书籍':{
            '炒菜指南':{'教你炒菜咯'},
            '美食菜谱':{'看看有什么美食'},
            '菜品介绍':{'关于菜品的介绍以及由来'}
        }
    },
    '饮料':{
        '能量饮料':{
            '红牛':{'喝了一晚上不睡觉'},
            '战马':{'喝了奋战到天明'},
            '魔爪':{'喝了提神呦'}
        },
        '普通饮料':{
            '矿泉水':{'就普通的纯净水'},
            '冰红茶':{'这是一瓶红茶'},
            '乌龙茶':{'这是一瓶乌龙茶'}
        }
    },
    '汽车':{
        '丰田':{
            'CROWN皇冠':{'皇冠车'},
            'COROLLA卡罗拉':{'卡罗拉呦'},
            'COROLLA花冠':{'花冠经典车'}
        },
        '劳斯莱斯':{
            '银色精灵':{'别看了，买不起'},
            'ParkWard':{'豪华座驾'},
            '100EX':{'CEO专用'}
        }
    }
}

current_layer = city

layers = [city]

while True :
    for k in current_layer:
        print(k)
    choice = input(">>:")
    if choice == "back":
        current_layer = layers[-1]
        layers.pop()
    elif  choice not in current_layer:
        continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]