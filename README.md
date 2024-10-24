# Port-Scanner
Several Port Scanning Tools using nmap and socket python library 

Scanner.py **Only works on Kali Linux** 


portscanner.py 
![image](https://github.com/user-attachments/assets/2f7312ed-df1a-4568-ab15-70dbe0a903d9)
<p>Checks if the ports are open or closed for a given IP address.</p>


scanner.py **Nmap Project**

![image](https://github.com/user-attachments/assets/ef8a535c-726c-4c39-8e59-e00e9d2a1a83)

Nmap Automation Tool - Detailed Description
This Python script leverages the nmap library to automate the process of scanning network ports for a given IP address. It provides users with three scanning options and uses specific Nmap commands to perform each scan. The key details of the script are as follows:

Features:
SYN ACK Scan (TCP):

Command used: nmap -v -sS <ip_address> -p 1-1024
Description: This scan uses a TCP SYN (half-open) scan to check for open ports in the range 1-1024. It is a faster and stealthier scan method.
Output: Displays open TCP ports and the state of the IP address.
UDP Scan:

Command used: nmap -v -sU <ip_address> -p 1-1024
Description: This scan checks for open UDP ports in the range 1-1024, which is slower but useful for detecting services like DNS or DHCP.
Output: Displays open UDP ports and the state of the IP address.
Comprehensive Scan:

Command used: nmap -v -sS -sV -sC -A -O <ip_address> -p 1-1024
Description: This detailed scan includes service version detection (-sV), default script scans (-sC), OS detection (-O), and additional aggressive scanning options (-A). It provides a complete overview of the target's network configuration.
Output: Displays open ports, detected services, protocols, and operating system information.
How It Works:
User Input: The user enters an IP address and selects the scan type (1 for SYN ACK, 2 for UDP, 3 for Comprehensive).
Scanning Process: Depending on the user's choice, the script runs the corresponding Nmap command and displays the results such as:
Open ports
Active protocols
IP state (whether the host is up or down)
Additional Features:
Displays Nmap version being used.
Handles invalid scan choices and ensures a valid scan type is selected.
Simple ASCII art for a creative introduction and user interaction.
This script is an easy-to-use tool for automating basic network scans, ideal for cybersecurity enthusiasts or IT professionals needing quick reconnaissance of a network.
