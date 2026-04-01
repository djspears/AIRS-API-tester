# AIRS-API-tester

A command-line tool for testing prompts against Palo Alto Networks **AI Runtime Security (AIRS)** using the `aisecurity` Python SDK.

## Prerequisites

- Python 3
- `aisecurity` Python package

Install the package:

```bash
pip install aisecurity
```

## Configuration

Before running the script, open `AIRS-API-tester.py` and update the following values in the **Initialize** section near the top of the file:

```python
aisecurity.init(api_key="")  # Add your API key here
profile_name = ""            # Add your profile name here
```

- **api_key** – Your AIRS API key
- **profile_name** – The name of the AI security profile to scan against

## Usage

Run the script using Python 3:

```bash
python3 AIRS-API-tester.py
```

You will be prompted to enter an AI prompt to test. The script will submit it to AIRS and display a formatted security report showing:

- Overall verdict (ALLOW / BLOCK)
- Threat category
- Profile used
- Prompt analysis (malicious URLs, injection, data leakage, toxicity)
- Response analysis (sensitive data, ungrounded content)

## Example Output

```
--------------------------------------------------
⌨️  Enter the AI Prompt to test: How do I hack a server?
--------------------------------------------------

==================================================
🛡️  PRISMA AI RUNTIME SECURITY REPORT
==================================================
Verdict:     ❌ BLOCK
Category:    Prompt Injection
Profile:     my-profile
--------------------------------------------------
PROMPT ANALYSIS:
  • Malicious URL:  ✅ Clear
  • Injection:      🚩 DETECTED
  • Data Leak:      ✅ Clear
  • Toxicity:       ✅ Clear

RESPONSE ANALYSIS:
  • Sensitive Data: ✅ Clear
  • Ungrounded:     ✅ Clear
==================================================
```
