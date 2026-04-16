import csv

def export_to_csv(networks, filename="wifi_report.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["SSID", "Signal", "Security"])

        for n in networks:
            writer.writerow([n["ssid"], n["signal"], n["security"]])

    print(f"Report saved as {filename}")