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
    ##   - string: member = User name of the user which used the command
    ##   - string: commandName = Codename of the command
    ##   - integer: executeType = Information about that if command was used as a slash or prefix command
    ##     * 1 = PREFIX COMMAND
    ##     * 2 = SLASH COMMAND

    if executeType == 1:
        commandExecutionMethod = str('prefix command')
    elif executeType == 2:
        commandExecutionMethod = str('slash command')

    logMessage = f'{Fore.CYAN}[Command Usage]{Fore.RESET} {Fore.YELLOW}{member}{Fore.RESET} used {Fore.BLUE}{commandName}{Fore.RESET} command as a {Fore.BLUE}{commandExecutionMethod}{Fore.RESET}.'
    return logMessage
    del executeType, commandExecutionMethod, member, commandName, logMessage

def supportTracker(stage):
    ## This function is used to return to hoster console logs messages 
    ## Variables Used There:
    ##   - integer: stage = giving us information about Support Tracker
    ##     * 1 = Everything got started after bot startup or task loop
    if stage == 1:
        logMessage = f'{Fore.MAGENTA}[Support Tracker]{Fore.RESET} Started downloading files.'
        return logMessage
        del stage, logMessage