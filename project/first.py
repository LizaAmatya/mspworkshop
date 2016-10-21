import requests
url = "https://nikhil.info.np"
newname = requests.get(url)

if newname.status_code == 200:
	print(newname.text)
else:
	print("ERROR")
	print("status code : %d" % newname.status_code)



