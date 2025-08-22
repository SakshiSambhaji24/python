# Server configuration
server_ip = ("192.168.1.1",)  # Tuple (cannot be changed)
allowed_ips = ["192.168.1.2", "192.168.1.3"]  # List (can be updated)

# Function to update allowed_ips
def update_allowed_ips(new_ip):
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(f"IP {new_ip} added to allowed list.")
    else:
        print(f"IP {new_ip} already in the list.")

# Function to display configuration
def display_config():
    print("Server IP:", server_ip)
    print("Allowed IPs:", allowed_ips)

# Main program
display_config()  # Show initial config

update_allowed_ips("192.168.1.4")  # Add a new allowed IP
update_allowed_ips("192.168.1.2")  # Try adding an existing IP

# Try changing server_ip (should be avoided)
# server_ip = ("10.0.0.1",)  # Uncommenting this would break the rule

display_config()  # Show updated config