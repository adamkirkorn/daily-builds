import subprocess
import random
import os
from datetime import datetime

# Expanded database of 40+ AI startup founders and leaders
TARGETS = [
    # YC Founders (Batch W23 - W25)
    {"first_name": "Robertson", "last_name": "Taylor", "company": "Calltree", "trigger": "the YC W25 launch for AI call center ops"},
    {"first_name": "Will", "last_name": "Bodewes", "company": "Phonely", "trigger": "the YC S24 launch for AI conversational support"},
    {"first_name": "Pierre-Eliott", "last_name": "Lallemant", "company": "Gojiberry AI", "trigger": "building the GTM Brain for B2B sales teams"},
    {"first_name": "Francis", "last_name": "Thumpasery", "company": "PermitFlow", "trigger": "using AI to streamline construction operations"},
    {"first_name": "Andrew", "last_name": "Yan", "company": "AthenaHQ", "trigger": "optimizing AI SEO and search visibility"},
    {"first_name": "Ben", "last_name": "Colman", "company": "Reality Defender", "trigger": "building AI workspaces for financial compliance"},
    {"first_name": "Mohammad", "last_name": "Gharbat", "company": "Open", "trigger": "scaling enterprise AI customer support"},
    {"first_name": "Edward", "last_name": "Haryono", "company": "Saudara AI", "trigger": "building remote human-in-the-loop AI operations"},
    {"first_name": "Sriman", "last_name": "Gaddam", "company": "Sennu AI", "trigger": "the YC W25 launch for AI-powered solutions"},
    {"first_name": "Tyler", "last_name": "Postle", "company": "Voker", "trigger": "the YC S24 launch for AI operations"},
    {"first_name": "Yassine", "last_name": "Tairi", "company": "ZeroEntropy", "trigger": "the YC W25 launch for Artificial Specialized Intelligence"},
    {"first_name": "Rishi", "last_name": "Choudhary", "company": "Kastle", "trigger": "the YC S24 launch for AI products"},
    {"first_name": "Darren", "last_name": "Lachtman", "company": "GoldenSet AI", "trigger": "the YC W24 launch for AI workflows"},
    {"first_name": "August", "last_name": "Chen", "company": "Hazel", "trigger": "the YC W24 launch for AI in government"},
    {"first_name": "David", "last_name": "Strömbäck", "company": "Crimson", "trigger": "the YC X25 launch for AI for litigators"},
    {"first_name": "Yurii", "last_name": "Rebryk", "company": "Fluently", "trigger": "the YC W24 launch for AI language learning"},
    {"first_name": "Elton", "last_name": "Chan", "company": "Second Talent", "trigger": "connecting leaders with AI-native talent"},
    {"first_name": "Catheryn", "last_name": "Li", "company": "Simple", "trigger": "building products to inspire future AI founders"},
    
    # Heads of Growth / Operations at Scaling AI Startups
    {"first_name": "Raman", "last_name": "Malik", "company": "Perplexity AI", "trigger": "scaling unprecedented user growth in AI search"},
    {"first_name": "Michelle", "last_name": "Kwon", "company": "Runway", "trigger": "leading operations and partnerships for generative video"},
    {"first_name": "Garrett", "last_name": "Serviss", "company": "Copy.ai", "trigger": "enabling the next billion entrepreneurs with AI workflows"},
    {"first_name": "Amol", "last_name": "Avasare", "company": "Anthropic", "trigger": "automating Claude's own unprecedented growth trajectory"},
    {"first_name": "Luke", "last_name": "Harries", "company": "ElevenLabs", "trigger": "scaling marketing and developer experience for AI audio"},
    {"first_name": "Sujude", "last_name": "Abicha", "company": "Replit", "trigger": "driving head of growth for the leading AI coding platform"},
    {"first_name": "Patrick", "last_name": "Coleman", "company": "Replit", "trigger": "former VP Growth scaling the AI coding platform"},
    {"first_name": "Joe", "last_name": "Cohen", "company": "Harvey AI", "trigger": "scaling enterprise AI agents for legal workflows"},
    {"first_name": "Millie", "last_name": "Lehmann", "company": "Harvey AI", "trigger": "leading legal engineering for enterprise AI agents"},
]

def load_contacted():
    """Load list of already contacted people to avoid repeats."""
    contacted_file = "contacted.txt"
    if os.path.exists(contacted_file):
        with open(contacted_file, "r") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_contacted(new_contacts):
    """Append newly contacted people to the list."""
    contacted_file = "contacted.txt"
    with open(contacted_file, "a") as f:
        for contact in new_contacts:
            f.write(f"{contact}\n")

def run_daily_build():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Load who we've already messaged
    contacted = load_contacted()
    
    # Filter out anyone we've already contacted
    available_targets = [t for t in TARGETS if f"{t['first_name']} {t['last_name']}" not in contacted]
    
    # If we run out of new people, reset the contacted list (fallback)
    if len(available_targets) < 20:
        print("⚠️ Warning: Running low on new targets. Resetting contacted list for continuous outreach.")
        contacted = set()
        available_targets = TARGETS
        # Clear the file
        with open("contacted.txt", "w") as f:
            f.write("")

    # Sample 20 fresh targets
    daily_targets = random.sample(available_targets, min(20, len(available_targets)))
    new_contacted_names = [f"{t['first_name']} {t['last_name']}" for t in daily_targets]
    
    print(f"[{timestamp}] Generating daily icebreakers for {len(daily_targets)} NEW AI startup leaders...\n")
    
    log_entry = f"\n## {timestamp} - Daily Outreach Batch ({len(daily_targets)} targets)\n"
    
    for target in daily_targets:
        full_name = f"{target['first_name']} {target['last_name']}"
        print(f"🎯 Generating for {full_name} at {target['company']}...")
        
        cmd = [
            "python3", "icebreaker_gen.py",
            "--name", target["first_name"],
            "--company", target["company"],
            "--trigger", target["trigger"]
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.split('\n')
        messages = [line for line in lines if line.startswith("[")]
        
        log_entry += f"\n### {target['company']} ({full_name})\n"
        log_entry += f"**Trigger:** {target['trigger']}\n"
        log_entry += "**Top Pick:**\n"
        if messages:
            clean_msg = messages[0].split('] ')[1].rsplit(' (', 1)[0]
            log_entry += f"> {clean_msg}\n"
        else:
            log_entry += f"> (Generation failed, check script)\n"
            
    with open("daily_log.md", "a") as f:
        f.write(log_entry)
        
    # Save the new contacts so they aren't repeated tomorrow
    save_contacted(new_contacted_names)
    
    print(f"\n✅ Daily batch generated, logged, and {len(new_contacted_names)} contacts saved to prevent repeats.")

if __name__ == "__main__":
    run_daily_build()