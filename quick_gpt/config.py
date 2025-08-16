"""Configuration handling for the coding agent."""

import yaml
import os
import json
import importlib.resources


def write_config():
    """Write configuration to a YAML file."""
    # write current working directory
    default_dir = os.getcwd()
    print("Default dir: ", default_dir)
    # write log dir
    log_dir = os.path.join(default_dir, "log")
    print("log dir: ", log_dir)

    # rewrite MCP config
    MCP_config_dir = os.path.join(default_dir, "quick_gpt/llm/config.json")
    try:
        with open(MCP_config_dir, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {MCP_config_dir} was not found.")
        exit()
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {MCP_config_dir}.")
        exit()

    data["servers"]["tools"]["args"][1] = os.path.join(
        default_dir, "quick_gpt/llm/mcp_tool_integrate.py"
    )

    print("Modified MCP config:", data)
    print(f"This file is located in {MCP_config_dir}")

    try:
        with open(MCP_config_dir, "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error writing to file {MCP_config_dir}: {e}")

    # Write into yaml file
    config_data = {
        "default_dir": default_dir,
        "log_dir": log_dir,
        "mcp_log_dir": MCP_config_dir,
    }

    # Write to YAML file
    with open("./quick_gpt/config.yaml", "w") as yaml_file:
        yaml.dump(config_data, yaml_file, default_flow_style=False)

    print("Configuration written to config.yaml")


def load_config():
    """Load configuration from the YAML file.

    Returns:
        dict: Configuration data.
    """
    with (
        importlib.resources.files("quick_gpt").joinpath("config.yaml").open("r") as f
    ):
        config = yaml.safe_load(f)
    return config


if __name__ == "__main__":
    write_config()
