from prettytable import PrettyTable  # Import PrettyTable for formatted output
import nmap # Import Python nmap
import ipaddress  # Import the ipaddress module for IP


def validate_ip(ip):
    """
    Validates if the provided IP is a valid IPv4 or IPv6 address.
    
    Args:
        ip (str): The IP address to validate.
        
    Returns:
        bool: True if valid, False if invalid.
    """
    try:
        ipaddress.ip_address(ip)  # Try to convert the IP address
        return True  # If no exception, the IP is valid
    except ValueError:  # If conversion fails, it's an invalid IP
        return False


def scan_host(ip_addresses):
    """
    Scans a list of IP addresses and prints the results in a formatted table.
    
    Args:
        ip_addresses (list): A list of IP addresses to be scanned.
    
    Returns:
        list: A list of scan results as formatted strings.
    """
    nm = nmap.PortScanner()  # Initialize PortScanner object to interact with Nmap
    scan_results = []  # List to store scan results
    
    # Initialize PrettyTable with column headers
    table = PrettyTable()
    table.field_names = ["IP Address", "Protocol", "Port", "State"]

    for host in ip_addresses:  # Loop through each IP address
        if not validate_ip(host):  # Validate the IP before scanning
            print(f"Skipping invalid IP address: {host}")
            continue  # Skip invalid IPs
        
        print(f'Scanning {host}...')  # Inform the user that the scan is starting
        nm.scan(host, '1-1024')  # Scan the host for open ports between 1-1024

        if host in nm.all_hosts():  # Check if the host is up and responsive
            for proto in nm[host].all_protocols():  # Get the protocols 
                ports = nm[host][proto].keys()  # Retrieve the list of open ports for that protocol
                for port in ports:  # Loop through each port
                    state = nm[host][proto][port]['state']  # Get the state of the port (open/closed)
                    
                    # Add row to PrettyTable
                    table.add_row([host, proto, port, state])
                    
        else:
            print(f'Host {host} is down or unresponsive.')  # Inform if the host is unreachable

    # Print the PrettyTable in terminal
    print(table)

    # Save PrettyTable to scan_results list (for saving to a file)
    scan_results.append(table.get_string())  # Store table as a formatted string

    return scan_results  # Return the list of scan results


def save_scan_results(scan_results):
    """
    Saves the scan results to a specified text file.
    
    Args:
        scan_results (list): The formatted scan results to be saved.
    
    Returns:
        None
    """
    file_name = input('Enter the name of the file to save the scan results (e.g., scan_results.txt): ')
    with open(file_name, 'w') as file:  # Open the file in write mode
        for result in scan_results:  # Write each result to the file
            file.write(result + '\n')  # Write the formatted table to the file
    print(f'Scan results have been saved to {file_name}')


def convert_lines(file_name):
    """
    Reads a list of IP addresses from a text file and returns them as a list.
    
    Args:
        file_name (str): The name of the file to read the IP addresses from.
    
    Returns:
        list: A list of IP addresses as strings.
    """
    with open(file_name, 'r') as file:  # Open the file in read mode
        ip_addresses = [line.strip() for line in file]  # Strip newlines and spaces from each line
    return ip_addresses  # Return the list of cleaned IP addresses


def add_ip(file_name):
    """
    Prompts the user to enter an IP address, validates it, and adds it to the file if valid.
    
    Args:
        file_name (str): The name of the file to save the IP addresses to.
    
    Returns:
        None
    """
    ip_input = input('Enter an IP address to add to the list: ').strip()  # Get input and strip spaces
    
    if validate_ip(ip_input):  # Validate the IP address
        with open(file_name, 'a') as file:  # Open the file in append mode
            file.write(ip_input + '\n')  # Write the new IP to the file and add a newline
        print(f'{ip_input} has been added to the file {file_name}')  # Confirm the addition
    else:
        print(f'Error: {ip_input} is not a valid IP address.')  # Notify the user if the IP is invalid


