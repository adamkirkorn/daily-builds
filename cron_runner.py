import subprocess
import random
from datetime import datetime

# Expanded database of 10 top AI startup leaders (5 YC Founders + 5 Head of Growth/Ops)
TARGETS = [
    # YC Founders
    {"first_name": "Robertson", "last_name": "Taylor", "company": "Calltree", "trigger": "the YC W25 launch for AI call center ops"},
    {"first_name": "Will", "last_name": "Bodewes", "company": "Phonely", "trigger": "the YC S24 launch for AI conversational support"},
    {"first_name": "Pierre-Eliott", "last_name": "Lallemant", "company": "Gojiberry AI", "trigger": "building the GTM Brain for B2B sales teams"},
    {"first_name": "Francis", "last_name": "Thumpasery", "company": "PermitFlow", "trigger": "using AI to streamline construction operations"},
    {"first_name": "Andrew", "last_name": "Yan", "company": "AthenaHQ", "trigger": "optimizing AI SEO and search visibility"},
    
    # Heads of Growth / Operations at Scaling AI Startups
    {"first_name": "Raman", "last_name": "Malik", "company": "Perplexity AI", "trigger": "scaling unprecedented user growth in AI search"},
    {"first_name": "Michelle", "last_name": "Kwon", "company": "Runway", "trigger": "leading operations and partnerships for generative video"},
    {"first_name": "Garrett", "last_name": "Serviss", "company": "Copy.ai", "trigger": "enabling the next billion entrepreneurs with AI workflows"},
    {"first_name": "Amol", "last_name": "Avasare", "company": "Anthropic", "trigger": "automating Claude's own unprecedented growth trajectory"},
    {"first_name": "Luke", "last_name": "Harries", "company": "ElevenLabs", "trigger": "scaling marketing and developer experience for AI audio"}
]

def run_daily_build():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Pick 10 random targets each day (or fewer if list is small)
    daily_targets = random.sample(TARGETS, min(10, len(TARGETS)))
    
    print(f"[{timestamp}] Generating daily icebreakers for {len(daily_targets)} AI startup leaders...\n")
    
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