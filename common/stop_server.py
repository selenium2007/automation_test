import sys
import paramiko
import ConfigParser
import os

def connect_server(rh,u,p):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(rh, username=u, password=p)
        print "Connected to %s\n" % rh
        return ssh
    except paramiko.AuthenticationException,err:
        print("SSH Authentication error: {} {}".format(rh,err))
        return None
    except Exception,err:
        print("SSH error: {}".format(err))
        return None

###################################################

def run_cmd(con,command):

    stdin, stdout, stderr = con.exec_command(command)
    stdin.close()
    status=stdout.channel.recv_exit_status()

    if status == 0:

       for line in stdout.read().splitlines():
           print '%s' % line

    else:

       for line in stderr.read().splitlines():
           print '%s' % line

###################################################

def closeconnect(con):
    print "closing SSH connection"
    if con != None:
        con.close()
###################################################
if __name__ == "__main__":
    parser = ConfigParser.ConfigParser()
    cfpath = os.path.dirname(os.path.abspath('.')) + '\\config\\config.ini'
    parser.read(cfpath)
    parser.read('config.ini')
    remote_host=parser.get('ssh', 'ubuntu_host')
    user=parser.get('ssh', 'ubuntu_user')
    pwd=parser.get('ssh', 'ubuntu_pwd')
    cmd=parser.get('ssh','stop_django_script')

    con=connect_server(remote_host,user,pwd)
    if con == None:
       print "connect error"
       sys.exit(1)
    run_cmd(con, cmd)
    closeconnect(con)
    sys.exit(0)