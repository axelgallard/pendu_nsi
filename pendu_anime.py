"""
Programme affichage
"""
import pygame
from random import *
from pygame import mixer



#liste qui contient les mots pouvant être choisi
lst_mot=["bismarck","tirpitz","gneisenau","scharnhorst","prinz eugen","admiral hipper","graf zeppelin","yamato","musashi","shinano","atago","takao","akagi","kaga","shokaku","zuikaku","ayanami","bretagne","dunkerque","algerie","le triomphant","surcouf","enterprise","iowa","dreadnought","king george v","queen elizabeth","prinz heinrich","emden","hidenburg","blucher","ibuki","hood","prince of wales","jean bart","saint louis","ark royal","hermes","perseus","hermione","belfast","atlanta","murmansk","sheffield","pyotr velikiy","bayern","kaiser","konig","konigsberg","terror","terrible","invicible","le malin","mackensen","maille breze","sovetsky soyuz","amagi","admiral graf spee","zara","pola","ammiraglio di saint bon","yukikaze"]
prefixe=["kms","kms","kms","kms","kms","kms","kms","ijn","inj","ijn","ijn","ijn","ijn","ijln","ijn","ijn","ijn","mnf","mnf","mnf","mnf","fnff","uss","uss","hms","hms","hms","sms","sms","sms","kms","ijn","hms","hms","mnf","uss","hms","hms","hms","hms","hms","uss","sn","hms","sn","kms","sms","sms","sms","hms","hms","hms","mnf","sms","mnf","sn","ijn","kms","rn","rn","rn","ijn"]
main_gun=["8 cannons 380mm montés en 4 tourelles","8 cannons 380mm montés en 4 tourelles","9 cannons 280mm montés en 3 tourelles","9 cannons 280mm montés en 3 tourelles","8 cannons 203mm montés en 4 tourelles","8 cannons 203mm montés en 4 tourelles","50 avions (chasseur,bombardier et torpilleur)","9 cannons 460mm montés en 3 tourelles","9 cannons 460mm montés en 3 tourelles","42 avions (5 en réserve)","10 cannons 203mm montés en 5 tourelles","10 cannons 200mm montés en 5 tourelles","60 avions(85 après refonte)","72 avions (90 après renfonte)","72 avions","72 avions","6 cannons 127mm montés en 3 tourelles","10 cannons 340mm montés en 5 tourelles","8 cannons 330mm montés en 2 tourelles","8 cannons 203mm montés en 4 tourelles","5 cannons 138.6mm","2 cannons 203mm montés en 1 tourelle (+12 tubes lance torpilles)","85 avions","9 cannons 407mm montés en 3 tourelles","10 cannons 305mm montés en 5 tourelles","10 cannons 380mm montés en 2 tourelles quadruples et une tourelle double","8 cannons 380mm montés en 4 tourelles","2 cannons 240mm","10 cannons 105mm","8 cannons 305mm montés en 4 tourelles","8 cannons 203mm montés en 4 tourelles","27 avions","8 cannons 381mm montés en 4 tourelles","10 cannons 381mm montés en 2 tourelles quadruples et tourelles double","8 cannons 380mm montés en 2 tourelles","15 cannons 152mm montés en 5 tourelles","60 à 72 avions","28 aéronefs","non armé (a part 25 cannons anti air)","10 cannons 127mm montés en 5 tourelles","12 cannons 152mm montés en 4 tourelles","16 cannons 127mm","10 cannons 152mm montés en 5 tourelles","2 lance missile et un cannon 115mm","20 missiles de croisères anti navire","8 cannons 380mm montés en 4 tourelles","10 cannons 305mm montés en 5 tourelles","10 cannons 305mm montés en 5 tourelles","10 cannons 105mm","2 cannons 381mm montés en 1 tourelles","37 avions","8 cannons 305mm montés en 4 tourelles","5 cannons 138.6mm","8 cannons 350mm montés en 4 tourelles","2 cannons 100m","9 cannons 406mm montés en tourelles de 3","10 cannons 410mm montés en tourelles de 2","6 cannons 280mm montés en 2 tourelles","8 canons 203 mm montés en 3 tourelles","8 canons 203 mm montés en 3 tourelles","4 cannons 254mm montés en 2 cannons","6 cannons 127mm montés en tourelles de 2 "]
classe=["cuirassé","cuirassé","cuirassé","cuirassé","croiseur lourd","croiseur lourd","porte avions","cuirassé","cuirassé","porte avions","croiseur lourd","croiseur lourd","croiseur de bataille converti en porte avions","cuirassé converti enr porte avions","porte avions","porte avions","destroyer","cuirassé","cuirassé","croiseur lourd","destroyer","croiseur sous-marin","porte avions","cuirassé","cuirassé","cuirassé","cuirassé","croiseur cuirassé (ancêtre du croiseur de bataille)","croiseur léger","croiseur lourd","croiseur lourd","croiseur lourd","croiseur de bataille","cuirassé","cuirassé","croiseur léger","porte avions","porte avions","porte avions","croiseur léger","croiseur léger","croiseur léger","croiseur léger","destroyer","cuirassé","cuirassé","cuirassé","cuirassé","croiseur léger","monitor","porte avions","croiseur de bataille","destroyer","croiseur de bataille","destroyer","cuirassé","croiseur de bataille","cuirassé","croiseur lourd","croiseur lourd","cuirassé","destroyer"]

