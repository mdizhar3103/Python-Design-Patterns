from datetime import datetime
from singleton_meta import Singleton


class Logger(metaclass=Singleton):
    log_file = None
 
    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode='w')
 
    def write_log(self, log_record):
        now = str(datetime.now())
        record = "%s: %s\n" % (now, log_record)
        self.log_file.write(record)
 
    def close_log(self):
        self.log_file.close()
        self.log_file = None
 
    
logger = Logger("my.log")
logger.write_log("Logging with classic Singleton pattern")
logger2 = Logger("********ignored********")
logger2.write_log("Another log record")
 
logger.close_log()
 
with open("my.log", 'r') as f:
    for line in f:
        print(line, end='')
