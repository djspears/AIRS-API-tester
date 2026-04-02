import os
import json
import aisecurity
from aisecurity.generated_openapi_client.models.ai_profile import AiProfile
from aisecurity.scan.inline.scanner import Scanner
from aisecurity.scan.models.content import Content

# 1. Initialize
aisecurity.init(api_key="")  # Add your API key here
profile_name = ""            # Add your profile name here


def send_scan(profile_name, user_prompt):
    """Send a prompt to the AIRS scanner and return the parsed result data."""
    ai_profile = AiProfile(profile_name=profile_name)
    scanner = Scanner()

    scan_response = scanner.sync_scan(
       ai_profile=ai_profile,
       content=Content(
           prompt=user_prompt,
           response="Standard Model Response for Testing",
       ),
    )
    return scan_response.to_dict()


def get_flag(detected):
    return "🚩 DETECTED" if detected else "✅ Clear"


def print_scan_report(data):
    """Pretty-print a scan result."""
    print("\n" + "="*50)
    print("🛡️  PRISMA AI RUNTIME SECURITY REPORT")
    print("="*50)

    status = data.get('action', 'N/A').upper()
    status_emoji = "❌" if status == "BLOCK" else "✅"

    print(f"Verdict:     {status_emoji} {status}")
    print(f"Category:    {data.get('category', 'N/A')}")
    print(f"Profile:     {data.get('profile_name', 'N/A')}")
    print("-"*50)

    print("PROMPT ANALYSIS:")
    p_det = data.get('prompt_detected', {})
    print(f"  • Malicious URL:  {get_flag(p_det.get('url_cats'))}")
    print(f"  • Injection:      {get_flag(p_det.get('injection'))}")
    print(f"  • Data Leak:      {get_flag(p_det.get('dlp'))}")
    print(f"  • Toxicity:       {get_flag(p_det.get('toxic_content'))}")

    print("\nRESPONSE ANALYSIS:")
    r_det = data.get('response_detected', {})
    print(f"  • Sensitive Data: {get_flag(r_det.get('dlp'))}")
    print(f"  • Ungrounded:     {get_flag(r_det.get('ungrounded'))}")
    print("="*50 + "\n")


def run_security_scan(profile_name):
    while True:
        print("\n" + "-"*50)
        user_prompt = input("⌨️  Enter the AI Prompt to test: ")
        print("-"*50)

        data = send_scan(profile_name, user_prompt)
        print_scan_report(data)

        again = input("Test another prompt? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting. Goodbye!")
            break


if __name__ == "__main__":
    run_security_scan(profile_name)
