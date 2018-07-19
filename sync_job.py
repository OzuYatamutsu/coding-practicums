from ftplib import FTP

with FTP('trial-ubuserv.infosec-trials.steakscorp.org') as ftp:
    ftp.login(user='infosec-trial-7', passwd='nuAoAl]yJZa')
    print(ftp.getwelcome())
    print(ftp.set_pasv(True))
    print(ftp.pwd())
    print(ftp.sendcmd('STAT update_file'))
