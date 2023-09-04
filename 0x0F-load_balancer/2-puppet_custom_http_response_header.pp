#Install Nginx server and include header

package {'nginx':
  ensure => 'present',
}

exec {'install Nginx':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
}

-> file_line { 'add_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => 'http {\n\t add_header X-Served-By \"${hostname}\";'
}

exec {'restart Nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
