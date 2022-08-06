from distutils.debug import DEBUG
from distutils.log import ERROR
import logging
# print('loaded')
logging.basicConfig(filename='test.log',level=logging.INFO)

# logging.info('this is my first loging code')   # this is like print statement
logging.error('there is chance of error')
l= list(range(1,11))
for i in l:
    if i==2:
        logging.info(i)
        logging.warning('there is possibility yha 2 list me ho hi na')
        logging.info('this is like as print statement')
        logging.info(l) 

# this is nothing but it is a process in which we want try print output
# of any file or our code into the log file , that i can analyse the 
# error at the run time of program.


# ......... there are only 5 types of log level
# 1  DEBUG   10
# 2  WARNING  30
# 3  CRITICAL 50
# 4  ERROR  40
# 5  INFO  20 