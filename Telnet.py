# encoding=utf-8
import telnetlib
import re


class Telnet(telnetlib.Telnet):
    start_welcome = re.compile('Microsoft Telnet Server')
    def get_result(self, Callback=None, welcome_math=None):
        """
        :param Callback: 回调函数这里可以进行实时打印比如调用tail的命令时
        :param welcome_math: 登录时的欢迎数据，因为这是单独发过来的
        :return: 执行结果
        """
        if welcome_math:
            self.start_welcome = re.compile(welcome_math)
        data = self.sock.recv(1024)
        if self.start_welcome.findall(data):
            if Callback:
                Callback()
        

        while True:
            buf = self.sock.recv(50)
            data+=buf
            if Callback:
                Callback()
            if 1520>len(buf):
                break
        return data.decode('gbk')


class telnet(object):
    connect = None

    def __init__(self):
        pass

    def login(self):
        import telnetlib
        '''''Telnet远程登录：Windows客户端连接Linux服务器'''
        # 连接Telnet服务器
        tn = Telnet(Host, port=23)
        # tn.set_debuglevel(100)
        # 输入登录用户名
        tn.read_until(b'login: ')
        tn.write(username.encode('ascii') + b"\r\n")
        # 输入登录密码
        tn.read_until(b'password:')
        print(tn.read_some())
        tn.write(password.encode('ascii') + b'\r\n')
        # 登录完毕后执行命令
        tn.read_some()
        return tn

    @classmethod
    def execmd(cls, cmd):
        cmd +=' \r\b'
        cmd = cmd.encode('ascii')
        if not cls.connect:

            cls.connect = telnet().login()
        cls.connect.write(cmd)
        result = cls.connect.get_result()
        print(result)



if __name__ == '__main__':
    # 配置选项
    Host = '192.168.193.128'  # Telnet服务器IP
    username = 'administrator'  # 登录用户名
    password = 'Changeme_123'  # 登录密码
    telnet().execmd(b'ipconfig')
    telnet().execmd(b'ping 192.168.24.211')
