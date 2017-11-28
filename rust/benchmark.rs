extern crate traildb;
use traildb::Db;
use std::path::Path;

fn main() {
    let db_path = Path::new("/mnt/data/wikipedia-history-small.tdb");
    let db = Db::open(db_path).unwrap();

    let fields = db.fields();
    let field_user = fields.get("user").expect("'user' field not in traildb");
    let field_ip = fields.get("ip").expect("'ip' field not in traildb");

    let empty_user = db.get_item(*field_user, "").unwrap();
    let empty_ip = db.get_item(*field_ip, "").unwrap();

    let mut user_edits = 0;
    let mut ip_edits = 0;

    let mut cursor = db.cursor();
    for trail_id in 0..db.num_trails() {
        cursor.get_trail(trail_id).expect("get_trail failed");

        while let Some(event) = cursor.next() {
            let user = event.items[(*field_user - 1) as usize];
            let ip = event.items[(*field_ip - 1) as usize];

            if user != empty_user {
                user_edits += 1;
            } else if ip != empty_ip {
                ip_edits += 1
            }
        }
    }

    println!("User edits: {}", user_edits);
    println!("IP edits: {}", ip_edits);
}
