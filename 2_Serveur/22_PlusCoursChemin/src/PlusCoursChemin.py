import math
from PIL import Image, ImageDraw
HistoriqueTOTAL=[] #garde en memoire tout les point meme les ereuure
HistoriqueDesPoint =[] #garde que les point important
ListePoint2eme = [[3,5],[22,25],[19,6],[4,5],[4,7],[7,5],[8,5],[7,6],[12,5],[12,6],[11,6],[17,5],[18,6],[15,12],[18,12],[20,13],[20,14],[20,17],[20,21],[21,26],[25,26],[27,26],[26,29],[28,29],[28,30],[28,33],[28,35],[28,36],[28,38],[28,41],[32,26],[36,26],[39,26],[40,26],[39,28],[38,30],[39,30],[39,33],[39,36],[39,38],[39,41],[26,6],[27,6],[28,6],[29,6],[33,6]]
ListePoint1er = [[25,18],[26,15],[5,9],[7,9],[7,11],[12,9],[11,10],[16,9],[15,10],[20,9],[25,9],[30,9],[30,10],[36,9],[36,10],[41,9],[43,10],[46,9],[48,10],[25,17],[20,17],[20,30],[27,20],[27,21],[27,25],[27,32],[28,35],[36,35],[37,35],[37,40],[37,44],[37,47],[37,50],[37,54],[42,35],[43,36],[44,36],[46,35],[48,35],[51,35],[51,40],[51,44],[51,47],[51,51],[51,54]]
ListeLiaision2eme = [[[3,5],[4,5]], #deffinistion des liaison
                [[3,5],[4,7]],
                [[19,6],[18,6]],
                [[22,25],[21,26]],
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
                [[39,38],[39,41]]
                ]
ListeLiaision1er = [[[5,9],[7,9]],
                    [[25,18],[25,17]],
                    [[26,15],[24,17]],
                    [[5,9],[7,11]],
                    [[7,9],[7,11]],
                    [[7,9],[12,9]],
                    [[7,9],[11,10]],
                    [[12,9],[11,10]],
                    [[12,9],[16,9]],
                    [[12,9],[15,10]],
                    [[16,9],[20,9]],
                    [[20,9],[25,9]],
                    [[25,9],[30,9]],
                    [[30,9],[30,10]],
                    [[30,9],[36,9]],
                    [[36,9],[36,10]],
                    [[36,9],[41,9]],
                    [[41,9],[43,10]],
                    [[43,10],[46,9]],
                    [[46,9],[48,10]],
                    [[25,9],[25,17]],
                    [[25,17],[20,17]],
                    [[20,17],[20,30]],
                    [[25,17],[27,20]],
                    [[27,20],[27,21]],
                    [[27,21],[27,25]],
                    [[27,25],[27,32]],
                    [[27,32],[28,35]],
                    [[28,35],[36,35]],
                    [[36,35],[37,35]],
                    [[37,35],[42,35]],
                    [[42,35],[43,36]],
                    [[43,36],[44,36]],
                    [[42,35],[46,35]],
                    [[44,36],[46,35]],
                    [[46,35],[48,35]],
                    [[48,35],[51,35]],
                    [[51,35],[51,40]],
                    [[51,40],[51,44]],
                    [[51,44],[51,47]],
                    [[51,47],[51,51]],
                    [[51,51],[51,54]],
                    [[37,35],[37,40]],
                    [[37,40],[37,44]],
                    [[37,44],[37,47]],
                    [[37,47],[37,50]],
                    [[37,50],[37,54]],
                    ]

Urlplant2eme = "../image/plan.png"
Urlplant1er = "../image/plan1er.png"


