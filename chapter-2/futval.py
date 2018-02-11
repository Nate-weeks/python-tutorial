# A program to calculate the future value of a 10 year investment with inflation taken into account
# by: John M. Zelle
def main():
    print "This program calculates the future value of a 10-year investment."
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annualized interest rate: ")
    infl = input("Enter the yearly inflation rate: ")
    years = input("Enter the total number of years the investment will build: ")
    for i in range(years):
        principal = principal * (1 + apr)
        principal = principal / (1 + infl)
    print "The amount in 10 years is:", principal
main()
