#!/usr/bin/python

import sys, getopt, re
from api_rest import ApiREST
from xml.etree.cElementTree import iterparse
from helper import get_temp_file_object, printer

APIURL = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'

def usage():
    printer ('run.py -db <database> -id <identifier> -rgx <regular expression> -o <outputfile>')
    printer ('All arguments are mandatory. -id must be non positive integer')    
    
def main(argv):
    
    try:
        opts, args = getopt.getopt(argv,"d:i:r:o:h")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    param = {}
    db = id = regex = output = None   
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit(2)
            
        elif opt == '-d':
            db = arg
        elif opt == '-i':
            id = arg
        elif opt == '-r':
            regex = arg
        elif opt == '-o':
            output = arg

    if None in [db,id,regex,output]:
        usage()
    else:
        param = {
            'db' : db,
            'id' : id,
            'rettype' : 'fasta',
            'retmode' : 'xml'
        }
        
        
        # Get xml File from url
        api = ApiREST()
        rs = api.get(APIURL, param)
        if not rs:
            printer("Error : cannot find result for database:{} and id/s:{}".format(db,id))
            sys.exit(2)
        if rs:
            # Store output in temp file
            result = ''
            fp = get_temp_file_object(rs)
            try:
                ofp = open(output, 'w+')
            except:
                printer('Error : cannot write output to "{}"'.format(output))
                sys.exit(2)
                
            try:
                # Iterate over xml tree
                for event, element in iterparse(fp):
                    if element.tag in ['TSeq_sequence']:
                        #iterate through text and search for patern
                        for match in re.finditer(regex, element.text):
                            ofp.write("{}, {}, {}\n".format(match.group(1),match.start()+1, match.end()))
                    
                    if event == 'end':
                        element.clear()
                
                # Write Output to file
                printer("\n Output File : {} \n".format(output))
                ofp.close()
                
            except:
                printer("Error : Invalid XML file!")    
            
        
if __name__ == "__main__":
    main(sys.argv[1:])
    
    
#python run.py -d nucleotide -i "30271926" -r "(A)" -o "out.txt"    
    
