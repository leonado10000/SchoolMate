import requests
import socket

def get_public_ip():
    """
    Retrieves the public IP address by sending a request to an external API.
    Uses the reliable 'https://api.ipify.org' service.
    """
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except requests.exceptions.RequestException as e:
        return f"Error getting public IP: {e}"

def get_local_ip():
    """
    Attempts to get the local IP address by connecting to an external server.
    This works by querying which local interface would be used to reach a 
    known external IP (e.g., Google's DNS server 8.8.8.8) without sending any data.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Does not require the remote host to be reachable
        s.connect(("8.8.8.8", 80)) 
        IP = s.getsockname()[0]
    except socket.error:
        IP = "127.0.0.1" # Fallback to loopback if no network connection
    finally:
        s.close()
    return IP
