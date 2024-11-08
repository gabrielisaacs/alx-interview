#!/usr/bin/python3
"""
A Python script that reads stdin line by line and computes the metrics.
"""

import sys
import re
import signal


def output(log: dict) -> None:
    """
    Helper function to display stats.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'(\d{3}) (\d+)'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
        }
    }

    def handle_exit(*args):
        output(log)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit)

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # Update file size
                log["file_size"] += file_size

                # Update status code frequency if valid
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                # Output after every 10 lines
                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        output(log)
        sys.exit(0)
    finally:
        output(log)
