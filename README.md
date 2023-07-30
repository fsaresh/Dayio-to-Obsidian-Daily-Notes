# Context

I've been using a sentence diary for years. It's come in many forms: 
- a notepad, which I lost after a move and lost several months of valuable context
- Google Keep (yeesh, not my favorite! Organization and formatting was tedious and not templated at all)
- [Daylio](https://daylio.net/), a convenient Android app meant for this, but it's only an Android app and has no desktop client, plus it costs (a reasonable) fee per year for some features I wanted
- [Obsidian](https://obsidian.md/), which has been pretty fantastic so far! I've combined my sentence diary, my personal notes, some logs, and my to-do and grocery lists here! Everything is just [Markdown](https://en.wikipedia.org/wiki/Markdown) files internally, meaning even if Obsidian catastrophically fails tomorrow or I get tired of it, my files are still available on both my phone and computer to move to another platform!

As a result of using Obsidian as a second brain software, I wanted all my old sentence diary entries in there as well. 

# Daylio to Obsidian
I keep a pretty specific structure in Obsidian (e.g. today's note would be `sentence diary/2023/07-July/2023-07-29-Saturday.md`), so I wanted a way to programmatically create those directories with month names and file names with day of the week as well.

This script migrated all of my entries from Daylio (exported to a CSV with date, weekday, mood, activities, and a full note) to my sentence diary format with a summary, mood and activities, and tasks today section. I could extend this a little farther out and format it nicer, but I really just wanted to have the important part (the note body) under the summary for my migration to Obsidian.

# Usage
1. Place your Daylio CSV backup file in the `daylio_exports folder`
2. Replace the `CSV_NAME` variable in `migration_constants.py`
3. Navigate to the project root and run the Python program from `main.py` via `python main.py`
4. Copy the output from the `sentence_diary` folder into your Obsidian vault! Note that the output will be in structure `YYYY/MM-MMMM/YYYY-MM-DD-dddd.md`
