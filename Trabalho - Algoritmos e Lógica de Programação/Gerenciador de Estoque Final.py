# ============================================================
# DESAFIO DE AUTOMAÇÃO DIGITAL
# Gestão de Peças, Qualidade e Armazenamento
# ============================================================


# ============================================================
# LISTAS PRINCIPAIS DO SISTEMA
# ============================================================

# Armazena todas as peças que foram aprovadas
pecas_aprovadas = []

# Armazena todas as peças que foram reprovadas
pecas_reprovadas = []

# Armazena as peças da caixa que está sendo preenchida
caixa_atual = []

# Armazena as caixas que já atingiram 10 peças
caixas_fechadas = []


# ============================================================
# FUNÇÃO DE CADASTRAMENTO
# ============================================================

def cadastrar_peca():

    print("\n========================================")
    print("           CADASTRO DE PEÇA")
    print("========================================")

    # Recebe os dados da peça
    id_peca = int(input("Digite o ID da peça: "))
    peso = float(input("Digite o peso da peça: "))
    comprimento = float(input("Digite o comprimento da peça: "))
    cor = input("Digite a cor da peça: ")

    # Cria um dicionário para organizar os dados da peça
    peca = {
        'id': id_peca,
        'peso': peso,
        'comprimento': comprimento,
        'cor': cor
    }

    # Envia os dados para a função que verifica a qualidade
    status, motivos = avaliar_peca(peso, cor, comprimento)

    # Adiciona o resultado da avaliação ao dicionário
    peca["status"] = status
    peca["motivos"] = motivos

    # Se a peça estiver dentro dos padrões,
    # ela é adicionada às peças aprovadas e à caixa
    if status == "Aprovado":

        pecas_aprovadas.append(peca)
        adicionar_na_caixa(peca)

        print("\n>>> PEÇA APROVADA!")
        print(f"Peça {id_peca} adicionada ao estoque.")

    # Caso contrário, a peça é armazenada
    # na lista de peças reprovadas
    else:

        pecas_reprovadas.append(peca)

        print("\n>>> PEÇA REPROVADA!")
        print("Motivos:")

        for motivo in motivos:
            print(f"- {motivo}")

    print("\nPeça cadastrada com sucesso!")


# ============================================================
# FUNÇÃO DE AVALIAÇÃO DA QUALIDADE
# ============================================================

def avaliar_peca(peso, cor, comprimento):

    # Lista que armazenará os motivos da reprovação
    motivos = []

    # Verifica se o peso está entre 95g e 105g
    if peso > 105 or peso < 95:
        motivos.append("Peso fora do padrão")

    # Verifica se a cor é azul ou verde
    if cor != "azul" and cor != "verde":
        motivos.append("Cor fora do padrão")

    # Verifica se o comprimento está entre 10cm e 20cm
    if comprimento < 10 or comprimento > 20:
        motivos.append("Tamanho fora do padrão")

    # Se existir algum motivo, a peça será reprovada
    if len(motivos) != 0:
        return "Reprovado", motivos

    # Se nenhum critério foi violado, a peça é aprovada
    else:
        return "Aprovado", motivos


# ============================================================
# FUNÇÃO DE ORGANIZAÇÃO DAS CAIXAS
# ============================================================

def adicionar_na_caixa(peca):

    # Adiciona a peça na caixa que está sendo preenchida
    caixa_atual.append(peca)

    # Quando a caixa atingir 10 peças,
    # ela é considerada fechada
    if len(caixa_atual) == 10:

        # Cria uma cópia da caixa atual
        # e adiciona às caixas fechadas
        caixas_fechadas.append(caixa_atual.copy())

        # Esvazia a caixa atual para começar uma nova
        caixa_atual.clear()

        print("\n>>> CAIXA FECHADA!")
        print("A caixa atingiu o limite de 10 peças.")


# ============================================================
# FUNÇÃO PARA REORGANIZAR AS CAIXAS
# ============================================================

def reorganizar_caixas():

    # Limpa as caixas existentes
    caixa_atual.clear()
    caixas_fechadas.clear()

    # Percorre novamente todas as peças aprovadas
    # e monta as caixas do zero
    for peca in pecas_aprovadas:
        adicionar_na_caixa(peca)


# ============================================================
# FUNÇÃO PARA LISTAR AS PEÇAS
# ============================================================

def listar_pecas():

    print("\n========================================")
    print("          PEÇAS APROVADAS")
    print("========================================")

    # Verifica se existem peças aprovadas
    if len(pecas_aprovadas) == 0:
        print("Nenhuma peça aprovada cadastrada.")

    # Mostra todas as peças aprovadas
    for peca in pecas_aprovadas:

        print(f"\nID: {peca['id']}")
        print(f"Peso: {peca['peso']} g")
        print(f"Comprimento: {peca['comprimento']} cm")
        print(f"Cor: {peca['cor']}")
        print("Status: Aprovado")
        print("----------------------------------------")


    print("\n========================================")
    print("          PEÇAS REPROVADAS")
    print("========================================")

    # Verifica se existem peças reprovadas
    if len(pecas_reprovadas) == 0:
        print("Nenhuma peça reprovada cadastrada.")

    # Mostra todas as peças reprovadas
    for peca in pecas_reprovadas:

        print(f"\nID: {peca['id']}")
        print(f"Peso: {peca['peso']} g")
        print(f"Comprimento: {peca['comprimento']} cm")
        print(f"Cor: {peca['cor']}")
        print("Status: Reprovado")

        print("Motivos:")

        for motivo in peca["motivos"]:
            print(f"- {motivo}")

        print("----------------------------------------")


