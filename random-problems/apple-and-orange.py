def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    # s - t =>range of house
    # a => position of apple tree
    # b => position of orange tree
    # apples => list of apple's positions
    # orange => list of orange's positions


    # check the position of each apple in the x-axis
    # a + [1, 2, 3] => a+1, a+2, a+3
    # check the position of each orange in the x-axis
    # b + [4, 5, 6] => b+4, b+5, b+6

    # check if the fruits position is in the range of s and t
    # when find an apple in the range -> count +=1 // same for orange
    # return the counts



    count_apples = 0
    count_oranges = 0
    for apple in apples:
        if (a + apple) >= s and (a + apple) <= t: 
            count_apples += 1
    for orange in oranges:
        if (b + orange) >= s and (b + orange) <= t:
            count_oranges += 1

    print(count_apples)
    print(count_oranges)



countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])