# Set Nginx max open files

service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => Exec['/etc/default/nginx'],
}

exec { '/etc/default/nginx':
    command => "sed -i 's/15/50000/g' /etc/default/nginx",
    path    => '/bin/',
    notify  => Service['nginx'],
}
