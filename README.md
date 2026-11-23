# ── ୨ৎ ── PIE DROP-BOX ── ୨ৎ ──

Normally a computer contains both a screen and keyboard. Headless means neither exists. Pie Dropbox still logs every device that enters your network.<br>Built with Python for a Raspberry Pi Zero 2 W, plus a Docker virtual network.

## ✦ʚ♡ɞ✦ ARCHITECTURE
```
pie-dropbox/
├── dropbox/
│   ├── store.py
│   └── fingerprint.py
├── lab/
│   └── docker-compose.yml
├── firmware/
│   └── scanner.py
├── host/
│   └── query_tool.py
├── tests_quick.py
├── tests_lab_scan.py
└── tests_firmware_scanner.py
```

## ✦ʚ♡ɞ✦ INSTALLATION

* **No hardware (any OS):** Python `3.9+`

```
git clone https://github.com/sudochaithra/pie-dropbox.git
cd pie-dropbox
python tests_quick.py
python tests_firmware_scanner.py
```

* **Hardware (Pi Zero 2 W):** Raspberry Pi OS Lite, `arp-scan`

```
sudo apt install -y arp-scan
git clone https://github.com/sudochaithra/pie-dropbox.git
cd pie-dropbox
python3 -m firmware.scanner
```

## ✦ʚ♡ɞ✦ Tests

```
python tests_quick.py             # unit tests: parser, fingerprint, storage
python tests_lab_scan.py          # runs the real scanner against the Docker lab (docker compose up & arp-scan)
python tests_firmware_scanner.py  # checks the parser against a recorded real arp-scan output

```

## ✦ʚ♡ɞ✦ SKILLS 
![device fingerprinting](https://img.shields.io/badge/Device%20fingerprinting-462b30?style=flat-square)
![mac privacy](https://img.shields.io/badge/MAC%20randomization%20detection-462b30?style=flat-square)
![network recon](https://img.shields.io/badge/Network%20recon-462b30?style=flat-square)
![Python](https://img.shields.io/badge/Python-dae7a1?style=flat-square&logo=python&logoColor=462b30)
![SQLite](https://img.shields.io/badge/SQLite-dae7a1?style=flat-square&logo=sqlite&logoColor=462b30)
![Bash](https://img.shields.io/badge/Bash-dae7a1?style=flat-square&logo=gnubash&logoColor=462b30)
![systemd](https://img.shields.io/badge/systemd-dae7a1?style=flat-square&labelColor=462b30)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-39426d?style=flat-square&logo=raspberrypi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-39426d?style=flat-square&logo=docker&logoColor=white)
![Tailscale](https://img.shields.io/badge/Tailscale-39426d?style=flat-square&logo=tailscale&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-39426d?style=flat-square&logo=linux&logoColor=white)
