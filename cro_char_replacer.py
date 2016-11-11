# -*- coding: utf-8 -*-
import sys
import os
import io


# Characters to be replaced in the file content.
CHARS_TO_REPLACE = {
	"È": "Č",
	"Æ": "Ć",
	"è": "č",
	"æ": "ć",
	"ð": "đ"
}
# Allowed types of files to be processed.
ALLOWED_FILE_TYPES = ('.srt', '.txt', '.sub')

# Define encoding values.
# There is no way to apsulutely correctly quess origin encoding so doing an educated guess.
# Change settings if working with different origin encoding.
SOURCE_ENCODING = "cp1250"
DESTINATION_ENCODING = "utf8"


def process_file(file_name):
	"""
	Process should happen in following steps:
	- check is this file allowed to be processed.
	- open the file in read mode and get its content
	- transfer the content to write encoding format
	- close the file and open it again for writing in its encoding
	- process the content by replacing all specified characters
	- write the new content to the file and close it
	"""
	if not allowed_file_type(file_name):
		print "-> %s is not supported. No action taken." % file_name
		return

	read_file = io.open(file_name, "r", encoding=SOURCE_ENCODING)
	read_file_content = read_file.read()
	read_file_content = read_file_content.encode(DESTINATION_ENCODING)
	read_file.close()

	write_file = io.open(file_name, "w", encoding=DESTINATION_ENCODING)
	write_file_content = replace_characters(read_file_content)
	write_file.write(write_file_content)
	write_file.close()
	print "-> %s successfuly processed." % file_name


def process_directory(dir_name):
	"""
	Process should happen in following steps:
	- get the list of files available in the directory
	- in case no files are found nothing will happen
	- in case some files are detected print the message we found them and process one by one.
	- if one of the "files" is a directory, call this method again to process all files inside it.
	"""
	files = os.listdir(dir_name)
	if files:
		print "Directory detected, attempting to process files:"
	for current_file in files:
		file_path = os.path.join(dir_name, current_file)
		process_based_on_type(file_path)


def process_based_on_type(file_path):
	"""
	Call the appropriate method based on is the path file or a directory.
	"""
	# Check is it directory or a file and do actions accordingly.
	if os.path.isfile(file_path):
		process_file(file_path)
	elif os.path.isdir(file_path):
		process_directory(file_path)


def replace_characters(content_to_change):
	"""
	Replace the characters in the content sent using CHARS_TO_REPLACE values.
	"""
	for old_char, new_char in CHARS_TO_REPLACE.iteritems():
		content_to_change = content_to_change.replace(old_char, new_char)

	return unicode(content_to_change, DESTINATION_ENCODING)


def allowed_file_type(file_name):
	"""
	Check is file one of the allowed file extensions.
	Return boolean based on check.
	"""
	return file_name.lower().endswith(ALLOWED_FILE_TYPES)


def main():
	"""
	Check arguments being sent and call the method to open and modify the files.
	In case its file process it, and in case its directory process all files with
	supported format inside it.
	"""
	arguments_sent = sys.argv
	if len(arguments_sent) > 1:
		file_path = arguments_sent[1]
		process_based_on_type(file_path)


# Standard boilerplate to run main method.
if __name__ == "__main__":
	main()
