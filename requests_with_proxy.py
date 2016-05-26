'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 5/26/16
'''

import requests

_URL = 'https://api.ipify.org?format=json'


def request_without_proxy():
    print "(+) Sending request without proxy..."
    r = requests.get(_URL)
    print "(+) IP is: " + r.text.replace("\n", "")


def request_with_proxy():
    """
    In order to use the proxy through socks5, must install the following python packages:
    requests (version 2.10.0)
    PySocks (Needed by requests)
    """
    print "(+) Sending request with proxy..."
    # We use `tor` as the sock proxy, so just set the port to 9050.
    # Must start `tor` to enable the proxy.
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    r = requests.get(_URL, proxies=proxies)
    print "(+) IP is: " + r.text.replace("\n", "")


if __name__ == '__main__':
    request_without_proxy()
    request_with_proxy()
