import requests
import sys
import utils
import logging

def set_custom_config(config_url):
    logging.info("writing custom config...")
    utils.url_to_file(config_url, '/etc/condor/condor_config', False)    

def set_shared_secret(shared_secret):
     logging.info("setting shared secret...")
     data=utils.read_file('condor/config_secret')
     utils.append_to_file('/etc/condor/condor_config', '\n'+data)
     utils.runcmd("condor_store_cred -f /etc/condor/condorSharedSecret -p "+shared_secret) 

def set_role_daemons(role,master_address):
     logging.info("setting role daemons...")
     daemons=""
     if role == 'master':
        daemons='COLLECTOR, NEGOTIATOR'
     elif role == 'submitter':
        daemons='SCHEDD'
     elif role == 'executor':
        daemons='STARTD'
     else:
       logging.error('role must be one of master, submitter or executor!')
       sys.exit(1)     

     content=utils.read_file('/etc/condor/condor_config') 
     content=content.replace('@ROLE_DAEMONS@', daemons)
     
     if role == 'master':
       content=content.replace("@CONDOR_HOST@", "$(IP_ADDRESS)")
       content+="\n\nCOLLECTOR_HOST=$(IP_ADDRESS)"
     else:
       content=content.replace("@CONDOR_HOST@", master_address)
     #print content  
     utils.write_file('/etc/condor/condor_config', content) 

     
