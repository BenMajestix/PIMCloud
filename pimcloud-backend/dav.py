import sys
from datetime import date
from datetime import datetime
from datetime import timedelta

sys.path.insert(0, "..")
sys.path.insert(0, ".")

import caldav

caldev_url = "https://cloud.benbartel.de/remote.php/dav"
username = "Ben"
password = "abb0t$f0rd_*"

with caldav.DAVClient(
    url=caldev_url,
    username=username,
    password=password,
) as client:
    my_principal = client.principal()

    calendars = my_principal.calendars()

    print_calendars_demo(calendars)


def print_calendars_demo(calendars):
    """
    This example prints the name and URL for every calendar on the list
    """
    if calendars:
        ## Some calendar servers will include all calendars you have
        ## access to in this list, and not only the calendars owned by
        ## this principal.
        print("your principal has %i calendars:" % len(calendars))
        for c in calendars:
            print("    Name: %-36s  URL: %s" % (c.name, c.url))
    else:
        print("your principal has no calendars")