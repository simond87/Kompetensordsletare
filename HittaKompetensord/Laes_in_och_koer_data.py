
import Leta_upp_kompetensord as luk

def rensa_listdubletter(ordlista):

    nedraeknare = len(ordlista)-1 # indexvariabel för att räkna ner genom listan

    while nedraeknare > 0:
        ordlista[nedraeknare] = ordlista[nedraeknare].lower() # versaler blir gemener
        if ordlista[nedraeknare] == ordlista[nedraeknare-1].lower():
            del ordlista[nedraeknare]

        nedraeknare -= 1
    return ordlista

if __name__ == '__main__':

    annonsfil = open('job-posting.txt', 'r')
    kompetensordsfil = open('skills.txt', 'r')
    # läser in textfilerna jobbannons och kompetenser

    annonstext = annonsfil.read() # annonsen hamnar i en stor sträng
    annonsfil.close()

    kompetensord = rensa_listdubletter(kompetensordsfil.readlines())
    # Från filen inläses en lista där varje element är ett kompetensord i form av en sträng.
    # Innan den sparas i kompetensord rensas dubletterna bort och
    # alla bokstäver konverteras alla element till gemener

    kompetensordsfil.close()

    luk.leta_upp(kompetensord,annonstext) # letar upp och skriver ut de hittade kompetensorden