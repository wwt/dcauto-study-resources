"""
    intersight_ops.py - shows how to use intersight REST API

    author: John McDonough (jomcdono@cisco.com)
"""
import json
import requests

from intersight_auth import IntersightAuth

# Create an AUTH object
AUTH = IntersightAuth(
    secret_key_filename='C:\\Users\\developer\\Desktop\\intersight-rest-api\\key\\SecretKey.txt',
    api_key_id='api-key-id'
    )

# Intersight REST API Base URL
BURL = 'https://www.intersight.com/api/v1/'

if __name__ == "__main__":

    # intersight operations, GET, POST, PATCH, DELETE
    OPERATIONS = [
        {
            "request_process":True,
            "resource_path":"compute/PhysicalSummaries",
            "request_method":"GET"
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"GET"
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"POST",
            "request_body":{
                "Enabled":True,
                "Name":"ntp-policy",
                "Description":"NTP Policy for ntp.org",
                "NtpServers":[
                    "pool.ntp.org"
                    ],
                "Tags":[]
            }
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"POST",
            "request_body":{
                "Enabled":True,
                "Name":"ntp-policy-west",
                "Description":"NTP Policy for ntp.org West Coast",
                "NtpServers":[
                    "0.pool.ntp.org",
                    "1.pool.ntp.org"
                    ],
                "Tags":[]
            }
        },
        {
            "request_process":False,
            "resource_path":"ntp/Policies",
            "request_method":"POST",
            "request_body":{
                "Enabled":True,
                "Name":"ntp-policy-east",
                "Description":"NTP Policy for ntp.org East Coast",
                "NtpServers":[
                    "2.pool.ntp.org",
                    "3.pool.ntp.org"
                    ],
                "Tags":[]
            }
        },
        {
            "request_process":False,
            "resource_name":"ntp-policy",
            "resource_path":"ntp/Policies",
            "request_method":"PATCH",
            "request_body":{
                "NtpServers":[
                    "pool.ntp.org",
                    "10.10.10.30"
                    ]
                }
        },
        {
            "request_process":False,
            "resource_name":"ntp-policy-east",
            "resource_path":"ntp/Policies",
            "request_method":"DELETE"
        }
    ]


    for operation in OPERATIONS:

        if operation['request_process']:

            response = None
            print(operation['request_method'])

            # GET
            if operation['request_method'] == "GET":
                response = requests.get(
                    BURL + operation['resource_path'],
                    auth=AUTH
                    )

            # POST
            if operation['request_method'] == "POST":
                response = requests.post(
                    BURL + operation['resource_path'],
                    data=json.dumps(operation['request_body']),
                    auth=AUTH
                    )

            # PATCH
            if operation['request_method'] == "PATCH":

                # GET the Moid of the MO to PATCH
                response = requests.get(
                    (
                        BURL + operation['resource_path'] +
                        "?$filter=Name eq '" + operation['resource_name'] + "'"
                        ),
                    auth=AUTH
                    )

                # Extract the Moid from the Results
                json_result = json.loads(response.text)
                moid = json_result["Results"][0]["Moid"]

                response = requests.patch(
                    BURL + operation['resource_path'] + "/" + moid,
                    data=json.dumps(operation['request_body']),
                    auth=AUTH
                    )

            # DELETE
            if operation['request_method'] == "DELETE":

                # GET the Moid of the MO to DELETE
                response = requests.get(
                    (
                        BURL + operation['resource_path'] +
                        "?$filter=Name eq '" + operation['resource_name'] + "'"
                        ),
                    auth=AUTH
                    )

                # Extract the Moid from the Results
                json_result = json.loads(response.text)
                moid = json_result["Results"][0]["Moid"]

                response = requests.delete(
                    BURL + operation['resource_path'] + "/" + moid,
                    auth=AUTH
                    )

            print(response)
            print(response.text)
