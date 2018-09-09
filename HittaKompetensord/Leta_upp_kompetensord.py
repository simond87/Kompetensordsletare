import re

def leta_upp(kompetenser, soektext):

    for kompetens in kompetenser:
        regexanpassat_soekord = re.compile('\\b' + re.escape(kompetens.rstrip()) + '\\b', re.IGNORECASE)
        upptaeckter = regexanpassat_soekord.finditer(soektext)
        #print(type(upptaeckter))
        for upptaeckt in upptaeckter:
            print("Startposition " + str(upptaeckt.start()) + " och slutposition " + str(upptaeckt.end()) + '\t\t' + kompetens.rstrip())
            #print(soektext[int(upptaeckt.start()-5):int(upptaeckt.end()+5)])
        #print ('***************')