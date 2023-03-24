import math
from PIL import Image, ImageDraw
import base64
import requests
import qrcode

HistoriqueTOTAL=[] #garde en memoire tout les point meme les ereuure
HistoriqueDesPoint =[] #garde que les point important

ListePoint2eme = [[21,21],[22,26],[19,6],[4,6],[4,7],[8,6],[7,6],[12,6],[11,6],[17,6],[18,6],[15,12],[18,12],[20,12],[20,14],[20,17],[20,21],[21,26],[25,26],[28,26],[26,29],[28,29],[28,30],[28,33],[28,35],[28,36],[28,38],[28,41],[32,26],[36,26],[39,26],[40,26],[39,28],[39,30],[39,33],[39,36],[39,38],[39,41],[26,6],[27,6],[28,6],[29,6],[33,6]]
ListePoint1er = [[31,35],[27,17],[25,18],[25,15],[5,9],[7,9],[7,11],[12,9],[11,9],[16,9],[15,9],[20,9],[25,9],[30,9],[36,9],[41,9],[43,9],[46,9],[48,9],[25,17],[20,17],[20,30],[27,20],[27,21],[27,25],[27,29],[27,35],[36,35],[37,35],[37,40],[37,44],[37,47],[37,50],[37,54],[42,35],[43,35],[44,35],[46,35],[48,35],[51,35],[51,40],[51,44],[51,47],[51,51],[51,54]]
ListeLiaision2eme = [ #deffinistion des liaison
                [[19,6],[18,6]],
                [[22,26],[21,26]],
                [[4,7],[4,6]],
                [[4,6],[7,6]],
                [[26,29],[28,29]],
                [[7,6],[8,6]],
                [[8,6],[11,6]],
                [[11,6],[12,6]],
                [[12,6],[17,6]],
                [[17,6],[18,6]],
                [[18,6],[26,6]],
                [[26,6],[27,6]],
                [[27,6],[28,6]],
                [[28,6],[29,6]],
                [[29,6],[33,6]],
                [[18,6],[18,12]],
                [[18,12],[15,12]],
                [[18,12],[20,12]],
                [[20,12],[20,14]],
                [[20,14],[20,17]],
                [[20,17],[20,21]],
                [[20,21],[21,21]],
                [[21,21],[21,26]],
                [[22,26],[25,26]],
                [[25,26],[28,26]],
                [[28,26],[28,29]],
                [[28,26],[32,26]],
                [[32,26],[36,26]],
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
                [[39,30],[39,33]],
                [[39,33],[39,36]],
                [[39,36],[39,38]],
                [[39,38],[39,41]]
                ]

