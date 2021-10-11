class DC:
    def __init__(self, date):
        [d, m, y] = map(int, date.split('/'))  # convert the date string to day,month,year value
        self.d = d
        self.m = m
        self.y = y


class DateCalculator:
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Distinguish whether it is a leap year
    def leap_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False

    # For date validation
    def verify_date(self, mmddyy):
        if mmddyy.y not in range(1901, 3000):
            raise ValueError('YEAR is not in the correct range.')

        elif mmddyy.m not in range(1, 13):
            raise ValueError('MONTH is not in the correct range.')

        elif mmddyy.m in [1, 3, 5, 7, 8, 10, 12] and mmddyy.d not in range(1, 32):
            raise ValueError('DAY is not in the correct range.')
        elif mmddyy.m in [4, 6, 9, 11] and mmddyy.d not in range(1, 31):
            raise ValueError('DAY is not in the correct range.')

            # for leap year (366 days)
        elif mmddyy.m == 2 and self.leap_year(mmddyy.y) is True and mmddyy.d not in range(1, 30):
            raise ValueError('DAY is not in the correct range.')

            # for normal year (365 days)
        elif mmddyy.m == 2 and self.leap_year(mmddyy.y) is False and mmddyy.d not in range(1, 29):
            raise ValueError('DAY is not in the correct range.')

        else:
            return mmddyy.y, mmddyy.m, mmddyy.d

    def count_date(self, new_date):
        yy, mm, dd = self.verify_date(new_date)

        # leap_yy = int((yy - 1900) / 4)  # count the number of leap years
        # normal_yy = yy - 1901 - leap_yy # get the number of normal years

        # count days for YEAR
        if yy == 1901:
            num_yy = 0
        else:
            leap_yy = 0                         # count leap years and normal years
            normal_yy = 0
            for i in range(1902, yy + 1):
                if self.leap_year(i) is True:   # leap year
                    leap_yy += 1
                else:
                    normal_yy += 1

            # count number of days for the year (start from year 1901)
            if self.leap_year(yy) is True:
                num_yy = leap_yy * 366 + normal_yy * 365 - 1
            else:
                num_yy = leap_yy * 366 + normal_yy * 365

        # count days for MONTH
        num_mm = 0  # days in month
        for i in range(0, mm-1):
            num_mm += self.days_of_month[i]  # 28 days for Feb normally

        # get total days for the date
        if self.leap_year(yy) is True and mm > 1:  # 29 days for Feb
            return num_yy + num_mm + dd + 1
        else:
            return num_yy + num_mm + dd


    def count(self, date_0, date_1):

        delta = abs(self.count_date(date_1) - self.count_date(date_0)) - 1   # two next day --> 0 // same day --> -1
        # two adjacent dates --> 0 // same day --> -1
        assert delta >= 0, 'SAME day!'

        return print(delta, 'days') if delta > 1 else print(delta, 'day')


def main():
    two_dates = input('Input Two Dates (DD/MM/YYYY - DD/MM/YYYY):  ')
    date0, date1 = two_dates.split('-')
    calculate = DateCalculator()
    calculate.count(DC(date0), DC(date1))


if __name__ == '__main__':
    main()


# 1) 02/06/1983 - 22/06/1983 = 19 days
# 2) 04/07/1984 - 25/12/1984 = 173 days
# 3) 03/01/1989 - 03/08/1983 = 1979 days

# 1/1/1919 - 31/12/2999 -> 394826
# 3/3/1919 - 12/12/1999 -> 29503
# 3/3/1919 - 12/12/2030 -> 40826
# 3/3/1904 - 12/12/2020 -> 42652
# 21/04/1990 - 27/09/2021 -> 11481
# 12/12/1999 - 4/4/2020 -> 7418
# 2/2/1977 - 2/2/2999 -> 373277
# 5/5/1977 - 12/12/2016 -> 14465
# 4/4/1919 - 30/4/1919 -> 25
# 1/1/2012 - 1/3/2012 -> 59
# 5/5/1919 - 4/4/1919 -> 30
# 6/6/2040 - 8/8/1944 -> 35000
