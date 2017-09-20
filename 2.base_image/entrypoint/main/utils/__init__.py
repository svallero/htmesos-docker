import os
import sys
import requests
import logging

def get_config(dictionary, key, default, exit):
    # given a dictionary, get the key value or assign default
    # exit true means abort if key is not defined
    value=default
    try:
        value=dictionary[key]
    except:
        if not exit:
            logging.warning('setting '+key+' to default value: '+default)
        else:
            logging.error('parameter '+key+' must be defined')
            sys.exit(1) 
    return value

def runcmd(cmd):
    # TODO: must be improved to catch system errors
    try:
        logging.info(cmd)
        os.system(cmd) 
    except:
        logging.error('error running command: ')
        logging.error(cmd)
        raise

def url_to_file(url, dest_file, append):
    content=requests.get(url).text.strip()

    if append:
        append_to_file(dest_file, content)    
    else:
        write_file(dest_file, content)    


def read_file(filename):
    with open (filename, 'r') as r_file:
        data=r_file.read().strip() 
    return data

def append_to_file(filename, string):
    with open(filename, 'a') as a_file:
        a_file.write('\n'+string) 
  
def write_file(filename, string):
    with open(filename, 'w') as w_file:
        w_file.write(string) 
