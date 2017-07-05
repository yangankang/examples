import random


class RandomIpAddr:
    common_ports = [80, 9000, 8080, 8118, 8081, 3128, 8123, 808, 8889, 82, 8998, 1080, 53281,
                    8888]

    def create_random_ip(self):
        a = int(random.uniform(0, 255))
        b = int(random.uniform(0, 255))
        c = int(random.uniform(0, 255))
        d = int(random.uniform(0, 255))

        return str(a) + "." + str(b) + "." + str(c) + "." + str(d)

    def get_random_url(self):
        ip = self.create_random_ip()
        urls = []
        for i in self.common_ports:
            urls.append({"protocol": "http", "ip": ip, "port": i})
            urls.append({"protocol": "https", "ip": ip, "port": i})
        return urls
