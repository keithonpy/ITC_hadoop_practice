#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

# Input comes from standard input (sys.stdin)
for line in sys.stdin:
    # Parse the input from mapper.py
    line = line.strip()

    # Split the line into word and count, separated by tab
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # If count was not a number, ignore/discard this line
        continue

    # This IF-switch works because Hadoop sorts the output of the mapper by key (here: word)
    # before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to standard output
            print "%s\t%s" % (current_word, current_count)
        current_count = count
        current_word = word

# Output the last word if needed!
if current_word == word:
    print "%s\t%s" % (current_word, current_count)
