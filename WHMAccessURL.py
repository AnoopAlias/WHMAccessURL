#!/usr/bin/env python


import requests
import os
import subprocess


__author__ = "Anoop P Alias"
__copyright__ = "Copyright 2014, PiServe Technologies Pvt Ltd , India"
__license__ = "GPL"
__email__ = "anoop.alias@piserve.com"


def get_whm_access():
    with open("/root/.accesshash", 'r') as accessfile:
        hashdata = accessfile.read().replace('\n', '')
    authdata = "WHM root:"+hashdata
    headers = {'Authorization': authdata}
    r = requests.get("https://127.0.0.1:2087/json-api/create_user_session?api.version=1&user=root&service=whostmgrd", headers=headers, verify=False)
    jsonresp = r.json()
    datadict = jsonresp.get('data')
    url = datadict.get('url')
    print(url)
    return


if __name__ == "__main__":
    if os.path.exists("/root/.accesshash"):
        get_whm_access()
    else:
        subprocess.call("/usr/local/cpanel/bin/mkaccesshash", shell=True)
        get_whm_access()
