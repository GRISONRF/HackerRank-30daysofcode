""" 

Given a string s representing a valid expression, implement a basic calculator to evaluate it, 
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval(). """

#-2+1 

def calculator(expression):
    
    #'delete' blank spaces
    #res
    #sign
    #temp_num
    #list
    #check if is a digit, an expression or a parentesis
    #if digit -> same as other question
    #if + or - -> same as other question
    #if ( -> take what we have so far: temp_num, sign and store in list. change temp_num to 0
    #if ) -> perform expression stored in the list and what we current have as temp_num and sign. add to result
    #after for loop, check for if there's num and sing stored

    ans = 0  #1
    sign = 1  #1
    temp_num = 0  # 1
    lst = [] # 

    for i in expression:

        #number
        if i.isdigit():
            i = int(i)
            temp_num = temp_num * 10 + i
        #+
        if i == "+":
            ans += temp_num * sign
            sign = 1
            temp_num = 0
        #-
        if i == '-':
            ans += temp_num * sign
            sign = -1
            temp_num = 0
        #(
        if i == '(':
            lst.append(ans)
            lst.append(sign)
            ans = 0
            sign = 1
        #)
        if i == ')':
            #finish to perform the operations inside the parentensis
            #add the expression in the stack to the curr ans
            ans += temp_num * sign
            temp_num = 0
            s = lst.pop() #
            n = lst.pop() #
            ans += n * s    

    ans += temp_num * sign    
    return ans
            

expression =  "(1+(4+5+2)-3)+(6+8)" # 23
expression1= "1+1"  #2
expression2= " 2-1 + 2 " #3
expression3 = "1-(     -2)" # 3


print(calculator(expression))
print(calculator(expression1))
print(calculator(expression2))
print(calculator(expression3))



""" 
    #i as 0
    i=0
    #store the final result
    result = 0
    #keep track of current sign
    sign = 1
    #stack to store intermediate results and signs while processing the parentheses
    stack = []

    # runs until i is not len of expression
    while i < len(expression):

        #if current character is a digit
        if expression[i].isdigit():
            #initialize num as 0
            num = 0
            #while current number is on bound of expression and its a digit
            while i < len(expression) and expression[i].isdigit():
                #this adds all consecutive numbers into num ( so 123 will be addes as 123)
                num = num * 10 +  int(expression[i])
                #add 1 to keep the while loop going
                i += 1
            # i decremented because inside the second while loop we might have processed more than 1 number, so decrementing 1 from the expression makes sure the next iteration will be correct    
            i -=1
            #add num and current sign to result
            result += num * sign
            #change sign to positive
            sign = 1

        #if an open parentesis, add the result and sign we have so far inside the stack so we can keep them for when the parentheses is closed
        elif expression[i] == "(":
            stack.append(result)
            stack.append(sign)
            #result = 0 so we can create a new result with the values inside of the parenteses
            result = 0
            sign = 1
          
        #when parentheses is closed, we get the previous result and the new result and add them together
        elif expression[i] == ")":
            result = result * stack.pop() + stack.pop()
        
        #if it's a "-", we just change the sign (the first if statement will deal with the sign before adding it inside the result)
        elif expression[i] == "-":
            sign*=-1

        # i+1 to keep the loop going!
        i+=1
    return result """
