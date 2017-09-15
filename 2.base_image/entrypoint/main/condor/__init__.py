import requests
import sys
import utils

def set_custom_config(config_url):
    print "writing custom config..."
    utils.url_to_file(config_url, '/etc/condor/condor_config', False)    

def set_shared_secret(shared_secret):
     print "setting shared secret..."
     data=utils.read_file('condor/config_secret')
     utils.append_to_file('/etc/condor/condor_config', '\n'+data)
     utils.runcmd("condor_store_cred -f /etc/condor/condorSharedSecret -p "+shared_secret) 

def set_role_daemons(role,master_address):
     print "setting role daemons..."
     daemons=""
     if role == 'master':
        daemons='COLLECTOR, NEGOTIATOR'
     elif role == 'submitter':
        daemons='SCHEDD'
     elif role == 'executor':
        daemons='STARTD'
     else:
       print 'error: role must be one of master, submitter or executor!'
       sys.exit(1)     

     content=utils.read_file('/etc/condor/condor_config') 
     content.replace("@ROLE_DAEMONS@", daemons)
     
     if role == 'master':
       content.replace("@CONDOR_HOST@", "$(IP_ADDRESS)")
       content+="\n\nCOLLECTOR_HOST=$(IP_ADDRESS)"
     else:
       content.replace("@CONDOR_HOST@", master_address)
    
     utils.write_file('/etc/condor/condor_config', content) 

     