print(len(lst_mot))
print(len(prefixe))
print(len(main_gun))
print(len(classe))


#choisi le mot
choix_mot=randint(0,len(lst_mot)-1)
motATrouver=lst_mot[choix_mot]
#initialise les variable
aide=0
motAChercher=""
nb_chance=0
trouve=False
liste_lettre=","
etat_aide=0
pays=""
if prefixe[choix_mot]=="ijn":
    pays="japonnais"
elif prefixe[choix_mot]=="mnf":
    pays="français"
elif prefixe[choix_mot]=="fnff":
    paus="français"
elif prefixe[choix_mot]=="kms":
    pays="germanique"
elif prefixe[choix_mot]=="sms":
    pays="germanique"
elif prefixe[choix_mot]=="uss":
    pays="américain"
elif prefixe[choix_mot]=="hms":
    pays="britanique"
elif prefixe[choix_mot]=="sn":
    pays="soviétique"
elif prefixe[choix_mot]=="rn":
    pays="italien"

#cache le mot eet le devoile quand le joueur entre une lettre dans le mot
def cachemot(motATrouver,motAChercher,liste_lettre):
    motAChercher=''
    for i in range(0,len(motATrouver)):
        if motATrouver[i]==' ':
            motAChercher+=' '
        elif motATrouver[i] in liste_lettre:
            motAChercher+=motATrouver[i]
        else:
            motAChercher+='-'
    return motAChercher

#verifie si le joueur a trouvé toutes les lettres du mot
def verif_mot (motATrouver,liste_lettre,aide):
    compteur=0
    longueur=len(motATrouver)
    trouve=False
    if nb_chance>=11:
        print("le navire était le",classe[choix_mot],pays,"nommé",prefixe[choix_mot],motATrouver+", son armement principale était constitué de",main_gun[choix_mot])
        trouve=False
    else:
        for i in range(0,len(motATrouver)):
            if motATrouver[i] in liste_lettre:
                compteur+=1
            elif motATrouver[i]==" ":
                compteur+=1
            if compteur==longueur:
                print("bien joué le navire était le",classe[choix_mot],pays,"nommé",prefixe[choix_mot],motATrouver,", son armement principale était constitué de",main_gun[choix_mot])
                print("vous avez utilisez "+str(aide)+" indice")
                trouve=False
            else:
                trouve=True
    return trouve


#constantes de la fenêtre d'affichage
LARGEUR=1200       #hauteur de la fenêtre
HAUTEUR=720      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
mixer.init()
mixer.music.load("musique_fond.mp3")
mixer.music.set_volume(0)
mixer.music.play()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("pendu")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 25)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame


def afficheCercle(x,y,rayon): #affiche un cercle aux coordonnées x,y avec un rayon
    pygame.draw.circle(fenetre, BLEU, (x,y), rayon)

