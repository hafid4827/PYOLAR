from plyer import notification as nt
from time import sleep
from datetime import datetime
from datetime import timedelta


def notify_description(title: str = "title", info: str = "info", time_duration_notify: int = 10) -> None:
    """
    Notificacion recibe una tupla
    """
    nt.notify(
        title=title,
        message=info,
        timeout=time_duration_notify  # displaying time
    )


def compare_argument(param_notify: tuple):
    # logic arguments compare with tuple void or not
    if param_notify:
        notify_description(*param_notify)
    else:
        notify_description()


def time_specs(repeat_number: int, time_interval: int, param_notify: tuple):
    """
    :repeat_number: int -> number of times the notification will be repeated
    :time_interval: int -> interval of times that the appearance of the notification will be repeated in a segment of time defined in the function
    :param_notify: tuple -> title, information and notification timeout rules
    """
    counter = 0
    while counter <= repeat_number:
        temporal = datetime.now() + timedelta(seconds=time_interval)
        while True:
            if temporal.second == datetime.now().second:
                compare_argument(*param_notify)
                break
        counter += 1
        sleep(1)
    counter = 0


def notify_config(notify: bool = False, time_interval: int = 1, repeat_number: int = 1, param_notify: tuple = ()):
    """
    Esto lo hara sebastian
    """
    if not notify:
        compare_argument(*param_notify)
    else:
        time_specs(repeat_number, time_interval, *param_notify)
