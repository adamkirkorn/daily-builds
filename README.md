# 🚀 Daily AI Outreach Automation

> **An automated, AI-powered outreach engine that generates highly personalized, sub-300-character connection messages for AI startup founders and leaders.**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Automated-brightgreen.svg)

---

## 🧠 What is this?
This repository houses a personal automation pipeline designed to scale high-quality, targeted outreach. Instead of manually drafting LinkedIn connection requests, this tool programmatically generates context-aware, highly personalized messages for 20+ verified AI startup leaders *every single day*, with **zero repeats**.

## ✨ Key Features
- **🎯 Zero-Repeats Tracking**: Maintains a `contacted.txt` ledger to ensure no founder is messaged twice.
- **⚡ Dynamic Prompt Engineering**: Uses optimized prompt templates (with optional OpenRouter LLM integration) to craft sub-300-character messages optimized for LinkedIn's connection note limits.
- **📱 Telegram Integration**: Automatically formats and delivers the daily batch of 20 ready-to-copy messages directly to a personal Telegram bot every morning at 9:00 AM.
- **🔄 Fully Automated**: Powered by a local Hermes cron job, requiring zero manual intervention to run daily.

## 🛠️ Tech Stack
- **Language**: Python 3.9+
- **Scheduling**: Hermes Cron / macOS `launchd`
- **Version Control**: Git & GitHub
- **Delivery**: Telegram Bot API

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/adamkirkorn/daily-builds.git
   cd daily-builds
   ```

2. **Run the generator manually (Dry Run):**
   ```bash
   python3 cron_runner.py
   ```
   *This will generate 20 fresh messages, log them to `daily_log.md`, and update the `contacted.txt` tracker.*

3. **Customize Targets:**
   Edit the `TARGETS` list in `cron_runner.py` to add your own companies, names, and trigger events.

## 📝 Project Structure
```text
daily-builds/
├── cron_runner.py          # Main orchestration script (selects targets, runs generator, logs)
├── icebreaker_gen.py       # Core prompt-engineering logic and message generation
├── contacted.txt           # Auto-generated ledger of messaged individuals (prevents repeats)
├── daily_log.md            # Historical log of all generated daily batches
└── README.md               # You are here!
```

## 🎯 Next Steps
- [ ] Integrate OpenRouter API for dynamic, on-the-fly LLM message generation.
- [ ] Add a `--scrape` flag to dynamically pull recent news/triggers from target company websites.

---
*Built by Adam Kirkorn. Automating the boring stuff, one commit at a time.*