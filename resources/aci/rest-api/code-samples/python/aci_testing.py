#!/usr/bin/env python3
""" Interactive Python code which allows abstract/free-formed requests
    to Cisco ACI.

    Run the code in a REPL and call the apic_helper() method to
    practice

    Usage option #1: ipython -i aci_testing.py
    Usage option #2: python3 -i aci_testing.py
"""

# Imports
from json.decoder import JSONDecodeError
from typing import Union
import requests

# Constants
CISCO_ALWAYS_ON_APIC_AUTH_URL = {
    'url': 'https://sandboxapicdc.cisco.com/api/aaaLogin.json',
}
CISCO_ALWAYS_ON_APIC_CREDS = {
    'aaaUser': {
        'attributes': {
            'name': 'admin',
            'pwd': 'ciscopsdt'
        }
    }
}

# Disable insecure HTTPS certificate warnings
requests.packages.urllib3.disable_warnings()

session = requests.session()
session.verify = False


def check_response(response: requests.models.Response) -> str:
    """Check for a valid HTTP response

    Args:
        response (requests.models.Response): requests.models.Response object.

    Returns:
        response_status (str): string evaluation of the HTTP response
                         (Successful, Failed).
    """

    # Set a default response
    response_status = 'Successful'

    # Check for HTTP errors
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        response_status = f'Failed {e!r}'

    # Check for invalid response data
    try:
        response.json()
    except JSONDecodeError as e:
        response_status = f'Failed {e!r}'

    return response_status


def apic_login() -> None:
    """APIC authentication

    Args:
        None

    Returns:
        None
    """

    login_response = session.post(
        **CISCO_ALWAYS_ON_APIC_AUTH_URL,
        json=CISCO_ALWAYS_ON_APIC_CREDS,
        timeout=3,
    )

    login_status = check_response(login_response)

    # Check for a token in the 'APIC-cookie' cookie
    try:
        login_response.cookies['APIC-cookie']
    except KeyError as e:
        login_status = f'Failed {e!r}'

    print(f'\n** Login {login_status} **\n')

    # These options are not necessary with the requests.session object
    # if login_response.json().get('totalCount', None) == '1':
    #     # Option #1
    #     token = session.cookies['APIC-cookie']

    #     # Option #2
    #     login_json = login_response.json()
    #     token = login_json['imdata'][0]['aaaLogin']['attributes']['token']


def apic_helper(
    method: str,
    url: str,
    data: Union[str, None] = None,
    json: Union[str, None] = None
) -> requests.models.Response:
    """Helper method for API requests to APIC

    Args:
        method: string for HTTP method (GET, POST, DELETE).
        url: string for APIC URL.
        data (optional): Form-encoded HTTP payload.
        json (optional): JSON-encoded HTTP payload.

    Returns:
        requests.models.Response object.
    """

    response = session.request(
        method=method,
        url=url,
        data=data,
        json=json
    )

    response_status = check_response(response)
    print(f'\n** Request {response_status} **\n')

    return response


def main() -> None:
    """ Main function to run when the code executes.

    Args:
        None

    Returns:
        None
    """

    # Perform APIC login
    apic_login()


if __name__ == '__main__':
    main()
