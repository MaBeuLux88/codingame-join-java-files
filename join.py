"""
Script permettant de mettre bout à bout des fichiers source java

Utilisation :
"join.py [ {fichiers} destination ]"

	fichiers : liste de fichiers, si non vide alors utilisée

	destination : fichier de destination (avec extension java)

exemples :
	"join.py"
	"join.py fichier1.java fichier2.java res.java"

Installation :
	A placer dans le dossier contenant le dossier <srcFolder>

-------------
Date de création : 13/11/2014
Auteur : Yann ROLLAND / TidyMaze
Mise à jour : Maxime BEUGNET / Polux

"""

import sys
import os

print(os.getcwd())

prefixImport = 'import '
prefixPackage = 'package '
srcFolder = 'src/main/java/fr/polux'
dstName = 'Player.java'
suffixSrc = '.java'

tabPaths = []

if len(sys.argv) == 1:
	pathDest = dstName
	for fileName in os.listdir(srcFolder):
		if fileName.endswith(suffixSrc):
			tabPaths.append(os.path.join(srcFolder,fileName))
elif len(sys.argv) >= 3:
	tabPaths = sys.argv[1:-1]
	pathDest = sys.argv[len(sys.argv)-1]
else:
	print('invalid parameters, check source for explanations')
	input('end')
	os.exit()


print("files : ", str(tabPaths))

fDest = open(pathDest, 'w+')

print('destination :', fDest.name)

tabImport = []
tabCode = []

# met le contenu des fichiers dans le tableau 
for path in tabPaths:
	print('processing ', path)
	f = open(path,'r')

	# pour chaque ligne : enregitrer ou passer
	for ligne in f:
		if ligne.startswith(prefixImport):
			if ligne not in tabImport:
				tabImport.append(ligne)
		elif ligne.startswith(prefixPackage):
			continue
		else:
			tabCode.append(ligne)

	f.close()

# recopie des imports
for ligne in tabImport:
	fDest.write(ligne)

# recopie des lignes de code
for ligne in tabCode:
	fDest.write(ligne)

# fini
fDest.close()

print("Done !")

