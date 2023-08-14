# This puppet script fixes a 500 error

exec { 'fix_error':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin','/usr/bin']
}
