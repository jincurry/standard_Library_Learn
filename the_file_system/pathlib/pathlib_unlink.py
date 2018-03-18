import pathlib
import time

p = pathlib.Path('touched')

p.touch()

print('exists before removing :', p.exists())

time.sleep(30)

p.unlink()

print('exists after removing :', p.exists())
