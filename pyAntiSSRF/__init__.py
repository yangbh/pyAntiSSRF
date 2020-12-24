#!/usr/bin/python
# coding: utf-8

import socket
import logging
from pyAntiSSRF.utils.compat import urlparse
from pyAntiSSRF.utils.helper import is_inner_ipaddress


def hijackRequests(obj, func_name):

	orig_func = getattr(obj, func_name)

	def wrapped_func(*args, **kwargs):

		anti_ssrf = kwargs.get('anti_ssrf')
		logging.debug('anti_ssrf %s' % anti_ssrf)

		if anti_ssrf:
			url = kwargs.get('url')
			if(len(args)) >= 2:
				url = args[1]

			domain = urlparse(url).hostname
			logging.info('domain:\t%s' % domain)
			ip = socket.gethostbyname(domain)
			logging.info('ip:\t%s' % ip)
			if is_inner_ipaddress(ip):
				logging.warning('internal ip found :%s' % ip)
				raise BaseException('%s-%s is internal ip' % (domain,ip))
			new_url = url.replace(domain, ip, 1)
			logging.info('new url:\t%s' % new_url)

			if(len(args)) >=2 or url in kwargs:
				# args[1] = new_url
				kwargs['url'] = new_url

			new_headers = kwargs.get('headers',{})
			new_headers['Host'] = domain
			kwargs['headers'] = new_headers
			kwargs['allow_redirects'] = False

		if 'anti_ssrf' in kwargs.keys():
			del kwargs['anti_ssrf']

		return orig_func(*args, **kwargs)

	setattr(obj, func_name, wrapped_func)


def patchRequests():
	'''
	:return:
	'''
	import requests
	if requests.sessions.Session.request.__name__ == 'request':
		logging.warning('hijack requests')
		hijackRequests(requests.sessions.Session, 'request')

