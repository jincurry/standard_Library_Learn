import subprocess

try:
    subprocess.run(['ls', '-al'], check=True)
except subprocess.CalledProcessError as err:
    print('Error:', err)
