"""
    intersight_user_ops.py - shows how to use intersight REST API

    author: John McDonough (jomcdono@cisco.com)
"""
import json
import requests

from intersight_auth import IntersightAuth

# Create an AUTH object
AUTH = IntersightAuth(
    secret_key_filename='/Path/To/SecretKey/SecretKey.txt',
    api_key_id='key-id'
    )

# Intersight REST API Base URL
BURL = 'https://www.intersight.com/api/v1/'

if __name__ == "__main__":

    # intersight operations, GET, POST, PATCH, DELETE
    OPERATIONS = [
        {
            "request_process":False,
            "resource_path":"iam/Users",
            "request_method":"POST",
            "request_body": {
                "Email":"person@email.com",
                "Idpreference": {
                    "Selector": "$filter=Name eq 'Cisco'"
                },
                "Permissions": [
                    {
                        "Selector": "$filter=Name eq 'Device Administrator'"
                    },
                    {
                        "Selector": "$filter=Name eq 'HyperFlex Cluster Administrator'"
                    }
                ]
            }
        },
        {
            "request_process":False,
            "resource_name":"person@email.com",
            "resource_path":"iam/Users",
            "request_method":"PATCH",
            "request_body":{
                "Permissions": [
                    {
                        "Selector": "$filter=Name eq 'Device Administrator'"
                    }
                ]
            }
        },
        {
            "request_process":False,
            "resource_name":"person@email.com",
            "resource_path":"iam/Users",
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
                        "?$filter=Email eq '" + operation['resource_name'] + "'"
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
                        "?$filter=Email eq '" + operation['resource_name'] + "'"
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
