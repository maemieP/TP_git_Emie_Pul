import json
def enregistrementJson (data, filename) :
	with open(filename, 'w') as f :
	json.dump(data,f)

monDictionaire = ('key', 'value')
enregistrementJson = (monDictionaire , 'data.json')

