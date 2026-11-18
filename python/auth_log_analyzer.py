
import re
import sys
from collections import Counter

def analyze_logs(filename):

    failed_attempts = Counter()

    pattern = re.compile(
        r"Failed password for (?:invalid user )?\S+ from ([\d.]+)"
    )

    try:
        with open(filename, "r") as log_file:

            for line in log_file:

                match = pattern.search(line)

                if match:
                    ip_address = match.group(1)
                    failed_attempts[ip_address] += 1

    except FileNotFoundError:
        print("[ERROR] Log file not found.")
        return

    print("\n--- SSH AUTHENTICATION REPORT ---")

    if not failed_attempts:
        print("No matching failed SSH logins found.")
        return

    for ip, attempts in failed_attempts.most_common():

        print(f"IP: {ip} | Failed attempts: {attempts}")

        if attempts >= 5:
            print("[WARNING] Multiple failed login attempts detected.")

    print("\nAnalysis completed.")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 auth_log_analyzer.py <logfile>")
        sys.exit(1)

    analyze_logs(sys.argv[1])

