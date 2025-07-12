import re
import os

from quick_gpt.utils import load_config, generate_filename
from quick_gpt.response import _response_google_sdk, _response_openai_sdk
from quick_gpt.history import load_history, append_message

from colorama import Fore, Style


class quick_GPT:
    def __init__(self, init_message, system_message, model_name) -> None:
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

        self.api_key, self.base_url = load_config(self.model_type)
        # initialize history
        self.initialize_history()

    def run(self, input_message):
        # single run iteration
        # todo
        pass

    def _init_run(self):
        # todo
        pass

    def show_history(self):
        print(Fore.GREEN + "================HISTORY================" + Style.RESET_ALL)
        load_history(self.file_path)

    def initialize_history(self):
        history_dir = os.path.join(os.getcwd(), "history")
        os.makedirs(history_dir, exist_ok=True)

        self.file_path = os.path.join(history_dir, self.id)
        self.file_path += ".json"
        with open(self.file_path, "w") as file:
            file.close()

        # add initial prompt
        append_message(self.file_path, role="system", content=self.system_message)


if __name__ == "__main__":
    test_list = ["gpt-4o-mini", "o3", "gfhjdn", "gemini-flash"]
    for test_name in test_list:
        test = quick_GPT("1", "hellpo", model_name=test_name)
