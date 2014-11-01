__author__ = 'robin'


import random


letters_lc = "abcdefghijklmnopqrstuvwxyz"
letters_uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_password(length):
    password = ""

    for i in xrange(length):
        x = random.randint(0, 2)

        if x == 0:
            y = random.randint(0, letters_uc.__len__()-1)
            password += letters_lc[y]
        if x == 1:
            y = random.randint(0, letters_lc.__len__()-1)
            password += letters_uc[y]
        if x == 2:
            y = random.randint(0, 9)
            password += str(y)

    return password


def main():
    print "PassGenerator v1.0"

    length = int(input("Length: "))
    password = generate_password(length)

    print password

main()
