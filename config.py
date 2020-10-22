from untis_class import Class
from untis_subject import Subject

username = 'myusername'  # Untis account username/email
password = 'mypassword'  # Untis account password
server = 'example.com'  # Untis server
useragent = 'Untis2iCal'  # User-agent (not-important)
school = 'School-Name'  # Untis school id

timezone = 'Europe/Brussels'  # Timezone
ics_location = 'ics/'  # Location where ics files will be stored

schoolYear = '2020/2021'  # Formatted as yyyy/yyyy
timeRangeMin = -14  # In days
timeRangeMax = 100  # In days

# List of classes
classes = [
    Class('CLASS1'),
    Class('CLASS2'),
    Class('CLASS3')
]

# List of subjects
subjects = [
    Subject('SUBJECT1'),
    Subject('SUBJECT2')
]
