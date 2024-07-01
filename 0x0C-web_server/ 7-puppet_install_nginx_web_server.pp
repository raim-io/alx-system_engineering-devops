# Define a class for Nginx configuration
class nginx_config {

  # Package installation and service management
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  # Nginx server configuration file
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Symbolic link to enable the site
  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify => Service['nginx'],
  }

  # Default index.html file
  file { '/var/www/html/index.html':
    ensure  => present,
    content => "Hello World!\n",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Apply the nginx_config class to configure Nginx
include nginx_config
