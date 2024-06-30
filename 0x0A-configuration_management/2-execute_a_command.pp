# Kill the process named 'killmenow'

exec { 'kill the process killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}