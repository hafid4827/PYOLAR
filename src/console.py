from colorama import Fore

"""
User content, console interface
"""


def console_option_menu() -> None:
    """ option selected menu """
    print(Fore.GREEN + "\nselect an option:", end="\n\n")
    print(Fore.CYAN + "(1) now the current value of a currency")
    print(Fore.CYAN + "(2) currency exchange")
    print(Fore.CYAN + "(3) price difference")
    print(Fore.RED + "(4) exit", end="\n\n")
    print(Fore.MAGENTA + "=" * 50)


def console_option_value_currency() -> None:
    """ 
    this is first option from menu\n
    * (1) now the current value of a currency
    """
    print(Fore.YELLOW + "\nNow the current value of a currency")
    print(Fore.GREEN + "\nSelect an option:", end="\n\n")
    print(Fore.CYAN + "(1) notification")
    print(Fore.CYAN + "(2) time")
    print(Fore.CYAN + "(3) exchange")
    print(Fore.CYAN + "(4) number of repetitions")
    print(Fore.RED + "(5) back", end="\n\n")
    print(Fore.MAGENTA + "=" * 50)


def console_options_currency_exchange() -> None:
    """ 
    this is second option from menu\n
    * (2) currency exchange
    """
    print(Fore.YELLOW + "\nCurrency exchange")
    print(Fore.GREEN + "\nSelect an option:", end="\n\n")
    print(Fore.CYAN + "(1) from")
    print(Fore.CYAN + "(2) to")
    # tarea voltear la divisa
    print(Fore.RED + "(3) back", end="\n\n")
    print(Fore.MAGENTA + "=" * 50)


def console_options_price_difference() -> None:
    """ 
    this is three option from menu\n
    * (3) price difference
    """
    print(Fore.YELLOW + "\nPrice difference")
    print(Fore.GREEN + "\nSelect an option:", end="\n\n")
    print(Fore.CYAN + "(1) flirts exchange")
    print(Fore.CYAN + "(2) second exchange")
    print(Fore.CYAN + "(3) time delay")
    print(Fore.CYAN + "(4) repeat number")
    print(Fore.RED + "(5) back", end="\n\n")
