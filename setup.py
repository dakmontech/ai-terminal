
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

import os
import sys
import shutil
import stat
from pathlib import Path

def detect_shell_rc():
    shell = os.environ.get("SHELL", "")
    home = str(Path.home())
    if "zsh" in shell:
        return os.path.join(home, ".zshrc")
    elif "bash" in shell:
        return os.path.join(home, ".bashrc")
    else:
        print("⚠️ Could not detect zsh or bash. You may need to add the alias manually.")
        return None

def main():
    home = str(Path.home())
    scripts_dir = os.path.join(home, ".scripts")
    venv_dir = os.path.join(home, ".venvs", "ai-terminal")
    target_script = os.path.join(scripts_dir, "ai_terminal.py")
    shell_rc = detect_shell_rc()

    print("📁 Creating necessary directories...")
    os.makedirs(scripts_dir, exist_ok=True)
    os.makedirs(os.path.dirname(venv_dir), exist_ok=True)

    print("📄 Copying script to ~/.scripts/")
    shutil.copyfile("ai_terminal.py", target_script)
    os.chmod(target_script, os.stat(target_script).st_mode | stat.S_IXUSR)

    print("🐍 Creating virtual environment in ~/.venvs/ai-terminal")
    os.system(f"python3 -m venv {venv_dir}")
    print("📦 Installing dependencies (openai)...")
    os.system(f"{venv_dir}/bin/pip install openai")

    if shell_rc:
        alias_line = f'alias ai-terminal="source {venv_dir}/bin/activate && python3 {target_script}"\n'
        with open(shell_rc, "a") as f:
            f.write(f"\n# Alias for ai-terminal\n{alias_line}")
        print(f"✅ Alias added to {shell_rc}. Reload it with: source {shell_rc}")

    print("\n✅ Installation completed.")
    print("💡 To activate the new alias in your current terminal session, run:")
    if shell_rc:
        print(f"   source {shell_rc}")
    print("\nThen run: ai-terminal")

if __name__ == "__main__":
    main()
