from urllib.request import urlopen

page =urlopen("http://info.cern.ch/")
content = str(page.read())

print(content)
separar = content.split("html","\n")
print(separar)