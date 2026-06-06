import subprocess
import random
from datetime import datetime

# Mini database of YC founders to target daily
TARGETS = [
    {"name": "Robertson", "company": "Calltree", "trigger": "the YC W25 launch for AI call center ops"},
    {"name": "Will", "company": "Phonely", "trigger": "the YC S24 launch for AI conversational support"},
    {"name": "Pierre-Eliott", "company": "Gojiberry AI", "trigger": "building the GTM Brain for B2B sales teams"},
    {"name": "Adam", "company": "Peakflo", "trigger": "automating finance and back-office ops with AI"}
]

def run_daily_build():
    target = random.choice(TARGETS)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{timestamp}] Generating daily icebreaker for {target['name']} at {target['company']}...")
    
    # Run the icebreaker generator (template mode for now, add --api-key later)
    cmd = [
        "python3", "icebreaker_gen.py",
        "--name", target["name"],
        "--company", target["company"],
        "--trigger", target["trigger"]
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Log the output
    log_entry = f"\n## {timestamp} - {target['company']}\n"
    log_entry += f"**Target:** {target['name']}\n"
    log_entry += f"**Trigger:** {target['trigger']}\n"
    log_entry += "```\n"
    log_entry += result.stdout
    log_entry += "```\n"
    
    with open("daily_log.md", "a") as f:
        f.write(log_entry)
        
    print("✅ Daily icebreaker generated and logged to daily_log.md")
    print("\n--- PREVIEW ---")
    print(result.stdout)

if __name__ == "__main__":
    run_daily_build()