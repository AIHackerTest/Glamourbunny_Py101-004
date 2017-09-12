#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#输入你想查询的城市
#city = input("City: ")
#输入拼音做转换？


#读取天气文件到列表
weather_f = open('weather_info.txt', mode='r',encoding='UTF-8')
weather_list = weather_f.readlines()
weather_f.close()  
city_weather = {}
history = {}

#遍历列表
for weather_line in weather_list:
    #每行数据拆分，写入字典city_weather
    #将序号、城市和天气分离
    w_temp = weather_line.split()
#    print (w_temp)
    (city,weather) = w_temp[1].strip().split(',', 2)
    city_weather[city] = weather
#    print ('%s 的天气是：%s' % (city,city_weather[city]))
      

#遍历列表
#for weather_line in weather_list:
    #每行字符串查找
#    if weather_line.find(city) > -1:
        #将城市和天气分离
#        city_weather = weather_line.split(',', 2)          
        #显示天气
#        print(city,":  ",city_weather[1])
#        break


   
while True:
    user_input = input('请输入指令：')
    # 随时输入 h或者 help 打印帮助文档 
    if user_input == 'h' or user_input == 'help':
        print(open('help.txt').read())
    # 输入指令，退出程序的交互（一般使用 quit 或 exit）
    elif user_input == 'quit' or user_input == 'exit':      
        sys.exit()
    elif user_input in city_weather:
        print('%s 的天气是：%s' % (user_input,city_weather[user_input]))
    # 存储查询历史
        history[user_input] = city_weather[user_input]
    elif user_input == 'history':
        #打印查询历史 
        print('\n查询过的城市天气包括：')
        for city,weather in history.items():
            print('%s 的天气是：%s' % (city,weather))        
    else:
        #全都没有时提示
        print("不在服务区！")
        continue
        


   


