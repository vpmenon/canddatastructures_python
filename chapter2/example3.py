#Chapter 2.3
# type casting

def main():
    dl = 123.56  # A
    il = 456  # B
    print("the value of d1 as int without cast operator" + str(dl))  # C
    print("the value of d1 as int without cast operator" + str(int(dl)))  # D
    print("the value of i1 as double without cast operator " + str(il))  # E
    print("the value of i1 as double with cast operator " + str(float(il)))  # F
    il = 10
    il = il + 1
    print("effect of multiple unary operator " + str(float(il)))  # G
    il = 10  #H
    il = -il + 1
    print("effect of multiple unary operator " + str(float(il)))  # I
    il = 10
    il = il + 1
    print("effect of multiple unary operator " + str(float(-il)))  # J
    il = 10  # K
    il = il - 1
    print("effect of multiple unary operator " + str(float(-il)))  # L
    il = 10  # M
    print("effect of multiple unary operator " + str(float(-il)))  # N
    il = il + 1


main()
