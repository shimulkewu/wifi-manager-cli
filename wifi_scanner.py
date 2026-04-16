import subprocess

def scan_wifi():
    try:
        result = subprocess.check_output([
            "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
            "-s"
        ])

        networks = result.decode()
        print("\nAvailable WiFi Networks:\n")
        print(networks)

    except Exception as e:
        print("Error:", e)
def parse_wifi():
    result = subprocess.check_output([
        "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
        "-s"
    ]).decode()

    lines = result.split("\n")[1:]  # skip header

    for line in lines:
        if line.strip():
            ssid = line[:32].strip()
            signal = line[48:52].strip()
            security = line[75:].strip()

            print(f"SSID: {ssid} | Signal: {signal} | Security: {security}")

if __name__ == "__main__":
    scan_wifi()