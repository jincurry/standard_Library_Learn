import subprocess

completed = subprocess.run(['ls', '-al'])
print('returnCode', completed.returncode)
