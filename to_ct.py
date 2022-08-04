import logging
from datetime import date, datetime
from zoneinfo import ZoneInfo


def to_ct(d: date) -> datetime:
    """
    Given a date, convert it to a UTC datetime and return its equivalent in CT.

    :type date: date
    :param date: A date (ex. 1970-01-01)

    :rtype: datetime
    :return: The datetime in CT (US/Central).
    """
    if isinstance(d, datetime):
        logging.error("ERROR: Argument must be of type datetime.datetime")
        raise TypeError
    dt = datetime(year=d.year, month=d.month, day=d.day, tzinfo=ZoneInfo("UTC"))
    return dt.astimezone(tz=ZoneInfo("US/Central"))
