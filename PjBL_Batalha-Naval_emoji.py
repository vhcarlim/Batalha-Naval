import random
import time

FROTA = {
    "Porta-aviões": 5,
    "Navio-tanque": 4,
    "Contratorpedeiro": 3,
    "Submarino": 2,
    "Destroier": 1
}

def cria_tabuleiro_oculto():
    """Retorna uma matriz 10x10 preenchida com zeros (lógica)."""
    return [[0 for _ in range(10)] for _ in range(10)]

def cria_tabuleiro_visivel():
    """Retorna uma matriz 10x10 preenchida com emojis de água (visual)."""
    return [["🟦" for _ in range(10)] for _ in range(10)]

def exibe_tabuleiros(tab_visivel_pc, tab_visivel_jog, navios_pc, navios_jog):
    """Exibe os tabuleiros alinhados, com réguas numéricas e sem colchetes."""
    print("\n" + "═"*45)
    print("🤖 TABULEIRO DO COMPUTADOR")
    print("   0  1  2  3  4  5  6  7  8  9") # Régua superior
    for i, linha in enumerate(tab_visivel_pc):
        print(f"{i} {' '.join(linha)}") # Número da linha + emojis separados por espaço
    print(f"🚢 Embarcações inimigas restantes: {navios_pc}")
    
    print("\n🧑 SEU TABULEIRO")
    print("   0  1  2  3  4  5  6  7  8  9")
    for i, linha in enumerate(tab_visivel_jog):
        print(f"{i} {' '.join(linha)}")
    print(f"🚢 Suas embarcações restantes: {navios_jog}")
    print("═"*45 + "\n")

def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite um número inteiro.")

def valida_posicao(tabuleiro, linha, coluna, tamanho, orientacao):
    if orientacao not in ['H', 'V']:
        return False
    
    for i in range(tamanho):
        if orientacao == 'H':
            if coluna + i >= 10 or tabuleiro[linha][coluna + i] != 0:
                return False
        else: 
            if linha + i >= 10 or tabuleiro[linha + i][coluna] != 0:
                return False
    return True

def posiciona_navio_pc(tab_oculto):
    coords_navios = {}
    for nome, tamanho in FROTA.items():
        posicionado = False
        while not posicionado:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            orientacao = random.choice(['H', 'V'])
            
            if valida_posicao(tab_oculto, linha, coluna, tamanho, orientacao):
                coords = []
                for i in range(tamanho):
                    if orientacao == 'H':
                        tab_oculto[linha][coluna + i] = 1
                        coords.append((linha, coluna + i))
                    else:
                        tab_oculto[linha + i][coluna] = 1
                        coords.append((linha + i, coluna))
                coords_navios[nome] = coords
                posicionado = True
    return coords_navios

def posiciona_navio_jogador(tab_oculto):
    coords_navios = {}
    print("\n" + "⚓"*20)
    print("       POSICIONAMENTO DA SUA FROTA")
    print("⚓"*20)
    
    for nome, tamanho in FROTA.items():
        posicionado = False
        while not posicionado:
            print(f"\n🗺️  Posicionando: {nome} (Tamanho: {tamanho} blocos)")
            linha = ler_inteiro("👉 Linha inicial (0-9): ")
            coluna = ler_inteiro("👉 Coluna inicial (0-9): ")
            orientacao = input("👉 Orientação (H para horizontal, V para vertical): ").strip().upper()
            
            if 0 <= linha <= 9 and 0 <= coluna <= 9:
                if valida_posicao(tab_oculto, linha, coluna, tamanho, orientacao):
                    coords = []
                    for i in range(tamanho):
                        if orientacao == 'H':
                            tab_oculto[linha][coluna + i] = 1
                            coords.append((linha, coluna + i))
                        else:
                            tab_oculto[linha + i][coluna] = 1
                            coords.append((linha + i, coluna))
                    coords_navios[nome] = coords
                    posicionado = True
                    print(f"✅ {nome} posicionado com sucesso!")
                else:
                    print("⚠️  Posição inválida! O navio sai do mapa ou bate em outro. Tente novamente.")
            else:
                print("⚠️  Coordenadas fora do limite! Escolha entre 0 e 9.")
    return coords_navios

def atacar(linha, coluna, tab_oculto, tab_visivel, coords_navios):
    if tab_visivel[linha][coluna] != "🟦":
        return 'ERRO' 
    
    if tab_oculto[linha][coluna] == 1:
        tab_visivel[linha][coluna] = '💥' # Emoji de acerto
        for nome, coords in coords_navios.items():
            if (linha, coluna) in coords:
                coords.remove((linha, coluna))
                if len(coords) == 0:
                    return 'AFUNDOU'
                return 'ACERTO'
    else:
        tab_visivel[linha][coluna] = '💦' # Emoji de água/erro
        return 'AGUA'

