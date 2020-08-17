# ssh-cert-helper
Add SSH Certificates to SSH Agent upon first SSH use



## Warning

This is not for someone who has a ton of certificates such as myself. It is for
users that only have a few but ssh does not auto load. If you have a ton of
certificates, I suggest you learn more about how to use the `ssh-agent `command
and get a good understanding of how `ssh` and `ssh-agent` interact with each
other.

## Installation 

Move the file to a directory where it can be accessed from anywhere in the
system such as `~/.bin/`. Then add the alias:

```
alias ssh='ssh-cert.py;ssh'
```

This will run the script before each ssh session.
