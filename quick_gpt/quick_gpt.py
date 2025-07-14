import re
import os

from quick_gpt.utils import load_config, generate_filename
from quick_gpt.response import _response_google_sdk, _response_openai_sdk
from quick_gpt.history import load_history, append_message

from colorama import Fore, Style


class quick_GPT:
    """
    A class for managing multi-turn conversations with OpenAI or Google Gemini models,
    including history management, system prompt handling, and model selection.
    """

    def __init__(self, init_message, system_message, model_name) -> None:
        """
        Initialize the quick_GPT instance with configuration, model selection, and history setup.

        Args:
            init_message (str): The initial user message for the conversation.
            system_message (str): The system prompt to guide the model's behavior.
            model_name (str): The name of the model to use (e.g., 'gpt-4o-mini', 'gemini-flash').
        """
        # several config settings
        self.init_message = init_message
        self.system_message = system_message
        self.model_name: str = model_name
        self.id = generate_filename()

        if ("gpt" in self.model_name) or re.search(r"o[134]", self.model_name):
            self.model_type = "openai"
        elif "gemini" in self.model_name:
            self.model_type = "gemini"
        else:
            print(
                Fore.YELLOW
                + "WARNING: Maybe you enter an invalid model_name?"
                + Style.RESET_ALL
            )
            self.model_type = "openai"

        if self.model_type == "openai":
            self.response_method = _response_openai_sdk
        elif self.model_type == "gemini":
            self.response_method = _response_google_sdk
        else:
            raise ValueError("Invalid Response Method is chosen")

        self.api_key, self.base_url = load_config(self.model_type)
        # initialize history
        self.initialize_history()

    def run(self, input_message):
        """
        Run a single conversation iteration:
        - Append user input to history
        - Call the model to get a response
        - Append the model response to history
        - Return the model response

        Args:
            input_message (str): The user's input message.

        Returns:
            str: The assistant's response.
        """
        # Append user input to history
        append_message(self.file_path, role="user", content=input_message)
        # Load conversation history
        history = load_history(self.file_path)
        # Call the model to get a response
        if self.model_type == "openai":
            response = self.response_method(
                content=input_message,
                api_key=self.api_key,
                base_url=self.base_url,
                model_name=self.model_name,
                system_prompt=self.system_message,
                history=history,
            )
            # Extract reply content (adjust as needed for your response format)
            reply = (
                response.get("content") if isinstance(response, dict) else str(response)
            )
        elif self.model_type == "gemini":
            response = self.response_method(
                original_content=input_message,
                api_key=self.api_key,
                base_url=self.base_url,
                history=history,
                system_prompt=self.system_message,
            )
            reply = response.text if hasattr(response, "text") else str(response)
        else:
            reply = "Model type not supported."
        # Append model response to history
        append_message(self.file_path, role="assistant", content=reply)
        # Return the model response

        # model output
        print(Fore.CYAN + reply + Style.RESET_ALL)
        return reply

    def _init_run(self):
        """
        Run the initial conversation turn with the system prompt and initial message.
        - Append the initial message to history
        - Call the model to get the first response
        - Append the model response to history
        - Return the model response

        Returns:
            str: The assistant's response to the initial message.
        """
        # Append initial user message to history
        append_message(self.file_path, role="user", content=self.init_message)
        # Load updated history
        history = load_history(self.file_path)
        # Call the model to get the first response
        if self.model_type == "openai":
            response = self.response_method(
                content=self.init_message,
                api_key=self.api_key,
                base_url=self.base_url,
                model_name=self.model_name,
                system_prompt=self.system_message,
                history=history,
            )
            reply = (
                response.get("content") if isinstance(response, dict) else str(response)
            )
        elif self.model_type == "gemini":
            response = self.response_method(
                original_content=self.init_message,
                api_key=self.api_key,
                base_url=self.base_url,
                history=history,
                system_prompt=self.system_message,
            )
            reply = response.text if hasattr(response, "text") else str(response)
        else:
            reply = "Model type not supported."
        # Append model response to history
        append_message(self.file_path, role="assistant", content=reply)

        # model output
        print(Fore.CYAN + reply + Style.RESET_ALL)
        return reply

    def show_history(self):
        """
        Print the current conversation history to the console.
        """
        print(Fore.GREEN + "================HISTORY================" + Style.RESET_ALL)
        print(load_history(self.file_path))

    def initialize_history(self):
        """
        Initialize the conversation history file and add the system prompt as the first message.

        Returns:
            list: The initial conversation history.
        """
        # !fix: stop using os.getcwd() for generating rubbish everywhere!
        home_dir = os.path.expanduser("~") 
        history_dir = os.path.join(home_dir, ".quick_gpt_dir")
        os.makedirs(history_dir, exist_ok=True)

        self.file_path = os.path.join(history_dir, self.id)
        self.file_path += ".json"
        with open(self.file_path, "w") as file:
            file.close()

        # add initial prompt
        append_message(self.file_path, role="system", content=self.system_message)

        return load_history(self.file_path)

