#!/usr/bin/python3
'''
    Log Parsing.
'''

import re
from sys import stdin


def print_logs_stats(file_size, stats):
    '''
        Prints the generated statistics.
    '''
    print(f'File size: {file_size}')
    for code, count in sorted(stats.items()):
        print(f'{code}: {count}')


if __name__ == '__main__':
    n = 0
    file_size = 0
    stats = {}
    pattern = re.compile(r'''
        \d+\.\d+\.\d+\.\d+ # ip address
        \s-\s\[(.*?)\]\s # date
        "GET\s/projects/260\sHTTP/1.1"\s # request line
        (?P<status_code>\d+)\s # status code
        (?P<file_size>\d+) # file size
    ''', re.VERBOSE)
    try:
        for line in stdin:
            match = pattern.match(line)
            if match:
                file_size += int(match.group('file_size'))
                status_code = match.group('status_code')
                if status_code in stats:
                    stats[status_code] += 1
                else:
                    stats[status_code] = 1
                n += 1
            if n % 10 == 0:
                print_logs_stats(file_size, stats)

    except (KeyboardInterrupt, EOFError):
        print_logs_stats(file_size, stats)