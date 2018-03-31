import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returnCode', completed.returncode)
