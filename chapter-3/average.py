# A program to print the average of values up to an input of N
def average():
    amount_of_numbers = input("Enter How many numbers you would like to average: ")
    numbers_array = []
    count = 0.0
    for i in range(amount_of_numbers):
        numbers_array.append(input("Enter a Number: "))
    for number in numbers_array:
        count += float(number)

    average = count/len(numbers_array)
    print average

def test():
    print "expect the average of user input of 4 numbers, 1, 2, 3, 4 - to be 2.5"
    print average()

test()
