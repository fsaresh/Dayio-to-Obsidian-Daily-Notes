import os.path

UTF_ENCODING = 'utf-8-sig'


class FileLocationSettings:
    DAYLIO_EXPORTS_LOCATION = os.path.relpath("./daylio_exports/")  # Exports location relative to main runner
    DAYLIO_CSV_NAME = "sample_daylio.csv"  # Change this to your real backup file!
    DAYLIO_CSV_LOCATION = os.path.join(DAYLIO_EXPORTS_LOCATION, DAYLIO_CSV_NAME)
    MIGRATED_ENTRY_LOCATION = os.path.relpath("./sentence diary")


class DailyNotesFormat:
    summary_header = "\n# Summary\n"
    mood_header = "\n\n## Mood and Activities"
    mood_entry = "\nMood: "
    activities_entry = "\nActivities: "
    tasks_header = "\n\n# Tasks Today\n"  # Feel free to remove this, I kept it for consistency with my existing notes


class DaylioEntryKeys:
    FULL_DATE = 'full_date'
    WEEKDAY = 'weekday'
    MOOD = 'mood'
    ACTIVITIES = 'activities'
    NOTE_BODY = 'note'


