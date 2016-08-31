import tempfile
import sys
from datetime import datetime
    
def get_temp_file_object(text):
    fp = tempfile.TemporaryFile()
    fp.write(text)
    fp.seek(0)
    return fp



def printer(message):
    sys.stderr.writelines(message)