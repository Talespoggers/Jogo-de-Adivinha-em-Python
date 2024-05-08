
print("O sistema a seguir é um jogo sobre adivinhação");
import random;
import time;
import os;
#funções
os.system("cls")
def linha():
    print("---------------------------------------------------------------------------------------------");
def explicacao_do_jogo():
    
    linha()
    print("Olá, tudo bem ? ");
    time.sleep(2)
    
    print("Que bom que NÃO");
    time.sleep(2)    ;
    print("Vamos jogar um jogo onde você tera que adivinhar um numero aleatorio!!");
    time.sleep(2);
    print("Parece facil né?");
    time.sleep(2);
    print("Então para nâo ficar muito facil teremos algumas regras!!\n");
    time.sleep(2);

    #regras
    print("1° - Regra: Você podera errar apenas 2 vezes.");
    time.sleep(2);
    print("2° - Regra: você  não podera pedir dicas, pq não tem! \n");
    time.sleep(2);
    print("voce tera que escolher a dificuldade do jogo digite o numero correspondente a dificuldade:");
    time.sleep(2);
    print("1 - Para facil");
    time.sleep(2);
    print("2 - Para casual");
    time.sleep(2);
    print("3 - Para dificil");
    time.sleep(2);
    print("Boa sorte!!");
    linha();
    time.sleep(2);
    
#variaveis
NumeroSorteado = int(0);
menu =int(0);
dificuldade = int(0);
NumeroSelecionado = int(0);
dicas = int(0);

#Explicação do jogo
explicacao_do_jogo();
os.system("cls")

#PROCESSAMENTO
    



linha()
print("vamos escolher a dificulade:");
linha()
        
print("digite 1 para facil: O numero gerado sera");
print("digite 2 para casual: Tera um tempora para que possa responder");
print("digite 3 para dificil: Terá um um tempo menir para responder");
print("digite 0 para SAIR\n")
linha()
        


while (True):
   
    dificuldade = int(input('Escolha a dificuldade: '));
   
    if (dificuldade > 3 or dificuldade < 0): print(' Escolha apenas dificuldades de 1 a 3\n');
    linha()
    
   
    if(dificuldade == 1):
        linha()
        print('Você é um Jogador de Free Fire??\n');
        SortedNumber = random.randint(1 , 25);
        break
   
    if(dificuldade == 2):
        linha()
        print('Você é um jogador casual!!?\n');
        SortedNumber = random.randint(1 , 50);
        os.system("cls")
        break
    if(dificuldade == 3):
        linha()
        print('Você é um jogador tryhard. Pra que??\n');
        SortedNumber = random.randint(1 , 100);
        os.system("cls")
        break
    if(dificuldade == 0):
        linha()
        print("- Você realmente deveria desistir da vida.  ;-;")
        exit()
count = 4;


while(dificuldade < 3 or dificuldade > 1):

    NumeroSelecionado = int(input(f'Digite um Número de (0 a 100)se escolheu 3\nDigite um Número de (0 a 50)se escolheu 2\nDigite um Número de (0 a 25)se escolheu 1\nvocê tem {count} tentativas: '));

    os.system("cls")
    print(f"Você tem {count} tentativas:")
    
    if(NumeroSelecionado == SortedNumber):
        print('Até que parece que você não é um animal tão burro.\n');
        print("nunca mais volte")
        exit()
    else:
        print('Realmente você não tem capacidade para isso. Va jogar Roblox. \nTente Novamente.\n');
        
    

    count = (count - 1)
    if(count <= 0):
        print("errou")
        break
    if(NumeroSelecionado > SortedNumber):
         print("(DICA) É pra baixo BURRO\n");
         print(f"sua tentativa foi:{NumeroSelecionado}\nTe falta errar mais {count} tentativas");
         linha()
    
    if(NumeroSelecionado < SortedNumber):
        print("(DICA) É pra cima BURRO\n");
        print(f"sua tentativa foi:{NumeroSelecionado}\n Te falta errar mais {count} tentativas");
        linha()
       
    
print(f"O Número era {SortedNumber} mas vc é burro msm\n-----------Game Over------------")

#seleção de dificuldade













 
   