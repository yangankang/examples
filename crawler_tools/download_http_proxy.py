from urllib import request
from bs4 import BeautifulSoup
import time
import logging

from http_proxy_db import ProxyData

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log')


class ProxyCrawler(ProxyData):
    url = "http://www.xicidaili.com/nn/"

    def refresh_db(self):
        # if self.count() < 100:
        i = 185
        logging.info("开始执行获取代理IP")
        while self.get_resolve_data(page=i, useAgent=False):
            print("第" + str(i) + "次抓取,共" + str(self.count()) + "条,等待10秒后重新抓取...")
            logging.info("第" + str(i) + "次抓取,共" + str(self.count()) + "条,等待10秒后重新抓取...")
            time.sleep(10)
            logging.info("第" + str(i) + "次执行获取代理IP")
            i = i + 1

    def get_resolve_data(self, page=1, useAgent=False):
        r = self.url + str(page)

        if useAgent:
            # c = self.get_random_ip()
            ip = "134.17.24.127"  # c[1]
            port = "8080"  # c[2]
            protocol = "http"  # c[4]
            try:
                response = self.proxy_request(r, protocol, ip, port)
            except Exception as e:
                print(protocol.lower() + "://" + ip + ":" + port + "Net Error : " + str(e))
                time.sleep(3)
                print("开始重新请求...")
                self.get_resolve_data(page, useAgent)
                return True
        else:
            h = self.random_user_agent()
            r = request.Request(url=r, headers=h)
            response = request.urlopen(r)

        if response.code == 200:

            html = response.read()
            html = html.decode("utf-8")
            ds = self.parse_html(html)
            self.save_ips(ds)

            print("保存第" + str(page) + "页数据:", ds)
            logging.info("保存第" + str(page) + "页数据:", ds)
            # logging.info("保存第" + str(page) + "页数据")

            return True
        else:
            return False

    def parse_html(self, html=None):
        ds = []
        if html != None:
            soup = BeautifulSoup(html, "html5lib")
            items = soup.select("#ip_list tr")
            for item in items:
                child = item.find_all("td")
                if len(child) > 0:
                    ip = child[1].get_text()
                    port = child[2].get_text()
                    addr = child[3].find("a")
                    if addr:
                        addr = addr.get_text()
                    type = child[5].get_text()
                    ds.append({"ip": ip, "port": port, "addr": addr, "type": type})
        return ds
