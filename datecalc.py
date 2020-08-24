#!/usr/bin/env python
"""
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
"""

import sys
from datetime import datetime

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


def apply_delta(ts, delta):
    delta_parsed = {i: int(j) for i, j in [n.split("=") for n in delta.split(",")]}
    rdelta = relativedelta(**delta_parsed)
    return (ts + rdelta).strftime("%A, %d %B %Y")


def calculate_delta(from_date, to_date):
    print(from_date - to_date)
    rdelta = relativedelta(from_date, to_date)
    return f"{rdelta.years} years, {int(rdelta.months)} months and {rdelta.days} days"


if len(sys.argv) == 3:
    if "=" in sys.argv[2]:
        print(apply_delta(parse(sys.argv[1]).date(), sys.argv[2]))
    else:
        to_date, from_date = sorted(
            [parse(sys.argv[1]).date(), parse(sys.argv[2]).date()]
        )

        print(calculate_delta(from_date, to_date))
elif len(sys.argv) == 2:
    if "=" in sys.argv[1]:
        print(apply_delta(datetime.now().date(), sys.argv[1]))
    else:
        to_date, from_date = sorted([parse(sys.argv[1]).date(), datetime.now().date()])

        print(calculate_delta(from_date, to_date))
else:
    print("no input")
