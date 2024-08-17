# Fix Apache 500 error due to improper "php" aliasing

exec { 'Resolve "php" aliasing error':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
