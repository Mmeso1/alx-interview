#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys
import re


def print_stats():
    print("File size: {:d}".format(total_size))
    for key in sorted(status.keys()):
        value = status[key]
        if value != 0:
            print("{}: {}".format(key, value))


status = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0
pattern = r"\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d{1,3})"

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            status_code = match.group(1)
            file_size = match.group(2)
            line_count += 1
            if status_code in status:
                status[status_code] += 1
            total_size += int(file_size)
        if line_count % 10 == 0:
            print_stats()
            line_count = 0
except KeyboardInterrupt:
    print_stats()
