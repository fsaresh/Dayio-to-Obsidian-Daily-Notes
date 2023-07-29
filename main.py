from migrater import DaylioMigration


CSV_LOCATION = "./daylio_export_2023_07_28.csv"


if __name__ == '__main__':
    daylio_migrater = DaylioMigration()
    daylio_migrater.migrate(CSV_LOCATION)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
