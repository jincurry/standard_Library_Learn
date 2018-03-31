import subprocess

try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print('Error:', err)
else:
    print('returnCode:', completed.returncode)
    print('Have {}bytes in stdout.\n{}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8')
    ))
    print('Have {}bytes in stderr.{!r}'.format(
      len(completed.stderr), completed.stderr.decode('utf-8')
    ))
