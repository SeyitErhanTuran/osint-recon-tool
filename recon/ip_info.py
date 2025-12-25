import requests

def get_ip_info(ip):
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}").json()
        return resp
    except Exception as e:
        print(f"[-] Could not fetch IP info: {e}")
        return {}
