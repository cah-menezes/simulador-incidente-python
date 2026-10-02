"""Treinamento de Segurança da Informação — Simulador de Incidente.
Você é um funcionário novo na empresa. A cada situação, escolha como reagiria.
No final, descobre se está pronto pra trabalhar com segurança ou precisa de mais treinamento."""


from time import sleep

#Variáveis fixas
nome = "nome"

#Funções
def etapa1(pontos):
    print("""\nBem-vindo(a) ao Treinamento de Segurança da Informação! 🛡️
Você acabou de ser contratado e o RH preparou esse treinamento obrigatório.
Aqui você vai enfrentar situações reais do dia a dia corporativo e descobrir se está preparado para lidar com elas.\n""")
    print("-" * 60)
    sleep(1)
    print("""\nA cada situação, escolha como você reagiria.
No final, descobre se está pronto para trabalhar com segurança ou... se precisa estudar mais. 👀\n""")
    sleep(1)

    nome = input("\nAntes de começarmos... qual o seu nome?\n").strip().capitalize()
    sleep(1)

    print(f"Certo, certo... {nome}. Vamos começar... \n")
    sleep(1)
    print("-" * 60)

    print("""\n🚨 SITUAÇÃO 1: Você recebeu um e-mail do 'RH' pedindo para clicar num link e atualizar seus dados bancários com urgência.
    O que você faz?
    a) Clica no link, afinal veio do RH
    b) Encaminha pro time de TI e não clica em nada
    c) Deleta o e-mail e ignora""")
    resposta1 = input("Alternativa: ")

    if resposta1 == "a":
        print(f"\nIh, {nome}, você caiu no phishing 😬...")
    elif resposta1 == "b":
        print(f"\n{nome}, resposta correta! ✅")
        pontos += 10
    else:
        print(f"\nMelhor que clicar, né? {nome}, mas nos próximos você deveria reportar, tá bom?")
        pontos += 5
    sleep(1)
    print(f"\nAté aqui você tem: {pontos} pontos. Vamos continuar...")
    return pontos




def etapa2(pontos):
    pass

def etapa3(pontos):
    pass

def etapa4(pontos):
    pass

def etapa5(pontos):
    pass

def resultado(pontos):
    pass

#Programa principal
if __name__ == "__main__":
    pontos = 0
    um = etapa1(pontos)
    dois = etapa2(um)
    tres = etapa3(dois)
    quatro = etapa4(tres)
    cinco = etapa5(quatro)
    resultado(cinco)