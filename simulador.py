"""Treinamento de Segurança da Informação — Simulador de Incidente.
Você é um funcionário novo na empresa. A cada situação, escolha como reagiria.
No final, descobre se está pronto pra trabalhar com segurança ou precisa de mais treinamento."""

from time import sleep

#region Introdução
print("""\nBem-vindo(a) ao SecureQuest! 🎮
Você está prestes a enfrentar situações reais do dia a dia corporativo.
Será que tomará as decisões certas?\n""")
print("-" * 60)
print("""\n🎮 A cada situação, escolha como você reagiria.
⚠️  Atenção: suas escolhas têm consequências, errar pode tornar as próximas situações mais difíceis.

No final, você descobre se está pronto para navegar com segurança no ambiente digital... ou se precisa estudar mais. 👀""")
sleep(1)
nome = input("\nAntes de começarmos... qual o seu nome?\n").strip().capitalize()
print(f"\nCerto, certo... {nome}. Vamos começar!\n")
sleep(1)
print("-" * 60)
#endregion

#region Funções

#region Etapa 1
def etapa1(pontos, nome):
    print("""\n📧 SITUAÇÃO 1: Você recebeu um e-mail:
Assunto: Você recebeu um vale-presente da empresa! 🎁
Conteúdo: É um bônus por desempenho, clique aqui[link] para receber.
O remetente é "rh@empresa-rh.com.br".

O que você faz?
a) Clica, o reconhecimento tarda mas não falha
b) Encaminha para o time de TI/RH sem clicar. Melhor confirmar, né...
c) Deleta sem reportar, é spam obviamente""")
    resposta = input("\nAlternativa: ")

    if resposta == "a":
        print(f"\nHmm... decisão tomada, {nome}. Vamos ver como isso afeta o resto...")
    elif resposta == "b":
        print(f"\n{nome}... boa escolha. Ou foi? 👀")
        pontos += 10
    else:
        print(f"\nRápido e direto, {nome}. Mas será que foi a melhor escolha?")
        pontos += 5
    sleep(1)
    print(f"\nAté aqui você tem: {pontos} pontos.")
    print("\n" + "-" * 60)
    return pontos, nome
#endregion

#region Etapa 2
def etapa2(pontos, nome):

    if pontos == 0:
        print(f"""\n⚠️  {nome}, você clicou no link sem confirmar...
💡 Num cenário real, esse clique poderia ter causado um vazamento de dados da empresa. Ainda bem que aqui é só um simulador, né?!
Por isso, antes de clicar em qualquer link, sempre verifique o remetente, ok?
Geralmente, o remetente correto seria: 'rh@empresa.com.br'. Fique atento!""")
        print("\n" + "-" * 60)
        sleep(1)
        print("""\n🔐 SITUAÇÃO 2: Seu colega de TI te manda uma mensagem no Teams:
'Ei, tô sem acesso aqui e o cliente tá esperando. Você pode me
passar seu login e senha do sistema de gestão só por hoje?
Prometo que troco minha senha assim que resolver.'

Vocês trabalham juntos há 2 anos. Você confia nele.

O que você faz?
a) Aciona o suporte para liberar um acesso temporário pra ele
b) Fala que não pode, mas abre o sistema e faz o que ele precisa supervisionando
c) Passa o login, é colega de confiança e é urgente""")
        resposta = input("\nAlternativa: ")

        if resposta == "a":
            print(f"\nBurocracia tem seu valor, {nome}. 😏")
        elif resposta == "b":
            print(f"\nHm... solução improvisada. Vamos ver como isso se desdobra... 🤔")
            pontos += 10
        else:
            print(f"\nDois anos de parceria pesam na balança, né {nome}? 😬")
            pontos += 5

    elif pontos == 5:
        print(f"""\n🤔 {nome}, você deletou sem reportar...
Spam óbvio? Talvez. Mas o time de TI precisaria saber pra bloquear o remetente pra empresa inteira.
Vamos ver se dessa vez você pensa um pouco mais... 😏""")
        print("\n" + "-" * 60)
        sleep(1)
        print("""\n💬 SITUAÇÃO 2: Seu colega de TI te manda uma mensagem no Teams:
"Ei, tô sem acesso aqui e o cliente tá esperando. Você pode me
passar seu login e senha só por hoje? Amanhã eu resolvo o meu acesso."

O que você faz?
a) Passa o login, é só por hoje e o cliente tá esperando
b) Aciona o suporte pra liberar um acesso temporário pra ele
c) Abre o sistema você mesmo e faz o que ele precisa, supervisionando""")
        resposta = input("\nAlternativa: ")

        if resposta == "a":
            print(f"\nCliente esperando é pressão, né {nome}... mas a pressa compromete a segurança da empresa. 🤔")
        elif resposta == "b":
            print(f"\n✅ Exato, {nome}! Acesso temporário pelo suporte garante rastreabilidade e não compromete suas credenciais.")
            pontos += 10
        else:
            print(f"\nSolução criativa, {nome}. Mas criativo nem sempre significa seguro... 😏")
            pontos += 5

    elif pontos == 10:
        print(f"""\n✅ {nome}, boa decisão na situação anterior!
Encaminhar para o time de TI sem clicar protege não só você... eles bloqueiam o remetente para a empresa inteira.
Agora vamos ver se você mantém o foco... 😏""")
        print("\n" + "-" * 60)
        sleep(1)
        print("""\n💬 SITUAÇÃO 2: Seu colega de TI te manda uma mensagem no Teams:
"Ei, tô sem acesso aqui. Você pode me passar seu login e senha?
É rapidinho!"

O que você faz?
a) Passa o login e senha, é rapidinho mesmo
b) Ah, é só dessa vez né... aciona o suporte para liberar um acesso temporário
c) Manda o login e senha, senha e CPF só para garantir 🙃""")
        resposta = input("\nAlternativa: ")

        if resposta == "a":
            print(f"\nRapidinho mesmo, {nome}... dá nada não, certo? 🤔")
        elif resposta == "b":
            print(f"\n✅ Exato, {nome}! Credenciais são intransferíveis. Cada acesso precisa ser rastreável individualmente.")
            pontos += 10
        else:
            print(f"\n😂 {nome}... CPF também não! Você acabou de entregar a vida inteira.")
            pontos += 5

    sleep(1)
    print(f"\nAté aqui você tem: {pontos} pontos.")
    print("\n" + "-" * 60)
    return pontos, nome
