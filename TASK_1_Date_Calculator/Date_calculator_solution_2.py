
class HandleDate:
    month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date: str):
        dlist = date.split("/")
        self.d, self.m, self.y = map(int, dlist)

    def check_date(self):
        if 3001 < self.y or self.y < 1900:
            return True
        if 0 > self.m or self.m > 12:
            return True
        if leap_year(self.y) and self.m == 2:
            if 0 > self.d or self.d > 29:
                return True
        else:
            if 0 > self.d or self.d > self.month_day_list[self.m - 1]:
                return True
        return False


def leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


class CalDate:
    day_of_year = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    def __init__(self, date1: HandleDate, date2: HandleDate):
        self.d1 = date1
        self.d2 = date2


    def cal_leap_normal_year(self, target_d: HandleDate):
        amount = target_d.y - 1900
        leap1 = amount // 100
        leap2 = (leap1 + 3) // 4
        leap3 = (amount % 100) // 4
        if leap_year(target_d.y):
            leap3 -= 1
        leap_count = leap1 * 24 + leap2 + leap3
        if target_d.m > 2 and leap_year(target_d.y):
            print("lead_year")
            month_day = self.day_of_year[target_d.m - 1] + 1
        else:
            month_day = self.day_of_year[target_d.m - 1]
        # print(target_d.y, amount - leap_count, leap_count, month_day, target_d.d)
        return (amount - leap_count) * 365 + leap_count * 366 + month_day + target_d.d

    def cal_days(self):
        return abs(self.cal_leap_normal_year(self.d1) - self.cal_leap_normal_year(self.d2)) - 1



input_date = input("date:")
d = input_date.strip().split("-")
d1 = HandleDate(d[0])
d2 = HandleDate(d[1])
# print(d[0], d[1])
if d1.check_date() or d2.check_date():
    print("please check date")
else:
    c1 = CalDate(d1, d2)
    print(c1.cal_days())

