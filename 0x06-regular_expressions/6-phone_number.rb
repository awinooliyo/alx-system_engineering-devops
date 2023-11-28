#!/usr/bin/env ruby
# A regex that must match a 10 digit phone number
puts ARGV[0].scan(/^\d{10}$/).join
