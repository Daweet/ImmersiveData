"""
You are going to develop an application to produce numbers in a sequence.
The user will be required to enter a number, and for that number, you will:
* Divide the number by 2 if it is even

* Multiply the number by 3, and add 1 if it is odd. 

* Do this until you get to 1. 
Ask the user if he/she would like to input another number, and continue until he/she does not want to enter any more numbers.
Show the results as you go. For example, the number 5 should produce the following output:
> 5 16 8 4 2 1
The number 3 should produce the following output:
> 3 10 5 16 8 4 2 1 
"""
def collatz_sequence(num):
    if num == 1:
        return num
    elif num % 2 == 0:
        return (num / 2)
    elif num % 2 != 0:
        return (3*num +1)

n = input("Enter a number: ")
while n != 1:
    n = collatz_sequence(int(n))
    
    print(int(n), end =" ")