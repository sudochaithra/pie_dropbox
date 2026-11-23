"""Second-opinion fingerprinting: MAC-randomization detection and hostname lookup.
J functions, no network access needed to test the logic itself."""
import socket


def is_randomized_mac(mac: str) -> bool:
    """True if the 'locally administered' bit is set, meaning this MAC is almost
    certainly randomized by the OS (iOS/Android privacy MACs) rather than the
    device's real, factory-assigned hardware address."""
    first_octet = int(mac.split(":")[0], 16)
    return bool(first_octet & 0b00000010)


def resolve_hostname(ip: str, timeout: float = 1.0) -> str:
    """Best-effort reverse DNS / NetBIOS name. Returns 'unknown' if nothing answers,
    which is common and not an error — lots of devices don't broadcast a name."""
    try:
        socket.setdefaulttimeout(timeout)
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror, socket.timeout):
        return "unknown"