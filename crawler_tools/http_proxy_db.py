import sqlite3
import random
from urllib import request
import socket


class ProxyData:
    user_agent_headers = [
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
        {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    ]

    db_name = "proxy_ips.db"

    def random_user_agent(self):
        return self.user_agent_headers[int(random.uniform(0, len(self.user_agent_headers) - 1))]

    def save_ips(self, ds=[]):
        if len(ds) > 0:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS t_ips(id INTEGER PRIMARY KEY AUTOINCREMENT,ip VARCHAR(64) NOT NULL,port INT NOT NULL,addr VARCHAR(64) ,`type` VARCHAR(8))''')

            for data in ds:
                if data["ip"] and data["port"] and cursor:
                    if not data["addr"]:
                        data["addr"] = ""
                    if not data["type"]:
                        data["type"] = ""

                    if not self.exists(cursor=cursor, ip=data["ip"], port=data["port"]):
                        values = "'" + data["ip"].strip() + "'," + data["port"].strip() + ",'" + data[
                            "addr"].strip() + "','" + \
                                 data["type"].strip() + "'"
                        cursor.execute("insert into t_ips (ip,port,addr,`type`) values(" + values + ")")

            conn.commit()
            cursor.close()
            conn.close()

    def exists(self, cursor, ip, port):
        cursor.execute("select * from t_ips where ip='" + ip + "' and port=" + port)
        ipd = cursor.fetchone()
        if ipd:
            return True
        else:
            return False

    def count(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT count(*) AS count FROM t_ips")
            c = cursor.fetchone()
            return c[0]
        except Exception as e:
            print(e)
            return 0
        finally:
            conn.close()

    def is_valid_proxy(self, protocol="http", ip=None, port=None):
        try:
            socket.setdefaulttimeout(5)
            proxy = {protocol: ip + ":" + str(port)}
            proxy_handler = request.ProxyHandler(proxy)
            opener = request.build_opener(proxy_handler)
            user_agent = self.random_user_agent()['User-Agent']
            opener.addheaders = [('User-Agent', user_agent)]
            request.install_opener(opener)
            response = request.urlopen("http://www.baidu.com")
            if response.code == 200:
                html = response.read().decode("utf-8")
                print("代理 " + protocol + "://" + ip + ":" + str(port) + " 是有效的" + html)
                return True
            else:
                return False
        except Exception as e:
            return False

    def proxy_request(self, url, protocol="http", ip=None, port=None, encode="utf-8"):
        if not protocol:
            protocol = "http"
        socket.setdefaulttimeout(10)
        proxy = {protocol.lower(): ip + ":" + str(port)}
        proxy_handler = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_handler)
        user_agent = self.random_user_agent()['User-Agent']
        opener.addheaders = [('User-Agent', user_agent)]
        request.install_opener(opener)
        response = request.urlopen(url=url)
        # html = response.read().decode("utf-8")
        return response

    def get_random_ip(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM t_ips ORDER BY RANDOM() LIMIT 1")
            c = cursor.fetchone()
            return c
        except Exception as e:
            print(e)
            return None
        finally:
            conn.close()
