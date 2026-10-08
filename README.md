# 🎮 SecureQuest — Simulador de Incidente de Segurança

Simulador interativo de treinamento em segurança da informação. Você assume o papel de um funcionário novo e precisa tomar as decisões certas diante de situações reais do dia a dia corporativo. No final, descobre se está pronto para navegar com segurança no ambiente digital... ou se precisa estudar mais.

---

## O que ele simula

- **Etapa 1 — Phishing:** um e-mail suspeito de vale-presente chega na sua caixa. O que você faz?
- **Etapa 2 — Engenharia social:** um colega pede suas credenciais com urgência. Você cede?
- **Etapa 3 — Senha segura:** na hora de criar uma senha, qual escolha você faz?

Cada decisão acumula (ou não) pontos. O resultado final classifica o jogador em três faixas.

---

## Tecnologias

- Python 3
- Biblioteca nativa: `time` (`sleep`)
- Git e GitHub

---

## Arquivo

- `simulador.py` — script principal com introdução, etapas e resultado final

---

## Como executar

```bash
git clone https://github.com/cah-menezes/simulador-incidente-python.git
cd simulador-incidente-python
python3 simulador.py
```

---

## Conceitos aplicados

- `def` com múltiplos `return`
- `if / elif / else`
- `f-string`
- `if __name__ == "__main__"`
- `from time import sleep`
- `input` e `print`