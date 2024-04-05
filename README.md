<div style="text-align: center;">
    
![Preview](https://github.com/muhammad-fiaz/GemGPT/assets/75434191/9c6566ca-db7f-49e2-9ddd-0781edea042f)

[![License](https://img.shields.io/github/license/muhammad-fiaz/gemgpt)](./LICENSE)
[![Version](https://img.shields.io/github/v/release/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt/releases)
[![Code Size](https://img.shields.io/github/languages/code-size/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt)
[![Top Language](https://img.shields.io/github/languages/top/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt)
[![Last Commit](https://img.shields.io/github/last-commit/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt/commits/main)
[![Contributors](https://img.shields.io/github/contributors/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt/graphs/contributors)
[![Open Issues](https://img.shields.io/github/issues-raw/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt/issues?q=is%3Aissue+is%3Aclosed)
[![Pull Requests](https://img.shields.io/github/issues-pr-raw/muhammad-fiaz/gemgpt)](https://github.com/muhammad-fiaz/gemgpt/pulls)
[![Forks](https://img.shields.io/github/forks/muhammad-fiaz/gemgpt?style=social)](https://github.com/muhammad-fiaz/gemgpt/network/members)
[![Stars](https://img.shields.io/github/stars/muhammad-fiaz/gemgpt?style=social)](https://github.com/muhammad-fiaz/gemgpt/stargazers)
[![Watchers](https://img.shields.io/github/watchers/muhammad-fiaz/gemgpt?style=social)](https://github.com/muhammad-fiaz/gemgpt/watchers)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/muhammadfiaz/GemGPT)

</div>

GemGPT is a project that leverages the Gemma model published by Google to create powerful natural language processing applications using the GPT architecture. This repository contains the codebase for GemGPT, which aims to provide a user-friendly interface for fine-tuning the Gemma model for 2b and 7b variants.

> Don't forget to star ⭐ and fork 🍴 the repository if you find GemGPT useful!

## Table of Contents

- [Overview](#)
- [Features](#features)
- [setup](#setup)
- [Getting Started](#getting-started)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Support](#support)
- [Acknowledgements](#acknowledgements)
- [License](#license)


## Features

- Utilizes the Gemma model for natural language processing tasks.
- Provides an easy-to-use interface for integrating Gemma with AI applications.
- Offers advanced features for text generation, sentiment analysis, and more.

## Setup

To use a model from Hugging Face Hub, you need to first install the transformers library and then use the CLI to log in to the Hugging Face Hub.

Install the transformers library:

```bash
pip install transformers
```

Login to the Hugging Face Hub using the CLI:

```bash
transformers-cli login
```
After that, you need to auth using your login token. for more info checkout:- [https://huggingface.co/docs/huggingface_hub/quick-start](https://huggingface.co/docs/huggingface_hub/quick-start)

## Getting Started

To get started with GemGPT, clone the repository and follow the setup instructions in the documentation.

```shell
git clone https://github.com/muhammad-fiaz/gemgpt.git
```
Navigate to the project directory and install the required dependencies:
    
```shell
    cd gemgpt
    pip install -r requirements.txt
```
Run the application using the following command:

```shell
    python launch.py
```
To use GemGpt on Colab or Jupyter Notebook, you can use the following code:

```bash
!git clone https://github.com/muhammad-fiaz/gemgpt.git
!python -m pip install -r requirements.txt
!python launch.py --share
```
You can try out a demo of GemGPT on Hugging Face Spaces, but for optimal performance, we recommend running it locally with a CPU or GPU.

[![Hugging Face Spaces Demo](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/muhammadfiaz/GemGPT)

## Technology Stack

GemGPT is built using the following technologies:

- **Python**: Programming language used for the core implementation.
- **PyTorch**: Deep learning framework used for training and inference.
- **Gradio**: Web-based UI library used for creating the user interface.
- **Transformers**: Library used for working with pre-trained language models.
- **Hugging Face**: Platform used for sharing and downloading pre-trained models.
- **Logly**: Logging library used for tracking and monitoring the application.


## Contributing

We welcome contributions from the community to improve GemGPT. If you're interested in contributing, please read our contributing guidelines.

## CODE OF CONDUCT

We expect contributors to adhere to the GemGPT code of conduct. Please read the [code of conduct](./CODE_OF_CONDUCT.md) before contributing.

## Support

If you have any questions or need help with GemGPT, please reach out to us via the issue tracker.

_Support the Project by Becoming a Sponsor on GitHub_

[![Sponsor muhammad-fiaz](https://img.shields.io/badge/Sponsor-%231EAEDB.svg?&style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/muhammad-fiaz)

## Acknowledgements

GemGPT is built on top of the Gemma model published by Google. We would like to thank the authors of the Gemma model for their work and for making it available as open-source.

## License

GemGPT is licensed under the Apache License 2.0. See the [LICENSE](./LICENSE) file for more details.


```bibtex
@software{Muhammad_Fiaz_GemGPT_2024,
  author = {{Muhammad Fiaz}},
  license = {Apache-2.0},
  month = mar,
  title = {{GemGPT}},
  url = {https://github.com/muhammad-fiaz/GemGPT},
  version = {0.0.0},
  year = {2024}
}

