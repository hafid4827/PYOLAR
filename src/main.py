from console import (
    console_option_menu,
    console_option_value_currency,
    console_options_currency_exchange,
    console_options_price_difference,
)

from notify.notify import notify_config


def console_interactive_menu(user_input_menu: str) -> None:
    match user_input_menu:
        case "1":
            console_execute_value_currency()
        case "2":
            console_execute_currency_exchange()
        case "3":
            console_execute_price_difference()
        case "4":
            exit()


def console_execute_menu():
    console_option_menu()
    input_user = input("=>\t")
    console_interactive_menu(input_user)


def console_execute_value_currency():
    console_option_value_currency()
    tuple_params = (
        "Hello world",
        "XD",
        3,
    )
    notify_config(
        notify=True,
        time_interval=10,
        repeat_number=5,
        param_notify=tuple_params
    )
    input_user = input("=>\t")
    match input_user:
        case "1":
            print("logic 1")
        case "2":
            print("logic 2")
        case "3":
            print("logic 3")
        case "4":
            print("logic 4")
        case "5":
            console_execute_menu()


def console_execute_currency_exchange():
    console_options_currency_exchange()
    input_user = input("=>\t")
    match input_user:
        case "1":
            print("logic 1")
        case "2":
            print("logic 2")
        case "3":
            console_execute_menu()


def console_execute_price_difference():
    console_options_price_difference()
    input_user = input("=>\t")
    match input_user:
        case "1":
            print("logic 1")
        case "2":
            print("logic 2")
        case "3":
            print("logic 3")
        case "4":
            print("logic 4")
        case "5":
            console_execute_menu()


def console_interactive_functional():
    console_execute_menu()


console_interactive_functional()
