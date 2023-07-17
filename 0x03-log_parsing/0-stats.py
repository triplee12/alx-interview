#!/usr/bin/python3
"""Log parsing."""

import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        line = line.strip()
        line = " ".join(line.split()[4:])

        # Check if the line matches the expected format
        if line.startswith('"GET /projects/260 HTTP/1.1"'):
            parts = line.split()

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update metrics
            total_file_size += file_size
            status_code_count[status_code] += 1

            line_count += 1

            # Check if 10 lines have been processed
            if line_count % 10 == 0:
                # Print statistics
                print("Total file size:", total_file_size)
                for code in sorted(status_code_count.keys()):
                    print(code + ":", status_code_count[code])
                print()

    # Print final statistics
    print("Total file size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        print(code + ":", status_code_count[code])

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    pass
