# logging with real time coding

import logging
logging.basicConfig(filename='test4.log',level=logging.critical,format='%(levelname)s %(name)s %(asctime)s %(message)s')

def devide(a,b):
    logging.info("number entered by user %s and %s ", a,b)
    # %S is placeholder which will be store the value of a and b
    try:
        logging.info('we are going into function')
        div= a/b
        logging.info('we have completed division funciton')
        logging.info('this is your result %s',div)
    except Exception as e:      # here capital E
        logging.exception(e)     # here small e remember
#logging.exception for store the error in log file   


devide(8,0)
# logging.info(devide(5,0)
