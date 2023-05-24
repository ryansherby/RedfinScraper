import functools
import logging
import time
from queue import Queue

class OrderedQueueHandler(logging.Handler):
    def __init__(self,filename):
        super().__init__()
        self.queue = Queue()
        self.filename = filename

    def emit(self, record):
        msg = self.format(record)
        self.queue.put(msg)

    def flush(self,mode='a'):
        with open(self.filename, mode) as f:
            while not self.queue.empty():
                msg = self.queue.get()
                f.write(msg + '\n')


logger=logging.Logger(__name__)
handler=OrderedQueueHandler("./package.log")

formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(message)s',datefmt='%b-%d-%y %H:%M:%S')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger.addHandler(handler)




def reset_log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        logger.info("*****Beginning Log*****")
        handler.flush(mode='w')
        func(*args,**kwargs)

    return wrapper




def timing_log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
     
        logger.info(f"Function {func.__name__} started.")
        handler.flush()
        
        tic=time.perf_counter()
        obj=func(*args,**kwargs)
        toc=time.perf_counter()

        logger.info(f"Function {func.__name__} took {toc-tic} seconds.")
        handler.flush()
        return obj
    return wrapper

        

def log_no_zip(func):
    @functools.wraps(func)
    def wrapper(self,zip_list,city_state):
   
        bool=func(self,zip_list,city_state)

        message=f"KEY ERROR: Zip Codes for {city_state} could not be found."

        if bool:
            logger.warning(message)
            handler.flush()

    return wrapper



def log_404(func):
    @functools.wraps(func)
    def wrapper(self,req,url):


        bool=func(self,req,url)

        message=f"HTTPS ERROR: {url} could not be found."

        if bool:
            logger.warning(message)
            handler.flush()

    return wrapper


def log_no_API_link(func):
    @functools.wraps(func)
    def wrapper(self,url):
      
        bool=func(self,url)

        message=f"HTTPS ERROR: API link for {url} could not be found."

        if bool:
            logger.warning(message)
            handler.flush()

    return wrapper

handler.flush()