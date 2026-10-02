"""Treinamento de Segurança da Informação — Simulador de Incidente.
Você é um funcionário novo na empresa. A cada situação, escolha como reagiria.
No final, descobre se está pronto pra trabalhar com segurança ou precisa de mais treinamento."""


from time import sleep

#Introdução
print("""\nBem-vindo(a) ao SecureQuest! 🎮
Você está prestes a enfrentar situações reais do dia a dia corporativo.
Será que tomará as decisões certas?\n""")

print("-" * 60)

print("""\n🎮 A cada situação, escolha como você reagiria.
⚠️  Atenção: suas escolhas têm consequências, errar pode tornar as próximas situações mais difíceis.\n
No final, você descobre se está pronto para navegar com segurança no ambiente digital... ou se precisa estudar mais. 👀""")

sleep(9)
nome = input("\nAntes de começarmos... qual o seu nome?\n").strip().capitalize()
print(f"Certo, certo... {nome}. Vamos começar... \n")
sleep(1)
print("-" * 60)

#Funções
def etapa1(pontos):
    print("""\n📧 SITUAÇÃO 1: Você recebeu um e-mail:
Assunto: Você recebeu um vale-presente da empresa! 🎁
Conteúdo: É um bônus por desempenho, clique aqui[link] para receber.
O remetente é "rh@empresa-rh.com.br".\n
O que você faz?
a) Clica, o reconhecimento tarda mas não falha
b) Encaminha para o time de TI/RH sem clicar. Melhor confirmar, né...
c) Deleta sem reportar, é spam obviamente""")
    resposta1 = input("Alternativa: ")

    if resposta1 == "a":
        print(f"\nHmm... decisão tomada, {nome}. Vamos ver como isso afeta o resto...")
    elif resposta1 == "b":
        print(f"\n{nome}... boa escolha. Ou foi? 👀")
        pontos += 10
    else:
        print(f"\nRápido e direto, {nome}. Mas será que foi a melhor escolha?")
        pontos += 5
    sleep(1)
    print(f"\nAté aqui você tem: {pontos} pontos. Será que você soube lidar com essa situação...?")
    return pontos, nome

def etapa2(pontos, nome):
    if pontos == 0:
        print("""\n⚠️ {nome}, você clicou no link sem confirmar...
💡 Dica: o domínio correto seria '@empresa.com.br'. Pequeno detalhe, grande consequência.
🔍 Pesquise depois: phishing e spoofing de e-mail.""")
        sleep(1)
        # cenário difícil
        pass
    elif pontos == 5:
        # cenário médio
        pass
    else:
        # cenário tranquilo
        pass

"""Caminho A — pontos == 0 (errou feio):

😬 SITUAÇÃO 2 — Você recebeu um e-mail do seu próprio chefe pedindo pra
transferir um arquivo confidencial para um link externo com urgência.
O e-mail parece legítimo, tem o nome e a foto dele.

O que você faz?
a) Transfere, veio do chefe
b) Liga pro chefe pra confirmar antes de fazer qualquer coisa
c) Encaminha pro time de TI e aguarda
a → 0 pontos
b → 10 pontos
c → 5 pontos

Caminho B — pontos == 5 (foi razoável):

📧 SITUAÇÃO 2 — Você recebeu um e-mail pedindo pra redefinir sua senha
corporativa clicando num link. O remetente parece ser o suporte de TI.

O que você faz?
a) Clica e redefine, veio do suporte
b) Acessa o sistema diretamente pelo navegador sem clicar no link
c) Responde o e-mail perguntando se é legítimo
a → 0 pontos
b → 10 pontos
c → 5 pontos

Caminho C — pontos == 10 (acertou):

✅ SITUAÇÃO 2 — Um colega te manda uma mensagem no chat interno com um
link dizendo "olha isso, é sobre você". O link parece estranho.

O que você faz?
a) Clica, veio de um colega conhecido
b) Pergunta pro colega o que é antes de clicar
c) Ignora e deleta
a → 0 pontos
b → 10 pontos
c → 5 pontos
        print(''\n🚨 SITUAÇÃO 1: Você recebeu um e-mail do 'RH' pedindo para clicar num link e atualizar seus dados bancários com urgência.
    O que você faz?
    a) Clica no link, afinal veio do RH
    b) Encaminha pro time de TI e não clica em nada
    c) Deleta o e-mail e ignora')
    resposta1 = input("Alternativa: ")"""

def etapa3(pontos, nome):
    pass

def etapa4(pontos, nome):
    pass

def etapa5(pontos, nome):
    pass

def resultado(pontos, nome):
    pass

#Programa principal
if __name__ == "__main__":
    pontos = 0
    um, nome = etapa1(pontos)
    dois = etapa2(um, nome)
    tres = etapa3(dois, nome)
    quatro = etapa4(tres, nome)
    cinco = etapa5(quatro, nome)
    resultado(cinco, nome)