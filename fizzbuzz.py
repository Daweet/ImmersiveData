"""
Write a program that prints the numbers from 1 to 100.

For multiples of 3 print “Fizz” instead of the number.

For the multiples of five print “Buzz”.

For numbers which are multiples of both 3 and 5 print “FizzBuzz”.
"""
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz' 
    elif number % 5 == 0:
        return 'buzz' 
    else:
        return number

for num in range(1,101):
    print(fizzbuzz(num))
