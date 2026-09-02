import calendar

# Full month names (slicing out the empty index 0)
full_months_cal = list(calendar.month_name)[1:]
print(full_months_cal)

# Abbreviated month names
short_months_cal = list(calendar.month_abbr)[1:]
print(short_months_cal)
