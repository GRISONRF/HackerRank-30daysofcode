#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.


def miniMaxSum(arr):
    # Write your code here
    
    arr.sort()
    total_sum = 0
    
    for n in arr:
        total_sum += n
    
    max = total_sum - arr[0]
    min = total_sum - arr[4]
    
    print(min, max)

miniMaxSum([7, 69, 2, 221, 8974])