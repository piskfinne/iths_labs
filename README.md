# README

## Project Overview

This repository contains two separate Python tools, each designed as a lab assignment for network and security tasks:

1. **Lab 1: Nmap Scanner**
2. **Lab 2: Encryption/Decryption Tool**

---

## Lab 1: Nmap Scanner

### Description
The Nmap Scanner is a Python script that reads a list of IP addresses from a text file, performs a port scan on the specified IPs using Nmap, and logs the results both to the terminal and to a text file.

### Features:
- Accepts a list of IP addresses from a file (`ip_addresses.txt`).
- Scans each IP for open ports in the range `1-1024` using Nmap.
- Outputs the scan results to the terminal and saves them to a file.
- Offers a menu to add, delete, view, or clear IP addresses from the list.

### How to Use:
1. **Install the required libraries**:
   Ensure you have Nmap installed on your system. Also, install the `python-nmap` library:
   ```bash
   pip install python-nmap
