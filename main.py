import socket
from recon.whois_info import get_whois_info
from recon.dns import get_dns_records
from recon.ip_info import get_ip_info
from report.report_writer import save_report
from recon.subdomains import get_subdomains


target = input("Enter domain or IP address: ").strip()

# IP çözümleme
try:
    ip_address = socket.gethostbyname(target)
    print(f"[+] Resolved IP: {ip_address}")
except socket.gaierror:
    print("[-] Invalid target")
    exit(1)

# WHOIS
whois_data = get_whois_info(target)
print("[+] WHOIS fetched successfully" if whois_data else "[-] WHOIS not available")

# DNS
dns_data = get_dns_records(target)
print("[+] DNS Records fetched")

# IP Info
ip_info = get_ip_info(ip_address)
print("[+] IP Info fetched")

raw_subdomains, subdomains = get_subdomains(target)
print(f"[+] Subdomains found: {len(subdomains)}")

# Rapor oluştur
report = {
    "target": target,
    "ip": ip_address,
    "whois": dict(whois_data) if whois_data else {},
    "dns_records": dns_data,
    "ip_info": ip_info,
    "subdomains": subdomains,
    "stats": {
        "raw_subdomains": len(raw_subdomains),
        "filtered_subdomains": len(subdomains)
    }
}



save_report(target, report)
