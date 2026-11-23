"""Proves the parser handles real arp-scan output, using a recorded sample.
No Pi or arp-scan installation needed to run this."""
from dropbox.store import parse_arp_scan_line

SAMPLE_OUTPUT = """Interface: wlan0, type: EN10MB, MAC: b8:27:eb:11:22:33, IPv4: 192.168.1.50
192.168.1.1\t00:11:22:33:44:01\tTP-LINK TECHNOLOGIES CO.,LTD.
192.168.1.14\tf4:9f:f3:aa:bb:cc\tSAMSUNG ELECTRO-MECHANICS

8 packets received by filter, 0 packets dropped by kernel
"""
rows = [r for line in SAMPLE_OUTPUT.splitlines() if (r := parse_arp_scan_line(line))]
assert rows == [
    ("192.168.1.1", "00:11:22:33:44:01", "TP-LINK TECHNOLOGIES CO.,LTD."),
    ("192.168.1.14", "f4:9f:f3:aa:bb:cc", "SAMSUNG ELECTRO-MECHANICS"),
]
print("firmware parser matches recorded arp-scan output:", len(rows), "devices parsed")