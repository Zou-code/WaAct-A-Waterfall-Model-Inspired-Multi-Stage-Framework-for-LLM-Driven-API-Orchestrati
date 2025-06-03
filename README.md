# WaAct-A-Waterfall-Model-Inspired-Multi-Stage-Framework-for-LLM-Driven-API-Orchestration

This repository contains the implementation of **WaAct**, a structured framework for orchestrating real-world APIs using large language models (LLMs) via a waterfall-style pipeline.

## Installation

Before running the code, install the required Python packages:

```bash
pip install -r requirements.txt
```

This project requires access to both web APIs and LLM services. You need to obtain the following API keys:

### External Service Keys

- **TMDB API Key:** [Get started here](https://developer.themoviedb.org/docs/getting-started)
- **Spotify API Key:** [Get started here](https://developer.spotify.com/documentation/web-api)

### LLM Service Key

- **OpenAI API Key** (for models like GPT-4 or GPT-4o): [Get your key here](https://platform.openai.com/account/api-keys)
- (Optional) API keys for other supported models, such as DeepSeek or LLaMA, if applicable.

All API keys must be filled in the `config.yaml` file before running the system. A template is provided as `config.yaml.example`. Please rename it to `config.yaml` and update the fields accordingly.

## Quick Start

We provide a simple end-to-end example for quick testing. The example uses the following user request:

**“Give me the number of movies directed by Sofia Coppola.”**

To run this example:

```bash
python run.py
```

The system will go through the full WaAct pipeline, from requirement analysis to code generation and execution, and output the result based on API responses.