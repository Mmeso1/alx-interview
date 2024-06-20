#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys

def print_stats():
    print("File size: {:d}".format(total_size))
    for key in sorted(status.keys()):
        value = status[key]
        if value != 0:
            print("{}: {}".format(key, value))


status = {"200": 0,
          "301": 0,
          "400": 0,
          "401": 0,
          "403": 0,
          "404": 0,
          "405": 0,
          "500": 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        args = line.split(' ')
        if len(args) > 2:
            status_code = args[-2]
            file_size = args[-1]
            if status_code in status:
                status[status_code] += 1
            total_size += int(file_size)
            line_count += 1
            if line_count == 10:
                print_stats()
                line_count = 0
except Exception:
    pass
finally: 
    print_stats()