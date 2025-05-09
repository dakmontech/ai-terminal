# 🧠 ai-terminal – AI-Integrated Terminal for Linux

This script turns your terminal into an AI-assisted tool. It reads your commands, analyzes the output, and suggests useful improvements, follow-ups, or techniques using the OpenAI API.

📗 [Leer en español](README_es.md)

---

## 🧰 Requirements

- Python 3.8+
- A valid OpenAI API key
- Any modern Linux distribution
- Terminal access

---

## 🔑 Set your OpenAI API key

Edit the `ai_terminal.py` file and replace the line:

```python
openai.api_key = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY_HERE"
```

Or set it as an environment variable:

```bash
export OPENAI_API_KEY="sk-..."
```

---

## ⚙️ Quick Installation

1. Unzip the package:
```bash
unzip ai_terminal_package_setup_en.zip
cd ai_terminal_package_setup_en
```

2. Run the installer:
```bash
python3 setup.py
```

✅ This will create a virtual environment, install dependencies, and configure the alias.

⚠️ Then run:
```bash
source ~/.zshrc  # or ~/.bashrc
```

---


---

## 🆕 Features

- ✅ Simulated directory navigation using `cd`, including `cd ..`, `cd ~/`, etc.
- ✅ Memory of previous commands for smarter suggestions.
- ✅ AI-powered improvements based on real output and session purpose.
- ✅ Command prompt dynamically reflects current working path (e.g. `~/Downloads>`).
- ✅ Warnings for unsupported shell commands like `export`, `alias`, or `source`.

---

## ▶️ Usage

Run the AI terminal with:

```bash
ai-terminal
```

When it starts, you'll be asked:

```
Describe the purpose of this session (e.g. 'learning bash scripting'):
```

Then:

1. Type commands like in a regular shell.
2. The output is displayed.
3. The AI suggests how to improve or continue based on memory of the whole session.
4. You decide what to run next.

---

## 🧠 Context Memory

This tool **remembers previous commands and suggestions**, allowing it to give smarter, more consistent advice over time — ideal for guided learning or complex investigations.

---

## 💡 Example

```bash
> ls -l
🤖 SUGGESTION: Try using `ls -lh` for human-readable sizes.
```

---


## ⚠️ Limitations

Some commands that rely on modifying the parent shell environment do not work as expected, such as:

- `export`, `alias`, `source`, `unset`, `set`, `exec`, etc.
- These affect only the subprocess used by Python, not your real shell session.
- Commands like `cd` are simulated internally and do not affect your real terminal state.

> ℹ️ If you need to change shell variables or execute persistent environment changes, do so in your main terminal.


## 🛡️ Security

- Suggestions are printed only.
- Nothing is executed without your manual input.

---

## 📄 License

MIT License — by [Dakmon](https://github.com/dakmontech)
