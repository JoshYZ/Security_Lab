"""
Nmap Automation Script
Author: JoshYZ
Requirement: Nmap must be installed on the host system.
Purpose: Automates port scanning and triggers conditional 'trawls' based on results.
"""
import subprocess

def scan_target(target_ip):
    print(f"[*] Scanning {target_ip} for open web services...")
    
    # Run Nmap to check Port 80
    command = ["nmap", "-p", "80", "-Pn", target_ip]
    result = subprocess.run(command, capture_output=True, text=True)
    
    if "80/tcp open" in result.stdout:
        print("[!] Port 80 found. Checking for robots.txt...")
        trawl = subprocess.run(["curl", "-s", f"http://{target_ip}/robots.txt"], 
                               capture_output=True, text=True)
        print(f"Results:\n{trawl.stdout}")
    else:
        print("[-] Port 80 is closed.")

if __name__ == "__main__":
    scan_target("scanme.nmap.org")