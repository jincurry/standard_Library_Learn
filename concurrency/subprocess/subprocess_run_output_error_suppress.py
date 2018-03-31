import subprocess

try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
except subprocess.CalledProcessError as err:
    print('Error:', err)
else:
    print('returnCode', completed.returncode)
    print('stdout is {!r}'.format(completed.stdout))
    print('stderr is {!r}'.format(completed.stderr))
