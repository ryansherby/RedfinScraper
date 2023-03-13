import functools
import datetime
import logging
import time


def reset_log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        logging.basicConfig(filename='package.log',filemode='w',encoding='utf-8',
                            format='%(asctime)s: %(levelname)s - %(message)s',
                            datefmt='%b-%d-%y %H:%M:%S',level=logging.INFO)
        logging.info("*****Beginning Log*****")
        func(*args,**kwargs)

    return wrapper




def timing_log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        logging.basicConfig(filename='package.log',filemode='w',encoding='utf-8',
                            format='%(asctime)s: %(levelname)s - %(message)s',
                            datefmt='%b-%d-%y %H:%M:%S')
        logging.info("Function started.")
        tic=time.perf_counter()
        obj=func(*args,**kwargs)
        toc=time.perf_counter()
        logging.info(f"Function {func.__name__} took {toc-tic} second.")
        return obj
    return wrapper

        

def log_no_zip(func):
    @functools.wraps(func)
    def wrapper(self,zip_list,city_state):
        logging.basicConfig(filename='package.log',filemode='a',encoding='utf-8',
                            format='%(asctime)s: %(levelname)s - %(message)s',
                            datefmt='%b-%d-%y %H:%M:%S')
        bool=func(self,zip_list,city_state)

        message=f"KEY ERROR: Zip Codes for {city_state} could not be found."

        if bool:
            logging.error(message)

    return wrapper



def log_404(func):
    @functools.wraps(func)
    def wrapper(self,req,url):
        logging.basicConfig(filename='package.log',filemode='a',encoding='utf-8',
                            format='%(asctime)s: %(levelname)s - %(message)s',
                            datefmt='%b-%d-%y %H:%M:%S')

        bool=func(self,req,url)

        message=f"HTTPS ERROR: {url} could not be found."

        if bool:
            logging.error(message)

    return wrapper