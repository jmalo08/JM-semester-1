# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_date(day, month, year, separator="-"):
    formatted_date = f"{day:02d}{separator}{month:02d}{separator}{year:02d}"
    return formatted_date

print(format_date(22,10, 2026, separator="."))
