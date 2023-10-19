#Increase the open file limit of hiberton user

exec {'increase_hard':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 5000/" /etc/security/limits.conf',
  before   => Exec['increase_soft'],
}

exec {'increase_soft':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 4000/" /etc/security/limits.conf',
}
