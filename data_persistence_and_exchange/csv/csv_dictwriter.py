import csv
import sys
fieldnames = ('Title1', 'Title2', 'Title3', 'Title4')

headers = {
    n: n for n in fieldnames
}

unicode_chars = 'kvm'

with open(sys.argv[1], 'wt') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(3):
        writer.writerow({
            'Title1': i + 1,
            'Title2': chr(ord('a') + i),
            'Title3': '08/{:02d}/07'.format(i+1),
            'Title4': unicode_chars[i],
        })
