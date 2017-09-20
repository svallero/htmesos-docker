import sys
import argparse
import json
from pprint import pprint
import users
import ssh 
import condor
import healthchecks
import utils
import ldap

def main():
    """ Main entry point for the script."""
    ### Parse the config file
    parser = argparse.ArgumentParser(description='Entrypoint.')
    parser.add_argument('config_file', nargs=1,
                    help='path to configuration file')

    args = parser.parse_args()
    print "Reading config file: ", args.config_file[0]

    with open(str(args.config_file[0])) as data_file:    
      config = json.load(data_file)
    # pprint(data)    
   
    ### Configure role 
    print "Role must be one of: master, submitter, executor" 
    role=utils.get_config(config, 'role', '', True)
    print "Configuring role: ", role 
    
    ### Setup root public key
    print "Setting up root public key..."
    rpc=utils.get_config(config, 'root_public_key', '', False)
    if rpc:   
       users.setup_root_public(rpc)

    ### Users and ssh access 
    print "### Setting up users..."
    ldap_config=utils.get_config(config,'ldap', {}, False)
    if ldap_config:
        print "configuring LDAP client..." 
        ldap.configure_sssd(ldap_config)
    else: 
        usr=utils.get_config(config, 'users', [], False)
        if usr:   
          users.setup_users(usr) 
          ssh.setup()
 
    ### Condor configuration
    print "### Configuring htcondor..."
    condor_c=utils.get_config(config, 'condor_config', {}, False)
    if condor_c:
        # custom config file
        config_url=utils.get_config(condor_c, 'config_url', '', False)
        if config_url:
          condor.set_custom_config(config_url)
        # shared secret 
        shared_secret=utils.get_config(condor_c, 'shared_secret', '', False)
        if shared_secret:
          condor.set_shared_secret(shared_secret)
    # set role daemons
    master_address=utils.get_config(config, 'master_address', '', True)
    condor.set_role_daemons(role, master_address)
    
    ### Health-checks
    # if we use htmframe, the executor's healthckeck is different
    # and the submitter should publish some additional info
    print "### Configuring helath-checks..."
    htmframe=utils.get_config(config, 'htmframe', False, False)
    healthchecks.configure_healthchecks(role, htmframe)
    if (htmframe and role == 'submitter'):
        healthchecks.configure_publish_queue()
        
    ### This is the real entrypoint
    print '### Starting supervisord...'
    utils.runcmd('/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf')

    pass

if __name__ == '__main__':
    sys.exit(main())