#endregion

#region Etapa 3
def etapa3(pontos, nome):

    if pontos <= 5:
        print(f"""\n😬 {nome}, até agora você clicou em link suspeito e compartilhou suas credenciais.
São dois erros graves que num cenário real poderiam comprometer você e a empresa inteira.
Mas ainda dá tempo de virar o jogo... ou não. 👀""")
        print("\n" + "-" * 60)
        sleep(1)
        print("""\n🔐 SITUAÇÃO 3: Você precisa criar uma senha para o sistema interno.
O sistema pede no mínimo 8 caracteres.

Qual você escolhe?
a) "Empresa@2024" — tem letra, número e símbolo
b) "E$7kM#2xQ!" — gerada pelo gerenciador de senhas
c) "Sistema@TI1" — fácil de lembrar e tem símbolo""")
        resposta = input("\nAlternativa: ")

        if resposta == "a":
            print(f"\nParece forte, né {nome}? Mas 'Empresa@2024' é exatamente o que um hacker testa primeiro. 😬")
        elif resposta == "b":
            print(f"\n✅ Isso, {nome}! Senha aleatória gerada por gerenciador é o padrão ouro. Sem padrão, sem brecha.")
            pontos += 10
        else:
            print(f"\n😬 {nome}... 'Sistema@TI1' tá quase gritando o que é. Evite qualquer referência ao trabalho na senha.")
            pontos += 5

    elif 5 < pontos <= 15:
        print(f"""\n🤔 {nome}, você acertou em algumas situações mas ainda escorregou em outras.
Segurança é consistência... um erro no meio do caminho já abre brecha.
Vamos ver como você se sai agora... 😏""")
        print("\n" + "-" * 60)
        sleep(1)
        print("""\n🔐 SITUAÇÃO 3: Você precisa criar uma senha para o sistema interno.
O sistema pede no mínimo 8 caracteres.

Qual você escolhe?
a) "Maria1990!" — fácil de lembrar, tem símbolo e número
b) "E$7kM#2xQ!" — gerada pelo gerenciador de senhas
c) "Flamengo@Campeão" — longa e tem símbolo""")
        resposta = input("\nAlternativa: ")

        if resposta == "a":
            print(f"\n😬 {nome}, nome e ano de nascimento são os primeiros dados que um hacker testa. Evite dados pessoais!")
        elif resposta == "b":
            print(f"\n✅ Isso, {nome}! Senha aleatória gerada por gerenciador é o padrão ouro.")
            pontos += 10
        else:
            print(f"\n🤔 {nome}, longa é bom... mas time de futebol é previsível demais. Tente algo sem significado pessoal.")
            pontos += 5

    elif pontos >= 20:
        print(f"""\n✅ {nome}, você tem se saído muito bem até aqui!
Suas decisões mostram que você entende os riscos do ambiente digital.
Mas não baixe a guarda agora... 😏""")
        print("\n" + "-" * 60)
        sleep(1)
        print("""\n🔐 SITUAÇÃO 3: Você precisa criar uma senha para o sistema interno.
O sistema pede no mínimo 8 caracteres.

Qual você escolhe?
a) "123456789" — simples e fácil de lembrar
b) "E$7kM#2xQ!" — gerada pelo gerenciador de senhas
c) "senha123" — clássico, né?""")
        resposta = input("\nAlternativa: ")

        if resposta == "a":
            print(f"\n😂 {nome}... 123456789 é a primeira senha que qualquer hacker testa. Literalmente.")
        elif resposta == "b":
            print(f"\n✅ Perfeito, {nome}! Você já sabe o que é uma senha forte. Siga sempre assim!")
            pontos += 10
        else:
            print(f"\n😂 {nome}... 'senha123' é quase um convite. Bora evitar isso, tá?")
            pontos += 5

    sleep(1)
    print(f"\nAté aqui você tem: {pontos} pontos.")
    print("\n" + "-" * 60)
    return pontos, nome
#endregion

#endregion

#region Resultado
def resultado(pontos, nome):
    print("\n" + "=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)
    print(f"\n{nome}, você fez {pontos} pontos!\n")

    if pontos >= 25:
        print("🏆 Parabéns! Você está pronto para navegar com segurança no ambiente digital!")
    elif pontos >= 15:
        print("💪 Quase lá! Você tem boas noções de segurança, mas ainda há pontos a melhorar.")
    else:
        print("📚 Hmm... Recomendamos refazer o treinamento. Segurança digital é coisa séria!")

    print("\nObrigado por participar do SecureQuest! 🛡️")
#endregion

#region Programa principal
if __name__ == "__main__":
    pontos = 20
    nome = "Cah"
    # um, nome = etapa1(pontos, nome)
    # dois, nome = etapa2(pontos, nome)
    tres, nome = etapa3(pontos, nome)
    resultado(tres, nome)
#endregion