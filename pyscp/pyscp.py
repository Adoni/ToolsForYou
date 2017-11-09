import pexpect


class pyscp:
    def __init__(self, username, ip, password, port):
        self.username = str(username)
        self.ip = str(ip)
        self.password = str(password)
        self.port = str(port)

    def download(self, local_pos, remote_pos):
        command = 'scp -P %s %s@%s:%s %s' % (self.port, self.username, self.ip,
                                             self.local_pos, self.remote_pos)
        child = pexpect.spawnu(command)
        i = child.expect(["password:", pexpect.EOF], timeout=60)
        if i == 0:
            child.sendline(self.password)
        else:
            print('Exception!!!!')
        child.expect(pexpect.EOF, timeout=600)
        print(child.before)
        child.close()

    def upload(self, local_pos, remote_pos):
        command = 'scp -P %d %s@%s:%s %s' % (self.port, self.username, self.ip,
                                             self.remote_pos, self.local_pos)
        child = pexpect.spawnu(command)
        i = child.expect(["password:", pexpect.EOF], timeout=60)
        if i == 0:
            child.sendline(self.password)
        else:
            print('Exception!!!!')
        child.expect(pexpect.EOF, timeout=600)
        print(child.before)
        child.close()


if __name__ == '__main__':
    scp = pyscp(username='', ip='', password='', port='')
    if len(sys.argv) != 4:
        print('Wrong parameters')
        print('Please use command like:')
        print('    python %s up local_pos remote_pos')
        print('to upload')
        print('And use command like:')
        print('    python %s down remote_pos local_pos')
        print('to download')
    if sys.argv[1] == 'up':
        scp.upload(sys.argv[2], sys.argv[3])
    if sys.argv[1] == 'down':
        scp.upload(sys.argv[2], sys.argv[3])
