import time 
# SITE PARA CORES https://raccoon.ninja/pt/dev-pt/utilizando-cores-para-escrever-no-terminal-python/
def verde():
    verde = "\033[1;32m"
    return verde
    
def vermelho():
    vermelho = "\033[1;31m"
    return vermelho
def limpacor():
    limpa = "\033[m"
    return limpa
    
def g():     # FAZENDO A VERIFICAÇÃO DE ENCERRAMENTO OU NOVA VOTAÇÃO 
    menuvoltar = ""
    while menuvoltar != "1" and menuvoltar != "2":
        limpartela()
        menuvoltar = input("\033[1;32m[1] NOVA VOTAÇÃO\033[m\n" + "\033[1;31m[2]ENCERRAR VOTAÇÃO\n\033[m")
        limpartela()
    if menuvoltar == "1":
        limpartela()
        menu()
    elif menuvoltar == "2" :
        limpartela()
        print("encerrando votação...")
        time.sleep(2)
        encerramento() 
    else:
        print("Não existe essa opção")
        time.sleep(2)
        g()


def ganhador_empate():
    global aline, jp, marcos, diego, branco, nulo
    #Dicionário
    candidatos = {}

    # Lista para interar ao meu dicionário
    lista_key_cand =['Aline','Jp', 'Marcos', 'Diego', 'Branco', 'Nulos' ]
    lista_values_cand = [aline, jp, marcos, diego, branco, nulo]
   
    # Tem valores maximos duplicados?
    duplicados = lista_values_cand.count(max(lista_values_cand))
    
    for x  in range(len(lista_key_cand)):
        candidatos[lista_key_cand[x]] = lista_values_cand[x]
    
    # Se tiver valores max duplicados, mostre-me os nomes 
    if duplicados >=2:
        print(f"\033[1;32m        EMPATE\n{imprime}")
        for key, values in candidatos.items(): # items() <<< Ele Separa os itens do meu dicionário 
            if values == max(lista_values_cand):
                print("      ",key, values)
    else:
        for key, values in candidatos.items():
            if values == max(lista_values_cand):
                print(f"       \033[1;032mVENCEDOR DAS ELEIÇÕES\n{imprime}\n", f"       Candidato  Votos\n{imprime}\n       ", key,"      ", values, "\n \n \n \n  ")
       


def encerramento():  #COMPUTANDO VOTOS 
    global aline, jp, marcos, branco, nulo, diego, enc
    print(f"{imprime}\n \033[1;30;43m  VOTAÇÃO ENCERRADA\033[m")
    lista_values_cand = [aline, jp, marcos, diego, branco, nulo]
    soma = sum(lista_values_cand)
    if soma >=1:
        divi = 100 / soma 
        a = aline * divi
         
        b = jp * divi
        
        c = marcos * divi
        
        d = branco * divi
        
        e = nulo * divi
        
        f = diego * divi
        limpartela()
        print(f"{imprime}\n     VOTAÇÃO ENCERRADA")
        print(f"{imprime}\n\033[1;35m                  \nAline recebeu     {a:.0f}%\nJp recebeu        {b:.0f}%\nMarcos recebeu    {c:.0f}%\nDiego recebeu     {f:.0f}%\nVotos Brancos     {d:.0f}%\nVotos Nulos       {e:.0f}%\n")
        ganhador_empate()
    elif soma == 0:
        print(f"\033[1;30m\nAline   recebeu {soma}%\nJp      recebeu {soma}%\nMarcos  recebeu {soma}%\nDiego   recebeu {soma}%\nVotos Brancos   {soma}%\nVotos Nulos     {soma}%\nNINGUÉM RECEBEU VOTOS\n{imprime}")
    
        
def limpartela(): # LIMPAR TELA 
    print("\x1b[2J\x1b[1;1H")
    return 


def verifica_senha_user(): #VERIFICA A CADA NOVA VOTAÇÃO SE A SENHA É VALIDA
    global user_senha, voto
    novovoto =""
    while novovoto != user_senha: 
        limpartela()
        novovoto = input("\033[1;37mÉ necessário senha para prosseguir: \033[m\n")
        limpartela()
    g()
    
    
