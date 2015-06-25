#fizzbuzz.py
#prints the numbers from 1 to 100. 
#But for multiples of three print “Fizz” instead of the number 
#and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz".

for current_number in range(1,101):
    if current_number % 15 == 0:
        print "fizzbuzz "#, current_number
    elif current_number % 3 == 0:
        print "fizz "#, current_number
    elif current_number % 5 == 0:
        print "buzz"#, current_number
    else:
        print current_number    