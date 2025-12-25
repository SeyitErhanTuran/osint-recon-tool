import json
import os
from datetime import datetime

def save_report(target, data):
    # datetime objelerini stringe çevir
    def convert(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    if not os.path.exists("reports"):
        os.makedirs("reports")
    filepath = os.path.join("reports", f"{target}.json")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4, default=convert)
    print(f"[+] Report saved: {filepath}")
