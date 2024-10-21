
Here is the full text as requested, in a single format so you can easily copy everything:

README
Project Overview
This repository contains two separate Python tools, each designed as a lab assignment for network and security tasks:

Lab 1: Nmap Scanner
Lab 2: Encryption/Decryption Tool
Lab 1: Nmap Scanner
Description
The Nmap Scanner is a Python script that reads a list of IP addresses from a text file, performs a port scan on the specified IPs using Nmap, and logs the results both to the terminal and to a text file.

Features:
Accepts a list of IP addresses from a file (ip_addresses.txt).
Scans each IP for open ports in the range 1-1024 using Nmap.
Outputs the scan results to the terminal and saves them to a file.
Offers a menu to add, delete, view, or clear IP addresses from the list.
How to Use:
Install the required libraries: Ensure you have Nmap installed on your system. Also, install the python-nmap library:

bash
Copy code
pip install python-nmap
Add IP Addresses: You can add IP addresses to the ip_addresses.txt file through the menu in the script or manually by editing the file. Each IP address should be on a new line.

Run the Script: Run the script to perform scans on the listed IP addresses:

bash
Copy code
python nmap_scanner.py
Menu Options:

1: Scan IP addresses.
2: Add an IP address to the list.
3: Delete an IP address from the list.
4: View all IP addresses currently in the list.
5: Clear all IP addresses from the list.
6: Exit the program.
Outputs:

The scan results will be displayed in the terminal.
A log of the results will be saved to a text file for later reference.
Lab 2: Encryption/Decryption Tool
Description
The Encryption/Decryption Tool is a Python application that allows you to securely encrypt and decrypt files using a symmetric key. It includes two separate scripts: one for generating and saving a symmetric encryption key and another for encrypting or decrypting files using the generated key.

Features:
Key Generation: A script that generates a symmetric encryption key and saves it to a file (key_file.key).
File Encryption: Encrypts any file using the saved key, replacing the original file with its encrypted version.
File Decryption: Decrypts an encrypted file, replacing the encrypted version with the decrypted one.
How to Use:
Install Required Libraries: The cryptography library is required to use this tool:

bash
Copy code
pip install cryptography
Generate a Key: First, generate a symmetric encryption key and save it to key_file.key:

bash
Copy code
python generate_key.py
Encrypt a File: To encrypt a file, run the following command:

bash
Copy code
python crypto_tool.py encrypt <file_to_encrypt> key_file.key
Example:

bash
Copy code
python crypto_tool.py encrypt my_file.txt key_file.key
This will encrypt my_file.txt and replace it with my_file.txt.encrypted.

Decrypt a File: To decrypt an encrypted file, use the following command:

bash
Copy code
python crypto_tool.py decrypt <file_to_decrypt> key_file.key
Example:

bash
Copy code
python crypto_tool.py decrypt my_file.txt.encrypted key_file.key
This will decrypt the file and replace my_file.txt.encrypted with my_file.txt.

Important Notes:

Ensure you keep the key_file.key secure, as it is required to both encrypt and decrypt files.
The original file is removed after encryption, and the encrypted file is removed after decryption to avoid keeping duplicates.
Contact Information
If you have any questions or feedback regarding these tools, please reach out to me at your_email@example.com.
