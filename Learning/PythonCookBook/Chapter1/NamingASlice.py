# Created by Admin at 5/9/2022
######   0123456789012345678901234567890123456789012345678901234567890'
record = '....................100         .......513.25     ..........'

SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost = int(record[SHARES]) * float(record[PRICE])
