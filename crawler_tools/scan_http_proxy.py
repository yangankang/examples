from http_proxy_db import ProxyData
from random_ip_addr import RandomIpAddr
import telnetlib


class ScanProxyIp(ProxyData, RandomIpAddr):
    def scan(self):
        while True:
            ips = self.get_random_url()
            print("开始扫描 " + ips[0]["ip"] + " ...")
            for ip in ips:
                try:
                    response = self.proxy_request("http://www.xicidaili.com", protocol=ip["protocol"], ip=ip["ip"],
                                                  port=int(ip["port"]),
                                                  timeout=2)
                    if response.code == 200 and telnetlib.Telnet(ip["ip"], port=int(ip["port"]), timeout=2):
                        print(response.read().decode("utf-8"))
                        print("是一个有效的代理" + str(ip))
                except Exception as e:
                    continue
