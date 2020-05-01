#!.env/bin/python3

import requests
import sys


if __name__ == '__main__':
	frontent_ip = sys.argv[1]
	backend_ips = sys.argv[2].split(',')

	for backend_ip in backend_ips:
		res = requests.get('http://{frontent_ip}'.format(**vars()))
		expected_reply = "Hi there, I'm served from ip-{}!".format(backend_ip.replace('.','-'))
		actual_reply = str(res.text)
		assert(expected_reply==actual_reply)