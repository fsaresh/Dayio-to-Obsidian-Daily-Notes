import calendar
import csv
import os

UTF_ENCODING = 'utf-8-sig'


class DaylioKeys:
    FULL_DATE = 'full_date'
    WEEKDAY = 'weekday'
    MOOD = 'mood'
    ACTIVITIES = 'activities'
    NOTE_BODY = 'note'


class ObsidianDailyNotesFormat:
    header = "\n# Summary\n"
    mood = "\n\n## Mood and Activities\nMood: "
    tasks = "\n\n# Tasks Today\n"


class DaylioMigration:
    def write_to_file(self, contents, migrated_file_folder, migrated_file_name):
        if not os.path.exists(migrated_file_folder):
            os.makedirs(migrated_file_folder)
        with open(f'{migrated_file_folder}/{migrated_file_name}', 'w') as migrated_file:
            migrated_file.write(contents)

    def migrate(self, csv_location: str):
        with open(csv_location, newline='', encoding=UTF_ENCODING) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contents = ObsidianDailyNotesFormat.header + row[DaylioKeys.NOTE_BODY].replace('<br>', '\n')
                contents += ObsidianDailyNotesFormat.mood + row[DaylioKeys.MOOD] + "\nActivities: " + row[DaylioKeys.ACTIVITIES]
                contents += ObsidianDailyNotesFormat.tasks

                # Construct Obsidian file structure of YYYY/MM-MMMM/YYYY-MM-DD-dddd
                entry_date_parts = row[DaylioKeys.FULL_DATE].split('-')
                entry_date_month_expanded = f"{entry_date_parts[1]}-{calendar.month_name[int(entry_date_parts[1])]}"
                migrated_file_folder = f"./sentence diary/{entry_date_parts[0]}/{entry_date_month_expanded}"
                migrated_file_name = f"{row[DaylioKeys.FULL_DATE]}-{row[DaylioKeys.WEEKDAY]}.md"

                self.write_to_file(contents, migrated_file_folder, migrated_file_name)
