# Created by Admin at 5/23/2022
class ValidatorError(Exception):
    """Raised when accessing a dict results in KeyError. """


d = {'some': 'key'}
mandatory_key = 'some_other'
try:
    print(d[mandatory_key])
except KeyError as err:
    raise ValidatorError(
        f'`{mandatory_key}` not found in d.'
    ) from err
