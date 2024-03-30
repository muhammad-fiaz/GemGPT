import os

from modules.log import logly

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import torch
from transformers import pipeline, AutoTokenizer, BitsAndBytesConfig


def pipeline_tunnel(model, device):
    return pipeline(
        "text-generation",
        model=model,
        model_kwargs={
            "torch_dtype": torch.float16,
        },
        device=device,
    )


def chatbot(input_text, max_new_tokens=1250, temperature=0.7, top_k=50, top_p=0.95, model="google/gemma-2b-it",
            quantization="4-bit", device="cuda"):
    try:
        if quantization == "4-bit":
            quantization_config = BitsAndBytesConfig(load_in_4bit=True)

        else:
            quantization_config = BitsAndBytesConfig(load_in_8bit=True)

        tokenizer = AutoTokenizer.from_pretrained(model, quantization_config=quantization_config)

        pipeline_model = pipeline_tunnel(model, device)
        messages = [{"role": "user", "content": input_text}]
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = pipeline_model(
            prompt,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
        )
        generated_text = outputs[0]["generated_text"][len(prompt):]
        return generated_text
    except Exception as e:
        logly.error(f"Error in GemGPT: {e}")
        return str(e)
