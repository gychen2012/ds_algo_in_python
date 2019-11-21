"""
C-1.26 Write a short program that takes as input three integers, a, b, and c, from the console and
determines if they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”
"""

def check_args(a, b, c):
    if a+b == c or b-c == a or a*b == c:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        a = int(input('Enter an integer a: '))
        b = int(input('Enter an integer b: '))
        c = int(input('Enter an integer c: '))
        if check_args(a, b, c):
            print("The integers {}, {}, and {} can be used in a correct arithmetic formula.".format(a, b, c))
        else:
            print("The integers {}, {}, and {} cannot be used in a correct arithmetic formula.".format(a, b, c))
            
"""
output: 

Enter an integer a: 2
Enter an integer b: 2
Enter an integer c: 4
The integers 2, 2, and 4 can be used in a correct arithmetic formula.
Enter an integer a: 2
Enter an integer b: 4
Enter an integer c: 2
The integers 2, 4, and 2 can be used in a correct arithmetic formula.
Enter an integer a: 2
Enter an integer b: 3
Enter an integer c: 6
The integers 2, 3, and 6 can be used in a correct arithmetic formula.
Enter an integer a: 10
Enter an integer b: 7
Enter an integer c: 1
The integers 10, 7, and 1 cannot be used in a correct arithmetic formula.
Enter an integer a: 
"""
