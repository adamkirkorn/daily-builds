import subprocess
import random
from datetime import datetime

# Expanded database of YC AI founders to target
TARGETS = [
    {"name": "Robertson", "company": "Calltree", "trigger": "the YC W25 launch for AI call center ops"},
    {"name": "Will", "company": "Phonely", "trigger": "the YC S24 launch for AI conversational support"},
    {"name": "Pierre-Eliott", "company": "Gojiberry AI", "trigger": "building the GTM Brain for B2B sales teams"},
    {"name": "Rohit", "company": "PermitFlow", "trigger": "using AI to streamline construction operations"},
    {"name": "David", "company": "AthenaHQ", "trigger": "optimizing AI SEO and search visibility"},
    {"name": "Kunal", "company": "Reality Defender", "trigger": "building AI workspaces for financial compliance"},
    {"name": "Adriaan", "company": "Open", "trigger": "scaling enterprise AI customer support"},
    {"name": "Saudara", "company": "Saudara AI", "trigger": "building remote human-in-the-loop AI operations"}
]

def run_daily_build():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Pick 5 random targets each day (or fewer if list is small)
    daily_targets = random.sample(TARGETS, min(5, len(TARGETS)))
    
    print(f"[{timestamp}] Generating daily icebreakers for {len(daily_targets)} YC founders...\n")
    
    log_entry = f"\n## {timestamp} - Daily Outreach Batch ({len(daily_targets)} targets)\n"
    
    for target in daily_targets:
        print(f"🎯 Generating for {target['name']} at {target['company']}...")
        
        # Run the icebreaker generator (template mode for now)
        cmd = [
            "python3", "icebreaker_gen.py",
            "--name", target["name"],
            "--company", target["company"],
            "--trigger", target["trigger"]
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Extract just the generated messages for the log
        lines = result.stdout.split('\n')
        messages = [line for line in lines if line.startswith("[")]
        
        log_entry += f"\n### {target['company']} ({target['name']})\n"
        log_entry += f"**Trigger:** {target['trigger']}\n"
        log_entry += "**Top Pick:**\n"
        if messages:
            log_entry += f"> {messages[0].split('] ')[1]}\n"
        else:
            log_entry += f"> (Generation failed, check script)\n"
            
    with open("daily_log.md", "a") as f:
        f.write(log_entry)
        
    print("\n✅ Daily batch generated and logged to daily_log.md")
    print("\n--- TODAY'S PREVIEW ---")
    print(log_entry)

if __name__ == "__main__":
    run_daily_build()