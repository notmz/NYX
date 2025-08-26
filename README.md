# NYX
NYX – A lightweight password-protected chatbot hosted on Hugging Face Spaces.
# NYX Chatbot

NYX is a conversational AI chatbot built using **Hugging Face’s Gemma-2-2b-it model**, **Transformers**, **Torch**, and **Gradio**. It allows users to chat naturally in a web interface.

---

## Features

- Friendly, sensible responses
- Runs entirely in a Hugging Face Space
- No login required for users (token is securely stored in Secrets)
- Simple setup for developers

---

## Files

- `app.py` — Main chatbot code
- `requirements.txt` — Python dependencies
- `README.md` — This file

---

## Setup (for developers)

If you want to run your own version:

1. Create a Hugging Face account and generate a **Fine-Grained Access Token**.
2. Create a new Hugging Face Space.
3. Add the token in **Settings → Secrets** with name `HF_TOKEN`.
4. Upload `app.py` and `requirements.txt` to the Space.
5. Run the Space — your chatbot should now respond to messages.

---

## Dependencies

```text
transformers
torch
gradio
huggingface_hub
