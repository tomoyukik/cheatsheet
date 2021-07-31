settings {
    logfile = "/tmp/lsyncd.log",
    statusFile = "/tmp/lsyncd.status",
    insist = true,
    nodaemon = false,
    statusInterval = 20,
    maxProcesses = 1
}
sync {
    default.rsync,
    delay = 10,
    source = "/Users/user/path/to.dir",
    target = "/Users/user/path/to/dir",
    rsync = {
        binary = "/usr/local/bin/rsync",
        _extra = {
            "--include=test.txt",
            "--exclude=*"
        }
    }
}

