import os
import sys
import argparse
from typing import List, Tuple
import asyncio
sys.path.append(os.getcwd())

from quick_gpt.utils.log import setup_logging_config
from quick_gpt.config import load_config
from quick_gpt.llm.agent.client_chat import MCPChat
logger = setup_logging_config()




async def main_():
    """Main function to run the coding agent service."""
    logger.info("[MAIN]: STARTING SERVICE")
    config = load_config()
    chatbox = MCPChat(
        config_file=os.path.join(
            config.get("default_dir"), "quick_gpt/llm/config.json"
        )
    )
    await chatbox.connect(server_name="tools")
    logger.info("[MAIN]: ENDING SERVICE")


def main():
    asyncio.run(main_())


if __name__ == "__main__":
    print("We recommend you to run this project via pip")
    asyncio.run(main_())