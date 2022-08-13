from tkinter import * 
from os import system, path
from tkinter import font
from Main import *

global mainWindow, file_name_label, file_name_entry, in_out_frame, logLabel, emptyLabel1

def Format(s):
    s = s[:tnum] +' '+ s[tnum:tnom+tnum] +' '+ s[tnum+tnom:tnum+tnom+tprénom] +' '+ s[tnum+tnom+tprénom:tnum+tnom+tprénom+taffiliation]
    s = s.replace('#', '')
    return s

def cancelDisplaying():
    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    file_name_entry["state"] = "normal"
    logLabel.config(text='', fg='black')
    for label in labels:
        label.destroy()
    
    nextButton.destroy()
    previousButton.destroy()
    cancelDisplayingButton.destroy()





def nextBlock(index):
    for label in labels:
        label.destroy()

    nextButton.destroy()
    previousButton.destroy()
    cancelDisplayingButton.destroy()

    affichier_block(fileName, index)


def previousBlock(index):
    for label in labels:
        label.destroy()
    
    nextButton.destroy()
    previousButton.destroy()
    cancelDisplayingButton.destroy()

    affichier_block(fileName, index)


def affichier_block(fn, blockIndex):
    with open(fn, 'rb') as file:
        global buf
        buf = lireBloc(file, blockIndex)
    global labels
    labels = []
    for i in range (b):
        labels.append(Label(master=in_out_frame, text=Format(buf[1][i]), font=('Consolas',12)))
    
    labels.append(Label(master=in_out_frame, text='\n\n', font=('Consolas',12)))

    i=0
    for label in labels:
        label.grid(column=1,row=i)
        i += 1
    
    logLabel.config(text=f'Block: {blockIndex+1} , NB: {buf[0]}', fg='black')

    global nextButton, previousButton, cancelDisplayingButton
    nextButton = Button(master=in_out_frame, text='next', command=lambda * args: nextBlock(blockIndex+1), font=('Consolas',14))
    previousButton = Button(master=in_out_frame, text='previous', command=lambda * args: previousBlock(blockIndex-1), font=('Consolas',14))
    cancelDisplayingButton = Button(master= in_out_frame, text='cancel', command=cancelDisplaying, font=('Consolas',14))

    nextButton.grid(row=i+3, column=0)
    previousButton.grid(row=i+3, column=1)
    cancelDisplayingButton.grid(row=i+3, column=3)

    if blockIndex == 0:
        previousButton["state"] = "disabled"
    if blockIndex == headline_0 - 1:
        nextButton["state"] = "disabled"


    emptyLabel2 = Label(master=in_out_frame,text='\n' * (6 - buf[0]))
    emptyLabel2.grid(row=i+4, column=0)

def search():
    num = numEntry.get()
    if num == '':
        logLabel.config(text='Vous devez remplir les informations', fg='red')
    else:
        logLabel.config(text='', fg='black')
        if num.isdecimal():
            num = int(num)
            a = recherche(fileName, num)
            if a[0]:
                logLabel.config(text=f'numero trouvé avec succes\nblock: {a[1]+1} enregistrement: {a[2]+1}', fg='black')
            else:
                logLabel.config(text='numero non trouvé', fg='red')

def cancel_searching():
    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    logLabel.config(text='', fg='black')
    file_name_entry["state"] = "normal"
    numEntry.destroy()
    numLabel.destroy()
    emptyLabel2.destroy()
    emptyLabel3.destroy()
    SearchButton.destroy()
    CancelSearching.destroy()

def delete():
    num = numEntry.get()
    if num == '':
        logLabel.config(text='Vous devez remplir les informations', fg='red')
    else:
        logLabel.config(text='', fg='black')
        if num.isdecimal():
            num = int(num)
            a = recherche(fileName, num)
            if a[0]:
                supression(fileName, num)
                logLabel.config(text=f'etudiant supprimé avec succés\nblock: {a[1]+1} enregistrement: {a[2]+1}', fg='black')
            else:
                logLabel.config(text='numero non trouvé', fg='red')
        else:
            logLabel.config(text='le nombre doit etre un entier', fg='red')

def cancel_deleting():
    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    logLabel.config(text='', fg='black')
    file_name_entry["state"] = "normal"
    numEntry.destroy()
    numLabel.destroy()
    DeleteButton.destroy()
    CancelDeletingButton.destroy()

def Continue():
    logLabel.config(text='', fg='black')
    file_name_entry["state"] = "normal"
    numLabel.destroy()
    nomLabel.destroy()
    prenomLabel.destroy()
    affiliationLabel.destroy()
    numEntry.destroy()
    nomEntry.destroy()
    prenomEntry.destroy()
    affiliationEntry.destroy()
    emptyLabel2.destroy()
    emptyLabel3.destroy()
    ContinueButton.destroy()
    StopButton.destroy()
    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    ContinueButton.destroy()
    StopButton.destroy()
    command0()

