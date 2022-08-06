import logging
logging.basicConfig(filename='test5.log',level=logging.INFO,format='%(levelname)s %(name)s %(asctime)s %(message)s')
try:
    logging.info('entered in try')   # in DEBUG is True
    with open('sudh.txt','r'):
        logging.info('successful is read the file')
except Exception as e:
    logging.exception(e)
    logging.error(e)
    logging.critical('critical section')