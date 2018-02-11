# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Suzie Programmer
# edited by Nate to print a line of guideance before asking for an input
def main():
    print "This program takes a Celsius temperature and converts it to Fahrenheit!"
    celsius = input("What is the Celsius temperature? ")
    fahrenheit = 9.0 / 5.0 * celsius + 32

    print "The temperature is", fahrenheit, "degrees Fahrenheit."
main()
