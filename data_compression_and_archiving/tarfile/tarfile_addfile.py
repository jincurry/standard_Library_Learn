import tarfile

print('creating archive')
with tarfile.open('tarfile_add.tar', mode='w') as out:
    print('Adding README.txt as RENAMED.txt')
    info = out.gettarinfo('README.txt', arcname='RENAMED.txt')
    out.addfile(info)

print()
print('Contents:')
with tarfile.open('tarfile_add.tar', mode='r') as input:
    for member_info in input.getmembers():
        print(member_info.name)
