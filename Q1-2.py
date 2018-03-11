def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """

    for i in range(100000, 1000000):
        str_i=str(i)
        flag1=str_i[-4:-2]==str_i[:-3:-1]
        str_i=str(i+1)
        flag2=str_i[-5:-3]==str_i[:-3:-1]
        str_i=str(i + 2)
        flag3=str_i[1:3]==str_i[-2:-4:-1]
        str_i=str(i + 3)
        flag4=str_i[0:3] == str_i[-1:-4:-1]
        if flag1 & flag2 & flag3 & flag4:
            print(i)
check_palindrome()