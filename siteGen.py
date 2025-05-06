def write_page(name, header, sidebar, script, main):
	with open(name+".html", 'w') as file:
		# Start file
		file.write("<!DOCTYPE html>\n<html lang=\"en\">\n")

		# Write in the header
		for line in header:
			file.write(line)

		# Set up main sections
		file.write("<body>\n<div class=\"wrapper\">\n")

		# Write side bar
		file.write("<div class=\"sidebar\">\n")
		for line in sidebar:
			file.write(line)
		file.write("</div>\n")

		# Write main body
		file.write("<div class=\"main-content\">\n")
		for line in main:
			file.write(line)
		file.write("</div>\n")
		
		# End of main section
		file.write("</div>\n")
		# Add scripts
		for line in script:
			file.write(line)
		# End file
		file.write("</body>\n</html>")

# Read in header content
header_content = []
with open("_header.html", 'r') as header_file:
	for line in header_file:
		header_content.append(line)

# Read in sidebar content
bar_content = []
with open("_sidebar.html", 'r') as bar_file:
	for line in bar_file:
		bar_content.append(line)

# Read in script content
script_content = []
with open("_script.html", 'r') as bar_file:
	for line in bar_file:
		script_content.append(line)

# Start searching for pages...
# Page 0 is the index, all other pages have a name at the top
for i in range(3):
	main_content = []
	with open(f"_page_{i}.html") as main_file:
		for line in main_file:
			main_content.append(line)

	# Write page
	write_page(main_content[0].strip(), header_content, bar_content, script_content, main_content[1:])