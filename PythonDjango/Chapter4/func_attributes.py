# Created by tung.dao thanhtungpfiev@gmail.com at 5/13/2022
def muliplication(a, b=1):
    """Return a multiplied by b."""
    return a * b


special_attributes = [
    "__doc__", "__name__", "__qualname__", "__module__",
    "__defaults__", "__code__", "__globals__", "__dict__",
    "__closure__", "__annotations__", "__kwdefaults__",
]
for attribute in special_attributes:
    print(attribute, '->', getattr(muliplication, attribute))
