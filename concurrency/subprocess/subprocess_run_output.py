import subprocess

completed = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
print('returnCode', completed.returncode)
print('Have {}bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8')
))
with open('stdout.txt', 'wb') as f:
    f.write(completed.stdout)
