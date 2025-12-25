# OSINT Recon Tool

A modular Python-based OSINT reconnaissance tool that gathers publicly available information about a target domain and produces a structured JSON report.

This tool is designed for **educational purposes**, **defensive security**, and **legal OSINT reconnaissance** only.

---

## Features

- Domain IP resolution
- WHOIS information lookup
- DNS record enumeration (A, MX, NS)
- Subdomain discovery using Certificate Transparency logs (crt.sh)
- Subdomain normalization and filtering
- External IP intelligence lookup
- Structured JSON reporting with statistics

---

## Example Data Collected

- Target domain
- Resolved IP address
- WHOIS metadata
- DNS records
- IP geolocation and ASN info
- Raw vs filtered subdomain count
- Clean subdomain list

---

## Installation

- git clone https://github.com/SeyitErhanTuran/osint-recon-tool.git
- cd osint-recon-tool
- python3 -m venv venv
- Activate virtual environment:
  - For Linux/macOS: `source venv/bin/activate`
  - For Windows: `venv\Scripts\activate`
- pip install -r requirements.txt
  
---

### Usage

python main.py

---

## Sample Report Output

{
    "target": "DOMAIN NAME",
    "ip": "IP ADDRESS",
    "subdomains": [...],
    "stats": {
        "raw_subdomains": 5,
        "filtered_subdomains": 2 
    }
}

---

## Legal Disclaimer

This tool uses only publicly available data sources such as:

- Certificate Transparency logs
- WHOIS records
- DNS records
- Public IP information APIs

No exploitation, scanning, or brute-force techniques are used.

Use this tool **only on domains you own or have permission to analyze**, or for educational purposes. The author is not responsible for misuse.

---
