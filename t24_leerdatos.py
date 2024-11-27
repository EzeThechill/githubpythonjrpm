#!curl https://raw.githubusercontent.com/itsfoss/text-script-files/refs/heads/master/agatha.txt > abc.txt

#!wget https://raw.githubusercontent.com/itsfoss/text-script-files/refs/heads/master/agatha.

#!wget https://raw.githubusercontent.com/itsfoss/text-script-files/refs/heads/master/sherlock.

import requests
URL = "https://raw.githubusercontent.com/itsfoss/text-script-files/refs/heads/master/agatha.txt"
r = requests.get(URL)
r.text()
r.content()
r.status_code