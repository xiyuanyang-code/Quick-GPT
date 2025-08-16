# Quick-GPT

**Run powerful AI conversations from your terminal in a single command!**

> [!IMPORTANT]
> It is accepted as a submodule for project: https://github.com/xiyuanyang-code/Repo-Coding-Agent

## Introduction

Here are the key features and benefits of our agent:

- Lightweight CLI: We support a streamlined command-line interface for conversation, allowing for custom settings and the integration of your own 100% Python-based MCPs (Modularized Code Processors).

- Integrated Tooling and History: The agent supports powerful tool calls and maintains a history of the conversation, ensuring a coherent and efficient workflow.

- More Than a Agent: By optimizing prompts and providing additional custom MCP resources, our agent can be easily transformed into a powerful AI assistant for various other specialized domains, extending its utility far beyond simple dialogue.

## Installation

```bash
git clone https://github.com/xiyuanyang-code/Quick-GPT.git
cd Quick-GPT
pip install -e .

# or you can use uv :)
```

### Model Config Settings

- For simple LLM response, we use `Anthropic` for our base model usage, thus `ANTHROPIC_API_KEY` and `ANTHROPIC_BASE_URL` are required.

- For web-search tools, `ZHIPU_API_KEY` is required in environment variables. 

We recommend you to write into your `~/.zshrc` or `~/.bashrc` file.

Several Recommendation:

- How to get your Anthropic API-KEY and base-url?
    - Original Settings: https://api.anthropic.com is the base url and you can get your api-key [here](https://docs.anthropic.com/en/home).

    - For third party proxy platform, I recommend [This platform](https://platform.closeai-asia.com/).

- How to get `ZHIPU_API_KEY` for web search?
    - Go to https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys to generating your own api-key.

> [!Note]
> ZHIPU_API_KEY only support Chinese search for current version, it will be optimized in future versions.

```bash
# write it into ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY="switch to yours"
export ANTHROPIC_BASE_URL="switch to yours"
export ZHIPU_API_KEY="switch to yours"
```

### MCP Settings

Model Name and custom MCP config can be manually defined in [`config.json`](./quick_gpt/llm/config.json)

> [!Note]
> Skip this part for default settings.

<details>

<summary> Custom MCP settings

</summary>

```json
{
    "model": {
        "model_name": [
            "claude-3-5-haiku-20241022",
            "claude-sonnet-4-20250514",
            // you can add more here...
            // the default calling sequence is by index.
        ]
    },
    "servers": {
        "tools": {
            "command": "uv",
            "args": [
                "run",
                "/home/user/quick-gpt/llm/mcp_tool_integrate.py"
            ]
        }
    }
}
```

- If you want to customize your own MCP-tools, write functions and pretty docstring in `./CodingAgent/llm/tools` folder, and MCP server will automatically grasp all the functions and view them as available tools. 

</details>

## Usage

```bash
# change to your current working directory
coding_agent

# then enjoy the chat with coding agent!
```

After typing the commands above, you can chat with the chatbox! 

- It will create a file named `.history.txt` which stores all the historical command you have typed in. 

- It will record the dialogue history in 'history' in the original folder (where you clone this project). 

- Logs will be saved here as well (in log in the original folder)


The chat interface supports:
- Multi-turn conversations with context management
- Tool calling via MCP protocol (now supporting file operations and web search for Chinese and English)
- Agent Memory Management
    - Automatic memory compression for long conversations
    - Manual memory storage with the `/memory` command
    - Write history into local files.
- A beautiful CLI UI design.


### DEMO

Now the UI shows like that:

![A simple Demo](https://github.com/xiyuanyang-code/Repo-Coding-Agent/blob/master/assets/imgs/ui_initial.png)


## Contributions

All PRs are welcome. Email the author or raise an issue to communicate how to collaborate in this project.