#!/usr/bin/python3
'''Log parsing'''

import sys
import re


def print_stats():
    print("File size: {}".format(total_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0
pattern = r"\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d{1,3})"

try:
    for line in sys.stdin:
        args = line.split(' ')
        if len(args) > 2:
            status_line = args[-2]
            file_size = args[-1]
            if status_line in status:
                status[status_line] += 1
            total_size += int(file_size)
            i += 1
            if i == 10:
                print_stats()
                i = 0
except Exception:
    pass
finally:
    print_stats()
