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

### Exemplos
1. Introdução ao jogo e posicionamento da frota:
<img width="927" height="369" alt="image" src="https://github.com/user-attachments/assets/69468474-7cb0-4605-bbbf-2f55e3d29f4d" />

2. Tabuleiro do computador e do jogador
<img width="754" height="461" alt="image" src="https://github.com/user-attachments/assets/0efb6e10-75d1-41db-aec3-b05c1cd22789" />

3. Ataque do jogador e do computador
<img width="462" height="180" alt="image" src="https://github.com/user-attachments/assets/960c9c35-139f-444f-ab07-d19f3cc4a9ba" />

4. Atualização do tabuleiro
<img width="546" height="455" alt="image" src="https://github.com/user-attachments/assets/a10d690e-6bd0-439d-8eeb-93d44e22415e" />

5. Ao afundar uma embarcação, você tem direito a uma nova jogada
<img width="765" height="356" alt="image" src="https://github.com/user-attachments/assets/22c52c87-915c-4755-904a-ed9f4f3113df" />

6. O jogo não permite atacar duas vezes a mesma posição
<img width="574" height="325" alt="image" src="https://github.com/user-attachments/assets/79821619-8dd7-4116-995d-7a8781346bbd" />

7. Encerramento do jogo após a última frota ser afundada
<img width="659" height="237" alt="image" src="https://github.com/user-attachments/assets/6f19557f-4f22-456f-8710-547e53ab273d" />

# 👥 Equipe Desenvolvedora
### Victor Hugo Carlim Pedroni dos Passos
### Pedro Henrique Camilo
### Felipe Henrique Hatschbach
