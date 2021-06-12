import os
import re


print("Veuillez saisir un nom de domaine|nom d'utilisateur|adresse e-mail... ==> ")
donnee=input()

regex_domaine = "^((?!-)[A-Za-z0-9-]" +"{1,63}(?<!-)\\.)" +"+[A-Za-z]{2,6}"
regex_username="^[A-Za-z_][A-Za-z0-9_]*$"


if re.search(regex_domaine, donnee):
    os.system("python3 metagoofil.py -d "+donnee+" -t pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx -o MetagoofilResults") 
    os.system("python3 theHarvester.py -d "+donnee+" -g -p -s --screenshot theHarvesterSSResults -v -f theHarvesterResults -b all")
    os.system("python3 ./sf.py -m sfp_spider,sfp_names,sfp_email,sfp_phone -s "+donnee+" -q -F HUMAN_NAME,EMAILADDR,PHONE_NUMB")
if re.search(regex_username, donnee):
    os.system("python3 ./sf.py -m sfp_accounts -s \""+donnee+"\" -q -n")
    os.chdir('/home/user/OSINT/sherlock')
    #print(os.getcwd())
    os.system("python3 sherlock "+donnee+" -o SherlockResults ")
