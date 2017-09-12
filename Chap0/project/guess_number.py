# define compare function
def compare_two(A, B):
    if A > B:
        print("Too Small!")
        return -1;
    elif A < B:
        print("Too Big!")
        return 1;
    else:
        print("Congratulations!")
        return 0;
      
    


import random
#生成随机正整数 
guess = random.randint(1,10)
#设置计数器
count = 0

#循环10次，答题机会
while count < 10:
    #提示猜测 
    try:
        #提示输入数字
        answer = int(input("Guess the Number（1-10）: "))            
    #进行比较
        if compare_two(guess, answer) == 0:
            break
        count += 1
    except ValueError:
         print("输入的不是数字！") 
    
    
