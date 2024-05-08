# install and configure nginx server

exec {'apt-get update':
	command => '/usr/bin/apt-get update -y'
}

package {'nginx':
	ensure => 'installed'
}

exec {'ufw allow':
	command => '/usr/bin/ufw allow "Nginx HTTP"'
}

exec {'hello world':
	command => 'echo "Hello World!" > /var/www/html/index.nginx-debian.html'
}

exec {'301':
  command => 'sudo sed -i "/listen 80 default_server/a location = /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; }" /etc/nginx/nginx.conf'
}

service { 'nginx':
   ensure => running,
   enable => true
}
