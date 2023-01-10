# Creates a manifest executes killmenow command

exec { 'killmenow':
    command  => 'pkill killmenow',
    path     => '/usr/bin',
    provider => 'shell',
}
