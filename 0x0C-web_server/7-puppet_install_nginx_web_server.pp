# install and configure nginx server

$packages = ['nginx', 'ufw']

exec {'apt-get update':
	command => '/usr/bin/apt-get update -y'
}

package {$packages:
	ensure => 'installed'
}

exec {'ufw allow':
	command => '/usr/bin/ufw allow "Nginx HTTP"'
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
   ensure => running,
   enable => true
}
