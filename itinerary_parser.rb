#!/usr/bin/env ruby

require "Nokogiri"
require "CSV"

#Load the HTML file
file = File.read("/Users/lazarova/Dev/brofiyaGit/brofiya/itinerary.html")
doc = Nokogiri::HTML(file)

#Map contents of header to array & loop over
all_data = doc.css("div.content").css("header").map do |header|
	#Get the date
	date = header.css("h3").css("strong").text
	#Get the location
	location = header.css("h3").css("> text()").text.strip
	#Get the description
	description = header.css("p").text
	#Place in inner array
	[date, location, description]
end

#Write array of information to CSV
	CSV.open("itinerary.csv", "w") do |csv|
	#Write headers
	csv << ["date", "location", "description"]
	#Write each inner array as row 
	all_data.each{|row| csv << row}
end

