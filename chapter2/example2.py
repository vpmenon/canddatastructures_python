#Chapter 2.1
# overflow in char



def main():
    i = 1
    j = 0
    while(i > 0 and i <= 0x7f):  #  Limited to c type integer 4 bytes
        j = i
        i = i + 1
    print("the maximum value of integer is "+ str(j))
    print("the value of integer after overflow is " + str(-i))


main()
