def main():
    notas = [int(input(f"Insira a {x+1}a nota: ")) for x in range(4)]
    print(
        f"""
Notas: {str(notas)}\n
Media: {sum(notas) / len(notas)}
        """
    )


if __name__ == "__main__":
    main()
