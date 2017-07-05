from reptile.download_http_proxy import ProxyCrawler

proxy = ProxyCrawler()
proxy.refresh_db()
# print(proxy.random_user_agent())
# print(proxy.is_valid_proxy(ip="60.169.19.66", port=9000))
