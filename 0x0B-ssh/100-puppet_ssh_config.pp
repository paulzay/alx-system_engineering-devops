# setup ssh with puppet
exec { 'echo':
  command => 'echo "PasswordAuthentication no" >> .etc/ssh/sshd_config'
  path => ['/usr/bin', '/usr/sbin', '/bin']
}

exec {'restart':
  command => 'sudo service ssh restart'
  path => ['/usr/bin', '/usr/sbin', '/bin']
}

exec {'ssh':
  command => 'ssh -A -i ~/.ssh/school ubuntu@100.27.12.25'
  path => ['/usr/bin', '/usr//sbin/', '/bin']
}
