extern crate traildb;
use traildb::Db;
use std::path::Path;

fn main() {
    let db_path = Path::new("/mnt/data/wikipedia-history-small.tdb");
    let db = Db::open(db_path).unwrap();
    let mut user_edits = 0;
    let mut ip_edits = 0;
    let mut fields = Vec::new();
    for i in 1..db.num_fields() as traildb::Field {
        fields.push(db.get_field_name(i).unwrap());
    }

    for trail in db.iter() {
        for event in trail {
            for (field, item) in fields.iter().zip(event.items) {
                let value = db.get_item_value(*item).unwrap_or("");
                if *field == "user" && value != "" {
                    user_edits += 1;
                } else if *field == "ip" && value != "" {
                    ip_edits += 1;
                }
            }
        }
    }

    println!("User edits: {}", user_edits);
    println!("IP edits: {}", ip_edits);
}