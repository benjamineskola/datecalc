datecalc: calculate date differences.

Usage:

    datecalc [date]  # returns the difference between the current date and the specified date
    datecalc [timedelta]  # returns the result of applying the timedelta to the current date
    datecalc [date] [date]  # returns the difference between the two specified dates
    datecalc [date] [timedelta]  # returns the result of applying the timedelta to the specified date

Timedeltas consist of comma-separated key=value pairs where the value is a
number and the key is a unit of time, e.g.:

    years=1  # one year in the future
    years=-1  # one year in the past
    months=6,days=14  # 6 months, 14 days in the future
    months=-6,days=-14  #  6 months, 14 days in the past
