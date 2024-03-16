import json
def enregistrementJson (data, filename) :
	with open(filename, 'w') as f :
	json.dump(data,f)

monDictionaire = ('key', 'value')
enregistrementJson = (monDictionaire , 'data.json')

def chargerJson (filename):
	with open(filename, 'r') as f:
		data = json.load(f)
	return data
