import os
import socket


class PackageSniffing:
    ip = None

    def __init__(self, ip):
        self.ip = ip

    def start(self):
        if os.name == "nt":
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP

        '''
        Python的套接字类型如下：
        socket.AF_UNIX	        用于同一台机器上的进程通信（既本机通信）
        socket.AF_INET	        用于服务器与服务器之间的网络通信(指定使用IPv4)
        socket.AF_INET6	        基于IPV6方式的服务器与服务器之间的网络通信
        
        socket.SOCK_STREAM	    基于TCP的流式socket通信
        socket.SOCK_DGRAM	    基于UDP的数据报式socket通信
        socket.SOCK_RAW	        原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次SOCK_RAW也可以处理特殊的IPV4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头
        socket.SOCK_SEQPACKET	可靠的连续数据包服务
        
        用法如：创建一个TCP Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        '''
        sniffing = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

        # IP 必须是一个元组
        sniffing.bind((self.ip, 0))

        '''
        MAC(链路层)首部 | IP首部 |TCP首部 | 数据
        
        IPPROTO_IP      指定了从IP层收发
        IP_HDRINCL      我们可以从IP报文首部第一个字节开始依次构造整个IP报文的所有选项
        '''
        sniffing.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if os.name == "nt":
            # 开启网卡的混杂模式
            sniffing.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        while True:
            print(sniffing.recvfrom(65535))

        if os.name == "nt":
            # 关闭网卡的混杂模式
            sniffing.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


ps = PackageSniffing("127.0.0.1")
ps.start()
