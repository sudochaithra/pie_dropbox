"""Tests for the shared logic. Pure functions, no network or Pi needed."""
import os
import tempfile

from dropbox.store import init_db, log_sighting, parse_arp_scan_line
from dropbox.fingerprint import is_randomized_mac

row = parse_arp_scan_line("192.168.1.5\t00:11:22:33:44:55\tVendor Co")
assert row == ("192.168.1.5", "00:11:22:33:44:55", "Vendor Co")
print("1 ok: parses a normal arp-scan line")

row = parse_arp_scan_line("192.168.1.5\t00:11:22:33:44:55")
assert row == ("192.168.1.5", "00:11:22:33:44:55", "unknown")
print("2 ok: missing vendor becomes 'unknown'")

assert parse_arp_scan_line("Interface: wlan0, type: EN10MB") is None
assert parse_arp_scan_line("") is None
print("3 ok: non-device lines are skipped")

assert is_randomized_mac("02:11:22:33:44:55") is True
assert is_randomized_mac("f4:9f:f3:aa:bb:cc") is False
print("4 ok: MAC-randomization bit check is correct")

fd, path = tempfile.mkstemp(suffix=".db")
os.close(fd)
con = init_db(path)
log_sighting(con, "192.168.1.9", "aa:bb:cc:dd:ee:ff", "Test Vendor", False, "test-host")
assert con.execute("SELECT COUNT(*) FROM sightings").fetchone()[0] == 1
os.remove(path)
print("5 ok: log_sighting writes a row")

print("all tests passed")