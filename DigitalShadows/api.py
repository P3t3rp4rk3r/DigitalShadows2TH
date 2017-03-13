#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import requests


class DigitalShadowsApi():
    """
		Python API for DigitalShadows

		:param config
	"""

    def __init__(self, config):

        self.url = config['url']
        self.key = config['ds_key']
        self.secret = config['ds_secret']
        self.proxies = config['proxies']
        self.verify = config['verify']
        self.headers = {
            'Content-Type': 'application/vnd.polaris-v22+json',
            'Accept': 'application/vnd.polaris-v22+json'
        }
        self.session = requests.Session()
        self.auth = requests.auth.HTTPBasicAuth(username=self.key,
                                                password=self.secret)

    def getIncidents(self, id, fulltext='false'):
        req = self.url + '/api/incidents/{}?fulltext='.format(id) + fulltext
        headers = self.headers
        try:
            return self.session.get(req, headers=headers, auth=self.auth,
                                    proxies=self.proxies, verify=False)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def getIntelIncidents(self, id, fulltext='false'):
        req = self.url + '/api/intel-incidents/{}?fulltext='.format(id) + fulltext
        headers = self.headers
        try:
            return self.session.get(req, headers=headers, auth=self.auth,
                                    proxies=self.proxies, verify=self.verify)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))
