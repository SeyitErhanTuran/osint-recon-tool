import requests
import time

def get_subdomains(domain, retries=3, timeout=30):
    url = f"https://crt.sh/?q={domain}&output=json"

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()

            data = response.json()
            subdomains = set()

            for entry in data:
                name = entry.get("name_value")
                if name:
                    subdomains.update(name.split("\n"))

            raw = sorted(subdomains)
            return raw, clean_subdomains(raw, domain)

        except requests.exceptions.RequestException as e:
            print(f"[-] Subdomain fetch failed ({attempt+1}/{retries}): {e}")
            time.sleep(2)

    print("[-] Subdomain enumeration failed completely")
    return []


def clean_subdomains(subdomains, domain):
    cleaned = []

    for sub in subdomains:
        if sub.startswith("*"):
            continue
        if "@" in sub:
            continue
        if not sub.endswith(domain):
            continue
        cleaned.append(sub)

    return sorted(set(cleaned))