ListeLiaision1er = [[[5,9],[7,9]],
                    [[15,9],[16,9]],
                    [[27,17],[27,20]],
                    [[27,17],[25,17]],
                    [[25,18],[25,17]],
                    [[25,15],[25,17]],
                    [[7,9],[7,11]],
                    [[7,9],[11,9]],
                    [[12,9],[11,9]],
                    [[12,9],[15,9]],
                    [[16,9],[20,9]],
                    [[20,9],[25,9]],
                    [[25,9],[30,9]],
                    [[30,9],[36,9]],
                    [[36,9],[41,9]],
                    [[41,9],[43,9]],
                    [[43,9],[46,9]],
                    [[46,9],[48,9]],
                    [[25,9],[25,15]],
                    [[25,17],[20,17]],
                    [[20,17],[20,30]],
                    [[27,20],[27,21]],
                    [[27,21],[27,25]],
                    [[27,25],[27,29]],
                    [[27,29],[27,35]],
                    [[27,35],[31,35]],
                    [[31,35],[36,35]],
                    [[36,35],[37,35]],
                    [[37,35],[42,35]],
                    [[42,35],[43,35]],
                    [[43,35],[44,35]],
                    [[44,35],[46,35]],
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
dicSalleCo2eme = {
        "C206":[4,6],
        "C207":[4,6],
        "C205":[4,7],
        "C208":[8,5],
        "C204":[7,6],
        "C209":[12,6],
        "C203":[11,6],
        "C210":[17,6],
        "C219":[20,7],
        "C213":[26,6],
        "C214":[27,6],
        "C218":[28,6],
        "C217":[29,6],
        "C215":[33,6],
        "C216":[33,6],
        "C202":[15,12],
        "B202":[20,12],
        "B203":[20,14],
        "B204":[20,17],
        "B205_polybot":[20,21],
        "A202":[25,26],
        "A230":[26,29],
        "A220":[28,29],
        "A204":[36,26],
        "A203":[32,26],
        "A205":[40,26],
        "A206":[39,28],
        "A216":[39,30],
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
        "A2Escalier":[22,26]
        }

dicSalleCo1er = {
        "C107":[5,9],
        "C108":[7,9],
        "C105":[7,11],
        "C104":[11,9],
        "C109":[12,9],
        "C103":[15,9],
        "C110":[16,9],
        "C111":[20,9],
        "C102":[20,17],
        "C114":[30,9],
        "C122":[30,9],
        "C115":[36,9],
        "C121":[36,9],
        "C116":[41,9],
        "C120":[43,9],
        "C117":[46,9],
        "C119":[48,9],
        "B120":[20,30],
        "B102":[27,20],
        "B103":[27,21],
        "B104":[27,25],
        "B105":[27,29],
        "B106":[27,35],
        "A102":[36,35],
        "A103":[37,35],
        "A104":[42,35],
        "A105":[46,35],
        "A106":[48,35],
        "A123":[43,35],
        "A122":[44,35],
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
        "A114":[51,54],
        "C1Escalier":[25,15],
        "A1Escalier":[31,35]
        }

listEsca2 = [[19,6],[22,26]]
listEsca1 = [[25,15],[31,35]]

listEsca2Nom = ["C2Escalier","A2Escalier"]
listEsca1Nom = ["C1Escalier","A1Escalier"]

def findEscalier(depart):
    if (depart[1] == '2'):
        listEsca = listEsca2
        listEscaNom = listEsca2Nom
        depart = dicSalleCo2eme[depart]
    else :
        listEsca = listEsca1
        listEscaNom = listEsca1Nom
        depart = dicSalleCo1er[depart]
    
    if (math.sqrt((depart[0]-listEsca[0][0])**2 + (depart[1]-listEsca[0][1])**2) >= math.sqrt((depart[0]-listEsca[1][0])**2 + (depart[1]-listEsca[1][1])**2)):
        return listEscaNom[1]
    else :
        return listEscaNom[0]
    
def changementEtage(nom): # envois le bas ou le haut de l'escalier emprinter
    if listEsca2Nom[0] == nom:
        return listEsca1Nom[0]
    
    elif listEsca2Nom[1] == nom:
        return listEsca1Nom[1]
    
    elif listEsca1Nom[0] == nom:
        return listEsca2Nom[0]
    
    elif listEsca1Nom[1] == nom:
        return listEsca2Nom[1]
    

def quelEtage(depart, arriver):
    if (depart[1] == '2'):
        res = 2
    else :
        res = 1
    if (arriver[1] != str(res)):
        res = 3
    return res


def pointVoisin(point): # regarde les point voisin au notre
    res = []
    for i in range(len(ListeLiaision)):
        for j in range (2):
            if (point == ListeLiaision[i][j]):
                res.append(ListeLiaision[i][abs(j-1)])
    return res

def listeVoisionMoinArriver(listeVoisin, arriver): #enleve la valeur de l'arriver pour calculer la disstance ||PD-PA||
    listeRes = []
    for i in range(len(listeVoisin)):
        listeRes.append([listeVoisin[i][0]-arriver[0],listeVoisin[i][1]-arriver[1]])
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

    image.save("../image/resultatDuChemin.png", "png")
                 
      
def Inisiatlisation(etage): # set les bonne donner
    global Urlplant
    global ListeLiaision
    global ListePoint
    global dicSalleCo
    if (etage == 1):
        ListeLiaision = ListeLiaision1er
        ListePoint = ListePoint1er
        Urlplant = Urlplant1er
        dicSalleCo = dicSalleCo1er
    else :
        ListeLiaision = ListeLiaision2eme
        ListePoint = ListePoint2eme
        Urlplant = Urlplant2eme
        dicSalleCo = dicSalleCo2eme
    

def PlusCours(depart, arriver):#code general
    etage = quelEtage(arriver, depart)
    
    if (etage != 3) : #3 sinifie que il y a un changement d'etage
        Inisiatlisation(etage)
        if (type(depart) == str):
            depart = dicSalleCo[depart]
            arriver = dicSalleCo[arriver]
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
        res = resultat()
        GenereImage(res)
        return res
    else :
        
        
        PlusCours(depart, findEscalier(depart))
        SaveResForDeuxEtage = Image.open("../image/resultatDuChemin.png")
        image1 = SaveResForDeuxEtage.copy()
        image1.save("../image/SaveResForDeuxEtage.png")
        
        depart = changementEtage(findEscalier(depart))
        
        HistoriqueTOTAL.clear()
        HistoriqueDesPoint.clear()
        
        PlusCours(depart, arriver)
        
        
        image2 = Image.open("../image/resultatDuChemin.png")
        # Créez une nouvelle image avec une taille suffisamment grande pour les deux images originales
        largeur_max = max(image1.width, image2.width)
        hauteur_totale = image1.height + image2.height
        nouvelle_image = Image.new("RGBA", (largeur_max, hauteur_totale))
        
        # Collez les deux images d'origine sur la nouvelle image
        nouvelle_image.paste(image1, (0, 0))
        nouvelle_image.paste(image2, (0, image1.height))
        
        # Enregistrez la nouvelle image
        nouvelle_image.save("../image/resultatDuChemin.png")
        
    
        
 #***************************      
f = open('../ficherTXT/Commande.txt','r')
tab = f.readlines()
depart = tab[0].replace("\n","")
arriver = tab[1].replace("\n","")
f.close()

tab = PlusCours(depart,arriver)

#bug :


#****************************

#qrCode
key_imgbb = "4f555dcb35f435943be57971b27ab3af"
with open("../image/resultatDuChemin.png", "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": key_imgbb,
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)
res = res.json()
url = res['data']["url"]

img = qrcode.make(url)
type(img)  # qrcode.image.pil.PilImage
img.save("../image/QRcode.png")


etage = quelEtage(depart, arriver)


def ligne(tab):
    pointFinal = tab[-1]
    #print(pointFinal)
    i = 0
    stop = 0
    while stop == 0:
        #print("stop entre ", stop)
        
        tab2=[]
        tab2.append(tab[i])
        tab2.append(tab[i+1])
        tab2.append(tab[i+2])
        #print(tab2)
        
        if(tab2[0][0] == tab2[2][0] and tab2[1] != [27,29]):
            if (len(tab2[1]) == 2):
                tab.remove(tab2[1])
                i=len(ligne(tab))-3
            
        elif(tab2[0][1] == tab2[2][1] and tab2[1] != [27,29]):
            if (len(tab2[1]) == 2):
                tab.remove(tab2[1])
                #print('remove1')
            
                i=len(ligne(tab))-3
        i+=1
        if (pointFinal == tab[i+1]):
            #print('in')
            stop = 1
            
            #print(stop)
    return tab
 
    
        
tailleCareau2eme = 1.63
tailleCareau1er = 1.29
tailleCareau = tailleCareau2eme  
    
croisementEtage2 = [[18,6],[39,26],[28,26],[18,12]]
croisementEtage1 = [[25,9],[25,17],[51,35],[28,35],[37,35]]

def croisement(tab) :
    if (etage == 1):
        tabCroisement = croisementEtage1
    else:
        tabCroisement = croisementEtage2
    
    for i in range(len(tabCroisement)):
        for j in range(len(tab)):
            if (tab[j] == tabCroisement[i]):
                tab[j].append("croisement")
    return tab

def removeCroisementManual(tab): # remove le croisement
    comp = 0
    tabOrdreArriver = []
    if (len(tab)>2):
        for i in tab :   

            if (i == [25,26] or i == [32,26]):
                tabOrdreArriver.append(i)
                comp += 1
                #print (comp)
                #print(tabOrdreArriver)
                
        if (comp == 2 and tabOrdreArriver == [[32,26],[25,26]]):
            tab.remove([27,26])
    return tab


def creationListeSection(tab):
    tabCroisement = []
    for i in range (len(tab)-1):
        tabTempo = [tab[i],tab[i+1]]
        tabCroisement.append(tabTempo)
    return tabCroisement
        

def mur(tabCroisement) : #On commance a set les section qui regarderon la cordoer de la section qui change est si elle augement ou diminue.
    for i in range(len(tabCroisement)-1):
        section1 = tabCroisement[i]
        section2 = tabCroisement[i+1]
        
        if (section1[0][0] == section1[1][0]):
            if (section1[0][1] > section1[1][1]):
                section1Variation = 0  #0 sinifie un - et 1 un +
            else:
                section1Variation = 1
            
            if (section2[0][0] == section2[1][0]):
                if (section2[0][1] > section2[1][1]):
                    section2Variation = 0  #0 sinifie un - et 1 un +
                else:
                    section2Variation = 1
            else :
                if (section2[0][0] > section2[1][0]):
                    section2Variation = 0  #0 sinifie un - et 1 un +
                else :
                    section2Variation = 1
# =============================================================================
# table de veriter en fonction de si la coordoner changante d'une section augement ou diminue
#   0   1   Mur       
# | + | - || D  |
# | - | - || G  |
# | + | + || G  |
# | - | + || D  |  on remarque que si on fais l'adition de la section 0 + 1 = 1 sinifie que on doit suivre le mur de Gauche
# =============================================================================

            if (section1Variation + section2Variation == 1):
                tabCroisement[i].append("droite")
            else:
                tabCroisement[i].append("gauche")
            

                
        else :
            if (section1[0][0] > section1[1][0]):
                section1Variation = 0  #0 sinifie un - et 1 un +
            else :
                section1Variation = 1
                
            if (section2[0][0] == section2[1][0]):
                if (section2[0][1] > section2[1][1]):
                    section2Variation = 0  #0 sinifie un - et 1 un +
                else:
                    section2Variation = 1
            else :
                if (section2[0][0] > section2[1][0]):
                    section2Variation = 0  #0 sinifie un - et 1 un +
                else :
                    section2Variation = 1
                
                
# =============================================================================
# table de veriter en fonction de si la coordoner changante d'une section augement ou diminue
#   0   1   Mur       
# | + | - || G  |
# | - | - || D  |
# | + | + || D  |
# | - | + || G  |  on remarque que si on fais l'adition de la section 0 + 1 = 1 sinifie que on doit suivre le mur de Gauche
# =============================================================================
            if (section1Variation + section2Variation == 1):
                tabCroisement[i].append("gauche")
            else:
                tabCroisement[i].append("droite")
                    
        
        
    tabCroisement[-1].append("droite")
    return tabCroisement

def nombreDeCarreau(tab):
    for i in range(len(tab)) :
        if (tab[i][0][0] != tab[i][1][0]):
            tab[i].append("{:.2f}".format(abs(tab[i][0][0] - tab[i][1][0])*tailleCareau))
        else:
            tab[i].append("{:.2f}".format(abs(tab[i][0][1] - tab[i][1][1])*tailleCareau))
            
    return tab


def casParticulier(tab):
    for i in range (len(tab)):
        tab[i].append(1)
        if (etage == 2):
            if (tab[i][0] == [20, 21] and tab[i][1] == [21, 21]) or (tab[i][0] == [21, 21] and tab[i][1] == [20, 21]):
                tab[i][-1] = 0
            
            if (tab[i][1] == [28, 26, 'croisement']):
                tab[i][-2] = "gauche"
                tab[i][-1] = 0
                tab[i][1][0] = 30
                
            if (tab[i][0] == [28, 26, 'croisement']):
                tab[i][0][0] = 30 
                
        if (etage == 1):
            if ((tab[i][0] == [27, 29] and tab[i][1] == [27, 35]) or (tab[i][1] == [27, 29] and tab[i][0] == [27, 35])):
                tab[i][-1] = 2 # sinifie le cas ou on ne doit pas suivre de mure et aller tout droit sur la distce.
               
            #le croisement chaint    
            
            if (tab[i][1] == [37, 35, 'croisement']):
                tab[i][-2] = "gauche"
                tab[i][-1] = 0
                tab[i][1][0] = 40
                
            if (tab[i][0] == [37, 35, 'croisement']):
                tab[i][0][0] = 40 
    tab[-1][-1] = 0
    return tab

def ecritDansFichier(tab):
    f = open("../ficherTXT/DonneeToPepper.txt", "w")
    for i in tab:
        f.write(i[-3])
        f.write("\n")
        f.write(str(i[-1]))
        f.write("\n")
        f.write(str(i[-2]))
        f.write("\n")
        f.write("\n")
    
    f.close()
          

res = ecritDansFichier(nombreDeCarreau(casParticulier(mur(creationListeSection(ligne(croisement(removeCroisementManual(tab))))))))