def remove_ip(file_name):
    """
    Prompts the user to enter an IP address to remove from the file and removes it if found.
    
    Args:
        file_name (str): The name of the file to modify.
    
    Returns:
        None
    """
    rmv_ip = input('Enter the IP address you wish to delete: ').strip()  # Get IP from user input and strip spaces
    print(f'The user wants to remove {rmv_ip}')  # Debugging print statement
    
    with open(file_name, 'r') as file:  # Open the file in read mode
        items = [i.strip() for i in file]  # Strip newlines from each IP in the file
    
    print(f'The current list of IP addresses is {items}')  # Debugging: show current list of IPs
    if rmv_ip in items:  # If the IP exists in the list
        items.remove(rmv_ip)  # Remove the IP from the list
        print(f'The IP address {rmv_ip} was removed from the list.')
        
        with open(file_name, 'w') as file:  # Open the file in write mode to overwrite the updated list
            for item in items:  # Write the updated list back to the file
                file.write(item + '\n')
        print(f'Updated list of IP addresses: {items}')  # Show the updated list
    else:
        print(f'The IP address {rmv_ip} is not in the list, nothing removed.')  # Notify if IP wasn't found


def view_ip(file_name):
    """
    Displays all IP addresses stored in the specified file.
    
    Args:
        file_name (str): The name of the file to read the IP addresses from.
    
    Returns:
        None
    """
    try:
        with open(file_name, 'r') as file:  # Open the file in read mode
            items = [i.strip() for i in file if i.strip()]  # Strip newlines and skip empty lines
            
            if items:  # If the list is not empty, print the IPs
                print('IP addresses currently in the list:')
                for item in items:
                    print(item)  # Print each IP address
                print('\n\n')  # Add two line breaks after listing the IPs
            else:
                print('The list of IP addresses is empty.\n\n')  # Notify if no IPs are in the list
                
    except FileNotFoundError:  # If the file doesn't exist
        print(f'The file {file_name} does not exist, add IP addresses first.\n\n')


def clear_list(file_name):
    """
    Clears the entire list of IP addresses from the specified file.
    
    Args:
        file_name (str): The name of the file to clear.
    
    Returns:
        None
    """
    print(f'Are you sure you want to clear the list of IP addresses?')
    clear_choice = input('y/n: ')  # Get confirmation from the user
    if clear_choice.lower() == 'y':  # If the user confirms
        with open(file_name, 'w') as file:  # Open the file in write mode (which clears the content)
            pass  # No content is written, so the file is effectively cleared
        print(f'IP address file cleared.')
    else:
        print(f'You entered {clear_choice}, list will not be cleared.')  # Notify if the user chooses not to clear


# Menu options for interacting with the program
menu_items = [
    "Scan IP-address", 
    "Add IP-address to scan list", 
    "Delete IP-address from scan list", 
    "View scan list", 
    "Clear scan list", 
    "Exit"
]
menu_title = 'Main Menu'

# Main menu loop
while True:
    print(menu_title)
    print('=' * len(menu_title))  # Print a separator line
    for value, menu_item in enumerate(menu_items):  # Loop through the menu items and print each with a number
        print(f'{value+1}. {menu_item}')
    menu_selection = input('> ')  # Get the user's selection
    
    if menu_selection == '1':  # If "Scan IP-address" is selected
        ip_addresses = convert_lines('ip_addresses.txt')  # Read IP addresses from the file
        scan_results = scan_host(ip_addresses)  # Perform the scan and get the results

        # Ask the user if they want to save the results
        save_choice = input('Do you want to save the scan results to a file? (y/n): ').lower()
        if save_choice == 'y':
            save_scan_results(scan_results)  # Save the scan results to a file

    elif menu_selection == '2':  # If "Add IP-address to scan list" is selected
        add_ip('ip_addresses.txt')  # Add a new IP to the file
            
    elif menu_selection == '3':  # If "Delete IP-address from scan list" is selected
        remove_ip('ip_addresses.txt')  # Remove an IP from the file
    
    elif menu_selection == '4':  # If "View scan list" is selected
        view_ip('ip_addresses.txt')  # View all IPs in the file
    
    elif menu_selection == '5':  # If "Clear scan list" is selected
        clear_list('ip_addresses.txt')  # Clear the list of IPs in the file
    
    elif menu_selection == '6':  # If "Exit" is selected
        break  # Exit the loop and the program

print('Thank you for using nmap-scanner. Bye!')  # Final message when exiting the program
