#!/usr/bin/env python
import sys

# Input comes from standard input (sys.stdin)
for line in sys.stdin:
    # Remove whitespace at the beginning and the end
    line = line.strip()

    # Split the line into words
    words = line.split()

    # Output tuples (word, 1) in tab-delimited format
    for word in words:
        print "%s\t%s" % (word, 1)
