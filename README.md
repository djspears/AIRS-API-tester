# AIRS-API-tester

A command-line tool for testing prompts against Palo Alto Networks **AI Runtime Security (AIRS)** using the `pan-aisecurity` Python SDK.

## Prerequisites

- Python 3.12+
- `pan-aisecurity` Python package

## Setup (macOS)

Create and activate a virtual environment, then install the package:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip3 install pan-aisecurity
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

Run the script using Python 3.12:

```bash
python3.12 AIRS-API-tester.py
```

You will be prompted to enter an AI prompt to test. After each scan, you will be asked if you want to test another prompt. Enter `y` to continue or `n` to exit.

## Code Structure

The script is organized into three standalone functions:

| Function | Description |
|---|---|
| `send_scan(profile_name, user_prompt)` | Sends the prompt to the AIRS API and returns the raw result dict |
| `print_scan_report(data)` | Pretty-prints the scan result to the terminal |
| `run_security_scan(profile_name)` | Main loop — prompts for input, calls the above functions, and asks to continue |

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

Test another prompt? (y/n):
```
