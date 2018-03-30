import tarfile

print('creating archive')
with tarfile.open('tarfile_add.tar', mode='w') as out:
    print('Adding README.txt')
    out.add('README.txt')

print()
print('Contents:')
with tarfile.open('tarfile_add.tar', mode='r') as input:
    for member_info in input.getmembers():
        print(member_info.name)
