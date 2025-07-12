# Quick-GPT

A CLI tool for multi-turn conversations with OpenAI and Google Gemini models.  
Supports conversation history, system prompts, and easy switching between models.

**Easy and Fast to use in the command line within single line of code**!

## Installation

```bash
git clone https://github.com/xiyuanyang-code/Quick-GPT.git
cd Quick-GPT

# install all the dependencies
pip install .
```


## API Key Configuration

Quick-GPT requires API keys for OpenAI and/or Google Gemini.  
You can set them in a `.env` file in your project root, or as environment variables.


```
# For OpenAI
OPENAI_API_KEY=sk-xxxxxx
BASE_URL=https://api.openai.com/v1/chat/completions

# For Google Gemini
GEMINI_API_KEY=your-gemini-api-key
GOOGLE_GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/models
```

> **Note:**  
> - The `BASE_URL` and `GOOGLE_GEMINI_BASE_URL` should match the endpoints required by your account or region.
> - You can also export these variables in your shell profile (`~/.bashrc`, `~/.zshrc`, etc).

## Quick Start

After installation and API configuration, you can use the CLI as follows:

```bash
quick-gpt "Your question here"
```

**Example:**
```bash
quick-gpt "Tell me something about Hexo Blog"
```

- The tool will automatically select the model based on your configuration and input.
- Conversation history is saved in the `history/` directory with a timestamped filename.
- You can view the full conversation history after each session.
- Enter `"@exit"` or `"@quit"` for quitting the conversation, and `"@history"` for displaying outputs.

## Advanced Usage

- To switch models, change the `model_name` parameter in your code or configuration.

```bash
quick-gpt "Hello world" --model_name "gpt-4o-mini"
```

- System prompts and initial messages can be customized in your Python code if you use the library as a module.

```bash
# add system message
quick-gpt "Hello world" --sys "You should only output in English"
```

