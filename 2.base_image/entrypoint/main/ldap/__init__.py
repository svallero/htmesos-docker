import utils
import logging
 
def configure_sssd(ldap_config):
    logging.info("configuring sssd...")
    filename='/etc/sssd/sssd.conf'
    content=utils.read_file(filename)     
    # substitute search strings from config file
    search_base=utils.get_config(ldap_config,'search_base', '', True) 
    user_search_base=utils.get_config(ldap_config,'user_search_base', '', True) 
    group_search_base=utils.get_config(ldap_config,'group_search_base', '', True) 
    server=utils.get_config(ldap_config,'server', '', True) 
    content=content.replace('@SEARCH_BASE@', search_base)    
    content=content.replace('@USER_SEARCH_BASE@', user_search_base)    
    content=content.replace('@GROUP_SEARCH_BASE@', group_search_base)    
    content=content.replace('@SERVER@', server)    
    utils.write_file(filename, content)
 
def configure_supervisor():
    logging.info("configuring sssd...")
    data=utils.read_file('ldap/supervisor_sssd.conf')  
    utils.append_to_file('/etc/supervisor/conf.d/supervisord.conf', data)

def configure_auth_keys_command(ldap_config):
    logging.info("configuring ldapAuthorizedKeysCommand...")
    server=utils.get_config(ldap_config,'server', '', True)
    search_base=utils.get_config(ldap_config,'search_base', '', True) 
    
    filename='/sbin/ldapAuthorizedKeysCommand'
    content=utils.read_file(filename)     
    content=content.replace('@SERVER@', server)    
    content=content.replace('@SEARCH_BASE@', search_base)    
    utils.write_file(filename, content)
    
