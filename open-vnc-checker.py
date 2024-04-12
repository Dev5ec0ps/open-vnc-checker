import argparse
import socket

def check_vnc_authentication(ip_address, ports):
    vulnerable_ports = []
    for port in ports:
        try:
            with socket.create_connection((ip_address, port), timeout=5) as sock:
                sock.sendall(b"RFB\n")
                response = sock.recv(1024).decode('utf-8')
                if 'RFB' in response:
                    vulnerable_ports.append(port)
        except Exception as e:
            pass
    return vulnerable_ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check for publicly accessible VNC service without authentication.')
    parser.add_argument('-ip', '--ip_address', required=True, help='IP address to check')
    args = parser.parse_args()

    target_ip = args.ip_address
    ports = [5900, 5901, 5902, 5903, 5904, 5905, 5906, 5907, 5908, 5909, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 6008, 6009]  # Additional potential ports to check for VNC service
    vulnerable_ports = check_vnc_authentication(target_ip, ports)
    if vulnerable_ports:
        print("Vulnerable ports detected on the target IP address:")
        for port in vulnerable_ports:
            print(f"Port {port} is accessible without authentication.")
    else:
        print("No vulnerable ports detected.")
