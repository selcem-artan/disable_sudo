#!/usr/bin/env python3

# This program is to disable/remove user sudo permissions
# for any user other than the default user

import pwd
import subprocess 
import shlex
import argparse
import re


def remove_sudo():
    """Remove non-default users from sudo group"""
    try:
        user_list,final_list = ([],) * 2
        with open('/etc/group', 'r') as file:
            for line in file:
                if re.search(r'^sudo:', line):
                    sudoers= re.sub(r'sudo.*:','', line).strip()
                    user_list = sudoers.split(',')

        for username in user_list:
            user_id = pwd.getpwnam(username)[2]
            del_sudo = 'gpasswd -d {0} sudo'.format(username)
            args = shlex.split(del_sudo)

            if user_id != 1000:
                subprocess.call(args,stdout=subprocess.DEVNULL,timeout=10)
                final_list.append(username)
        
        print(f"Sudo permission was removed for Users: {*final_list,}")
    
    except Exception as e:
        print("Error removing sudo: %s" % repr(e))


if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(
                prog='sudo_disable',
                description='This script removes sudo privilidge from non-default unix users',
                epilog='For sudo removal action, run script with --users flag only!'
    )
    parser.add_argument(
        "--version",
        action='version',
        version='%(prog)s v1.0',
        help="Print the version of this application",
    )
    parser.add_argument(
        "--users",
        action='store_true',
        required=True,
        help="Users argument to execute sudo removal action",
    )
    
    args = parser.parse_args()

    if args.users:
        remove_sudo()
