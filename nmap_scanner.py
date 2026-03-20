import subprocess

def check_nmap():
    try:
        subprocess.run(["nmap", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Nmap is installed\n")
        return True
    except:
        print("Nmap not installed")
        return False


def run_scan(target, choice):
    if choice == "1":
        command = ["nmap", "-sn", target]

    elif choice == "2":
        command = ["nmap", target]

    elif choice == "3":
        ports = input("Enter port range (e.g. 20-80): ")
        command = ["nmap", "-p", ports, target]

    elif choice == "4":
        command = ["nmap", "-sV", target]

    elif choice == "5":
        command = ["nmap", "-O", target]

    else:
        print("Invalid choice")
        return

    try:
        print("\nScanning...\n")
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, timeout=60)

        print("=== RESULTS ===")
        print(result.stdout)

    except:
        print("Scan failed or timed out")


if __name__ == "__main__":
    print("=== Nmap Scanner ===")

    if not check_nmap():
        exit()

    target = input("Enter target IP: ")

    print("""
1. Host Discovery
2. Port Scan
3. Custom Port Scan
4. Service Version
5. OS Detection
""")

    choice = input("Enter choice: ")
    run_scan(target, choice)