def turno_jogador(tab_oculto_pc, tab_visivel_pc, coords_navios_pc, navios_restantes, tab_visivel_jog, navios_jog_restantes):
    while True:
        print("\n🎯 --- SUA VEZ DE ATACAR --- 🎯")
        linha = ler_inteiro("Qual linha deseja atacar? (0-9): ")
        coluna = ler_inteiro("Qual coluna deseja atacar? (0-9): ")
        
        if not (0 <= linha <= 9 and 0 <= coluna <= 9):
            print("⚠️  Coordenadas fora do radar! Tente novamente.")
            continue
            
        print("\nLançando míssil...")
        time.sleep(1) # Cria um suspense dramático de 1 segundo
        
        resultado = atacar(linha, coluna, tab_oculto_pc, tab_visivel_pc, coords_navios_pc)
        
        if resultado == 'ERRO':
            print("❌ Você já atacou essa posição, comandante! Escolha outra.")
            continue
        elif resultado == 'AGUA':
            print("💦 SPLASH! Tiro na água... Não foi dessa vez.")
            break 
        elif resultado == 'ACERTO':
            print("💥 KABOOM! Acerto confirmado! Você atingiu uma embarcação!")
            break 
        elif resultado == 'AFUNDOU':
            navios_restantes -= 1
            print("🐙 Do you fear death? 🚨 Você AFUNDOU um navio inimigo por completo! 🚨")
            if navios_restantes > 0:
                print("⚡ Vai com calma, Davy Jones e o Holandês Voador! Você afundou um navio, agora tem direito a um NOVO ATAQUE!⚡")
                exibe_tabuleiros(tab_visivel_pc, tab_visivel_jog, navios_restantes, navios_jog_restantes) 
                continue 
            else:
                break
                
    return navios_restantes

def turno_pc(tab_oculto_jog, tab_visivel_jog, coords_navios_jog, navios_restantes):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        
        resultado = atacar(linha, coluna, tab_oculto_jog, tab_visivel_jog, coords_navios_jog)
        
        if resultado == 'ERRO':
            continue 
            
        print("\n💻 --- VEZ DO COMPUTADOR --- 💻")
        time.sleep(1)
        print(f"📡 O Inimigo mirou na linha {linha}, coluna {coluna}...")
        time.sleep(1)
        
        if resultado == 'AGUA':
            print("💦 SPLASH! O computador errou e acertou os peixes!")
            break
        elif resultado == 'ACERTO':
            print("💥 IMPACTO! O computador acertou uma de suas embarcações!")
            break
        elif resultado == 'AFUNDOU':
            navios_restantes -= 1
            print("☠️  SITUAÇÃO CRÍTICA! O computador AFUNDOU um dos seus navios!")
            if navios_restantes > 0:
                print("⚡ O inimigo ganhou um ATAQUE EXTRA! ⚡")
                continue
            else:
                break
                
    return navios_restantes

def main():
    print("🌊"*20)
    print("       BEM-VINDO AO BATALHA NAVAL       ")
    print("🌊"*20)
    
    tab_oculto_pc = cria_tabuleiro_oculto()
    tab_oculto_jog = cria_tabuleiro_oculto()
    
    # Agora os tabuleiros visíveis iniciam cheios de água
    tab_visivel_pc = cria_tabuleiro_visivel()
    tab_visivel_jog = cria_tabuleiro_visivel()
    
    coords_navios_pc = posiciona_navio_pc(tab_oculto_pc)
    coords_navios_jog = posiciona_navio_jogador(tab_oculto_jog)
    
    navios_pc_restantes = 5
    navios_jog_restantes = 5
    
    while True:
        exibe_tabuleiros(tab_visivel_pc, tab_visivel_jog, navios_pc_restantes, navios_jog_restantes)
        
        navios_pc_restantes = turno_jogador(tab_oculto_pc, tab_visivel_pc, coords_navios_pc, navios_pc_restantes, tab_visivel_jog, navios_jog_restantes)
        if navios_pc_restantes == 0:
            print("\n🏆 VITÓRIA MAGNÍFICA! Você afundou toda a frota inimiga! \n🏴‍☠️ This is the day you will always remember as the day you almost caught Captain Jack Sparrow!")
            break
            
        navios_jog_restantes = turno_pc(tab_oculto_jog, tab_visivel_jog, coords_navios_jog, navios_jog_restantes)
        if navios_jog_restantes == 0:
            print("\n🩻 Nothing personal, Jack... it's just good business! \n💀 O computador destruiu sua última embarcação.")
            break

    print("\n" + "═"*45)
    print("Jogo desenvolvido por: Victor Hugo Carlim, Pedro Henrique Camilo e Felipe Henrique Hatschbach.")
    print("Obrigado por jogar nosso jogo! Até a próxima batalha naval!")
    print("═"*45 + "\n")

if __name__ == "__main__":
    main()