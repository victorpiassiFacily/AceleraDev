def main():

    print("Responda com S ou N.")
    perguntas = [
        "Telefonou pra vítima? ",
        "Esteve no local do crime? ",
        "Mora perto da vítima? ",
        "Devia dinheiro pra vítima? ",
        "Já trabalhou com a vítima? "
    ]

    respostas = [True for pergunta in perguntas if input(pergunta) == "S"]

    classificacao = {
        "0": "Inocente",
        "1": "Inocente",
        "2": "Suspeito",
        "3": "Cúmplice",
        "4": "Cúmplice",
        "5": "Assassino",
    }

    print(f"Julgado como: {classificacao[str(len(respostas))]}")


if __name__ == "__main__":
    main()
