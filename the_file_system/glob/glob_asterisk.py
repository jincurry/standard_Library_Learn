import glob

for name in sorted(glob.glob('dir/*')):
    print(name)
