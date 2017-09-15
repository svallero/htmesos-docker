import utils

def setup():
  utils.runcmd('ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa')
  utils.runcmd('ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa')
  utils.runcmd('ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519')

  data=utils.read_file('ssh/supervisor_ssh.conf') 
  print data

  utils.append_to_file('/etc/supervisor/conf.d/supervisord.conf', data) 
