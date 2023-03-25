
def get_common_enumeration_template_mio():
    return '''
# Common enumeration

## Nmap

| Port | Software       | Version               | Status |
| ---- | -------------- | --------------------- | ------ |
| 22   | ssh            | OpenSSH 8.4p1 Debian 5+deb11u1  | open   |
| 80   | http           | nginx/1.18.0 + Phusion Passenger(R) 6.0.15          | open   |

## Gobuster

### Directory listing
```bash
sudo gobuster dir -u 'http://.htb' -t 200 -w '/usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt'
```

### Subdomain listing
```bash
sudo gobuster vhost -u 'http://.htb' -t 200 -w '/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt' 
```

****

'''