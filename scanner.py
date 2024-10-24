

import nmap

scanner = nmap.PortScanner()

print("Welcome, This is my simple nmap automation tool - created by Carl Samson")
print("""
      
             /'.    /|    .'
           ,._   |+i\  /++\  / +|    ,,
           |*+'._/+++\/+ ++\/+++<_.-'+|
      :-.  \ ++++?++ +++++*++++++ +++ /  .-:11
      |*+\_/++++ +++*++ ++++++ ++?++++\_/ +|
  ,    \*+++++ ++++ +++*+++ ++++ +++ +++++/   ,
  \'-._> +__+*++__*+++_+__*++ ++__++++__*<_.-'/
   `>*+++|  \++/  |+*/     `\ +|  |++/  |++++<'
_,-'+ * +*\  \/  /++|__.-.  |+ |  |+/  /+ +*+'-._
'-.*+++++++\    /+ ++++++/  / *|  |/  /+ ++++++.-'
    > *+++++\  /*++++ +/` /`+++|     < *++ +++< 
_,-'* +++ ++|  |++ +*/` /` +* +|  |\  \+ ++++++'-._
`-._+ +*++?+|  |+++*|  '-----.+|  |+\  \+* ++ +_.-'
   _`\++++++|__|+ *+|________|+|__|++\__|++++/`_
  /*++_+* + +++++ ++ + ++++ +++++ ++ ++++ ++_+*+
  '--' `>*+++ +++++ +++++*++++  +++ ++++ ?<' '--'
       /++_++ ++ ++++++ ++?+ +++++*+++ ++++ 
       |_/ `\++ ++ +++*++++++++++ ++++*./`\_|
            /+*.-.*+ +_ ++*+ _+++ .-.* +
      jgs   | /   | +/ `\?+/` \*+|    \ |
             '    \.'    |/    './     '
      
      
      """)
print("<----------------------------------------------------------------------------->")

ip_address = input("Please Enter The IP Address you want to scan:  ")
print("The IP you enter is: ", ip_address)
type(ip_address)

response = input("""\nPlease enter the type of scan you want to run
             1) SYN ACK Scan
             2) UDP Scan
             3) Comprehensive Scan
             \n""")
print("You have selected option: ", response)

while True:
    if response == '1':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_address, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_address].state())
        print(scanner[ip_address].all_protocols())
        print("Open Ports: ", scanner[ip_address]['tcp'].keys())
        break
    elif response == '2':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_address, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_address].state())
        print(scanner[ip_address].all_protocols())
        print("Open Ports: ", scanner[ip_address]['udp'].keys())
        break
    elif response == '3':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_address].state())
        print(scanner[ip_address].all_protocols())
        print("Open Ports: ", scanner[ip_address]['tcp'].keys())
        break
    elif response >= '4':  # Handle invalid options
        print("Please enter a valid option")
        break
    else:
        print("Invalid input, please enter a number between 1 and 3.")
        



