"""
Identifies prime number
A prime number is a number that has only itself and 1 as a factor.
This means that for each of the numbers from 2 to that number, the number cannot be divided without a remainder.
For example, 9 is not a prime number because it can be divided by 3 without a remainder. But 7 is a prime number because it cannot be divided by 2, 3, 4, 5, or 6 without a remainder.
Write an appliation that will that show a list of numbers and indicate whether or not they are prime.
The user will have to input the last number in the range, and you will print all of the numbers from 1 to that number.
"""
prime_numbers = 0

def prime_number(n):
    if n >= 2:
        for num in range(2,n):
            if not ( n % num ):
                return False
    else:
        return False
    return True
	        
#ranges = int()
for ur_num in range(1,int(input("Enter the last number in the range: "))):
    if prime_number(ur_num):
        prime_numbers += 1
        print (f"{ur_num} is prime number." )
    else:
        print (f"{ur_num} is not prime number." )