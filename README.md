# disable sudo permission
Disable sudo privilidge for all unix users except default user (uid:1000)

Script needs to be run with "--users" flag without any arguments

```
# python3 sudo_disable.py  --help
usage: sudo_disable [-h] [--version] --users

This script removes sudo privilidge from non-default unix users

options:
  -h, --help  show this help message and exit
  --version   Print the version of this application
  --users     Users argument to execute sudo removal action

For sudo removal action, run script with --users flag only!
```

