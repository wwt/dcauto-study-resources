"""
    intersight_firmware.py - shows how to use intersight REST API
                             to initiate a firmware upgrade.

    author: John McDonough (jomcdono@cisco.com)
"""
# pylint: disable=line-too-long,invalid-name

import json
import requests

from intersight_auth import IntersightAuth

# Create an AUTH object
AUTH = IntersightAuth(
    secret_key_filename='/Users/jomcdono/Downloads/SecretKey.txt',
    api_key_id='59dd1f1916267c00015e0929/59dd1ec316267c00015e0496/5b2bc9317a76627434a609d1'
    )

# Intersight REST API Base URL
BURL = 'https://www.intersight.com/api/v1/'

if __name__ == "__main__":

    # Intersight REST API Operations
    rackunit_json_body = {
        "request_method":"GET",
        "resource_path": (
            'https://www.intersight.com/api/v1/'+
            'compute/RackUnits?$select=DeviceMoId,Model,AssetTag&'+
            '$filter=AssetTag eq \'DMZ-R-L3-ADJM\''
        )
    }
    firmware_json_body = {
        "request_method":"POST",
        "resource_path":"https://www.intersight.com/api/v1/firmware/Upgrades",
        "request_body":{
            "DirectDownload":{},
            "NetworkShare":{
                "MapType":"www",
                "Upgradeoption":"nw_upgrade_full",
                "HttpServer":{
                    "LocationLink": "http://cloud-city-gateway.eastus.cloudapp.azure.com/ucs-c240m4-huu-4.0.2h.iso"
                }
            },
            "UpgradeType":"network_upgrade",
            "Server":""
        }
    }

    RESPONSE = requests.request(
        method=rackunit_json_body['request_method'],
        url=rackunit_json_body['resource_path'],
        auth=AUTH
    )
    print(RESPONSE)
    print(RESPONSE.text)

    firmware_json_body['request_body']['Server'] = (
        json.loads(RESPONSE.text)['Results'][0]['Moid']
    )

    print(firmware_json_body['request_body'])

    RESPONSE = requests.request(
        method=firmware_json_body['request_method'],
        url=firmware_json_body['resource_path'],
        data=json.dumps(firmware_json_body['request_body']),
        auth=AUTH
    )

    print(RESPONSE)
    print(RESPONSE.text)
