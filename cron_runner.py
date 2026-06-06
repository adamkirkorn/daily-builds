import subprocess
import random
from datetime import datetime

# Expanded database of YC AI founders with FULL NAMES for accurate targeting
TARGETS = [
    {"first_name": "Robertson", "last_name": "Taylor", "company": "Calltree", "trigger": "the YC W25 launch for AI call center ops"},
    {"first_name": "Will", "last_name": "Bodewes", "company": "Phonely", "trigger": "the YC S24 launch for AI conversational support"},
    {"first_name": "Pierre-Eliott", "last_name": "Lallemant", "company": "Gojiberry AI", "trigger": "building the GTM Brain for B2B sales teams"},
    {"first_name": "Francis", "last_name": "Thumpasery", "company": "PermitFlow", "trigger": "using AI to streamline construction operations"},
    {"first_name": "Andrew", "last_name": "Yan", "company": "AthenaHQ", "trigger": "optimizing AI SEO and search visibility"},
    {"first_name": "Ben", "last_name": "Colman", "company": "Reality Defender", "trigger": "building AI workspaces for financial compliance"},
    {"first_name": "Mohammad", "last_name": "Gharbat", "company": "Open", "trigger": "scaling enterprise AI customer support"},
    {"first_name": "Edward", "last_name": "Haryono", "company": "Saudara AI", "trigger": "building remote human-in-the-loop AI operations"}
]

def run_daily_build():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Pick 5 random targets each day
    daily_targets = random.sample(TARGETS, min(5, len(TARGETS)))
    
    print(f"[{timestamp}] Generating daily icebreakers for {len(daily_targets)} YC founders...\n")
    
    log_entry = f"\n## {timestamp} - Daily Outreach Batch ({len(daily_targets)} targets)\n"
    
    for target in daily_targets:
        full_name = f"{target['first_name']} {target['last_name']}"
        print(f"🎯 Generating for {full_name} at {target['company']}...")
        
        # Run the icebreaker generator using FIRST NAME for natural greeting
        cmd = [
            "python3", "icebreaker_gen.py",
            "--name", target["first_name"],
            "--company", target["company"],
            "--trigger", target["trigger"]
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Extract just the generated messages for the log
        lines = result.stdout.split('\n')
        messages = [line for line in lines if line.startswith("[")]
        
        log_entry += f"\n### {target['company']} ({full_name})\n"
        log_entry += f"**Trigger:** {target['trigger']}\n"
        log_entry += "**Top Pick:**\n"
        if messages:
            # Remove the "[1] " prefix and character count for a clean copy-paste
            clean_msg = messages[0].split('] ')[1].rsplit(' (', 1)[0]
            log_entry += f"> {clean_msg}\n"
        else:
            log_entry += f"> (Generation failed, check script)\n"
            
    with open("daily_log.md", "a") as f:
        f.write(log_entry)
        
    print("\n✅ Daily batch generated and logged to daily_log.md")

if __name__ == "__main__":
    run_daily_build()