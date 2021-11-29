def main():
    alturas = [
        int(input(f"Insira a altura do {x+1}o aluno: ")) for x in range(10)
    ]

    media_altura = sum(alturas) / len(alturas)

    alturas_inferiores = [x for x in alturas if x < media_altura]
    print(len(alturas_inferiores))


if __name__ == "__main__":
    main()
