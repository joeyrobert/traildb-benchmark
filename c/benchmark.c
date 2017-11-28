#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "traildb.h"

int main()
{
    tdb* db = tdb_init();
    tdb_error err;

    if ((err = tdb_open(db, "/mnt/data/wikipedia-history-small.tdb"))) {
        printf("Opening TrailDB failed: %s\n", tdb_error_str(err));
        exit(1);
    }

    uint64_t ip_edits = 0;
    uint64_t user_edits = 0;

    tdb_field user_field;
    tdb_field ip_field;

    if (tdb_get_field(db, "user", &user_field) != 0) {
        fprintf(stderr, "'user' field not found");
        exit(1);
    }

    if (tdb_get_field(db, "ip", &ip_field) != 0) {
        fprintf(stderr, "'ip' field not found");
        exit(1);
    }

    tdb_item empty_user = tdb_get_item(db, user_field, "", 0);
    tdb_item empty_ip = tdb_get_item(db, ip_field, "", 0);


    tdb_cursor *cursor = tdb_cursor_new(db);
    uint64_t i;
    for (i = 0; i < tdb_num_trails(db); i++) {
        const tdb_event *event;
        tdb_get_trail(cursor, i);

        while ((event = tdb_cursor_next(cursor))) {
            tdb_item ip_item = event->items[ip_field-1];
            tdb_item user_item = event->items[user_field-1];

            if (event->items[ip_field-1] != empty_ip) {
                ip_edits++;
            } else if (event->items[user_field-1] != empty_user) {
                user_edits++;
            }
        }
    }

    printf("User edits: %lu\n", user_edits);
    printf("IP edits: %lu\n", ip_edits);
    tdb_cursor_free(cursor);
    tdb_close(db);
    return 0;
}