#Dictionaire raport salle co
dicSalleCo = {
        "C206":[3,5],
        "C207":[4,5],
        "C205":[4,7],
        "C208":[8,5],
        "C204":[7,6],
        "C209":[12,5],
        "C203":[11,6],
        "C210":[17,5],
        "C219":[20,7],
        "C213":[26,6],
        "C214":[27,6],
        "C218":[28,6],
        "C217":[29,6],
        "C215":[33,6],
        "C216":[33,6],
        "C202":[15,12],
        "B202":[20,13],
        "B203":[20,14],
        "B204":[20,17],
        "B205_polybot":[20,21],
        "A202":[25,26],
        "A230":[26,29],
        "A220":[28,29],
        "A204":[36,26],
        "A205":[40,26],
        "A206":[39,28],
        "A216":[38,30],
        "A207":[39,30],
        "A229":[28,30],
        "A221":[28,30],
        "A215":[39,33],
        "A208":[39,33],
        "A228":[28,33],
        "A227":[28,35],
        "A214":[39,36],
        "A209":[39,36],
        "A222":[28,36],
        "A226":[28,38],
        "A223":[28,38],
        "A213":[39,38],
        "A210":[39,38],
        "A225":[28,41],
        "A224":[28,41],
        "A212":[39,41],
        "A211":[39,41],
        "C2Escalier":[19,6],
        "A2Escalier":[22,25]
        }

dicSalleCo1er = {
        "C107":[5,9],
        "C108":[7,9],
        "C105":[7,11],
        "C104":[11,10],
        "C109":[12,9],
        "C103":[15,10],
        "C110":[16,9],
        "C111":[20,9],
        "C102":[20,17],
        "C114":[30,9],
        "C122":[30,10],
        "C115":[36,9],
        "C121":[36,10],
        "C116":[41,9],
        "C120":[43,10],
        "C117":[46,9],
        "C119":[48,10],
        "B120":[20,30],
        "B102":[27,20],
        "B103":[27,21],
        "B104":[27,25],
        "B105":[27,32],
        "B106":[28,35],
        "A102":[36,35],
        "A103":[37,35],
        "A104":[42,35],
        "A105":[46,35],
        "A106":[48,35],
        "A123":[43,36],
        "A122":[44,36],
        "A134":[37,40],
        "A126":[37,40],
        "A119":[51,40],
        "A110":[51,40],
        "A133":[37,44],
        "A118":[51,44],
        "A111":[51,44],
        "A132":[37,47],
        "A127":[37,47],
        "A117":[51,47],
        "A112":[51,47],
        "A131":[37,50],
        "A128":[37,50],
        "A116":[51,51],
        "A113":[51,51],
        "A130":[37,54],
        "A129":[37,54],
        "A115":[51,54],
        "A114":[51,54]
        }

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
        actuelle = (math.sqrt(listeVoisinArriver[i][0]**2 + listeVoisinArriver[i][1]**2))#+(math.sqrt(distancePointDepart[0]**2 + distancePointDepart[1]**2))
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
            
def GenereImage(resultat):
    
    listePoint = resultat
    image = Image.open(Urlplant)

    # Obtention du contexte graphique
    draw = ImageDraw.Draw(image)

    RED = (255, 0, 0, 0)
    for i in range(len(listePoint)-1):
        coPt1 =[(listePoint[i][0]+2)*11-6,(listePoint[i][1]+1)*11-6]
        coPt2 =[(listePoint[i+1][0]+2)*11-6,(listePoint[i+1][1]+1)*11-6]
        draw.line((coPt1[0], coPt1[1], coPt2[0], coPt2[1]),fill=RED,width=3)

    image.show()
    image.save("../image/resultatDuChemin.png", "png")
                 
      
def Inisiatlisation(etage): # set les bonne donner
    global Urlplant
    global ListeLiaision
    global ListePoint
    if (etage == 1):
        ListeLiaision = ListeLiaision1er
        ListePoint = ListePoint1er
        Urlplant = Urlplant1er
    else :
        ListeLiaision = ListeLiaision2eme
        ListePoint = ListePoint2eme
        Urlplant = Urlplant2eme
    

def PlusCours(depart, arriver, etage):#code general
    Inisiatlisation(etage)
    if (type(depart) == str):
        depart = dicSalleCo[depart]
        arriver = dicSalleCo[arriver]
        print(depart, arriver)
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
    GenereImage(resultat())
    print(resultat())
    print(HistoriqueTOTAL)
    
        
 #***************************      

PlusCours("A222","C204",2)
#PlusCours([51, 54],[27, 32],1)
#****************************
