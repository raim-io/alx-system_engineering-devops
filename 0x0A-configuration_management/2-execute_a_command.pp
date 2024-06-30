# Kill the process named 'killmenow'

exec { 'kill the process killmenow':
  command    => 'pkill killmenow',
  provider => 'shell',
}