def Stop():
    logLabel.config(text='', fg='black')
    file_name_entry["state"] = "normal"
    numLabel.destroy()
    nomLabel.destroy()
    prenomLabel.destroy()
    affiliationLabel.destroy()
    numEntry.destroy()
    nomEntry.destroy()
    prenomEntry.destroy()
    affiliationEntry.destroy()
    emptyLabel2.destroy()
    emptyLabel3.destroy()
    ContinueButton.destroy()
    StopButton.destroy()
    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"

def submit():
    num = numEntry.get()
    nom = nomEntry.get()
    prenom = prenomEntry.get()
    affiliation = affiliationEntry.get()

    if num == '' or nom == '' or prenom == '' or affiliation == '':
        logLabel.config(text='Vous devez remplir les informations', fg='red')
    else:
        logLabel.config(text='', fg='black')
        if num.isdecimal():
            num = resize_chaine(num, tnum)
            nom = resize_chaine(nom, tnom)
            prenom = resize_chaine(prenom, tprénom)
            affiliation = resize_chaine(affiliation, taffiliation)
            etud = str(num) + nom + prenom + affiliation

            a = insertion(fileName, etud)
            if not a[0]:
                logLabel.config(text='Etudiant ajouté avec succés\nVoud voulez continue ?')

                SubmitButton.destroy()
                CancelButton.destroy()

                global ContinueButton, StopButton
                ContinueButton = Button(master=in_out_frame, text='Oui', command=Continue, font=('Consolas',14))
                StopButton = Button(master=in_out_frame, text='Non', command=Stop, font=('Consolas',14))

                ContinueButton.grid(row=5, column=0)
                StopButton.grid(row=5, column=1)
            else:
                logLabel.config(text=f'L\'etudiant deja existe\nblock:{a[1]+1} enregistrement:{a[2] + 1}', fg='red') 
        else:
            logLabel.config(text='le nombre doit etre un entier', fg='red')

def cancel():
    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    logLabel.config(text='', fg='black')
    file_name_entry["state"] = "normal"
    numLabel.destroy()
    nomLabel.destroy()
    prenomLabel.destroy()
    affiliationLabel.destroy()
    numEntry.destroy()
    nomEntry.destroy()
    emptyLabel2.destroy()
    emptyLabel3.destroy()
    prenomEntry.destroy()
    affiliationEntry.destroy()
    SubmitButton.destroy()
    CancelButton.destroy()

def command0():
    global fileName
    fileName = file_name_entry.get().replace(' ', '')
    if fileName == '':
        logLabel.config(text='Please enter a file name', fg='red')
    else:
        file_name_entry["state"] = "disabled"
        button0["state"] = "disabled"
        button1["state"] = "disabled"
        button2["state"] = "disabled"
        button3["state"] = "disabled"
        button4["state"] = "disabled"
        logLabel.config(text='entrez les information de l\'etudiant', fg='black')
        
        if not path.isfile(fileName):
            with open(fileName, 'wb') as file:
                affecter_entete(file, 0, 0)
                affecter_entete(file, 1, 0)
    
        global numLabel, nomLabel, prenomLabel, affiliationLabel
        numLabel = Label(master=in_out_frame, text='numero      :', font=('Consolas',14))
        nomLabel = Label(master=in_out_frame, text='nom         :', font=('Consolas',14))
        prenomLabel = Label(master=in_out_frame, text='prenom      :', font=('Consolas',14))
        affiliationLabel = Label(master=in_out_frame, text='affiliation :', font=('Consolas',14))

        numLabel.grid(column=0,row=0)
        nomLabel.grid(column=0,row=1)
        prenomLabel.grid(column=0,row=2)
        affiliationLabel.grid(column=0,row=3)

        global numEntry, nomEntry, prenomEntry, affiliationEntry
        numEntry = Entry(master=in_out_frame, font=('Consolas',14))
        nomEntry = Entry(master=in_out_frame, font=('Consolas',14))
        prenomEntry = Entry(master=in_out_frame, font=('Consolas',14))
        affiliationEntry = Entry(master=in_out_frame, font=('Consolas',14))

        numEntry.grid(column=1,row=0)
        nomEntry.grid(column=1,row=1)
        prenomEntry.grid(column=1,row=2)
        affiliationEntry.grid(column=1,row=3)

        global emptyLabel2, emptyLabel3
        emptyLabel2 = Label(master=in_out_frame, text='\n')
        emptyLabel2.grid(row=4, column=0)

        global SubmitButton, CancelButton
        SubmitButton = Button(master=in_out_frame, text='Submit', command=submit, font=('Consolas',14))
        CancelButton = Button(master=in_out_frame, text='Cancel', command=cancel, font=('Consolas',14))
        
        SubmitButton.grid(row=5, column=0)
        CancelButton.grid(row=5, column=1)

        emptyLabel3 = Label(master=in_out_frame, text='\n')
        emptyLabel3.grid(row=6, column=0)

def command1():
    global fileName
    fileName = file_name_entry.get().replace(' ', '')
    if fileName == '':
        logLabel.config(text='Please enter a file name', fg='red')
    else:
        if not path.isfile(fileName):
            logLabel.config(text="le fichier n\'existe pas", fg='red')
        else:
            file_name_entry["state"] = "disabled"
            button0["state"] = "disabled"
            button1["state"] = "disabled"
            button2["state"] = "disabled"
            button3["state"] = "disabled"
            button4["state"] = "disabled"

            with open(fileName, 'rb') as file:
                global headline_0, headline_1
                headline_0 = entete(file, 0)
                headline_1 = entete(file, 1)

            block_index = 0
            affichier_block(fileName, block_index)

