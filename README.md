# TNEH DDOS Tool

![TNEH DDOS](https://img.shields.io/badge/TNEH-DDOS%20Tool-red)
![Educational](https://img.shields.io/badge/Educational-Purpose%20Only-yellow)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Termux](https://img.shields.io/badge/Termux-Supported-green)

A professional terminal-based DDoS testing tool designed for educational purposes and authorized penetration testing.

## ⚠️ DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY**

- 🚫 **Illegal Use Prohibited**: Never use this tool against systems you don't own or without explicit permission
- 📚 **Educational Purpose**: Designed for learning about network security and DDoS mitigation
- 🔒 **Authorized Testing**: Only use on your own systems or with written authorization
- ⚖️ **Legal Compliance**: Users are solely responsible for complying with local laws

## 🎯 Features

### Attack Methods
- **TCP Flood Attack**: Overwhelm target with TCP packets
- **HTTPS Flood Attack**: Send HTTP requests to web servers

### Technical Features
- 🖥️ **Terminal-based Interface**: Works on Termux (Android) and Linux
- 🎨 **Color-coded Output**: Real-time status with colored messages
- 🔢 **Multi-threading**: Configurable thread count for parallel attacks
- ⏱️ **Attack Duration Tracking**: Monitor attack timing and statistics
- ⚡ **Real-time Status**: Live attack progress updates

### Safety Features
- ✅ **Input Validation**: Prevents misconfiguration
- 🛑 **Safe Stop**: Ctrl+C to stop attacks immediately
- 📋 **Clear Warnings**: Prominent educational disclaimers

## 📥 Installation

### Prerequisites
- Python 3.6 or higher
- Termux (Android) or Linux terminal
- Required Python packages

### Installation Steps

1. **Navigate to Directory**
```bash
cd TNEH-DDOS-ATTACK
```

1. Make Install Script Executable

```bash
chmod +x install.sh
```

1. Run Installation

```bash
./install.sh
```

1. Start the Tool

```bash
python3 TNEH_DDOS.py
```

🚀 Usage Guide

Starting the Tool

```bash
python3 TNEH_DDOS.py
```

Main Menu Options

1. 🚀 START DDOS ATTACK - Launch attack configuration
2. 📊 ATTACK STATISTICS - View attack metrics
3. ❌ EXIT - Close the application

Attack Configuration

TCP Flood Attack

· Target IP: IP address to target (default: 127.0.0.1)
· Target Port: Port number (default: 80)
· Threads: Number of parallel threads (default: 10)
· Packets: Packets per thread (0 = unlimited)

HTTPS Flood Attack

· Target URL: Full URL with https:// (default: https://example.com)
· Threads: Number of parallel threads (default: 10)
· Requests: Requests per thread (0 = unlimited)

During Attack

· Real-time Status: Green = success, Red = failures
· Attack Control: Press Ctrl+C to stop immediately
· Duration Tracking: Automatic timing of attack duration

📁 File Structure

```
TNEH-DDOS-ATTACK/
│
├── TNEH_DDOS.py          # Main application
├── install.sh            # Installation script
├── README.md             # This documentation
└── requirements.txt      # Python dependencies
```

🛡️ Legal & Ethical Usage

✅ Permitted Uses

· Testing your own servers and infrastructure
· Educational environments with supervision
· Authorized penetration testing with written consent
· Learning about DDoS mitigation techniques

❌ Prohibited Uses

· Attacking systems you don't own
· Disrupting public services or websites
· Any illegal or unauthorized activities
· Malicious attacks on third parties

🔧 Technical Details

Requirements

· Python: 3.6+
· Libraries:
  · socket (built-in)
  · threading (built-in)
  · requests (install via pip)
  · random (built-in)
  · time (built-in)
  · os (built-in)

Supported Platforms

· ✅ Termux (Android)
· ✅ Linux
· ✅ macOS
· ✅ Windows (with modifications)

📊 Attack Methods Explained

TCP Flood

· Creates multiple TCP connections to target
· Sends random data packets (1024 bytes)
· Overwhelms target's connection pool
· Effective against web servers and services

HTTPS Flood

· Sends legitimate HTTPS requests
· Uses random User-Agent headers
· Mimics real browser traffic
· Targets web application layers

🎨 Interface Preview

```
╔══════════════════════╗
║   🚀 START DDOS ATTACK   ║
╚══════════════════════╝

[TCP] Packet 15 sent to 192.168.1.1:80 ✅
[TCP] Packet 16 sent to 192.168.1.1:80 ✅
[HTTPS] Request 23 sent to https://example.com | Status: 200 ✅
```

🔒 Security Recommendations

For Defenders

· Implement rate limiting
· Use Web Application Firewalls (WAF)
· Configure DDoS protection services
· Monitor network traffic patterns

For Testers

· Always get written authorization
· Test during maintenance windows
· Have rollback plans ready
· Document all testing activities

📝 Developer Information

Developer: Noman
Contact: WhatsApp: 01611229803
Purpose: Educational cybersecurity tool

🆘 Troubleshooting

Common Issues

1. ModuleNotFoundError: No module named 'requests'
   ```bash
   pip install requests
   ```
2. Permission Errors (Linux)
   ```bash
   chmod +x TNEH_DDOS.py
   ```
3. Connection Refused
   · Verify target IP/port
   · Check network connectivity
   · Ensure target service is running

Performance Tips

· Start with low thread counts
· Test locally first
· Monitor system resources
· Use packet limits for initial tests

📚 Learning Resources

Recommended Study

· Network Security Fundamentals
· DDoS Mitigation Strategies
· Ethical Hacking Certifications (CEH, OSCP)
· Python Network Programming

Practice Platforms

· HackTheBox
· TryHackMe
· OverTheWire
· VulnHub

🤝 Contributing

This is an educational project. Contributions should focus on:

· Improving educational content
· Enhancing safety features
· Adding defensive techniques
· Documentation improvements

📄 License

This tool is provided for educational purposes only. Users are responsible for complying with all applicable laws and regulations.

---

Remember: With great power comes great responsibility. Use this knowledge to protect and secure, not to harm. 🛡️

```
