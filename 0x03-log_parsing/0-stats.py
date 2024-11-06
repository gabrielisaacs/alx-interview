#!/usr/bin/env python3
"""
A Python script that reads stdin line by line and computes the metrics:
    - Total file size
    - Number of occurrences of specified status codes
"""

import sys
import signal

status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
}

total_size = 0
line_count = 0


def print_stats():
    """
    Prints the accumulated statistics
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """
    Handles keyboard interrupt signal
    """
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        p = parts

        if len(p) < 7 or not p[-1].isdigit() or not p[-2].isdigit():
            continue

        # Extract data
        try:
            status_code = p[-2]
            file_size = int(p[-1])
        except ValueError:
            continue

        # update metrics
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        # print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats when interrupted
    print_stats()
    sys.exit(0)
