"""Run on your laptop against a copy of sightings.db.
Usage: python -m host.query_tool [path-to-sightings.db]
Get a copy with: scp youruser@dropbox.local:~/sightings.db ."""
import sqlite3
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "sightings.db"
con = sqlite3.connect(path)
rows = con.execute("""SELECT mac, vendor, hostname, randomized_mac, COUNT(*) as hits
                       FROM sightings GROUP BY mac ORDER BY hits DESC""").fetchall()
for mac, vendor, hostname, randomized, hits in rows:
    tag = " [randomized]" if randomized else ""
    print(f"{mac:<18} {vendor:<20} {hostname:<20} seen {hits} times{tag}")