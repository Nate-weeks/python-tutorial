def main():
    year = input("type a year")
    if year % 4 == 0:
        if str(year)[-1] == "0" and str(year)[-2] == "0" and year % 400 != 0:
            print "its not a leap year"
        else:
            print "its a leap year"
    else:
        print "its not a leap year"

main()
