# saved_wifi.py
import subprocess
def get_wifi_password(ssid):
    try:
        result = subprocess.check_output(
            ["security", "find-generic-password", "-wa", ssid]
        )
        return result.decode().strip()
    except:
        return "Access denied / Not found"
def analyze_security(networks):
    print("\nSecurity Analysis:\n")

    for n in networks:
        if "WEP" in n["security"] or "OPEN" in n["security"]:
            print(f"⚠ Weak Security: {n['ssid']} ({n['security']})")
        else:
            print(f"✔ Secure: {n['ssid']} ({n['security']})")
def rank_networks(networks):
    return sorted(networks, key=lambda x: x["signal"], reverse=True)

def list_saved_wifi():
    try:
        result = subprocess.check_output(
            ["security", "find-generic-password", "-D", "AirPort network password"]
        ).decode(errors="ignore")

        networks = []
        for line in result.split("\n"):
            if "acct" in line:
                networks.append(line.split('"')[1])
        return networks
    except:
        return []