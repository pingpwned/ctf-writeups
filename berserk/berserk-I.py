import requests

def make_request():
#	boo = true
#	url = http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/answer=01010101
#	while(bool):
	s = requests.Session()
	request = s.get('http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/')
	#s = requests.Session()
	text = request.text
	split_request = text.split('[')[1].split(']')[0]
	dict = split_request.split(',')
	print(dict)

	acc = ' mineral oil electric engine  fast CPU large hard drive drone swarm artificial intelligence automatic transmission resistor 10 Ohm'

	for index, item in enumerate(dict):
		find = acc.find(item)
		if find == -1: # not found
			dict[index] = '0'
		else:
			dict[index] = '1'
	answer = ''.join(dict)

	url = 'http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/' + '?answer=' + answer

	print(url)

	captcha = s.get(url)

	print(captcha.text)

make_request()
