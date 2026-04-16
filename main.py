from scanner import scan_wifi
from utils import search_network, strongest_network
from exporter import export_to_csv


def display(networks):
    if not networks:
        print("\nNo networks found.\n")
        return

    print("\nAvailable Networks:\n")
    for i, n in enumerate(networks, 1):
        print(f"{i}. {n['ssid']} | Signal: {n['signal']} | Security: {n['security']}")


def main():
    networks = scan_wifi()  # initial scan

    while True:
        print("\n===== WIFI MANAGER CLI =====")
        print("1. Scan WiFi")
        print("2. Search Network")
        print("3. Show Strongest Network")
        print("4. Export to CSV")
        print("5. Refresh Scan")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            display(networks)

        elif choice == 2:
            keyword = input("Enter network name: ")
            results = search_network(networks, keyword)
            display(results)

        elif choice == 3:
            best = strongest_network(networks)

            if best:
                print("\nStrongest Network:")
                print(f"{best['ssid']} | Signal: {best['signal']} | {best['security']}")
            else:
                print("No networks found.")

        elif choice == 4:
            export_to_csv(networks)

        elif choice == 5:
            print("Refreshing scan...")
            networks = scan_wifi()

        elif choice == 6:
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()