def is_leap_year(year):
    """ returns true if year is a leap year, false otherwise """

    print("Year:", year)
    if (year % 4) == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(is_leap_year(2020))
print(is_leap_year(1900))
print(is_leap_year(2025))