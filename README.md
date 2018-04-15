# ansible-cisco
set of short Ad-Hoc commands

### Solaris 11.4 environment:

#### ansible --version

```
ansible 2.4.3.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/export/home/openbsod/.ansible/plugins/modules',
  '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.5/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.5.3 (default, Dec 21 2017, 19:26:57) [C]
```
  
#### uname -a

```
SunOS solarbsod 5.11 11.4.0.12.0 i86pc i386 i86pc
```

#### sshpass -V

```
sshpass 1.05 (C) 2006-2011 Lingnu Open Source Consulting Ltd.
This program is free software, and can be distributed under the terms of the GPL
See the COPYING file for more information.
```

In order to get sshpass working you have to add sshpass to work with ansible:

```
pkgadd -d http://get.opencsw.org/now
/opt/csw/bin/pkgutil -U
/opt/csw/bin/pkgutil -y -i sshpass
cp -r //opt/csw/bin/sshpass /usr/bin/
```

##### USAGE:

```
ansible 65blk -i netdev -m raw -a "sh bgp summ" -u cisco --ask-pass
```

##### Ansible ad-hoc BGP-SUMM example

```
ansible asrm61 -i netdev -m raw -a "sh bgp summ" -u cisco --ask-pass
```

![alt text](https://github.com/openbsod/ansible-cisco/blob/master/img/bgp-summ-example.png)

##### Python pexpect example

```
okey-asr "sh bgp ipv4 flowspec neighbors 10.1.0.101 routes | b Network"
```

![alt text](https://github.com/openbsod/ansible-cisco/blob/master/img/flowspec-example.png)