def afficheRectangle(x,y,largeur,hauteur):   #affiche un rectangle en position x,y avec une largeur et une hauteur
    pygame.draw.rect(fenetre, BLEU, [x, y, largeur, hauteur])

def afficheTexte(x,y,txt):  #affiche un texte aux coordonnées x,y
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))



loop=True
start=0
lettre=''
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        elif event.type == pygame.KEYDOWN:
            lettre=(event.unicode)
            if lettre==',':
                if aide==0:
                    aide+=1
                elif aide==1:
                    aide+=1
                    nb_chance+=1
                elif aide==2:
                    aide+=1
                    nb_chance+=2
            fenetre.fill((0,0,0))
            print(lettre)
            if lettre in motATrouver:
                if lettre in liste_lettre:
                    afficheTexte(200,50,"déjà essayer")
                else:
                    liste_lettre+=lettre[0]+","
            else:
                if lettre in liste_lettre:
                    afficheTexte(200,50,"déjà essayer")
                else:
                    liste_lettre+=lettre[0]+","
                    nb_chance+=1
                    afficheTexte(200,50,"il vous reste "+str(11-nb_chance)+" chance")
            afficheTexte(100,150,"les lettres déjà testées sont:"+" "+liste_lettre)
            afficheTexte(100,200,"vous avez utilisé "+str(aide)+" indice")
            afficheTexte(100,650,"appuyer sur ',' pour avoir un indince")
            if nb_chance>=1:
                afficheRectangle(800,500,100,10)
            if nb_chance>=2:
                afficheRectangle(840,500,10,-200)
            if nb_chance>=3:
                afficheRectangle(840,290,100,10)
            if nb_chance>=4:
                afficheRectangle(940,290,10,50)
            if nb_chance>=5:
                afficheCercle(945,360,20)
            if nb_chance>=6:
                afficheRectangle(940,380,10,50)
            if nb_chance>=7:
                afficheRectangle(930,430,10,50)
            if nb_chance>=8:
                afficheRectangle(950,430,10,50)
            if nb_chance>=9:
                afficheRectangle(950,400,50,10)
            if nb_chance>=10:
                afficheRectangle(950,400,-50,10)
            motAChercher=''
            for n in range(0,len(motATrouver)):
                if motATrouver[n]==" ":
                    motAChercher+=" "
                elif motATrouver[n] in liste_lettre:
                    motAChercher+=motATrouver[n]
                else:
                    motAChercher+='-'
            loop=verif_mot (motATrouver,liste_lettre,aide)
            if aide==0:
                afficheTexte(540,360,motAChercher)
            elif aide==1:
                if etat_aide==0:
                    aide_supp=randint(0,len(motATrouver)-1)
                    while str(aide_supp) in str(liste_lettre):
                        aide_supp=randint(0,len(motATrouver)-1)
                    liste_lettre+=motATrouver[aide_supp]+","
                    etat_aide+=1
                afficheTexte(500,360,prefixe[choix_mot]+" "+motAChercher)
                afficheTexte(0,500,"vous cherchez un navire "+pays)
            if aide==2:
                afficheTexte(500,360,prefixe[choix_mot]+" "+motAChercher)
                afficheTexte(0,500,"vous cherchez un navire "+pays)
                afficheTexte(0,600,"son armement principale est constitué de "+main_gun[choix_mot])
            if aide==3:
                afficheTexte(500,360,prefixe[choix_mot]+" "+motAChercher)
                afficheTexte(0,500,"vous cherchez un navire "+pays)
                afficheTexte(0,600,"son armement principale est constitué de "+main_gun[choix_mot])
                afficheTexte(0,550,"ce navire était un "+classe[choix_mot])
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == '1': #touche q pour quitter
                loop = False

    if start==0:
        for n in range(0,len(motATrouver)):
            if motATrouver[n]==" ":
                motAChercher+=" "
            else:
                motAChercher+='-'
        afficheTexte(540,360,motAChercher)
        afficheTexte(100,150,"les lettres déjà testées sont:"+" "+liste_lettre)
        afficheTexte(100,200,"vous avez utilisé "+str(aide)+" indice")
        afficheTexte(100,650,"appuyer sur ',' pour avoir un indince")
        start+=1




    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()
