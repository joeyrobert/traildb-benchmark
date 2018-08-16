from __future__ import print_function
from traildb import TrailDB

def loading():
    traildb = TrailDB("/mnt/data/wikipedia-history-small.tdb")
    user_edits = 0
    ip_edits = 0
    empty_str = ""

    for uuid, trail in traildb.trails():
        for event in trail:
            if event.user != empty_str:
                user_edits += 1
            elif event.ip != empty_str:
                ip_edits += 1

    print("User edits: {}".format(user_edits))
    print("IP edits: {}".format(ip_edits))

loading()
