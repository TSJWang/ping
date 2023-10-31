import subprocess

def ping(ip_address):
    """Pings an IP address and returns True if it is pingable, False otherwise."""
    command = ['ping', '-w', '1', '-c', '1', '-n', '1', ip_address]
    output = subprocess.run(command, stdout=subprocess.PIPE)
    return output.returncode == 0

def scan_ip_range(first_three_fields):
    """Scans an IP address range and returns a list of pingable IP addresses."""
    pingable_ips = []
    for i in range(0, 256):
        ip_address = first_three_fields + '.' + str(i)
        # print(ip_address)
        if ping(ip_address):
            print(ip_address)
            pingable_ips.append(ip_address)
    return pingable_ips
 
if __name__ == '__main__':
    first_three_fields = input('Enter the first three fields of the IP address range: ')
    pingable_ips = scan_ip_range(first_three_fields)
    print('Pingable IP addresses:')
    for ip_address in pingable_ips:
        print(ip_address)