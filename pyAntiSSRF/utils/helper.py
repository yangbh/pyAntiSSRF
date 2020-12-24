#!/usr/bin/python
# coding: utf-8

import requests
import socket
import logging
from socket import inet_aton
from struct import unpack
from .compat import urlparse

def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0]

def is_inner_ipaddress(ip):
    ip = ip2long(ip)
    return ip2long('127.0.0.0') >> 24 == ip >> 24 or \
           ip2long('10.0.0.0') >> 24 == ip >> 24 or \
           ip2long('172.16.0.0') >> 20 == ip >> 20 or \
           ip2long('192.168.0.0') >> 16 == ip >> 16 or \
           ip2long('0.0.0.0') >> 24 == ip >> 24 or \
           ip2long('100.0.0.0') >> 24 == ip >> 24 or \
           ip2long('30.0.0.0') >> 24 == ip >> 24 or \
           ip2long('11.0.0.0') >> 24 == ip >> 24

def safe_request_url(url):
    hostname = urlparse(url).hostname
    logging.info(hostname)
    ip = socket.gethostbyname(hostname)
    logging.info(ip)
    if is_inner_ipaddress(ip):
        logging.warning(ip)
        return None
    new_url = url.replace(hostname,ip)
    return requests.get(new_url,headers={'Host':hostname},allow_redirects=False)

# if __name__ == '__main__':
#     url = 'http://11.1.1.1/aaaaaa'
#     ret = safe_request_url(url)

