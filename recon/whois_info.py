import whois

def get_whois_info(target):
    try:
        domain_info = whois.whois(target)
        return domain_info
    except Exception as e:
        print(f"[-] Could not fetch WHOIS info: {e}")
        return None
