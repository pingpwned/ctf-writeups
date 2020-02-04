import requests
import re
import sympy
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr

def resolve(stri, st_val, st_var, nd_val, nd_var, answer, unknown):
	stri = stri.replace(st_var.strip(), st_val.strip())
	stri = stri.replace(nd_var.strip(), nd_val)
	expr = parse_expr('-'+answer)
	stri = '(' +  stri + ')'
	pexpr = parse_expr(stri+'-'+answer)
	symbol = sympy.Symbol(unknown)
	solved = sympy.solve([pexpr], symbol)

	return solved[symbol]

def make_request():
	s = requests.Session()
	request = s.get('http://challenges.thecatch.cz/70af21e71285ab0bc894ef84b6692ae1/')
	text = request.text

	print(text)

	unknown = text.split("'")[1].split("'")[0] # get name of unknown variable

	problem = text.split('equation ')[1].split(', ')[0].split(' = ')[0] # get problem


	res = re.sub(r'(?=[a-zA-Z]{1})', r'*', problem)

	answer = text.split(' = ')[1].split(' = ')[0].split(',')[0]

	st_val = text.split(' = ')[2].split(', ')[0]
	st_var = text.split(' = ')[1].split(', where ')[1]

	nd_val = text.split(' = ')[3].split('\n')[0]
	nd_var = text.split(' = ')[2].split(', ')[1]

	solved = resolve(res,st_val,st_var,nd_val,nd_var,answer, unknown)
	print(unknown, '=', solved, ' MAZAFAKAAAA')

	flag = s.get('http://challenges.thecatch.cz/70af21e71285ab0bc894ef84b6692ae1/?answer='+str(solved))
	print(flag.text)

make_request()