def command3():
    global fileName
    fileName = file_name_entry.get().replace(' ', '')
    if fileName == '':
        logLabel.config(text='Please enter a file name', fg='red')
    else:
        logLabel.config(text='entrez le numero de l\'etudiant', fg='black')

        if not path.isfile(fileName):
            logLabel.config(text="le fichier n\'existe pas", fg='red')
        else:
            file_name_entry["state"] = "disabled"
            button0["state"] = "disabled"
            button1["state"] = "disabled"
            button2["state"] = "disabled"
            button3["state"] = "disabled"
            button4["state"] = "disabled"

            global numLabel, numEntry
            numLabel = Label(master=in_out_frame, text='numero      :', font=('Consolas',14))
            numEntry = Entry(master=in_out_frame, font=('Consolas',14))

            numLabel.grid(column=0,row=0)
            numEntry.grid(column=1,row=0)

            global emptyLabel2, emptyLabel3
            emptyLabel2 = Label(master=in_out_frame, text='\n')
            emptyLabel2.grid(row=1, column=0)
            

            global DeleteButton, CancelDeletingButton
            DeleteButton = Button(master=in_out_frame, text='Delete', command=delete, font=('Consolas',14))
            CancelDeletingButton = Button(master=in_out_frame, text='Cancel', command=cancel_deleting, font=('Consolas',14))
            
            DeleteButton.grid(row=2, column=0)
            CancelDeletingButton.grid(row=2, column=1)

            emptyLabel3 = Label(master=in_out_frame, text='\n\n\n\n\n\n')
            emptyLabel3.grid(row=3, column=0)

def command4():
    global fileName
    fileName = file_name_entry.get().replace(' ', '')
    if fileName == '':
        logLabel.config(text='Please enter a file name', fg='red')
    else:
        logLabel.config(text='entrez le numero de l\'etudiant', fg='black')
        if not path.isfile(fileName):
            logLabel.config(text="le fichier n\'existe pas", fg='red')
        else:
            file_name_entry["state"] = "disabled"
            button0["state"] = "disabled"
            button1["state"] = "disabled"
            button2["state"] = "disabled"
            button3["state"] = "disabled"
            button4["state"] = "disabled"

            global numLabel, numEntry
            numLabel = Label(master=in_out_frame, text='numero      :', font=('Consolas',14))
            numEntry = Entry(master=in_out_frame, font=('Consolas',14))

            numLabel.grid(column=0,row=0)
            numEntry.grid(column=1,row=0)

            global emptyLabel2, emptyLabel3
            emptyLabel2 = Label(master=in_out_frame, text='\n')
            emptyLabel2.grid(row=1, column=0)
            

            global SearchButton, CancelSearching
            SearchButton = Button(master=in_out_frame, text='Search', command=search, font=('Consolas',14))
            CancelSearching = Button(master=in_out_frame, text='Cancel', command=cancel_searching, font=('Consolas',14))
            
            SearchButton.grid(row=2, column=0)
            CancelSearching.grid(row=2, column=1)

            emptyLabel3 = Label(master=in_out_frame, text='\n\n\n\n')
            emptyLabel3.grid(row=3, column=0)


system('cls')

mainWindow = Tk(className='les fichiers binaires (keziz mouayed groupe 8)')
mainWindow.geometry('450x500')

file_name_label = Label(master=mainWindow, text='entrez le nom du fichier ici')
file_name_label.config(font=('Consolas',18))
file_name_label.pack()

file_name_entry = Entry(master=mainWindow)
file_name_entry.config(font=('Consolas',15))    
file_name_entry.pack()

frame_of_buttons = Frame()
frame_of_buttons.pack()

global button0, button1, button2, button3, button4

button0 = Button(master=frame_of_buttons, text='---créer fichier---', command=command0)
button1 = Button(master=frame_of_buttons, text='-affichier fichier-', command=command1)
button2 = Button(master=frame_of_buttons, text='-----insertion-----', command=command0)
button3 = Button(master=frame_of_buttons, text='----supression-----', command=command3)
button4 = Button(master=mainWindow, text='-----recherche-----', command=command4)

button0.config(font=('Consolas',13))
button1.config(font=('Consolas',13))
button2.config(font=('Consolas',13))
button3.config(font=('Consolas',13))
button4.config(font=('Consolas',13))

button0.grid(row=0, column=0)
button1.grid(row=0, column=1)
button2.grid(row=1, column=0)
button3.grid(row=1, column=1)
button4.pack()

emptyLabel1 = Label(master=mainWindow, text='\n')
emptyLabel1.pack()

in_out_frame = Frame(master=mainWindow, width=450, height=250)
in_out_frame.pack()

logLabel = Label(master=mainWindow, text='', font=('Consolas',14))
logLabel.pack()


mainWindow.mainloop()