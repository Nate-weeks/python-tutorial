'''
babysitter.py

A program to calculate babysitter earnings by Nate Weeks
'''
#split an input of military time into hours and minutes
def convert_time(time):
    split_time = time.split(":")
    hours = int(split_time[0])
    minutes = int(split_time[1])
    return [hours, minutes]

#take an input of two split military times and output the pay of the babysitter
def calculate_pay(beginning, ending):
    '''
    >>> calculate_pay([18, 0], [22, 0])
    9.0
    >>> calculate_pay([15, 30], [18, 30])
    7.5
    >>> calculate_pay([20, 30], [22, 30])
    3.5
    >>> calculate_pay([22, 0], [24, 0])
    3.0
    '''

    beginning_hours = beginning[0]
    beginning_minutes = beginning[1]
    ending_hours = ending[0]
    ending_minutes = ending[1]
    #handle for the case of minutes being greater than 0 at the beginning ie 22:15
    if beginning_minutes > 0:
        total_hours = ending_hours - (beginning_hours + 1)
        total_minutes = (60 - beginning_minutes) + ending_minutes
    else:
        #handle for total hours and minutes with an even hour at the beginning
        total_hours = ending_hours - beginning_hours
        total_minutes = ending_minutes
        #handle for an ending after 9:00
    if ending_hours >= 21:
        hours_after_bed = ending_hours - 21
        hours_before_bed = total_hours - hours_after_bed
        #if all times are after 9:00 set hours_after_bed to total hours
        if beginning_hours >= 21:
             hours_before_bed = 0
             hours_after_bed = total_hours
        #handle for minutes before and after bed
        minutes_after_bed = ending_minutes
        minutes_before_bed = total_minutes - minutes_after_bed
        #calculate total pay given time before and after bedtime
        total_pay = hours_after_bed * 1.50 + hours_before_bed * 2.50 + minutes_after_bed/60.0 * 1.50 + minutes_before_bed/60.0 * 2.50
        # print "hours before bed: " + str(hours_before_bed)
        # print "hours after bed: " + str(hours_after_bed)
        # print "minutes after bed: " + str(minutes_after_bed)
        # print "minutes before bed: " + str(minutes_before_bed)

    #calculate total pay given only time before bedtime
    else:
        total_pay = (total_hours * 2.50) + ((total_minutes/60) * 2.50)

    return total_pay



def main():
    start_time = convert_time(raw_input("Enter a time in military time that your babysitter will start working, ie: 20:15\n"))
    end_time = convert_time(raw_input("Enter a time in military time that your babysitter will stop working, ie: 23:30\n"))
    print "Total babysitter pay: " + str(calculate_pay(start_time, end_time))

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()

    '''
Confusing error: What's going wrong with my calculation? Seems like minutes aren't being handled but i dont understand why.

>>> Enter a time in military time that your babysitter will start working, ie: 20:15
20:30
Enter a time in military time that your babysitter will stop working, ie: 23:30
22:30
hours before bed: 0
hours after bed: 1
minutes after bed: 30
minutes before bed: 30
Total babysitter pay: 1.5
'''
