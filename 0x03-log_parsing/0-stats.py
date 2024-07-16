#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        
        parts = line.split()
        if len(parts) < 7:
            continue
        
        ip_address = parts[0]
        date = parts[3][1:] + ' ' + parts[4][:-1]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = parts[-2]
        file_size = parts[-1]
        
        # Validate the input format
        if request != '"GET /projects/260 HTTP/1.1"':
            continue
        if not status_code.isdigit():
            continue
        if not file_size.isdigit():
            continue
        
        status_code = int(status_code)
        file_size = int(file_size)
        
        # Update metrics
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        line_count += 1
        
        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print("Error: {}".format(e))