def sim_nao(cand):   # VERIFICAÇÃO = CONFIRMAÇÃO OU CANCELAMENTO DE CANDIDATOS
    global aline, jp, marcos, diego, branco, nulo
    sn = ""
    while sn != "S" and sn != "s" and sn != "N" and sn != "n":
        limpartela()
        sn = input (f"     DIGITE\n {imprime}\n[s] para" + verde() + "  CONFIRMAR \n"+ limpacor()+ "[n] para" + vermelho() +"  CANCELAR \n")
    if sn == "S" or sn == "s":
        limpartela()
        print("\033[1;32mVOTO COMPUTADO\033[m")
        time.sleep(2)
        limpartela()
        if cand == "10":
            aline = +1
            verifica_senha_user()
        elif cand == "20":
            jp = +1 
            verifica_senha_user()
        elif cand == "30":
            marcos = + 1
            verifica_senha_user()
        elif cand == "40":
            diego = +1
            verifica_senha_user()
        elif cand == "0":
            branco = +1
            verifica_senha_user()
        else:
            nulo = +1
            verifica_senha_user()
    elif sn == "n" or sn == "N":
        limpartela()
        print ("\033[1;35mVoltando ao menu de candidatos") 
        time.sleep(2)
        limpartela()
        menu()
    
def SN(senha): # CASDASTRO USUARIO
    if user_senha == senha:
        limpartela()
        user_confirme_senha = input(f"\033[33m{mesario}, Confirme a senha\n")
        limpartela()
        while user_confirme_senha != senha:
            limpartela()
            user_confirme_senha = input("\033[1;31mSenhas não conferem\n\033[m" + "\033[36mConfirme a senha\n")
            limpartela()
        else:
            limpartela()
            print(verde() + f"{mesario},SENHA CADASTRADA COM SUCESSO!")
            time.sleep(2)
            limpartela()


def votacao(votar): # VERIFICAÇÃO = ESCOLHA DOS CANDIDATOS
    global voto
    voto = input("")
    if voto == "10" or (voto == "20") or (voto =="30") or (voto == "40") or (voto == "0") or (voto == "1"):
        if voto == "1":
            limpartela()
            verifica_senha_user()
            
        elif voto== "10":
            print("\033[1;33mAline")
            time.sleep(2)
            limpartela()
            sim_nao(voto)
        elif voto== "20":
            print("\033[1;33mJp")
            time.sleep(2)
            limpartela()
            sim_nao(voto)
        elif voto== "30":
            print("\033[1;33mMarcos")
            time.sleep(2)
            limpartela()
            sim_nao(voto)
        elif voto== "40":
            print("\033[1;33mDiego")
            time.sleep(2)
            limpartela()
            sim_nao(voto)
        elif voto== "0":
            print("\033[1;33mVoto em Branco")
            time.sleep(2)
            limpartela()
            sim_nao(voto)
    else:
        print ("\033[1;36m" +"VOTO NULO" + "\033[m")
        time.sleep(2)
        sim_nao(voto)
         
         
def menu(): # MENU DE CANDIDATOS
    print("\033[1;34m"+"BEM VINDO AS ELEIÇÕES DO PROFESSOR FAVORITO"+"\033[m")
    print(imprime)
    print(str(" Escolha um número correspondente ao seu candidato"))
    print(f"\N{winking face}", "\033[1;037m Aline\033[m"   + "\033[1;33m" +"         10" + "\033[m ")
    print(f"\N{grinning face}", " \033[1;037mJp\033[m"   + "\033[1;33m" +"            20" + "\033[m ")
    print("\U0001F606",         " \033[1;037mMarcos\033[m" +"\033[1;33m"+"        30" +"\033[m") 
    print("\N{grinning face}",   " \033[1;037mDiego\033[m"+ "\033[1;33m"+"         40"+"\033[m")
    print(">\033[1;037mVOTAR EM BRANCO \033[m " + "\033[1;33m"  +"0"  "\033[m           ")
    print("\033[1;035m>>DIGITE [1] para encerrar a votação\033[m")
    votacao(voto)
    
def verifica_nome(nome):
    global mesario
    while  nome.isalpha() == False:
        
            limpartela()
            nome = str(input("\033[1;31mNome inválido\033[m\nDigite novamente:\n"))
            limpartela()
    mesario = nome
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CODIGO PRINCIPAL(INICIO)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    
imprime = "\033[1;33m"+ "=-" * 26 +"\033[m"

mesario=str(input("\033[1;34m" + f"          BEM VINDO AS ELEIÇÕES 2022\n{imprime}\n" + "\033[1;37mOlá mesário, para começarmos digite o seu nome\n"))
verifica_nome(mesario)
mesario = mesario.upper()

limpartela()
nulo=0
branco = 0
aline = 0
marcos = 0
jp = 0
diego = 0
user_senha = ""
user_confirme_senha = ""
voto = ""
user_senha = input(f"\033[1;37m{mesario}, Insira uma senha\n")
limpartela()
while user_senha == "" or user_senha.isspace():
    limpartela()
    user_senha = input(f"\033[1;31m{mesario}, Senha inválida!\n")
    
SN(user_senha) # Aqui é meu argumento, esta variavel será inserida na variavel da função
menu()





















