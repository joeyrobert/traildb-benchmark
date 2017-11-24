package main

import (
	"fmt"
	"github.com/traildb/traildb-go"
)

type Event struct {
	Ip        string `tdb:"ip"`
	User      string `tdb:"user"`
}

func main() {
	db, err := tdb.Open("/mnt/data/wikipedia-history-small.tdb")
	if err != nil {
		panic(err)
	}
	trail, err := tdb.NewCursor(db)
	if err != nil {
		panic(err)
	}
	user_edits := 0
	ip_edits := 0
	for i := uint64(0); i < db.NumTrails; i++ {
		err := tdb.GetTrail(trail, i)
		if err != nil {
			panic(err)
		}

		for {
			evt := trail.NextEvent()

			if evt == nil {
				trail.Close()
				break
			}

			r := Event{}
			// evt.ToStruct(r)
			evt.ToMap()

			// if r.User != "" {
			// 	user_edits += 1
			// } else if r.Ip != "" {
			// 	ip_edits += 1
			// }
		}
	}

	fmt.Printf("User edits: %d", user_edits)
	fmt.Printf("IP edits: %d", ip_edits)
}
