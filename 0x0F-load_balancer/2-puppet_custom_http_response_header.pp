#Install Nginx server and include header

package {'nginx':
  ensure => 'present',
}

exec {'install Nginx':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'add_header':
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  provider    => shell,
}

exec {'restart Nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
