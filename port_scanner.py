import socket
import  common_ports

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    for port in common_ports.ports_and_services:
        if port in range(port_range[0],port_range[1]+1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Set timeout to 1 second
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                    if verbose:
                        print(f"Port {port}:{common_ports.ports_and_services[port]} is open on {target}")






    return(open_ports)

