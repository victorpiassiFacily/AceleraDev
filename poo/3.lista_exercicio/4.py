def main():

    medias = []
    for x in range(5):
        notas_aluno = []

        notas_aluno.append(
            int(input(f"Insira a primeira nota do aluno {x+1}: "))
        )
        notas_aluno.append(
            int(input(f"Insira a segunda nota do aluno {x+1}: "))
        )

        media = sum(notas_aluno) / len(notas_aluno)

        if media >= 7:
            medias.append(media)

    print(f"{len(medias)} médias maiores que 7")


if __name__ == "__main__":
    main()
