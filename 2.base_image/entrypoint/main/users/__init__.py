import utils

def setup_users(users):
  for u in users:
      # read config values
      name=utils.get_config(u, 'name', '', True)
      uid=utils.get_config(u, 'uid', -1, False)
      password=utils.get_config(u, 'password', 'dummy', False)
      keyurl=utils.get_config(u, 'key', '', False)
     
      # create user
      useradd(name, uid)
      # set password 
      chpasswd(name, password)
      # setup ssh access
      if keyurl: 
        setup_key(name, keyurl)

def useradd(name, uid):

    args=name+" -d /home/"+name+" -s /bin/bash"
    if uid:
        args+=' -u '+str(uid) 
    utils.runcmd('useradd '+args)

    utils.runcmd('mkdir -p /home/'+name)
    utils.runcmd('chown -R '+name+':'+name+' /home/'+name)

def chpasswd(name, password):

    utils.runcmd('echo '+name+':'+password+' | chpasswd')

def setup_key(name,keyurl):

    folder='/home/'+name+'/.ssh' 

    utils.runcmd('mkdir -p '+folder)
    utils.runcmd('chmod 700 '+folder)
    
    utils.url_to_file(keyurl, folder+'/authorized_keys', True)
    utils.runcmd('chmod 600 '+folder+'/authorized_keys')
    utils.runcmd('chown -R '+name+':'+name+' '+folder)

def setup_root_public(keyurl):
 
    utils.url_to_file(keyurl, '/root/.ssh/authorized_keys', True)
