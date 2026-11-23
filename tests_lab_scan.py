"""Runs the real scanner against the Docker lab network.
Needs: docker compose -f lab/docker-compose.yml up -d, and arp-scan installed."""
from firmware.scanner import scan

rows = scan()
assert len(rows) >= 2, "expected to see at least the lab containers"
print(f"saw {len(rows)} real devices on the lab network:", rows)