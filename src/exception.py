import sys
from src.logger import logging

def error_msg_detail(error,error_detail:sys):
    # It will give details about exceptions that has occurred in which line , which file etc.
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = 'Error occurred in Python script name: [{0}] in line number [{1}] error message [{2}]'.format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_msg
    

class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_detail(error_msg,error_detail=error_detail)
    
    def __str__(self):
        return self.error_msg

if __name__=='__main__':
    try:
        a=1/0
    
    except Exception as e:
        logging.info('Logging started')
        raise CustomException(e,sys)
