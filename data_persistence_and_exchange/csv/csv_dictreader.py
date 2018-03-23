import csv
import sys

with open(sys.argv[1]) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
