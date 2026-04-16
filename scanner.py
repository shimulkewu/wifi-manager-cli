import subprocess

AIRPORT_PATH = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"

def scan_wifi():
    try:
        result = subprocess.check_output([AIRPORT_PATH, "-s"]).decode()
        return parse_output(result)
    except Exception as e:
        print("Error scanning WiFi:", e)
        return []

def parse_output(raw):
    lines = raw.split("\n")[1:]
    networks = []

    for line in lines:
        if line.strip():
            ssid = line[:32].strip()
            signal = line[48:52].strip()
            security = line[75:].strip()

            networks.append({
                "ssid": ssid,
                "signal": int(signal) if signal else 0,
                "security": security
            })

    return networks