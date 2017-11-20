const TrailDB = require('traildb').TrailDB;

const tdb = new TrailDB({
  path: '/mnt/data/wikipedia-history-small.tdb'
});

var ipEdits = 0;
var userEdits = 0;

for (var trail of tdb.trails()) {
  for (var event of trail.events({ toMap: true })) {
    if (event.user) {
      userEdits++; 
    } else if(event.ip) {
      ipEdits++;
    }
  }
}

console.log('User edits:', userEdits);
console.log('IP edits:', ipEdits);