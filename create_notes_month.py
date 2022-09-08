import datetime
import calendar
import os
from os.path import exists

global year
global month
global day


def get_today():
    global year, month, day

    today = datetime.datetime.now()
    year = today.year
    month = today.month
    day = today.day


def create_year_month_directory():

    year_directory = os.path.join(os.getcwd(), str(year))
    if not exists(year_directory):
        os.mkdir(year_directory)

    month_directory = os.path.join(os.getcwd(), str(year), calendar.month_name[month])
    if not exists(month_directory):
        os.mkdir(month_directory)

    return month_directory


def create_week_directories(month_directory):
    calendar_month = calendar.monthcalendar(year, month)

    week_num = 1
    for week in calendar_month:
        week_path = month_directory + "/week{}".format(week_num)
        if not exists(week_path):
            os.mkdir(week_path)

        for date_num in week:
            if date_num >= day:
                weekday_num = calendar.weekday(year, month, date_num)
                weekday_name = calendar.day_name[weekday_num]
                new_day_path = week_path + "/{}_{}_{}_{}.md".format(year, month, date_num, weekday_name)

                if not exists(new_day_path):
                    new_day_file = open(new_day_path, "x")
                    with open(os.getcwd() + "/notes_template.md") as template:
                        template_lines = template.readlines()

                    template = ""
                    for line in template_lines:
                        template += line

                    new_day_file.write(template)

        week_num += 1


def main():
    get_today()
    directory = create_year_month_directory()
    create_week_directories(directory)


main()
