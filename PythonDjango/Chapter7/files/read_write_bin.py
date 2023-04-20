# Created by Admin at 5/18/2022
with open('example_bin', 'wb') as fw:
    fw.write(b'This is binary data...')

with open('example_bin', 'rb') as f:
    print(f.read())
