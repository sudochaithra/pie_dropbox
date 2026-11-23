"""Real drop-box scanner. Needs arp-scan installed, runs on the Pi (or WSL for testing).
Only scan networks you own or have permission to scan."""
import subprocess
import time

from dropbox.store import init_db, log_sighting, parse_arp_scan_line
from dropbox.fingerprint import is_randomized_mac, resolve_hostname


def scan():
    result = subprocess.run(
        ["sudo", "arp-scan", "--localnet", "--plain"],
        capture_output=True, text=True, timeout=30,
    )
    rows = []
    for line in result.stdout.splitlines():
        parsed = parse_arp_scan_line(line)
        if parsed:
            ip, mac, vendor = parsed
            rows.append((ip, mac, vendor, is_randomized_mac(mac), resolve_hostname(ip)))
    return rows


def main():
    con = init_db()
    print("scanning... (Ctrl+C to stop)")
    try:
        while True:
            for ip, mac, vendor, randomized, hostname in scan():
                log_sighting(con, ip, mac, vendor, randomized, hostname)
                flag = " [randomized MAC]" if randomized else ""
                print(f"{ip:<15} {mac:<18} {vendor:<20} {hostname}{flag}")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()