# Created by Admin at 5/23/2022
import logging

logging.basicConfig(
    filename='ch10.log',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

mylist = [1, 2, 3]
logging.info('Starting to process `my list`...')

for position in range(4):
    try:
        logging.debug('Value at position %s  is %s', position, mylist[position])
    except IndexError:
        logging.exception('Faulty position: %s', position)

logging.info('Done parsing `mylist`.')