# ============================================================
# FUNÇÃO PARA REMOVER UMA PEÇA
# ============================================================

def remover_peca():

    print("\n========================================")
    print("            REMOVER PEÇA")
    print("========================================")

    id_remover = int(input("Digite o ID da peça que deseja remover: "))

    encontrada = False

    # Procura a peça entre as aprovadas
    for peca in pecas_aprovadas:

        if peca["id"] == id_remover:

            pecas_aprovadas.remove(peca)

            # Como uma peça aprovada foi removida,
            # as caixas precisam ser reorganizadas
            reorganizar_caixas()

            encontrada = True

            print("\n>>> Peça removida com sucesso!")

            return


    # Procura a peça entre as reprovadas
    for peca in pecas_reprovadas:

        if peca["id"] == id_remover:

            pecas_reprovadas.remove(peca)

            encontrada = True

            print("\n>>> Peça removida com sucesso!")

            return


    # Caso o ID não tenha sido encontrado
    if not encontrada:
        print("\n>>> Peça não encontrada no sistema.")


# ============================================================
# FUNÇÃO PARA LISTAR AS CAIXAS
# ============================================================

def listar_caixas():

    print("\n========================================")
    print("             CAIXAS FECHADAS")
    print("========================================")

    # Verifica se existe alguma caixa fechada
    if len(caixas_fechadas) == 0:

        print("Nenhuma caixa fechada.")

    # Percorre cada caixa fechada
    for numero, caixa in enumerate(caixas_fechadas, start=1):

        print(f"\n----------- CAIXA {numero} -----------")
        print(f"Quantidade de peças: {len(caixa)}")

        # Mostra as peças daquela caixa
        for peca in caixa:

            print(
                f"ID: {peca['id']} | "
                f"Peso: {peca['peso']}g | "
                f"Comprimento: {peca['comprimento']}cm | "
                f"Cor: {peca['cor']}"
            )


    print("\n========================================")
    print("              CAIXA ATUAL")
    print("========================================")

    # Mostra a caixa que ainda está sendo preenchida
    print(f"Quantidade de peças: {len(caixa_atual)}/10")

    if len(caixa_atual) == 0:

        print("Nenhuma peça na caixa atual.")

    else:

        for peca in caixa_atual:

            print(
                f"ID: {peca['id']} | "
                f"Peso: {peca['peso']}g | "
                f"Comprimento: {peca['comprimento']}cm | "
                f"Cor: {peca['cor']}"
            )


# ============================================================
# FUNÇÃO PARA GERAR O RELATÓRIO FINAL
# ============================================================

def gerar_relatorio():

    # Conta as peças aprovadas e reprovadas
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)

    # Soma as duas quantidades
    total_geral = total_aprovadas + total_reprovadas

    # Conta as caixas fechadas
    total_caixas = len(caixas_fechadas)

    # Se existir uma caixa atual com peças,
    # ela também está sendo utilizada
    if len(caixa_atual) > 0:
        total_caixas += 1


    print("\n========================================")
    print("            RELATÓRIO FINAL")
    print("========================================")

    print(f"\nPeças aprovadas: {total_aprovadas}")
    print(f"Peças reprovadas: {total_reprovadas}")
    print(f"Total de peças: {total_geral}")
    print(f"Caixas utilizadas: {total_caixas}")


    print("\n========================================")
    print("       MOTIVOS DAS REPROVAÇÕES")
    print("========================================")

    # Mostra os motivos de cada peça reprovada
    if total_reprovadas == 0:

        print("Nenhuma peça foi reprovada.")

    else:

        for peca in pecas_reprovadas:

            print(f"\nPeça ID {peca['id']}:")

            for motivo in peca["motivos"]:
                print(f"- {motivo}")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def mostrar_menu():

    while True:

        print("\n")
        print("========================================")
        print("       GERENCIADOR DE ESTOQUE")
        print("========================================")
        print("1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas")
        print("5 - Gerar relatório")
        print("0 - Sair")
        print("========================================")

        opcao = int(input("Escolha uma opção: "))


        # Seleciona a função de acordo com a opção escolhida
        match opcao:

            case 1:
                cadastrar_peca()

            case 2:
                listar_pecas()

            case 3:
                remover_peca()

            case 4:
                listar_caixas()

            case 5:
                gerar_relatorio()

            case 0:
                print("\n========================================")
                print("       PROGRAMA ENCERRADO")
                print("========================================")
                break

            case _:
                print("\n>>> Opção inválida. Tente novamente.")


# ============================================================
# INÍCIO DO PROGRAMA
# ============================================================

print("\n")
print("========================================")
print("     SISTEMA DE GESTÃO DE PEÇAS")
print("========================================")
print("      Automação de Qualidade")
print("========================================")

mostrar_menu()