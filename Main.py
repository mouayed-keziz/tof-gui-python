from pickle import dumps,loads
from sys import getsizeof
from os import system
global b
global tnom
global tprénom
global tnuminscpt 
global taffiliation


b = 3                                                   #Taille max du bloc
tnum = 10                                               #Taille max du num
tnom = 20                                               #Taille max du nom
tprénom = 20                                            #Taille max du prenom
taffiliation = 20                                       #Taille max de l'affiliation
Tetud = tnum + tnom + tprénom + taffiliation            #Taille d'un enregistrements
Tnreg = '#' * Tetud                                     #enregistrement = chaine de caractaires de # repeté (Taille d'un enregistrements fois)

global buf                                              #le buffer du programme (global)
Tbloc = [0, [Tnreg] * b]                                #C'est le bloc ou Tbloc[0] est NB et Tbloc[1] est une list d'enregistrements(list de chaines de caractaires)

global blocsize                                         #Taille d'un bloc (global)
blocsize=getsizeof(dumps(Tbloc))+len(Tnreg)*(b-1)+(b-1) #Calculer la taille d'un bloque en binaire


#Complete le reste du chaine de caractaires avec '#' (jusqu'à la taille max)
def resize_chaine(chaine, maxtaille):
    for _ in range(len(chaine),maxtaille):
          chaine=chaine+'#' 
    return chaine


#créer un fichier et le remplir avec les information des etudiants (chargements inisial)
def créer_fichier():
    system('cls')
    file_name = input('Entrer le nom du fichier à créer: ')
    j = 0
    i = 0
    n = 0
    buf_tab = [Tnreg] * b
    buf_nb = 0
    try:
        f = open(file_name, 'wb')
    except:
        print('impossible d\'ouvrir le fichier en mode d\'écriture ')
    rep = 'O'
    while (rep == 'O'):
        system('cls')
        print('Entrer les information de l\'étudiant: ')
        num = int(input('Enter le numéro d\'inscription : '))
        nom = input('Enter le nom: ')
        prénom = input('Entrer le prénom: ')
        affiliation = input('Entrer l\'affiliation: ')
        num = resize_chaine(str(num), tnum)
        nom = resize_chaine(nom, tnom)
        prénom = resize_chaine(prénom, tprénom)
        affiliation = resize_chaine(affiliation, taffiliation)
        etud = str(num) + nom + prénom + affiliation
        n += 1
        if (j < b):
            buf_tab[j] = etud
            buf_nb += 1
            j += 1
        else:
            buf = [buf_nb, buf_tab]
            ecrireBloc(f,i,buf)
            buf_tab = [Tnreg] * b
            buf_nb = 1
            buf_tab[0] = etud
            j = 1
            i += 1
        rep = input('Avez vous un autre élement à entrer O/N: ').upper()

    buf = [j,buf_tab]
    ecrireBloc(f,i,buf)
    affecter_entete(f,0,i+1)
    affecter_entete(f,1,n)
    f.close()


#Lire le bloc dans la position i dans le fichier file
def lireBloc(file, i):
    dp = 2 * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0)
    buf = file.read(blocsize)
    return (loads(buf))


#Ecrire le contenue du buffer dans le bloc dans la position i dans le fichier file
def ecrireBloc(file, i, bf):
    dp = 2 * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0)
    file.write(dumps(bf))


#Affecter la valeur c à la caracteristique numero 'of' de l'entete du fichier file
def affecter_entete(file, of, c):
    dp= of * getsizeof(dumps(0))
    file.seek(dp, 0)
    file.write(dumps(c))


#Lire la caracteristique numero 'offset' de l'entete du fichier file
def entete(file,offset):
    dp = offset * getsizeof(dumps(0))
    file.seek(dp, 0)
    c = file.read(getsizeof(dumps(0)))
    return loads(c)



def afficher_fichier(fn):
    system('cls')
    file_name = fn

    with open(file_name,'rb') as file:
        caracteristique1 = entete(file,0)
        caracteristique2 = entete(file,1)
        print(f'votre fichier contient {caracteristique1} block ')
        print(f'votre fichier contient {caracteristique2} enregistrements \n')
        for i in range(caracteristique1):
            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_tab = buf[1]
            print(f'Le contenu du block {i + 1} est:\n' )
            for j in range(buf_nb):
                print((buf_tab[j]))
            print('\n')


#recupérer les champs à partir de chaque enregistrement et remplacer les '#' par un espace
def afficher_enreg(e):
     num = e[0:tnom].replace('#', ' ')
     nom = e[tnom:tprénom].replace('#', ' ')
     prénom = e[tprénom:taffiliation].replace('#', ' ')
     affiliation = e[taffiliation:len(e)].replace('#', ' ')
     return  (num + ' ' +  nom + ' ' + prénom +  ' '+affiliation )



def recherche(file_name, c):
    with open(file_name, 'rb') as file:
        caracteristique1 = entete(file, 0)
        for i in range(caracteristique1):
            buf = lireBloc(file, i)
            buf_nb = buf[0]
            buf_tab = buf[1]
            for j in range(buf_nb):
                if int(buf_tab[j][:10].replace('#', '')) == c:
                    return [True, i, j]
    return [False]
    

def insertion(file_name, e):
    a = recherche(file_name,int(e[:10].replace('#', '')))
    if not a[0]:
        with open(file_name, 'rb+') as file:
            car0 = entete(file, 0)
            car1 = entete(file, 1)
            if car0 == 0:
                buf = [0, [Tnreg] * b]
                buf[0] = 1
                buf[1][0] = e
                ecrireBloc(file, 0, buf)
                affecter_entete(file, 0, 1)
                affecter_entete(file, 1, 1)
            else:

                buf = lireBloc(file, car0 - 1)
                nb = buf[0]
                tab = buf[1]
                if nb < b:
                    tab[nb] = e
                    nb = nb + 1
                    buf = [nb, tab]
                    ecrireBloc(file, car0 - 1, buf)
                else:
                    tab = [Tnreg] * b
                    tab[0] = e
                    nb = 1
                    buf = [nb, tab]
                    ecrireBloc(file, car0 , buf)
                    affecter_entete(file, 0, car0 + 1)
                affecter_entete(file, 1, car1 + 1)
    return a
        


def supression(file_name, cle):
    a = recherche(file_name, cle)
    if a[0]:
        with open(file_name, 'rb+') as file:

            buf1 = lireBloc(file, entete(file, 0) - 1)
            e = buf1[1][buf1[0] - 1]
            buf1[1][buf1[0] - 1] = Tnreg
            buf1[0] -= 1
            if buf1[0] != 0:
                ecrireBloc(file, entete(file, 0) - 1, buf1)
            else:
                affecter_entete(file, 0, entete(file, 0) - 1)

            buf = lireBloc(file, a[1])            
            buf[1][a[2]] = e
            ecrireBloc(file, a[1], buf)
            
            affecter_entete(file, 1, entete(file, 1) - 1)
    






system('cls')


#créer_fichier()

#print( recherche('keziz', 22) )

#e = '22########5###################5###################5###################'
#insertion('keziz', e)


#supression('keziz', 22)

afficher_fichier('a')

