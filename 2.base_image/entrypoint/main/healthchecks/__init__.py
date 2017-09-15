import utils

def configure_healthchecks(role, htmframe):
    print 'configuring health-checks...'
    content=utils.read_file('/etc/supervisor/conf.d/supervisord.conf')    
    content.replace('@ROLE@',role)
 
    if htmframe and role == 'executor':
        print 'info: configuring for htmframe'
        content.replace('executor_healthcheck.py','executor_healthcheck_htmf.py')
   
    utils.write_file('/etc/supervisor/conf.d/supervisord.conf', content) 

def configure_publish_queue():
    print 'configuring publish_queue...'
    content=utils.read_file('healthchecks/config_publish_queue')    

    utils.append_to_file('/etc/supervisor/conf.d/supervisord.conf', '\n'+content)  
    
