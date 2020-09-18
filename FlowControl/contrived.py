# array of numbers
numbers = [1, 45, 8, 12, 60]

for number in numbers:
    # if the number is evenly divisible by 8, reject array, end program
    if number % 8 == 0:
        print("The numbers are unacceptable")
        break

else:
    print("All those  numbers are fine")