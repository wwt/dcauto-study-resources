#!/usr/bin/env python3
""" APIC SDK wrapper to test REST APIC calls to Cisco ACI.
    Performs automatic login to ACI on init.

    Usage (in a Python file):
        from apic_sdk import Apic
        apic = Apic()
        apic.make_request(**kwargs)
"""

# Imports
import requests

# Constants
ALWAYS_ON_URL = 'https://sandboxapicdc.cisco.com:'
ALWAYS_ON_PORT = '443'
ALWAYS_ON_NAME = 'admin'
ALWAYS_ON_PWD = 'ciscopsdt'
APIC_LOGIN_EP = '/api/aaaLogin.json'
DEFAULT_METHOD = 'GET'
DEFAULT_TIMEOUT = 3

# Disable HTTPS certificate warnings
requests.packages.urllib3.disable_warnings()


class Apic:
    def __init__(
        self,
        base_url=ALWAYS_ON_URL,
        port=ALWAYS_ON_PORT,
        name=ALWAYS_ON_NAME,
        pwd=ALWAYS_ON_PWD,
    ):

        self._base_url = base_url
        self._port = port
        self._name = name
        self._pwd = pwd

        self.login()

    def login(self):
        json = {
            'aaaUser': {
                'attributes': {
                    'name': self._name,
                    'pwd': self._pwd
                }
            }
        }

        url = f'{self._base_url}{self._port}{APIC_LOGIN_EP}'
        self._session = requests.session()
        self._session.verify = False
        login_response = self._session.request(
            method='POST',
            url=url,
            json=json,
            timeout=DEFAULT_TIMEOUT
        )

        response = login_response.json()
        self._cookie = response['imdata'][0]['aaaLogin']['attributes']['token']

    def make_request(
        self,
        method=DEFAULT_METHOD,
        endpoint=None,
        json=None
    ):

        url = f'{self._base_url}{self._port}{endpoint}'
        response = self._session.request(
            method=method,
            url=url,
            json=json,
            timeout=DEFAULT_TIMEOUT
        )

        return response
