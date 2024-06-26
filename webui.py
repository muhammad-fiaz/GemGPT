"""
This Part of the code is responsible for the web interface of the GemGPT model.
It uses the Gradio library to create a simple web interface that allows users to interact with the model.
The interface allows users to select the model, device, and input prompt, and then generates a response from the model.
The interface also includes advanced options such as adjusting the temperature, top-k, and top-p parameters, as well as quantization.

"""
import torch

from modules.log import logly
from modules.pipeline import chatbot

import gradio as gr

if torch.cuda.is_available():
    device = "cuda"
    logly.info("CUDA is available and using GPU instead.")
    print("Device name:", torch.cuda.get_device_properties("cuda").name)
    print("FlashAttention available:", torch.backends.cuda.flash_sdp_enabled())
elif torch.xpu.is_available():
    device = "xpu"
    logly.info("XPU is available and using XPU instead.")
    logly.warn("this feature is not yet supported. Please use a GPU or CPU instead!.")
else:
    device = "cpu"
    logly.info("CUDA is not available and using CPU instead.")

print(f"torch version: {torch.version}")

with gr.Blocks(theme=gr.themes.Soft(), title="GemGPT") as app:#head="<link rel='icon' href='' sizes='32x32' />"
    gr.HTML("<link rel='icon' href='https://gemmamodels.com/wp-content/uploads/2021/10/cropped-gem-32x32.png' sizes='32x32' />")
    gr.HTML("<h1 style='text-align: center;'>GemGPT</h1>")
    gr.HTML("<h3 style='text-align: center;'>Talk to GemGPT, Powered by Gemma Models</h3>")
    with gr.Row():
        gr.Markdown("Select a model to run. Gemma-2b-it is a smaller model that is faster and uses less memory. Gemma-7b-it is a larger model that is slower and uses more memory.")
    model_options = gr.Dropdown(label="Select a Model", choices=["google/gemma-2b-it", "google/gemma-7b-it"],
                                value="google/gemma-2b-it")
    with gr.Row():
        gr.Markdown("Select the device to run the model on. If you are running this on a CPU, select CPU. If you are running this on a GPU, select CUDA.")
    device = gr.Dropdown(label="Device", choices=["cuda", "cpu","xpu"], value=device)
    with gr.Row():
        gr.Markdown("Output Generated by Selected Model:")
    with gr.Row():
        outputs = gr.Chatbot( placeholder="the model will respond here.",label="Output")
    with gr.Row():
        gr.Markdown("Input your Prompt and click Generate to get a response.")
    with gr.Row():
        inputs = gr.Textbox(lines=2, label="Prompt", placeholder="Type here")
    with gr.Row():
        generate = gr.Button("Generate",interactive=True)
        clear = gr.ClearButton([inputs, outputs])

    with gr.Row():
        advanced_checkbox = gr.Checkbox(label="Show Advanced Options", container=False, elem_classes='min_check',
                                            value=False)

    with gr.Column(scale=1,visible=False) as advanced_column:
            with gr.Row():
                gr.Markdown("<h4>Adjust the parameters to control the model's output.</h4>")
            with gr.Row():
                gr.Markdown("Max New Tokens is the maximum number of tokens that the model will generate.")
            with gr.Row():
                tokens = gr.Slider(minimum=50, maximum=2000, label="Max New Tokens", value=1250)
            with gr.Row():
                gr.Markdown("Temperature is a parameter that controls the randomness of the model's output. A higher temperature will produce more random output.")
            with gr.Row():
                temp = gr.Slider(minimum=0.0, maximum=1.0, label="Temperature", value=0.7)
            with gr.Row():
                gr.Markdown("Top K is a parameter that controls the diversity of the model's output. A higher value will produce more diverse output.")
            with gr.Row():
                top_k = gr.Slider(minimum=1, maximum=100, label="Top K", value=50)
            with gr.Row():
                gr.Markdown("Top P is an alternative to Top K that selects the smallest set of tokens whose cumulative probability exceeds the threshold P.")
            with gr.Row():
                top_p = gr.Slider(minimum=0.0, maximum=1.0, label="Top P", value=0.95)
            with gr.Row():
                gr.Markdown("Quantization is a technique to reduce the size of the model and speed up inference. 4-bit quantization is faster but less accurate than 8-bit.")
            with gr.Row():
                quantization = gr.Dropdown(label="Quantization", choices=["8-bit", "4-bit","2-bit"], value="2-bit")

            generate.click(fn=chatbot, inputs=[inputs, tokens, temp, top_k, top_p, model_options,quantization,device], outputs=outputs)


    advanced_checkbox.change(lambda x: gr.update(visible=x), advanced_checkbox, advanced_column,
                                 queue=False, show_progress=False)
