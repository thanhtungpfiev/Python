# Created by tung.dao at 1/13/2022
try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('This is not allowed')
except Exception as err:
    print('Some other error occurred.', str(err))
