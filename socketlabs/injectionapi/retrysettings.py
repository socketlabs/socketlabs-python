from datetime import timedelta
import random

class RetrySettings(object):

    __default_number_of_retries = 0
    __maximum_allowed_number_of_retries = 5
    __minimum_retry_time = timedelta(seconds=1)
    __maximum_retry_time = timedelta(seconds=10)

    def __init__(self, maximum_retries = None):

        if maximum_retries:

            if maximum_retries < 0:
                raise AttributeError("maximumNumberOfRetries must be greater than 0")

            if maximum_retries > self.__maximum_allowed_number_of_retries:
                raise AttributeError("The maximum number of allowed retries is ", self.__maximum_allowed_number_of_retries)

            self.__maximum_number_of_retries = maximum_retries
            
        else:
            self.__maximum_number_of_retries = self.__default_number_of_retries
        
    @property
    def maximum_number_of_retries(self):
        return self.__maximum_number_of_retries
    
    def get_next_wait_interval(self, number_of_attempts):
        
        interval = int(min(
            ((self.__minimum_retry_time.seconds * 1000) + self.get_retry_delta(number_of_attempts)),
            (self.__maximum_retry_time.seconds * 1000)
            ))
        
        return timedelta(milliseconds=interval)
    
    def get_retry_delta(self, number_of_attempts):
        
        minimum = (int)((timedelta(seconds=1).seconds * 1000) * 0.8)
        maximum = (int)((timedelta(seconds=1).seconds * 1000) * 1.2)

        return (int)((pow(2.0, number_of_attempts) - 1.0) * random.randint(minimum, maximum))