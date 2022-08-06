#  logged data with timestamp
import logging
# logging.basicConfig(filename='test2.log' , level = logging.DEBUG ,format='%(asctime)s %(message)s')
# format print system time in str as well as message as str in log file
# 2022-08-06 17:33:21,745 this is my log with timestamp   .....output of format

# logging.info('this is my log with timestamp')

logging.basicConfig(filename='test2.log',level=logging.DEBUG,format='%(levelname)s %(name)s %(asctime)s %(message)s')
logging.info('full format with name and level and time as well as message')