import argparse
import os
import requests

def generate_with_ai(name, company, trigger, api_key):
    """Generates an icebreaker using a free LLM API."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/adamkirkorn/daily-builds",
        "X-Title": "Daily AI Builds Icebreaker"
    }
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are an expert in B2B outreach and prompt engineering. Write a concise, highly personalized LinkedIn connection note (under 300 characters) to a startup founder. Be direct, no fluff, no 'I hope this finds you well'. Focus on immediate value."},
            {"role": "user", "content": f"Write a LinkedIn connection note for {name} at {company}. Trigger/Context: {trigger}. Keep it under 300 characters."}
        ]
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[AI Fallback - No API Key or Error]: Hey {name}, saw {company} is {trigger}. I build AI automations for founders and have a quick idea to save your team 5 hrs/week on that. Open to connecting?"

def generate_template(name, company, trigger):
    """Fallback template generator."""
    return [
        f"Hey {name}, saw {company} is {trigger}. I build AI automations for founders and have a quick idea to save your team 5 hrs/week on that. Open to connecting?",
        f"Hi {name}, huge fan of {company}, especially {trigger}. I’m a UofA student building free AI tools for early-stage teams. Mind if I send over a quick 2-hr build idea?",
        f"Hey {name}, {trigger} at {company} caught my eye. I specialize in prompt engineering and just built a custom workflow for this. Would love to gift it to your team. Open to connecting?"
    ]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LinkedIn Icebreaker Generator v2.0 (AI-Powered)")
    parser.add_argument("--name", required=True, help="Target's first name")
    parser.add_argument("--company", required=True, help="Target's company")
    parser.add_argument("--trigger", required=True, help="Recent event, post, or YC launch")
    parser.add_argument("--api-key", default=os.getenv("OPENROUTER_API_KEY", ""), help="OpenRouter API Key (optional)")
    parser.add_argument("--ai", action="store_true", help="Force AI generation (falls back to template if no key)")
    
    args = parser.parse_args()
    
    print(f"\n🎯 TARGET: {args.name} at {args.company}")
    print(f"🔥 TRIGGER: {args.trigger}\n")
    
    if args.ai or args.api_key:
        print("🤖 Generating with AI...\n")
        msg = generate_with_ai(args.name, args.company, args.trigger, args.api_key)
        print(f"✨ AI MESSAGE ({len(msg)} chars):\n{msg}")
        print("-" * 60)
    else:
        print("👇 GENERATED TEMPLATES (Optimized for <300 chars):\n")
        icebreakers = generate_template(args.name, args.company, args.trigger)
        for i, msg in enumerate(icebreakers, 1):
            print(f"[{i}] {msg} ({len(msg)} chars)")
            print("-" * 60)