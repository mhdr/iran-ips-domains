from ipaddress import ip_address, IPv4Address


def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"


if __name__ == '__main__':
    # Enter the Ip address
    line = "109.110.160.0"
    pp = line.partition("/")
    if len(pp) == 3:
        ip = pp[0]
        print(validIPAddress(ip))
