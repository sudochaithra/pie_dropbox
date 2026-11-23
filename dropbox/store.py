"""Shared storage and parsing logic — one source of truth, used everywhere."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "sightings.db"


def init_db(path=DB_PATH):
    con = sqlite3.connect(path)
    con.execute("""CREATE TABLE IF NOT EXISTS sightings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seen_at TEXT, ip TEXT, mac TEXT, vendor TEXT,
        randomized_mac INTEGER, hostname TEXT)""")
    con.commit()
    return con


def log_sighting(con, ip, mac, vendor, randomized_mac=False, hostname="unknown"):
    con.execute(
        """INSERT INTO sightings (seen_at, ip, mac, vendor, randomized_mac, hostname)
           VALUES (datetime('now'), ?, ?, ?, ?, ?)""",
        (ip, mac, vendor, int(randomized_mac), hostname),
    )
    con.commit()


def parse_arp_scan_line(line):
    """One line of `arp-scan --localnet --plain` -> (ip, mac, vendor), or None
    if the line is a header/summary line rather than a device."""
    parts = line.split("\t")
    if len(parts) >= 2 and parts[0].count(".") == 3:
        return parts[0], parts[1], (parts[2] if len(parts) > 2 else "unknown")
    return None