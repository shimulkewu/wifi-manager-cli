# utils_network.py
import subprocess

def current_wifi():
    try:
        out = subprocess.check_output(["networksetup", "-getairportnetwork", "en0"]).decode()
        return out.strip()
    except:
        return "Not connected"
def search_network(networks, keyword):
    return [n for n in networks if keyword.lower() in n["ssid"].lower()]

def strongest_network(networks):
    if not networks:
        return None
    return max(networks, key=lambda x: x["signal"])