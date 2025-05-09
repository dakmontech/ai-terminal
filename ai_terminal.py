
"""
ai_terminal.py - AI-assisted terminal for command-line exploration

Author: Dakmon
License: MIT
Repository: https://github.com/dakmontech/ai-terminal

MIT License

Copyright (c) 2025 Dakmon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import subprocess
from openai import OpenAI
import os

# CONFIGURE YOUR OPENAI API KEY
api_key = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY_HERE"
client = OpenAI(api_key=api_key)

# Ask for a free-form purpose
print("🧠 AI Terminal")
print("Describe the purpose of this session (e.g. 'learning Linux basics', 'exploring system performance', 'configuring a production Linux server'):")
purpose = input("[🔍 Purpose]: ").strip()

# Initialize conversation history
history = [
    {"role": "system", "content": f"You are an AI assistant in a Linux terminal session. The purpose is: {purpose}"}
]

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

def ai_suggestion(command, output):
    user_prompt = f"""Executed command:
```
{command}
```

Command output:
```
{output[:1000]}
```

Based on the command and output, suggest the next useful command, improvement, or idea. Avoid repeating previous suggestions unless necessary. If there is nothing new to suggest, say: "No suggestions for now."
"""
    history.append({"role": "user", "content": user_prompt})
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=history,
            temperature=0.3,
            max_tokens=300
        )
        answer = response.choices[0].message.content.strip()
        history.append({"role": "assistant", "content": answer})
        return answer
    except Exception as e:
        return f"⚠️ Error with AI: {str(e)}"

print("AI Terminal ready. Type your commands below:")

while True:
    try:
        cmd = input("> ")
        if cmd.strip() in ("exit", "quit"):
            break
        if len(cmd.strip()) < 2:
            continue

        output = run_command(cmd)
        print(output)

        suggestion = ai_suggestion(cmd, output)
        print("🤖", suggestion)

        print("\n⏳ Waiting for your next command...")

    except KeyboardInterrupt:
        print("\n⛔ Interrupted.")
