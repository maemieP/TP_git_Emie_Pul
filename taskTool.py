task = {}
def ajouterTache(tache, description) :
	task[tache] = description 


def suprimerTache(tache) :
	if tache in task :
		del task[tache]
	else:
		print ("cette tache n'existe pas")

def marquerFin(tache) :
	if tache in task :
		task[tache] = task[tache] + "finish"
	else :
		print ("cette tache n'existe pas")

