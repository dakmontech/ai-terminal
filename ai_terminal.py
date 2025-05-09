
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
print("Describe the purpose of this session (e.g. 'learning Linux basics', 'exploring system performance'):")
purpose = input("[🔍 Purpose]: ").strip()

# Initial working directory and memory
current_dir = os.path.expanduser("~")
history = [{"role": "system", "content": f"You are an AI assistant in a Linux terminal session. The purpose is: {purpose}"}]

# Commands that won't work as expected
unsupported_commands = [
    "export", "unset", "alias", "unalias", "source", ".", "set", "shopt", "exec",
    "fg", "bg", "jobs", "read", "trap", "select", "complete", "bind",
    "function", "return", "break", "time"
]

def run_command(command):
    global current_dir

    cmd = command.strip()

    if not cmd:
        return ""

    if cmd.startswith("cd"):
        parts = cmd.split(maxsplit=1)
        new_path = os.path.expanduser(parts[1] if len(parts) > 1 else "~")
        new_path = os.path.abspath(os.path.join(current_dir, new_path)) if not os.path.isabs(new_path) else new_path
        if os.path.isdir(new_path):
            current_dir = new_path
            return ""
        else:
            return f"cd: no such directory: {parts[1]}"

    if cmd.split()[0] in unsupported_commands:
        return f"⚠️ The command `{cmd.split()[0]}` may not work properly in this assistant. Try running it in your real shell."

    try:
        result = subprocess.run(cmd, shell=True, cwd=current_dir, capture_output=True, text=True)
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
        display_dir = os.path.relpath(current_dir, os.path.expanduser("~"))
        prompt = f"~/{display_dir if display_dir != '.' else ''}> ".replace("//", "/")
        cmd = input(prompt)

        if cmd.strip() in ("exit", "quit"):
            break
        if len(cmd.strip()) < 1:
            continue

        output = run_command(cmd)
        if output:
            print(output)

        suggestion = ai_suggestion(cmd, output)
        print("🤖", suggestion)
        print("⏳ Waiting for your next command...")

    except KeyboardInterrupt:
        print("⛔ Interrupted.")
