from time import time
import requests, urllib
from helper import printer

class ApiREST(object):
    error = None
    
    def get(self,url,data={}, headers={}):
        self.error = None
        result = None
        
        if url is None or url == '':
            return None
        
        url = url + '?' + urllib.urlencode(data)
        
        start_time = time()
        result = requests.get(url, headers=headers)
        total_time = time() - start_time
        print('API Get Request : ' + url + ' |  Response time : ' + total_time.__repr__())

        if result.status_code == 200:
            return result.text            
        else:
            printer("Error : API call failed for %s with status code %i" % (url, result.status_code))
            return result