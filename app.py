import gradio as gr

# Basic chatbot function
def chat(message, history):
    history = history or []
    bot_reply = f"NYX says: {message}"  # for now, it just repeats with NYX prefix
    history.append((message, bot_reply))
    return history, history

# Gradio chat interface
with gr.Blocks() as demo:
    gr.Markdown("# 💬 NYX - Your Chatbot")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message")
    clear = gr.Button("Clear Chat")

    msg.submit(chat, [msg, chatbot], [chatbot, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
