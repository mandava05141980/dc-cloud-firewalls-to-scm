def map_port(port):
    port_mapping = {
        'www': '80',
        'https': '443',
        'ssl': '443',
        'ssh': '22',
        'snmp': '161',
        'snmptrap': '162',
        'telnet': '23',
        'ntp': '123',
        'syslog': '514',
        'ftp': '21',
        'tftp': '69',
        'dhcp': '67',
        'tacacs': '49',
        'dns': '53',
        'smtp': '25',
        'pop3': '110',
        'imap': '143',
        'ldap': '389',
        'ldaps': '636',
        'radius': '1812',
        'radius-acct': '1813',
        'radius-dynauth': '3799',
        'radius-dynauth-acct': '3800',
        'radius-coa': '1700',
        'radius-dynauth-coa': '3799',
        'radius-dynauth-coa-acct': '3800',
        'radius-dynauth-coa-acct': '3799',
        'radius-dynauth-coa-acct': '3800',
        'auth': '113',
        'ident': '113',
        'rsync': '873',
        'rsh': '514',
        'nfs': '2049',
        'smb': '445',
        'mssql': '1433',
        'mysql': '3306',
        'postgresql': '5432',
        'oracle': '1521',
        'rdp': '3389',
        'vnc': '5900',
        'pcanywhere': '5631',
        'pcanywhere-data': '5632',
        'sunrpc': '111',
        'ftp-data': '20',
        'pptp': '1723',
        'l2tp': '1701',
        'ike': '500',
        'domain': '53',
        'kerberos': '88',
        'kerberos-sec': '750',
        'kerberos-master': '751',
        'bootps': '67',
        'netbios-ns': '137',
        'netbios-dgm': '138',
        'netbios-ssn': '139',
        'nntp': '119',
        'irc': '194',
        'ircs': '994',
        'h323': '1720',
        'sip': '5060',
        'sip-tls': '5061',
        'rtsp': '554',
        'bgp': '179',
        'sqlnet': '1521',
        'lpd': '515',
        # Add other mappings as needed
    }
    return port_mapping.get(port, port)

def map_application(app):
    app_mapping = {
        'icmp': 'icmp',
        'time-exceeded': 'icmp',
        'unreachable': 'icmp',
        'echo-reply': 'ping',
        'echo': 'ping',
        'destination-unreachable': 'icmp'
    }
    return app_mapping.get(app, app)