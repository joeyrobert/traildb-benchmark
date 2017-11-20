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

    tdb_cursor *cursor = tdb_cursor_new(db);
    uint64_t i;
    uint64_t ip_edits = 0;
    uint64_t user_edits = 0;
    uint64_t user_field = 0;
    uint64_t ip_field = 1;


    for (i = 0; i < tdb_num_trails(db); i++) {
        const tdb_event *event;
        tdb_get_trail(cursor, i);

        while ((event = tdb_cursor_next(cursor))) {
            uint64_t ip_len;
            uint64_t user_len;
            tdb_get_item_value(db, event->items[ip_field], &ip_len);
            tdb_get_item_value(db, event->items[user_field], &user_len);
            
            if (ip_len) {
                ip_edits++;
            } else if (user_len) {
                user_edits++;
            }
        }
    }

    printf("User edits: %d\n", user_edits);
    printf("IP edits: %d\n", ip_edits);
    tdb_cursor_free(cursor);
    tdb_close(db);
    return 0;
}