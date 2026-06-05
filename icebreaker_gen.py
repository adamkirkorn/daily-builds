import argparse

def generate_icebreakers(name, company, trigger):
    # 3 distinct psychological angles optimized for <300 char LinkedIn notes
    return [
        f"Hey {name}, saw {company} is {trigger}. I build AI automations for founders and have a quick idea to save your team 5 hrs/week on that. Open to connecting?",
        f"Hi {name}, huge fan of {company}, especially {trigger}. I’m a UofA student building free AI tools for early-stage teams. Mind if I send over a quick 2-hr build idea?",
        f"Hey {name}, {trigger} at {company} caught my eye. I specialize in prompt engineering and just built a custom workflow for this. Would love to gift it to your team. Open to connecting?"
    ]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LinkedIn Icebreaker Generator v1.0")
    parser.add_argument("--name", required=True, help="Target's first name")
    parser.add_argument("--company", required=True, help="Target's company")
    parser.add_argument("--trigger", required=True, help="Recent event, post, or YC launch")
    
    args = parser.parse_args()
    
    print(f"\n🎯 TARGET: {args.name} at {args.company}")
    print(f"🔥 TRIGGER: {args.trigger}\n")
    print("👇 GENERATED ICEBREAKERS (Optimized for <300 chars):\n")
    
    icebreakers = generate_icebreakers(args.name, args.company, args.trigger)
    for i, msg in enumerate(icebreakers, 1):
        print(f"[{i}] {msg} ({len(msg)} chars)")
        print("-" * 60)