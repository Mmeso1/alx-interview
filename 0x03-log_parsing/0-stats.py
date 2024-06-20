#!/usr/bin/python3
"""Log parsing"""
import sys
import re

status = {"200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0
pattern = r"\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d{1,3})"

def print_stats():
    """Print statistics."""
    print("File size: {}".format(total_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    """Main function."""
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
    except KeyboardInterrupt:
        print_stats()

    
        