require "traildb"

def loading
  traildb = TrailDB.new("/mnt/data/wikipedia-history-small.tdb")
  traildb.reuse_cursor = true
  user_edits = 0
  ip_edits = 0
  user_field = traildb.field("user")
  ip_field = traildb.field("ip")

  traildb.trails.each do |(uuid, trail)|
    trail.each do |event|
      if event[user_field] != ""
        user_edits += 1
      elsif event[ip_field] != ""
        ip_edits += 1
      end
    end
  end

  puts "User edits: #{user_edits}"
  puts "IP edits: #{ip_edits}"
end

loading
