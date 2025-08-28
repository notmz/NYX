NYX – Password-Protected Chatbot on Hugging Face Spaces

NYX is a lightweight conversational AI chatbot powered by the Gemma-2-2B-IT model, built with Transformers, PyTorch, and Gradio. It runs directly in a Hugging Face Space, providing a simple web interface for natural conversations.

✨ Features

🤖 Conversational AI – generates friendly, coherent responses

☁️ Hosted on Hugging Face Spaces – no local setup required

🔒 Secure – developer token stored safely as a Space secret

⚡ Lightweight setup – minimal dependencies, easy deployment

📂 Project Structure
app.py            # Main chatbot code
requirements.txt  # Python dependencies
README.md         # Project documentation

🚀 Setup (Developers)

To run your own instance:

Create a Hugging Face account
 and generate a Fine-Grained Access Token.

Create a new Hugging Face Space.

Add your token in Settings → Secrets with the name HF_TOKEN.

Upload app.py and requirements.txt to the Space.

Launch the Space — your chatbot should now be live! 🎉

📦 Dependencies

transformers

torch

gradio

huggingface_hub

Install locally with:

pip install -r requirements.txt
