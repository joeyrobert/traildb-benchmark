extern crate traildb;
use traildb::Db;
use std::path::Path;

fn main() {
    let db_path = Path::new("/mnt/data/wikipedia-history-small.tdb");
    let db = Db::open(db_path).unwrap();
    let mut user_edits = 0;
    let mut ip_edits = 0;
    let field_vals = ["user", "ip", "title", "blah"];

    for trail in db.iter() {
        for event in trail {
            for (item, item_ref) in event.items.into_iter().zip(field_vals.iter()) {

                let item = db.get_item_value(*item).unwrap();

                if *item_ref == "user" && item != "" {
                    user_edits += 1
                } else if *item_ref == "ip" && item != "" {
                    ip_edits += 1
                }
            }
        }
    }

    println!("User edits: {}", user_edits);
    println!("IP edits: {}", ip_edits);
}