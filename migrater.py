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


class SentenceDiaryFormat:
    header = "\n# Summary\n"
    mood = "\n\n## Mood and Activities\nMood: "
    tasks = "\n\n# Tasks Today\n"


class DaylioMigration:
    def write_to_file(self, contents, migrated_file_folder, migrated_file_name):
        relative_folder_path = f"./sentence diary/{migrated_file_folder}"
        if not os.path.exists(relative_folder_path):
            os.makedirs(relative_folder_path)
        with open(f'{relative_folder_path}/{migrated_file_name}', 'w') as migrated_file:
            migrated_file.write(contents)

    def migrate(self, csv_location: str):
        with open(csv_location, newline='', encoding=UTF_ENCODING) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contents = SentenceDiaryFormat.header + row[DaylioKeys.NOTE_BODY].replace('<br>', '\n')
                contents += SentenceDiaryFormat.mood + row[DaylioKeys.MOOD] + "\nActivities: " + row[DaylioKeys.ACTIVITIES]
                contents += SentenceDiaryFormat.tasks

                migrated_file_name = f"{row[DaylioKeys.FULL_DATE]}-{row[DaylioKeys.WEEKDAY]}.md"
                entry_date_components = row[DaylioKeys.FULL_DATE].split('-')
                entry_date_month = entry_date_components[1]
                migrated_file_folder = entry_date_components[0] + "/" + entry_date_month + "-" + calendar.month_name[int(entry_date_month)]
                #print(migrated_file_folder)

                self.write_to_file(contents, migrated_file_folder, migrated_file_name)
