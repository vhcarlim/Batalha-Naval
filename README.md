# ⚓ Batalha Naval - Raciocínio Algorítmico

Sistemas computacionais baseados em matrizes para simulação do clássico jogo de tabuleiro Batalha Naval, desenvolvido como atividade somativa para a disciplina de Raciocínio Algorítmico na **PUCPR**

---

## 📝 Sobre o Projeto

O projeto consiste em uma versão simplificada e modernizada do jogo Batalha Naval, implementada na linguagem Python e executada diretamente no terminal de comando.
O jogo opera no modo **Humano x Computador**, onde o jogador enfrenta a inteligência artificial do programa em turnos alternados.

O grande diferencial desta versão foi a implementação completa do **Desafio (Nota Extra)**, que engloba a frota original com embarcações de múltiplos tamanhos e a regra de turno extra ao afundar um navio.

---

## 🚀 Funcionalidades e Requisitos Atendidos

O código foi integralmente estruturado para cumprir todas as exigências acadêmicas do projeto:

**Estrutura Base**: Tabuleiros gerados dinamicamente a partir de matrizes $10\times10$.
**Modularização**: Código 100% organizado e limpo, distribuído em funções com responsabilidades únicas.
**Posicionamento da Frota**: 
O **Jogador** define manualmente a linha, coluna e orientação (Horizontal ou Vertical) de suas peças.
O **Computador** distribui suas peças de forma completamente aleatória e automatizada.
* **Interface Fluida**: 
  * Feedback visual em tempo real utilizando Emojis (`🟦` Água, `💥` Acerto, `💦` Erro).
  * Alinhamento milimétrico do tabuleiro com réguas numéricas de coordenadas no terminal.
  * Sistema de *delay* dramático de 1 segundo que simula o disparo dos mísseis.
**Tratamento de Exceções**: Sistema robusto de validação de entradas que impede o travamento ou quebra do programa caso o usuário digite dados inválidos (como letras nas coordenadas).

### 🚢 A Frota
O jogo utiliza as 5 embarcações tradicionais do jogo de tabuleiro[cite: 44]:
1. **Porta-aviões**: Ocupa 5 posições.
2. **Navio-tanque**: Ocupa 4 posições.
3. **Contratorpedeiro**: Ocupa 3 posições.
4. **Submarino**: Ocupa 2 posições.
5. **Destroier**: Ocupa 1 posição.

>💡 **Regra**: Conforme as especificações do desafio, um navio só é considerado destruído quando todas as suas partes forem atingidas. Quem afundar a embarcação por completo ganha o direito de realizar um **Ataque Extra** imediatamente.

---

## 🕹️ Como Jogar

### Pré-requisitos
* Python instalado em sua máquina.

### Passo a Passo
1. Clone o repositório para a sua máquina local.
2. Navegue até a pasta do projeto.
3. Execute o arquivo principal do jogo.
4. Siga as instruções do terminal para posicionar seus navios.
5. Digite as coordenadas de linha (0-9) e coluna (0-9) para atacar a frota inimiga quando for a sua vez!

# 👥 Equipe Desenvolvedora
### Victor Hugo Carlim Pedroni dos Passos
### Pedro Henrique Camilo
### Felipe Henrique Hatschbach
