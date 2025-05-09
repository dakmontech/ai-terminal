# 🧠 ai-terminal – Terminal con IA para Linux

Este script convierte tu terminal en una herramienta asistida por IA. Lee tus comandos, analiza la salida y sugiere mejoras o próximos pasos usando la API de OpenAI.

📘 [Read this in english](README.md)

---

## 🧰 Requisitos

- Python 3.8+
- Una clave válida de la API de OpenAI
- Cualquier distribución moderna de Linux
- Acceso a la terminal

---

## 🔑 Configura tu clave de API

Edita el archivo `ai_terminal.py` y reemplaza la línea:

```python
openai.api_key = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY_HERE"
```

O usa una variable de entorno:

```bash
export OPENAI_API_KEY="sk-..."
```

---

## ⚙️ Instalación rápida

1. Descomprime el paquete:
```bash
unzip ai_terminal_package_setup_es.zip
cd ai_terminal_package_setup_es
```

2. Ejecuta el instalador:
```bash
python3 setup.py
```

✅ Esto creará el entorno virtual, instalará dependencias y configurará el alias.

⚠️ Luego ejecuta:
```bash
source ~/.zshrc  # o ~/.bashrc
```

---

## ▶️ Uso

Inicia la terminal con IA:

```bash
ai-terminal
```

Al comenzar, verás el mensaje:

```
Describe el propósito de esta sesión (ej: 'aprender comandos básicos de Linux'):
```

Luego:

1. Escribe comandos como siempre.
2. Verás la salida.
3. La IA sugiere cómo continuar o mejorar, recordando el contexto de toda la sesión.
4. Tú decides qué ejecutar.

---

## 🧠 Memoria contextual

Este asistente **recuerda los comandos y sugerencias anteriores** para ofrecerte consejos más inteligentes y consistentes. Perfecto para aprender, investigar o realizar pruebas más complejas.

---

## 💡 Ejemplo

```bash
> ls -l
🤖 SUGERENCIA: Usa `ls -lh` para ver tamaños legibles.
```

---

## 🛡️ Seguridad

- Las sugerencias se imprimen solamente.
- Nada se ejecuta automáticamente.

---

## 📄 Licencia

Licencia MIT — por [Dakmon](https://github.com/dakmontech)
