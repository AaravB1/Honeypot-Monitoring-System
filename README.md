# Honeypot + Monitoring System

A cybersecurity demonstration project for CNIT176 using OpenCanary honeypot with real-time Discord alerting.

## 🎥 Demo Video

[Watch the full demonstration on YouTube](https://www.youtube.com/watch?v=O-4L6w7C-c0)

## 📊 Project Slideshow

[View the project slideshow](https://docs.google.com/presentation/d/1GrJ1yD1qjbkfVJMM0FFYEKBX_z9L5lxfUaEnJlff57Y/edit?usp=sharing)


##📋 Overview

This project demonstrates:
- OpenCanary honeypot deployment on Raspberry Pi
- FTP brute-force and HTTP flood attack simulation
- Real-time Discord webhook alerts for detected attacks
- Complete attack detection and notification pipeline

## 📁 Project Files

- `ftpbruteforce.py` - Simulates FTP brute force attacks
- `httpflood.py` - Simulates HTTP flood attacks
- `opencanary.conf` - Honeypot configuration 

## 🎯 How It Works

1. **Raspberry Pi** runs OpenCanary honeypot with FTP and HTTP services
2. **Attack scripts** (from laptop) generate malicious traffic via ethernet connection
3. **OpenCanary** detects the attacks and logs them
4. **Discord webhook** sends real-time alerts to Discord server

See the full setup and demonstration in the video!

## ⚠️ Disclaimer

**FOR EDUCATIONAL PURPOSES ONLY**

These tools are for:
- Educational demonstrations
- Authorized security testing only
- Personal lab environments

Do not use on systems you don't own or without explicit permission. Unauthorized access is illegal.

## 📝 License

MIT License - see LICENSE file for details.

---
