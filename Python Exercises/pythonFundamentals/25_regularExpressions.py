import re

emails = ['bob.doe@gmail.com', 'jerryAYetes@hotmail.com', 'notAnEmail',
          '23soccerStar4@yahoo.com', 'sdak--.@', 'spyGuy@gov.gov']
emailPattern = '.+?@.+?\.[a-z]+$'
comEmailPattern = '.+?@.+?\.com$'
validEmails = [email for email in emails if re.match(emailPattern, email)]

numberPattern = '.*?(?P<myNumber>[0-9]+).*'
mySentence = 'Looking for a number in 23 can be difficult in the middle of a sentence'
numberMatch = re.match(numberPattern, mySentence)
numberMatch.group('myNumber')