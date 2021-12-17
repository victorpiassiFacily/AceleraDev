def main():
    notas = [int(input(f"Insira a {x+1}a nota: ")) for x in range(4)]
    media(notas)


def media(notas):
    media = sum(notas) / len(notas)
    print(
        f"""
Notas: {str(notas)}\n
Media: {media}
        """
    )

    return media


if __name__ == "__main__":
    main()
