#!/usr/bin/env python

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
