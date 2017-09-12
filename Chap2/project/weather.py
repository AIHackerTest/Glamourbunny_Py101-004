#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests

# XinZhiTianQi uid and key
xinzhi_uid = 'U5A06E9001'
xinzhi_key = 'mean2amqu5doidko'

# define dict history
history = {}

#define function find_weather to get weather info from XinZhiTianQi
def find_weather(user_input):
    #make requests url
    pay_load = {'key':xinzhi_key,'location':user_input}
    r = requests.get("https://api.seniverse.com/v3/weather/now.json",params = pay_load)
    #print(r.url)
    try:
        # analyse the result and get the city's weather info
        result = r.json()['results']
        result_1 = result[0]
        #print("result_1:",result_1)  
        result_2 = result_1['now']
        #print("result_2:",result_2) 
        # save results to history
        history[user_input] = result_2['text']
        #print(history)
        # return weather info
        return result_2['text']
    except KeyError:
         print("不在服务区！") 


while True:
    user_input = input('请输入指令：')   #中文
    # input h or help to get help info
    if user_input == 'h' or user_input == 'help':
        print(open('help.txt').read())
    # input quit or exit to exit
    elif user_input == 'quit' or user_input == 'exit':      
        sys.exit()
    elif user_input == 'history':
        # input history to get weather history 
        print('查询过的城市天气包括：')
        for city,weather in history.items():
            print('%s 的天气是：%s' % (city,weather))        
    else:
        # get weather info from XinZhiTianQi
        print('%s 的天气是：%s' % (user_input,find_weather(user_input))) 
        continue
        
