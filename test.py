from http_request import HttpRequest, default_cache_key_calculator
from reactivex import operators as ops

import logging
logging.basicConfig(level=logging.DEBUG)
    
if __name__ == '__main__':
    request = HttpRequest(cache_key_calculator=default_cache_key_calculator)
    response1 = request.get_response_stream("https://www.google.com")
    response1.pipe(ops.map(lambda res: None)).subscribe()
    
    response2 = request.get_response_stream("https://www.google.com")
    response2.pipe(ops.map(lambda res: None)).subscribe()