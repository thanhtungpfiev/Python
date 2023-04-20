# Created by Admin at 5/19/2022
class Exception1:
    pass


class Exception2:
    pass


class Exception3:
    pass


class Exception4:
    pass


try:
    pass
    # some code
except Exception1:
    pass
    # react to Exception1
except (Exception2, Exception3):
    pass
    # react to Exception2 or Exception3
except Exception4:
    pass
    # react to Exception4
