import gradio as gr
from transformers import AutoTokenizer, pipeline
import torch

model = "google/gemma-2b-it"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = pipeline(
    "text-generation",
    model=model,
    model_kwargs={
        "torch_dtype": torch.float16,
    },
    device="cuda",
)


def chatbot(input_text, max_new_tokens=1250, temperature=0.7, top_k=50, top_p=0.95):
    messages = [{"role": "user", "content": input_text}]
    prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipeline(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p
    )
    generated_text = outputs[0]["generated_text"][len(prompt):]
    return generated_text




iface = gr.Interface(
    fn=chatbot,
    inputs=[
        gr.Textbox(lines=2, label="Input"),
        gr.Slider(minimum=50, maximum=2000, label="Max New Tokens",  value=1250),
        gr.Slider(minimum=0.0, maximum=1.0, label="Temperature",  value=0.7),
        gr.Slider(minimum=1, maximum=100, label="Top K",  value=50),
        gr.Slider(minimum=0.0, maximum=1.0, label="Top P",  value=0.95),
    ],
    outputs=gr.Textbox(label="Output"),
    title="GemGPT",
    description="Talk to GemGPT,Powered by a 2 billion parameter Gemma Model",
)

iface.launch()
