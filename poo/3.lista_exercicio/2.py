def main():
    phrase = list(input("Digite uma frase: "))
    vowals = ["a", "e", "i", "o", "u"]
    consonants = [x for x in phrase if x not in vowals]

    print(f"{', '.join(consonants)} - {len(consonants)} resultados")


if __name__ == "__main__":
    main()
