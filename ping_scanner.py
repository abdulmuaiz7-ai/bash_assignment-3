import subprocess
import platform
import re

def ping_host(host):
    system = platform.system().lower()

    # Set ping command based on OS
    if system == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        output = result.stdout

        reachable = False
        avg_time = None

        # Check if host is reachable
        if "ttl" in output.lower():
            reachable = True

        # Extract average response time
        if system == "windows":
            match = re.search(r"Average = (\d+)ms", output)
        else:
            match = re.search(r"= [\d\.]+/([\d\.]+)/", output)

        if match:
            avg_time = match.group(1)

        return {
            "host": host,
            "reachable": reachable,
            "avg_response_time": avg_time
        }

    except subprocess.TimeoutExpired:
        return {
            "host": host,
            "reachable": False,
            "avg_response_time": None
        }


def scan_hosts(hosts):
    results = []
    for host in hosts:
        result = ping_host(host)
        results.append(result)
    return results


if __name__ == "__main__":
    user_input = input("Enter hostname/IP (comma-separated for multiple): ")

    # Split input into multiple hosts
    hosts = [h.strip() for h in user_input.split(",")]

    results = scan_hosts(hosts)

    print("\n--- Scan Results ---")
    for res in results:
        print(f"\nHost: {res['host']}")
        print("Reachable:", "Yes" if res["reachable"] else "No")
        print("Average Response Time:", f"{res['avg_response_time']} ms" if res["avg_response_time"] else "N/A")