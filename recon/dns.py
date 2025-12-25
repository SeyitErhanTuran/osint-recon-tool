import dns.resolver

def get_dns_records(domain):
    records = {}
    for rtype in ['A', 'MX', 'NS']:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(rdata) for rdata in answers]
        except Exception as e:
            records[rtype] = []
    return records
