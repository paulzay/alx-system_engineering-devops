exec {'setup ssh':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/sshd_config'
  command => 'sudo service ssh restart'
  command => 'ssh -A -i ~/.ssh/school ubuntu@100.27.12.25'
}
