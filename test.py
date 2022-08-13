from os import system
system('cls')
tnum = 10                                               #Taille max du num
tnom = 20                                               #Taille max du nom
tprenom = 20                                            #Taille max du prenom
taffiliation = 20

def Format(s):
    s = s[:tnum] +' '+ s[tnum:tnom+tnum] +' '+ s[tnum+tnom:tnum+tnom+tprenom] +' '+ s[tnum+tnom+tprenom:tnum+tnom+tprenom+taffiliation]
    s = s.replace('#', '')
    return s


s = '22########5###################5###################5###################'
print(s)
print(Format(s))

