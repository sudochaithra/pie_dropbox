# ── ୨ৎ ── PIE DROP-BOX ── ୨ৎ ──

Normally a computer needs a screen to tell you what's happening, and a keyboard for you to respond. Headless means neither exists:, except it logs every device that enters your network.<br>Built with Python for a Raspberry Pi Zero 2 W, plus a Python virtual network.

## ✦ʚ♡ɞ✦ ARCHITECTURE 
```
pi-dropbox/
├── dropbox/
│   ├── store.py         
│   └── fingerprint.py    
├── lab/                 
│   ├── docker-compose.yml  
│   └── devices/           
├── firmware/
│   ├── scanner.py       
│   └── dropbox-scanner.service
├── host/
│   └── query_tool.py
├── tests_quick.py              
├── tests_lab_scan.py            
└── tests_firmware_scanner.py   
```

## ✦ʚ♡ɞ✦ INSTALLATION 

* **Simulator (Windows):** Python `3.9+`

```
git clone https://github.com/sudochaithra/pie-dropbox.git
cd pie-dropbox
python -m simulator.fake_scanner
```

* **Hardware (Pi Zero 2 W):** Raspberry Pi OS Lite, `arp-scan`, Tailscale

```
sudo apt install -y arp-scan
scp firmware/scanner.py youruser@dropbox.local:~/
sudo cp firmware/dropbox-scanner.service /etc/systemd/system/
sudo systemctl enable --now dropbox-scanner
```

## ✦ʚ♡ɞ✦ TESTS

```
python tests_quick.py             # unit tests: parser, fingerprint, storage
python tests_lab_scan.py          # runs the real scanner against the Docker lab
python tests_firmware_scanner.py  # parity test vs a recorded pcap-derived sample

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
