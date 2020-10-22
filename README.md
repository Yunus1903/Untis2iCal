# Untis2iCal

Untis2iCal is a python program the generates iCal files from [WebUntis](https://webuntis.com/) timetables.

## Dependencies

- [webuntis](https://pypi.org/project/webuntis/)
- [ics](https://pypi.org/project/ics/)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [pytz](https://pypi.org/project/pytz/)

Missing dependencies can be installed using [PIP](https://pypi.org/project/pip/).

## Configuration
All config options can be found within `config.py`.

Before running the script, your account credentials and timetables need to be configured.

## Usage
Just run `main.py` and the .ics files will be generated inside the folder specified in `config.py`.

### Recommend usage
The recommended way of using this script is by having a cron job run the script daily.

If you host the .ics files on a webserver, you can subscribe to them using Google Calendar or Outlook Calendar.

## License
This project is licensed under [GNU General Public License v3.0](https://raw.githubusercontent.com/Yunus1903/Untis2iCal/master/LICENSE).
