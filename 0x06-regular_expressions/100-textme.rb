#!/usr/bin/env ruby
# A script that outputs: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/\[from:(\+?\w*)\]\s\[to:(\+?\w*)\]\s\[flags:(\S*)\]/).join(',')
