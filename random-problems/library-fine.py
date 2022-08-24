# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

# If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be .


# +++++++++++++++++ #

#if book returned:
# BEFORE or ON expected date -> fine = 0.
# after day but within same month and year -> fine = 15 x numbers of days late.
# after month but within same year -> fine = 500 x number of months.
# after the year -> fine = 10,000.

# input: 9 6 2015  6 6 2015
# output: 45


def libraryFine(d1, m1, y1, d2, m2, y2):

    if y1 > y2:
        return 10000
    elif m1 > m2 and y1 == y2:
        return 500 * (m1 - m2)
    elif d1 > d2 and  m1 == m2 and y1 == y2:
        return 15 * (d1 - d2) 
    else:
        return 0 


print(libraryFine(9, 6, 2015, 6, 6, 2015))