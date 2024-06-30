# SSH config using puppet
include stdlib

file_line { 'Do not require password authentication':
    ensure => present,
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no'
}

file_line { 'Require private key authentication':
    ensure => present,
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school'
}