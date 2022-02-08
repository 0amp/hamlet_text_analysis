import requests
from bs4 import BeautifulSoup
import re

hamlet = requests.get('http://shakespeare.mit.edu/hamlet/full.html').text

raw_site = BeautifulSoup(hamlet, 'html.parser')

speech_by_char = {"HORATIO": [],"HAMLET": [],"OPHELIA": [],"KING CLAUDIUS": [],"LORD POLONIUS": [],
                  "LAERTES": [],"QUEEN GERTRUDE": [],"Ghost": [],"PRINCE FORTINBRAS": [],"VOLTIMAND": [],
                  "GUILDENSTERN": [],"ROSENCRANTZ": [],"OSRIC": [],"Captain": [], "BERNARDO": [], 
                  "REYNALDO": [], "CORNELIUS": [], "First Clown": [], "Second Clown": [], "First Priest": [], 
                  "Player King": [], "Player Queen": [], "FRANCISCO": [], "MARCELLUS": [], "LUCIANUS": [], 
                  "Messenger": [], "All": [], "Lord": []}

chars_list = re.compile(r'(\nHORATIO\n|\nHAMLET\n|\nOPHELIA\n|\nKING CLAUDIUS\n|\nLORD POLONIUS\n|\nLAERTES\n|\nQUEEN GERTRUDE\n|\nGhost\n|\nPRINCE FORTINBRAS\n|\nVOLTIMAND\n|\nGUILDENSTERN\n|\nROSENCRANTZ\n|\nOSRIC\n|\nCaptain\n|\nBERNARDO\n|\nREYNALDO\n|\nCORNELIUS\n|\nFirst Clown\n|\nSecond Clown\n|\nFirst Priest\n|\nPlayer King\n|\nPlayer Queen\n|\nFRANCISCO\n|\nMARCELLUS\n|\nLUCIANUS\n|\nMessenger\n|\nAll\n|\nLord\n)')

A = chars_list.split(raw_site.get_text())

for i,text in enumerate(A[2:len(A)/2]): 
  A[i-1] = A[i-1] + A[i]
  A.pop(i)

for text in A[1:]: 
  start = text.index("\n")
  end = text[start+len("\n"):].index("\n") + start

  character = text[start + len("\n"):end+1]

  speech_by_char[character].append(text[end+1:])

speech_data = []

for entry in speech_by_char.keys(): 
  total_words = 0
  
  for t in speech_by_char[entry]: 
    t = t.replace("\n", " ").split(" ")
    t[:] = [x for x in t if x != ("" and " " and ", " and "." and "," and ". ")]
    total_words += len(t)

  speech_data.append([entry, len(speech_by_char[entry]), total_words])
  
  print(entry + ": " + str(len(speech_by_char[entry])) + ", " + str(total_words) + ", " + str(round(total_words / len(speech_by_char[entry]), 2)))

#print(speech_data)