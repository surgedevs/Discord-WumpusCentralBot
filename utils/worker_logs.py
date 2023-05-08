"""
:author @DzikStar
:contributors @DzikStar

This util is used for generating fancy logs messages in the hoster console
Will be used for client events, commands and bot tasks

:used
  - ./main.py
"""

from colorama import Fore

import enums.ExecutionType
import enums.Stage


def user_used_command(member: str, command_name: str, execute_type: enums.ExecutionType.ExecutionType) -> str:
    """
    Console logs command usage (without metrics)

    :param member: str
    :param command_name: str
    :param execute_type: enums.ExecutionType.ExecutionType
    :return: str
    """
    command_execution_method = None

    if execute_type == enums.ExecutionType.ExecutionType.TEXT_COMMAND:
        command_execution_method = 'text command'
    elif execute_type == enums.ExecutionType.ExecutionType.SLASH_COMMAND:
        command_execution_method = 'slash command'

    log_message = f'{Fore.CYAN}[Command Usage]{Fore.RESET} {Fore.YELLOW}{member}{Fore.RESET} used {Fore.BLUE}' \
                  f'{command_name}{Fore.RESET} command as a {Fore.BLUE}{command_execution_method}{Fore.RESET}.'

    return log_message


def support_tracker(stage: enums.Stage.Stage) -> str:
    """
    returns console log messages

    :param stage: enums.Stage.Stage
    :return: str
    """

    if stage == enums.Stage.Stage.AFTER_STARTUP:
        log_message = f'{Fore.MAGENTA}[Support Tracker]{Fore.RESET} Started downloading files.'

        return log_message
