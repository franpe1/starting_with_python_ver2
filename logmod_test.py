import logging

logging.basicConfig(level=logging.INFO, 
                    filename='myserver.log', # log to this file
                    format='%(asctime)s %(message)s') # include timestamp
logging.info("some message")
