import http.client
import json
import sys
import config.settings as conf


def _read_from_jamf(serialnumber):
    """Reads data from Jamf API. 

    Parameters: 
    serialnumber (string): Computer serialnumber

    Returns: 
    json: Computer object. None if serialnumber not found or failed to contact Jamf API."""
    try:
        conn = http.client.HTTPSConnection(conf.jss_server)

        # Generate credentials with
        # printf "username:password" | iconv -t ISO-8859-1 | base64 -i -

        headers = {
            'authorization': "Basic %s" % (conf.jss_credential),
            'Accept': 'application/json'
        }

        conn.request("GET", "/JSSResource/computers/serialnumber/%s" % (serialnumber),
                     headers=headers)

        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return(json.loads(data))
    except:
        return None


def extenssion_attribute(data, id):
    for attribute in data["computer"]["extension_attributes"]:
        if attribute["id"] == id:
            return attribute["value"]
    return None


def get_computer(serialnumber):
    data = _read_from_jamf(serialnumber)

    if not data:
        return None

    computer = {
        "asset_tag": data["computer"]["general"]["asset_tag"],
        "serial_number": data["computer"]["general"]["serial_number"],
        "username": data["computer"]["location"]["username"],
        "ad_user": data["computer"]["location"]["position"][3:].split(',')[0]
    }

    # extenssion attributes from settings.py
    for ea in conf.attributes["extension_attributes"]:
        name = ea["name"]
        id = ea["id"]
        value = extenssion_attribute(data, id)
        if not value:
            continue
        computer[name] = value

    return(computer)
