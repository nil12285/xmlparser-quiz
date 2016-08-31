# xmlparser-quiz

### Design/Module Choices
* I used XML cElementTree instead of ElementTree because, the cElementTree module is a C implementation of the ElementTree API, optimized for fast parsing and low memory use. On typical documents, cElementTree is 15-20 times faster than the Python version of ElementTree and uses 2-5 times less memory.
(http://effbot.org/zone/celementtree.htm)

* I tried to abstract out all that can be reusable outside this program. 
 - I have ```get_temp_file_objectand()``` and  ```printer()``` as helper
 - I have ```get()``` as part of ApiTEST.  Reason behind this is; It can be extended with other HTTP methods 

### How to Run?
```
python run.py -d nucleotide -i "30271926" -r "(A)" -o "out.txt"
```
