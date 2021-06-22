#!/usr/bin/env python3

# Imports
from cisco_gnmi import ClientBuilder
from time import sleep

# Constants
GNMI_AUTH = {
    'username': 'admin',
    'password': 'Cisco123'
}
GNMI_CERT_CN = 'sbx-n9kv'
GNMI_CERT_PATH = './gnmi.pem'
GNMI_OS = 'NX-OS'
GNMI_PORT = '50051'
GNMI_SWITCH = '10.10.20.58'
XPATH_CPU_0_INSTANT = str('components/component[name="cpu0"]'
                          '/cpu/utilization/state/instant')

# Create client connection object
builder = ClientBuilder(f'{GNMI_SWITCH}:{GNMI_PORT}')
builder.set_os(GNMI_OS)
builder.set_secure_from_file(GNMI_CERT_PATH)
builder.set_ssl_target_override()
builder.set_call_authentication(**GNMI_AUTH)

client = builder.construct()

# Start GNMI subscription
gnmi_subscription = client.subscribe_xpaths(
    XPATH_CPU_0_INSTANT
)

while gnmi_subscription.is_active() is True:
    print(f'{gnmi_subscription.next()}\n')
    sleep(10)
