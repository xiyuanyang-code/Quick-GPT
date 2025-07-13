# Quick-GPT

A fast, user-friendly CLI tool for multi-turn conversations with OpenAI and Google Gemini models.  
Supports conversation history, system prompts, and easy model switching.

**Run powerful AI conversations from your terminal in a single command!**


## Installation

```bash
git clone https://github.com/xiyuanyang-code/Quick-GPT.git
cd Quick-GPT
pip install .
```


## API Key Configuration

Quick-GPT requires API keys for OpenAI and/or Google Gemini.  
You can provide them via a `.env` file in your project root, or as environment variables. You can also export these variables in your shell profile (`~/.bashrc`, `~/.zshrc`, etc).

**Example `.env` file:**
```env
# OpenAI
OPENAI_API_KEY=sk-xxxxxx
BASE_URL="your api key here"

# Google Gemini
GEMINI_API_KEY=your-gemini-api-key
GOOGLE_GEMINI_BASE_URL=""your api key here"
```


## Quick Start

After installation and API configuration, use the CLI as follows:

```bash
quick-gpt "Your question here"
```

**Example:**
```bash
quick-gpt "Tell me something about Hexo Blog"
```

- The tool auto-selects the model based on your configuration and input.
- Conversation history is saved in the `history/` directory with a timestamped filename.
- View the full conversation history after each session.
- Use `@exit` or `@quit` to quit, and `@history` to display previous outputs.

---

## Advanced Usage

**Switch models:**
```bash
quick-gpt "Hello world" --model_name "gpt-4o-mini"
```

**Add a system prompt:**
```bash
quick-gpt "Hello world" --sys "You should only output in English"
```

- You can also customize system prompts and initial messages in your Python code if using Quick-GPT as a module.

