require "traildb"

def loading
  puts "Starting benchmark"
  traildb = TrailDB.new("/mnt/data/wikipedia-history-small.tdb")
  user_edits = 0
  ip_edits = 0

  traildb.trails.each do |(uuid, trail)|
    trail.each do |event|
      if event["user"] != ""
        user_edits += 1
      elsif event["ip"] != ""
        ip_edits += 1
      end
    end
  end

  puts "User edits: #{user_edits}"
  puts "IP edits: #{ip_edits}"
end

loading
