import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #“All vanity plates must start with at least two letters.
    check=[]
    for i in range(len(s)):
        check += s[i]
    # Check lenght of list is between 2 and 6
    a = (2 <= len(check) <= 6)

    # Check if first two chars are alphabets
    b = (''.join(check[:2])).isalpha()

    # Check if any element contains special characters
    c = not any(not s.isalnum() for s in check)

    # Check if the first char after an digit is not a alphabet
    d = not any(check[i].isdigit() and check[i + 1].isalpha() for i in range(len(check) - 1))
    #print("this is d", d)

    # Check if the first digit after an alphabet is not zero
    e = all(not(check[i].isalpha() and check[i + 1].isdigit() and check[i + 1] == '0') for i in range(len(check) - 1))

    return a and b and c and d and e

main()
