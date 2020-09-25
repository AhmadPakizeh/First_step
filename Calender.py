import calendar

print(calendar.weekheader(1))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 9))
print()

print(calendar.monthcalendar(2020, 9))
print()

print(calendar.calendar(2020))
print()

day_of_the_week = calendar.weekday(2020, 9, 23)

print(day_of_the_week)
print()

is_leap = calendar.isleap(2020)
print(is_leap)
print()

how_many_leap_days = calendar.leapdays(2020, 2025)
print(how_many_leap_days)