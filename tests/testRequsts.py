#!/usr/bin/python
# coding: utf-8

import logging
logging.basicConfig(level=logging.DEBUG)

import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logging.info(BASE_DIR)
sys.path.append(BASE_DIR)

import requests
import pyAntiSSRF

pyAntiSSRF.patchRequests()


# print(requests.get(url='http://100.67.154.183:50001/').content)

# test internal
# print(requests.get(url='http://30.225.32.50:8888/', anti_ssrf=False).content)
# print(requests.get(url='http://30.225.32.50:8888/', anti_ssrf=True).content)

# test internet
# print(requests.get('http://111.1.dns.m0d9.me/aaa', anti_ssrf=False).content)
# print(requests.get('http://111.1.dns.m0d9.me/bbb', anti_ssrf=True).content)

# test 302 redirect
# print(requests.get('http://52.23.124.133', anti_ssrf=False, verify=False).status_code)
# print(requests.get('http://52.23.124.133', anti_ssrf=True, verify=False).status_code)

# test ssl
print(requests.get('https://baidu.com', anti_ssrf=False).status_code)
print(requests.get('https://baidu.com', anti_ssrf=True, verify=False).status_code)
