import subprocess

def arp_scan():
    try:
        result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE, text=True)

        print("\nIP Address        MAC Address")
        print("-----------------------------------")

        lines = result.stdout.split("\n")
        count = 0

        for line in lines:
            parts = line.split()

            if len(parts) >= 2:
                ip = parts[0]
                mac = parts[1]

                print(f"{ip:<18} {mac}")
                count += 1

        print(f"\nTotal entries: {count}")

    except:
        print("Error occurred")


if __name__ == "__main__":
    print("=== ARP Scanner ===")
    arp_scan()