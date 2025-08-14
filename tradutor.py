import os

# ===== Alfabeto Calculável =====
alfabeto = {
    "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I", "0": "J",
    "*1": "K", "*2": "L", "*3": "M", "*4": "N", "*5": "O", "*6": "P", "*7": "Q", "*8": "R", "*9": "S", "*0": "T",
    "*1": "U", "2": "V", "3": "W", "4": "X", "5": "Y", "*6": "Z",
    ".": " ", "..": ".", "/": ",", "=*": "!", "=/": "?",
    "-": "^",      # Circunflexo
    "--": "~",     # Til
    "_": "-",      # Hífen real
    "(": "(", ")": ")"
}

acentos = {
    "+": {"A": "Á", "E": "É", "I": "Í", "O": "Ó", "U": "Ú"},
    "++": {"A": "À"},
    "%": {"C": "Ç"},
    "-": {"A": "Â", "E": "Ê", "I": "Î", "O": "Ô", "U": "Û"},  # Circunflexo
    "--": {"A": "Ã", "O": "Õ"},  # Til
}

alfabeto_inv = {v: k for k, v in alfabeto.items()}

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_tabela():
    print("\n Tabela do Alfabeto Calculável\n")
    print("| Código | Letra | Código | Letra | Código | Letra |")
    print("|--------|-------|--------|-------|--------|-------|")
    print("| 1      | A     | *1     | K     | **1    | U     |")
    print("| 2      | B     | *2     | L     | **2    | V     |")
    print("| 3      | C     | *3     | M     | **3    | W     |")
    print("| 4      | D     | *4     | N     | **4    | X     |")
    print("| 5      | E     | *5     | O     | **5    | Y     |")
    print("| 6      | F     | *6     | P     | **6    | Z     |")
    print("| 7      | G     | *7     | Q     |        |       |")
    print("| 8      | H     | *8     | R     |        |       |")
    print("| 9      | I     | *9     | S     |        |       |")
    print("| 0      | J     | *0     | T     |        |       |\n")

    print(" Acentos e Símbolos")
    print("| Código | Significado |")
    print("|--------|-------------|")
    print("| +      | Acento agudo (Á, É, Í, Ó, Ú) |")
    print("| ++     | Crase (À) |")
    print("| %      | Cedilha (Ç) |")
    print("| +-     | Algum acento (desconhecido) |")
    print("| -      | Circunflexo (^: Â, Ê, Î, Ô, Û) |")
    print("| --     | Til (Ã, Õ) |")
    print("| _      | Hífen - |")
    print("| .      | Espaço |")
    print("| ..     | Ponto final . |")
    print("| /      | Vírgula , |")
    print("| =*     | Exclamação ! |")
    print("| =/     | Interrogação ? |")
    print("| (      | Parêntese abrindo |")
    print("| )      | Parêntese fechando |\n")

while True:
    limpar()
    print("=== Alfabeto Calculável ===")
    print("1 - Texto normal -> Código")
    print("2 - Código -> Texto")
    print("3 - Mostrar tabela")
    print("4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        limpar()
        texto = input("Digite o texto: ").upper()
        codigo = ""
        for letra in texto:
            if letra in ["Á","É","Í","Ó","Ú"]:
                base = {"Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U"}[letra]
                codigo += alfabeto_inv[base] + "+"
            elif letra == "À":
                codigo += alfabeto_inv["A"] + "++"
            elif letra == "Ç":
                codigo += alfabeto_inv["C"] + "%"
            elif letra in ["Â","Ê","Î","Ô","Û"]:
                base = {"Â":"A","Ê":"E","Î":"I","Ô":"O","Û":"U"}[letra]
                codigo += alfabeto_inv[base] + "-"
            elif letra in ["Ã","Õ"]:
                base = {"Ã":"A","Õ":"O"}[letra]
                codigo += alfabeto_inv[base] + "--"
            elif letra in alfabeto_inv:
                codigo += alfabeto_inv[letra]
            else:
                codigo += letra
        print("\nCódigo calculável:", codigo, "\n")
        input("Pressione ENTER para continuar...")

    elif opcao == "2":
        limpar()
        cod = input("Digite o código: ").replace(" ", "")
        texto = ""
        i = 0
        while i < len(cod):
            if cod[i:i+3] in alfabeto:
                letra = alfabeto[cod[i:i+3]]
                texto += letra
                i += 3
            elif cod[i:i+2] in alfabeto:
                letra = alfabeto[cod[i:i+2]]
                texto += letra
                i += 2
            elif cod[i] in alfabeto:
                letra = alfabeto[cod[i]]
                texto += letra
                i += 1
            else:
                texto += cod[i]
                i += 1

            # Aplica acento na última letra já escrita
            if i < len(cod):
                if cod[i:i+2] == "+-":  # acento desconhecido
                    texto = texto[:-1] + texto[-1] + "+-"
                    i += 2
                elif cod[i:i+2] in acentos:
                    if texto[-1] in acentos[cod[i:i+2]]:
                        texto = texto[:-1] + acentos[cod[i:i+2]][texto[-1]]
                    i += 2
                elif cod[i:i+1] in acentos:
                    if texto[-1] in acentos[cod[i:i+1]]:
                        texto = texto[:-1] + acentos[cod[i:i+1]][texto[-1]]
                    i += 1

        print("\nTexto normal:", texto, "\n")
        input("Pressione ENTER para continuar...")

    elif opcao == "3":
        limpar()
        mostrar_tabela()
        input("Pressione ENTER para continuar...")

    elif opcao == "4":
        limpar()
        print("Você escolheu sair.")
        print("1 - Sair de vez")
        print("2 - Voltar ao menu")
        escolha_saida = input("Escolha: ")
        if escolha_saida == "1":
            limpar()
            print("Saindo... Até logo!")
            break
        else:
            continue

    else:
        limpar()
        print("Opção inválida!\n")
        input("Pressione ENTER para continuar...")