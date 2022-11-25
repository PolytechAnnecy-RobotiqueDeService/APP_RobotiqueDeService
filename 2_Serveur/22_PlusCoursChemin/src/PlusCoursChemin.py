import math
from PIL import Image, ImageDraw
HistoriqueTOTAL=[] #garde en memoire tout les point meme les ereuure
HistoriqueDesPoint =[] #garde que les point important
ListePoint = [[3,5],[4,5],[4,7],[7,5],[8,5],[7,6],[12,5],[12,6],[11,6],[17,5],[18,6],[15,12],[18,12],[20,13],[20,14],[20,17],[20,21],[21,26],[25,26],[27,26],[26,29],[28,29],[28,31],[28,34],[28,36],[28,37],[28,39],[28,42],[32,26],[36,26],[39,26],[40,26],[39,28],[38,30],[39,30],[39,33],[39,36],[39,39],[39,42],[26,6],[27,6],[28,6],[29,6],[33,6]]
ListeLiaision = [[[3,5],[4,5]], #deffinistion des liaison
                [[3,5],[4,7]],
                [[4,7],[4,5]],
                [[4,5],[7,5]],
                [[4,5],[7,6]],
                [[7,5],[7,6]],
                [[7,5],[8,5]],
                [[8,5],[12,5]],
                [[7,6],[11,6]],
                [[12,6],[18,6]],
                [[26,29],[28,29]],
                [[38,30],[39,30]],
                [[7,6],[8,5]],
                [[8,5],[11,6]],
                [[11,6],[12,5]],
                [[11,6],[12,6]],
                [[12,5],[17,5]],
                [[12,6],[17,5]],
                [[17,5],[18,6]],
                [[18,6],[26,6]],
                [[26,6],[27,6]],
                [[27,6],[28,6]],
                [[28,6],[29,6]],
                [[29,6],[33,6]],
                [[18,6],[18,12]],
                [[18,12],[15,12]],
                [[18,12],[20,13]],
                [[20,13],[20,14]],
                [[20,14],[20,17]],
                [[20,17],[20,21]],
                [[20,21],[21,26]],
                [[21,26],[25,26]],
                [[25,26],[27,26]],
                [[27,26],[26,29]],
                [[27,26],[28,29]],
                [[27,26],[31,26]],
                [[31,26],[36,26]],
                [[36,26],[39,26]],
                [[39,26],[40,26]],
                [[39,26],[39,28]],
                [[28,29],[28,30]],
                [[28,30],[28,33]],
                [[28,33],[28,35]],
                [[28,35],[28,36]],
                [[28,36],[28,38]],
                [[28,38],[28,41]],
                [[39,28],[39,30]],
                [[39,28],[38,30]],
                [[39,30],[39,33]],
                [[39,33],[39,36]],
                [[39,36],[39,38]],
                [[39,38],[39,41]],
                ]

def pointVoisin(point): # regarde les point voisin au notre
    res = []
    for i in range(len(ListeLiaision)):
        for j in range (2):
            if (point == ListeLiaision[i][j]):
                res.append(ListeLiaision[i][abs(j-1)])
    #print (res)
    return res

def listeVoisionMoinArriver(listeVoisin, arriver): #enleve la valeur de l'arriver pour calculer la disstance ||PD-PA||
    listeRes = []
    for i in range(len(listeVoisin)):
        listeRes.append([listeVoisin[i][0]-arriver[0],listeVoisin[i][1]-arriver[1]])
    #print (listeRes)
    return listeRes
    

def CalculePlusProche(listeVoisin, arriver, depart): #calcule la distance entre le poind de depart et le point d'arriver et choisis le point le plus proche
    minDistance = 10000
    co = [-100,-100]
    liV = listeVoisin
    
    listeVoisinArriver = listeVoisionMoinArriver(liV, arriver)
    for i in range(len(listeVoisinArriver)):
        distancePointDepart = [listeVoisin[i][0]-depart[0],listeVoisin[i][1]-depart[1]]
        actuelle = (math.sqrt(listeVoisinArriver[i][0]**2 + listeVoisinArriver[i][1]**2))+(math.sqrt(distancePointDepart[0]**2 + distancePointDepart[1]**2))
        if (actuelle <= minDistance):
            minDistance = actuelle
            co = listeVoisin[i]
    print("co : ", co)
    print("distance : ", minDistance)
    return co

