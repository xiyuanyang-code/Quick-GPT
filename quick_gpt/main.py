import argparse

from colorama import Fore, Style
from quick_gpt.quick_gpt import quick_GPT


def _load_parser() -> tuple[str, str, str]:
    parser = argparse.ArgumentParser(
        description="Quick Calling an LLM in the command line, in just one command and get the answer immediately."
    )

    parser.add_argument("message", type=str, help="Your message")

    parser.add_argument(
        "--sys",
        type=str,
        default="You are a helpful assistant, please ensure you will respond to me as fast as you can.",
        help="The system prompt, optional",
    )

    parser.add_argument(
        "--model_name", type=str, default="gemini-2.5-flash", help="Default model type"
    )

    args = parser.parse_args()
    return args.message, args.sys, str(args.model_name).strip()


def main():
    message, system_message, model_name = _load_parser()
    Chat = quick_GPT(message, system_message, model_name)

    Chat._init_run()

    terminal_state = False

    while True:
        input_message = str(input("Input your message:")).strip().lower()

        # deal with some specific commands
        if input_message == "@exit" or input_message == "@quit":
            terminal_state = True
        elif input_message == "@history":
            Chat.show_history()
        elif input_message[0] == "@":
            print(Fore.YELLOW + "WARNING, invalid magical command" + Style.RESET_ALL)

        if terminal_state is True:
            print(
                Fore.BLUE
                + f"Round Ends, all the history file can be seem via: {Chat.file_path}"
                + Style.RESET_ALL
            )
            break

        Chat.run(input_message)


if __name__ == "__main__":
    main()
