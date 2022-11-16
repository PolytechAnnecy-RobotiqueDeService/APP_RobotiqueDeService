# coding: utf-8




def RenvoieListeQuestion():
    EnUneChaine = ''
    tabLinge =[]
    with open("reponce.txt", "r") as f:
        tabLinge = f.readlines()
    #print(tabLinge)
    f.close()
    
    ListeQuestion = []
    
    for i in range (len(tabLinge)):
        #print (tabLinge[i][0])
        if (tabLinge[i][0]=='$'):
            for j in range(len(tabLinge[i].split('$'))):
                if (tabLinge[i].split('$')[j] != ''):
                    ListeQuestion.append(tabLinge[i].split('$')[j])
            
            
    for i in range (len(ListeQuestion)):
        ListeQuestion[i] = ListeQuestion[i].replace('\n', '')
        EnUneChaine = EnUneChaine+ListeQuestion[i]+';'
    print(ListeQuestion)
    print(EnUneChaine)

def findInFile(word):
    ReponceAction=[]
    NumLigne=-1
    with open("reponce.txt", "r") as f:
        # read all lines in a list
        lines = f.readlines()
        f.close()
        word = '$'+ word
        for line in lines:
            if line.find(word) != -1:
                #print('Line Number:', lines.index(line))
                NumLigne = lines.index(line)
                #print('Line:', line)
    ReponceAction.append(lines[NumLigne+1])
    ReponceAction.append(lines[NumLigne+2])
    ReponceAction[0] = ReponceAction[0].replace('$', '')
    ReponceAction[0] = ReponceAction[0].replace('\n', '')
    ReponceAction[1] = ReponceAction[1].replace('$', '')
    ReponceAction[1] = ReponceAction[1].replace('\n', '')
    print(ReponceAction)
    return ReponceAction
                
    
def selectionneLeBon(num, liste):
    return liste[num]
    
    
#print(selectionneLeBon(1,findInFile('Ou est la salle de math')))
#findInFile('Bonjour')

RenvoieListeQuestion()