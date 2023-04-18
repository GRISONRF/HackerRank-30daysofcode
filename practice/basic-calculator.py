""" -  BASIC CALCULATOR:
# The input is a string, such as "2+3-999", which contains +- operations, and returns the calculation result.
"""

def calculator(expression):

# input is a string
# output int

    res = 0   #-1
    temp_num = 0   #5
    sign = 1    #1

    for i in expression:
        
        #number
        if i.isdigit():
            i = int(i)
            temp_num = temp_num * 10 + i

        #+
        if i == "+":
            res += temp_num * sign
            sign = 1
            temp_num = 0
        
        #-
        if i == "-":
            res += temp_num * sign
            sign = -1
            temp_num = 0

    res += temp_num * sign
    print(res)
        


print(calculator("3-4+5")) #4
print(calculator("2+3-999")) #-994














    # #initialize var to track the sign
    # sign = 1  
    # #initialize var with result
    # result = 0  
    # #initialize var num
    # nums = 0  

    # #for i in the len of expression
    # for i in range(len(expression)):
    #     #check if current iteration is a digit
    #     if expression[i].isdigit():
    #         #if it is, change nums to nums * 10 + expression[i] 
    #         nums = nums * 10 + int(expression[i])
    #     #if current iteration is "+"
    #     if expression[i] == "+":
    #         #update answer to += num * sign
    #         result += nums * sign
    #         #change sign to +1
    #         sign = 1
    #         #change num to 0
    #         nums = 0
    #     #if curr iteration is "-"
    #     if expression[i] == "-":
    #         #update answer to += num * sign
    #         result += nums * sign
    #         #change sign to -1
    #         sign = -1
    #         #change num to 0
    #         nums = 0
    # #when loop is done, add to result the last num * the sign
    # result += nums*sign
    # return result



