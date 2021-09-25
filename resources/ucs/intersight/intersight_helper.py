#!/usr/bin/env python3

# Imports
import requests
from intersight_rest_api.intersight_auth import IntersightAuth
from json import dumps
from operator import itemgetter

# Constants
AUTH_PATH = './api_keys/'
AUTH_KEY_ID_FILE = 'keyId.txt'
AUTH_KEY_SECRET_FILE = 'keySecret.txt'
BASE_URL = 'https://intersight.com/api/v1'

# Extract Secret Key ID
with open(
    file=f'{AUTH_PATH}{AUTH_KEY_ID_FILE}',
    mode='rt',
    encoding='utf-8'
) as file:
    api_key_id = file.read().strip()

# Setup Intersight authentication
auth = IntersightAuth(
    secret_key_filename=f'{AUTH_PATH}{AUTH_KEY_SECRET_FILE}',
    api_key_id=api_key_id
)

# Setup Intersight headers
headers = {
    'Accept': '*/*'
}


# Intersight helper function
def intersight(
    method: str = 'GET',
    endpoint: str = '/',
    params: str = None,
    json_data: dict = None
) -> requests.Response:

    """Send request to Cisco Intersight REST API

       Args:
            method (str): HTTP method ('GET', 'POST', 'PATCH', or 'DELETE').
            endpoint (str): Intersight API endpoint ('/compute/Blades').
            params (str): Query parameters ('$select=Dn,Model,Moid')
            json_data (dict): Request body.

       Prints:
            HTTP status code and reason (200 OK) and the number of
            objects returned.
            Example:
                HTTP response: 200 OK
                Objects returned: 9

       Returns:
            response (requests.Response): Requests library response object.
    """

    # Format request fields
    method = method.upper()
    if json_data is not None:
        json_data = dumps(json_data)

    # Set the 'Content-Type' header
    if method == 'PATCH':
        content_type = 'application/json-patch+json'
    else:
        content_type = 'application/json'
    headers.update({'Content-Type': content_type})

    # Set endpoint URL and send request
    url = f'{BASE_URL}{endpoint}'
    r = requests.request(
        method=method.upper(),
        url=url,
        headers=headers,
        params=params,
        auth=auth,
        data=json_data
    )

    if r.ok is True:
        # Format output
        try:
            num_objects = len(r.json()['Results'])
        except KeyError:
            num_objects = 1
        finally:
            print(f'\nHTTP response: {r.status_code} {r.reason}\n'
                  f'Objects returned: {num_objects}\n')
    else:
        print(f'\n{r.text}\n')

    # Raise HTTP status exception for bad request/response
    r.raise_for_status()

    return r.json()


def sort_items(
    response: dict,
    sort_field: str = 'Dn'
) -> None:
    """Sorts the items in an intersight response based on a specific field.

       Args:
            response (dict): Dictionary of response from intersight,
                             converted from JSON with the .json() method.
            sort_field (str): Name of an alternate sort field (default is Dn).

       Prints:
            Sorted, numbered list of results with columns for DN and Model.
            Example:
                Sorted by "Dn"
                --------------
                1. DN: sys/chassis-3/blade-1     Model: UCSB-EX-M4-1
                2. DN: sys/chassis-3/blade-3     Model: UCSB-EX-M4-1
                3. DN: sys/chassis-3/blade-5     Model: UCSB-EX-M4-1
                4. DN: sys/chassis-3/blade-7     Model: UCSB-EX-M4-1
                5. DN: sys/chassis-4/blade-1     Model: UCSC-C3K-M4SRB
                6. DN: sys/chassis-4/blade-2     Model: UCSC-C3K-M4SRB
                7. DN: sys/chassis-5/blade-1     Model: UCSB-B200-M5
                8. DN: sys/chassis-5/blade-2     Model: UCSB-B200-M5
                9. DN: sys/chassis-5/blade-3     Model: UCSB-B480-M5

       Returns:
            None
    """

    items = sorted(
        response['Results'],
        key=itemgetter(sort_field)
    )

    header = f'\nSorted by "{sort_field}"'
    print(f'\n{header}\n'
          f'{"-" * (len(header) - 1)}')
    for index, item in enumerate(items):
        print(f'{index + 1}. '
              f'DN: {item["Dn"]:<25} '
              f'Model: {item["Model"]}')
    print()
