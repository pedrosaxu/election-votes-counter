from requests import get
from os import system
from time import sleep

loop = 1

votos_bolso = 0
votos_lula = 0
votos_tarcisio = 0
votos_haddad = 0


while loop == 1: 

    system('clear')

    ###### PRESIDENTE ######
    ant_votos_bolso=votos_bolso
    ant_votos_lula=votos_lula

    votacao_presidente=get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json').json()
    
    votos_bolso=votacao_presidente["cand"][1]["pvap"].replace(",",".")
    
    if float(votos_bolso) > float(ant_votos_bolso):
        change_bolso = "↑"
    elif float(votos_bolso) < float(ant_votos_bolso):
        change_bolso = "↓"


    votos_lula=votacao_presidente["cand"][0]["pvap"].replace(",",".")

    if float(votos_lula) > float(ant_votos_lula):
        change_lula = "↑"
    elif float(votos_lula) < float(ant_votos_lula):
        change_lula = "↓"

    ###### GOVERNADOR ######
    ant_votos_tarcisio=votos_tarcisio
    ant_votos_haddad=votos_haddad

    votacao_governador=get('https://resultados.tse.jus.br/oficial/ele2022/547/dados-simplificados/sp/sp-c0003-e000547-r.json').json()
    votos_tarcisio=votacao_governador["cand"][0]["pvap"].replace(",",".")

    if float(votos_tarcisio) > float(ant_votos_tarcisio):
        change_tarcisio = "↑"
    elif float(votos_tarcisio) < float(ant_votos_tarcisio):
        change_tarcisio = "↓"
    
    votos_haddad=votacao_governador["cand"][1]["pvap"].replace(",",".")

    if float(votos_haddad) > float(ant_votos_haddad):
        change_haddad = "↑"
    elif float(votos_haddad) < float(ant_votos_haddad):
        change_haddad = "↓"

    urnas=get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json').json()["pst"].replace(",",".")

    print(f'\
        \n{"_"*30}\
        \nUrnas apuradas: {urnas}%')

    print(f'\
        \n{"_"*30}\
        \nLula: {votos_lula}% {change_lula}\
        \nBolsonaro: {votos_bolso}% {change_bolso}')

    if votos_bolso > votos_lula:
        print('\nB O L S O N A R O')
    else:
        print('\nL U L A')

    print(f'\
        \n{"_"*30}\
        \nHaddad: {votos_haddad}% {change_haddad}\
        \nTarcísio: {votos_tarcisio}% {change_tarcisio}')

    if votos_tarcisio > votos_haddad:
        print('\nT A R C Í S I O ')
    else:
        print('\nH A D D A D')

    print(f'{"_"*30}')
    sleep(2)
    



    


    

