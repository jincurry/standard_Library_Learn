import pathlib
import tempfile

with tempfile.TemporaryDirectory() as dirctory_name:
    the_dir = pathlib.Path(dirctory_name)
    print(the_dir)
    a_file = the_dir / 'a_file.txt'
    a_file.write_text('this file is delete!')

print('Directory exists after? :', the_dir.exists())
print('Contents after:', list(the_dir.glob('*')))
