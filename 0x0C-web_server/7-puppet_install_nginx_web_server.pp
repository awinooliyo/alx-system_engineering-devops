# Configuring server using puppet
# Nginx should be listening on port 80

include stdlib

package { 'nginx':
  ensure => installed,
}

exec { "install nginx":
  command  => 'sudo apt -y update && sudo apt -y install nginx',
  provider => shell,
}

file { "/etc/nginx/sites-available/default":
  content => "server {
                listen 80 default_server;
                root /var/www/html; # Added space here
                location / {
                  index index.html;
                }
                rewrite ^/redirect_me https://www.youtube.com permanent;
              }",
  require => Exec['install nginx'],
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Exec['install nginx'],
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}

