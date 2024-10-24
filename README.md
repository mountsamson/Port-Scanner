# Port-Scanner
Several Port Scanning Tools using nmap and socket python library 

Scanner.py **Only works on Kali Linux** 


portscanner.py 
![image](https://github.com/user-attachments/assets/2f7312ed-df1a-4568-ab15-70dbe0a903d9)
<p>Checks if the ports are open or closed for a given IP address.</p>


scanner.py **Nmap Project**

![image](https://github.com/user-attachments/assets/ef8a535c-726c-4c39-8e59-e00e9d2a1a83)



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nmap Automation Tool - Detailed Description</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }
        .command {
            color: #007bff;
            font-weight: bold;
        }
        .feature {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<h1>Nmap Automation Tool - Detailed Description</h1>

<p>This Python script leverages the <code>nmap</code> library to automate the process of scanning network ports for a given IP address. It provides users with three scanning options and uses specific Nmap commands to perform each scan. The key details of the script are as follows:</p>

<h2>Features:</h2>

<div class="feature">
    <h3>1. SYN ACK Scan (TCP)</h3>
    <p><strong>Command used:</strong> <span class="command">nmap -v -sS &lt;ip_address&gt; -p 1-1024</span></p>
    <p><strong>Description:</strong> This scan uses a TCP SYN (half-open) scan to check for open ports in the range 1-1024. It is a faster and stealthier scan method.</p>
    <p><strong>Output:</strong> Displays open TCP ports and the state of the IP address.</p>
</div>

<div class="feature">
    <h3>2. UDP Scan</h3>
    <p><strong>Command used:</strong> <span class="command">nmap -v -sU &lt;ip_address&gt; -p 1-1024</span></p>
    <p><strong>Description:</strong> This scan checks for open UDP ports in the range 1-1024, which is slower but useful for detecting services like DNS or DHCP.</p>
    <p><strong>Output:</strong> Displays open UDP ports and the state of the IP address.</p>
</div>

<div class="feature">
    <h3>3. Comprehensive Scan</h3>
    <p><strong>Command used:</strong> <span class="command">nmap -v -sS -sV -sC -A -O &lt;ip_address&gt; -p 1-1024</span></p>
    <p><strong>Description:</strong> This detailed scan includes service version detection (<code>-sV</code>), default script scans (<code>-sC</code>), OS detection (<code>-O</code>), and additional aggressive scanning options (<code>-A</code>). It provides a complete overview of the target's network configuration.</p>
    <p><strong>Output:</strong> Displays open ports, detected services, protocols, and operating system information.</p>
</div>

<h2>How It Works:</h2>
<p><strong>User Input:</strong> The user enters an IP address and selects the scan type (1 for SYN ACK, 2 for UDP, 3 for Comprehensive).</p>
<p><strong>Scanning Process:</strong> Depending on the user's choice, the script runs the corresponding Nmap command and displays the results such as:</p>
<ul>
    <li>Open ports</li>
    <li>Active protocols</li>
    <li>IP state (whether the host is up or down)</li>
</ul>

<h2>Additional Features:</h2>
<ul>
    <li>Displays Nmap version being used.</li>
    <li>Handles invalid scan choices and ensures a valid scan type is selected.</li>
    <li>Simple ASCII art for a creative introduction and user interaction.</li>
</ul>

<p>This script is an easy-to-use tool for automating basic network scans, ideal for cybersecurity enthusiasts or IT professionals needing quick reconnaissance of a network.</p>

</body>
</html>
