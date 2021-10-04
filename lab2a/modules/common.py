import datetime
import sys
import logging
import random


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def parn_num(num):
    s = ''
    for x in range(1, 101):
        if num == True and x % 2 == 0:
            s += str(x) + " "
        elif num == False and x % 2 != 0:
            s += str(x) + " "
    return s


logger = logging.getLogger()


def logg_fun():
    mass = [1, "1"]
    try:
        s = 10 + random.choice(mass)
    except TypeError:
        logger.error("ПОМИЛКА")

    else:
        logger.info("УСПІХ")
