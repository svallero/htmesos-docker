import utils
import logging

def configure_healthchecks(role, htmframe):
    logging.info('configuring health-checks...')
    content=utils.read_file('/etc/supervisor/conf.d/supervisord.conf')    
    content=content.replace('@ROLE@',role)
 
    if htmframe and role == 'executor':
        logging.info('configuring for htmframe')
        content=content.replace('healthcheck.py','healthcheck_htmf.py')
   
    utils.write_file('/etc/supervisor/conf.d/supervisord.conf', content) 

def configure_publish_queue():
    logging.info('configuring publish_queue...')
    content=utils.read_file('healthchecks/config_publish_queue')    

    utils.append_to_file('/etc/supervisor/conf.d/supervisord.conf', '\n'+content)  
    
