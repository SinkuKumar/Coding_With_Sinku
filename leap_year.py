"""
Module: Leap Year
Author: Sinku Kumar
Date: 6 June 2023

To determine whether a year is a leap year, follow these steps:
    1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
    2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
    3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
    4. The year is a leap year (it has 366 days).
    5. The year is not a leap year (it has 365 days).
"""


def is_leap_year(year):
    """
    Return True if year is leap year, else False

    :param year:
    :return: True when leap year, else False
    """
    # step 1
    if not year % 4:
        # step 2
        if not year % 100:
            # step 3
            if not year % 400:
                return True
        # step 4
        else:
            return True
    # step 5
    else:
        return False


#print(is_leap_year(2008))
