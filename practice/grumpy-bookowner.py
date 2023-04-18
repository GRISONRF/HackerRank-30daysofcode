""" There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store.
 You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. 
You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day. """


def maxSatisfied(customers, grumpy, minutes):


    #create a int to store customers that are already happy
    already_happy = 0
    #iterate over the grumpy
    for i in range(len(grumpy)):
        #if customer == 0 means they are already happy
        if grumpy[i] == 0:
            #add this customer to the list
            already_happy += customers[i]
            customers[i] = 0 
            #delete this customer from customers

    # print(already_happy)

    
    #[0,0,0,2,0,1,0,5]

    #max_happy
    max_happy = 0
    #cur_customers 
    cur_customers = 0

    #iterate over customers
    # for i in range(len(customers)):
    for i, customer in enumerate(customers):
        
        #add customer to curr_customers
        cur_customers += customer
        
        #keep iterating until i = to minutes
        if i >= minutes:
            
            #making the window to "slide" -> it makes sure we will always keep a window of length 'minutes', so we are always subtracting the 'last number before the window starts, so we always have 'minutes' length sum of customers inside of cur_customers. 

            cur_customers -= customers[i-minutes]
            #check the max betqeen max_happy and cur_customer
        max_happy = max(max_happy, cur_customers)
    # return max_customers + already_happy
    return max_happy + already_happy
        



customers = [1,0,1,2,1,1,7,5]
grumpy =    [0,1,0,1,0,1,0,1]
minutes = 3
print(maxSatisfied(customers, grumpy, minutes)) 

customers = [1, 2, 3, 4, 5]   
grumpy = [0, 1, 0, 1, 0]
x = 2
print(maxSatisfied(customers, grumpy, x)) 
# Expected output: 9


customers = [1, 2, 3, 4, 5]
grumpy = [0, 0, 0, 0, 0]
x = 2
print(maxSatisfied(customers, grumpy, x)) 
# Expected output: 15


customers = [1, 2, 3, 4, 5]
grumpy = [1, 1, 1, 1, 1]
x = 2
print(maxSatisfied(customers, grumpy, x)) 
# Expected output: 3



customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #55
grumpy = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
x = 3
print(maxSatisfied(customers, grumpy, x)) 
# Expected output: 25


customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grumpy = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
x = 20
print(maxSatisfied(customers, grumpy, x)) 




# # # Expected output: 55