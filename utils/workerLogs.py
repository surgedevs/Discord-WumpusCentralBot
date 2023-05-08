## Author: @DzikStar
## Contributors: @DzikStar
##
## Description:
## This util is used for generating fancy logs messages in the hoster console
## Will be used for client events, commands and bot tasks
##
## Used in:
##   - ./main.py

from colorama import Fore

def userUsedCommand(member, commandName, executeType):
    ## This function is used to return to hoster console logs message about command usage (actually lowpoly version without metrics)
    ## Variables Used There:
    ##   - string: member: User name of the user which used the command
    ##   - string: commandName: Codename of the command
    ##   - int: executeType: Information about that if command was used as a slash or prefix command
    ##     * 1 = PREFIX COMMAND
    ##     * 2 = SLASH COMMAND

    ## Setting up convertion
    if executeType == 1:
        commandExecutionMethod = str('prefix command')
    elif executeType == 2:
        commandExecutionMethod = str('slash command')

    logMessage = f'{Fore.CYAN}[COMMAND USAGE]{Fore.RESET} {Fore.YELLOW}{member}{Fore.RESET} used {Fore.BLUE}{commandName}{Fore.RESET} command as a {Fore.BLUE}{commandExecutionMethod}{Fore.RESET}.'
    return logMessage
    del executeType, commandExecutionMethod, member, commandName, logMessage