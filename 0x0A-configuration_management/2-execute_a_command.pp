# Kill the process named 'killmenow'

exec { 'kill the process killmenow':
  path => '/bin/',
  command    => 'pkill killmenow',
}
