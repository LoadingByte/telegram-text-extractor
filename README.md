# Telegram Text Extractor

A tool to extract raw chatlog text from Telegram JSON exports.

## Usage:

You need Python 3 to run this tool.

1. Export your data from Telegram. This can be done in the desktop app via Settings → Advanced → Export Telegram Data. There you can choose whether to only export private chats, or group chats, or both. Remember to disable picture export; that'll just waste time since we're not interested in pictures at all.
2. Go to the folder containing the exported data and locate the `result.json` file. Copy that file into the same folder as the Python script.
3. Launch the script: `python3 telegram_text_extractor.py`
4. Enter the name of the contact or group you wish to extract. All available choices are listed to you.
5. Now enter the name of the person whose messages you'd like to extract. If you want to extract the messages of all conversational partners, just leave this one empty.
6. Your results have been written to `output.txt`. Have fun!