#[[point,nbVoision,nb voisin qui reste,HistoriqueDesPoint], [....], ]
def historiqueAdd (point): # ajoute dans l'historique le point actuelle et ses voisin par le quel on est pas encore passer
    pointVoisinActuelle = pointVoisin(point)
    CoPointDavans = len(HistoriqueDesPoint)-1
    if (CoPointDavans != -1):
        PointAvans = HistoriqueDesPoint[CoPointDavans][0]
        ListPointVoisinAvans = HistoriqueDesPoint[CoPointDavans][2]
    
        if (PointAvans in pointVoisinActuelle) : # revove les point par les quel on est deja passer
            pointVoisinActuelle.remove(PointAvans)
        if (point in ListPointVoisinAvans) :
            ListPointVoisinAvans.remove(point)
            HistoriqueDesPoint[CoPointDavans][1] = len(ListPointVoisinAvans)
        
    res = [point, len(pointVoisinActuelle), pointVoisinActuelle]
    HistoriqueTOTAL.append(point)
    HistoriqueDesPoint.append(res)

def historiqueAddReturnCroisement(point):
    #Je suprime tout les donne entre le point nouveaux point et le cus de sac
    while (HistoriqueDesPoint[-1][0] != point):
            HistoriqueDesPoint.pop()
            print("pop")
            
    

def resultat(): # revoie que le chemin
    res=[]
    for i in range(len(HistoriqueDesPoint)):
        res.append(HistoriqueDesPoint[i][0])
    return res


def pointInHisto(point): # renvoie les point voisin si il sont dans l'historique
    for i in range (len(HistoriqueDesPoint)):
        if (HistoriqueDesPoint[i][0] == point):
            return HistoriqueDesPoint[i][2]
    return -1

def findCroisement(): # recherche le croisement le plus proche (par le quel on est deja passer)
    for i in range(len(HistoriqueDesPoint)):
        emplacement = len(HistoriqueDesPoint)-1-i #commance par la fin
        if (HistoriqueDesPoint[emplacement][1] != 0):
            return HistoriqueDesPoint[emplacement][0]
    print("EREREUR Aucun croisement trouver")
    return -1
            
        

def PlusCours(depart, arriver): #code general
    nbCycle=0
    historiqueAdd(depart)
    while ((depart != arriver) and (nbCycle < 100)):
        nbCycle += 1
        #print(nbCycle)
        if (pointInHisto(depart) != -1): #donne la liste des point dans l'historique si elle existe sinon la cree
            ptV = pointInHisto(depart)
        else:
            ptV =  pointVoisin(depart)
        
        NextPoint = CalculePlusProche(ptV,arriver,depart)
        if (NextPoint[0] == -100): # detecte les cus de sac
            if (findCroisement() != -1):
                NextPoint = findCroisement()
                HistoriqueTOTAL.append(["Return to ", NextPoint])
                historiqueAddReturnCroisement(NextPoint)
            else:
                nbCycle = 101
        else :
            historiqueAdd(NextPoint)
        depart = NextPoint
    print(resultat())
    print(HistoriqueTOTAL)
    
        
 #***************************      
PlusCours([7, 6],[36, 26])
#****************************

listePoint = resultat()
image = Image.open("../image/plan.png")

# Obtention du contexte graphique
draw = ImageDraw.Draw(image)

RED = (255, 0, 0, 0)
for i in range(len(listePoint)-1):
    coPt1 =[(listePoint[i][0]+2)*11-6,(listePoint[i][1]+1)*11-6]
    coPt2 =[(listePoint[i+1][0]+2)*11-6,(listePoint[i+1][1]+1)*11-6]
    draw.line((coPt1[0], coPt1[1], coPt2[0], coPt2[1]),fill=RED,width=3)


image.show()
image.save("../image/resultatDuChemin.png", "png")
                 
