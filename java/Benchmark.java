import traildb.*;

import java.io.FileNotFoundException;

public class Benchmark {
	public static void main(String[] args) throws FileNotFoundException {
		TrailDB tdb = new TrailDB("/mnt/data/wikipedia-history-small.tdb");
		TrailDBTrail trail = new TrailDBTrail(tdb, 0);
		long userEdits = 0;
		long ipEdits = 0;

		int ipIndex = tdb.fieldMap.get("ip");
		int userIndex = tdb.fieldMap.get("user");

		do {
			while (trail.next() != null) {
				if (!"".equals(trail.getItem(userIndex))) {
					userEdits++;
				} else if (!"".equals(trail.getItem(ipIndex))) {
					ipEdits++;
				}
			}
		} while (trail.nextTrail());

		System.out.println("User edits: " + userEdits);
		System.out.println("IP edits: " + ipEdits);
	}
}