# ── ୨ৎ ── PIE DROP-BOX ── ୨ৎ ──

Normally a computer needs a screen to tell you what's happening, and a keyboard for you to respond. Headless means neither exists:, except it quietly logs every device that walks onto your own network.<br>Built with Python for a Raspberry Pi Zero 2 W, plus a Python virtual network.

## ✦ʚ♡ɞ✦ Architecture
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

## ✦ʚ♡ɞ✦ Installation

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

## ✦ʚ♡ɞ✦ Tests

```
python tests_quick.py             # unit tests: parser, fingerprint, storage
python tests_lab_scan.py          # runs the real scanner against the Docker lab
python tests_firmware_scanner.py  # parity test vs a recorded pcap-derived sample

```

## ✦ʚ♡ɞ✦ Skills
