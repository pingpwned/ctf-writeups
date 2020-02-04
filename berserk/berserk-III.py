import requests
import base64

def make_request():
	s = requests.Session()
	url = 'http://challenges.thecatch.cz/42fd967386d83d7ecc4c716c06633da9/'
	request = s.get(url)
	text = request.text


	text = text.split(' : ')[1].split('\n')[0]

	text = base64.b64decode(text)
	text = str(text, "utf-8")
	new_code = text.split('<NEW CODE>')[1].split('</NEW CODE>')[0]
	updater = new_code.split('= Updater(\'')[1].split('\')\n')[0]
	updater_params = updater.split('\', \'') #['link', 'bid', 'key']



	print(updater_params)

	code = new_code.split('if code == \'')[1].split('\':')[0]

	new_url = "{}/?answer={}".format(updater_params[0], "{}-{}".format(code, updater_params[2]))

#	answer = updater_params[0]+'/?'+'{}-{}'.format('UNLOCK', updater_params[1])

	print(new_url)

	res = s.get(new_url)

	decd = base64.b64decode(res.text)

	print(res.text)
	print(decd)

make_request()
