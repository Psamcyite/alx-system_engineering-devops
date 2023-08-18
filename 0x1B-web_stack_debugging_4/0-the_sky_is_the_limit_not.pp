# This puppet script fixes the limit for number of open files on an Nginx server

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec {'restart-nginx':
  command     => 'service nginx restart',
  path        => '/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}
