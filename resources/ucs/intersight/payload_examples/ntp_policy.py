#!/usr/bin/env python3
""" Example payload for sending POST/PUT/PATCH requests
    to the Intersight API.

    Updates NTP servers list.
"""

ntp_policy = {
    'Description': 'Python NTP Policy',
    'Name': 'Python_NTP_Policy',
    'NtpServers': [
        'pool.ntp.org',
        'time.windows.com'
    ],
    'Timezone': 'America/Los_Angeles',
    'Enabled': True
}
