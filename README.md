# Croatian Special Character Replacer
Replacer for reverting Croatian special characters to their original form before saving the file in UTF-8.

Primary usage is for subtitles. In many cases subtitle files are encoded in CP1250 encoding, and certain Croatian characters are not displayed in the original form - č, ć, đ, Č, Ć.
Characters š, ž, Š, Ž seem not to be affected by this.
This script will open the file, replace all the characters in their original form, and re-save the script as UTF-8.

### Usage
`python cro_char_replacer.py name_of_file_or_directory`

If you provide the script with a directory it will automatically detect it and attempt to find all subtitle files inside and process them. In case it finds another directory inside, it will enter it and also find and process all subitle files. This will go as deep in the folder structure as required.

### Customization
You can customize the script to do whatever character replacement you want it to do and with whatever encoding by just modifying the settings on top of the file.
- CHARS_TO_REPLACE - characters to replace in the files.
- ALLOWED_FILE_TYPES - which file types are allowed to be processed.
- SOURCE_ENCODING - estimated encoding of the source file.
- DESTINATION_ENCODING - encoding to be applied to file after processing.
