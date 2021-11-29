def main():
    numeros = [int(input(f"Insira o {x+1}o número: ")) for x in range(20)]
    impar = []
    par = []

    [par.append(x) if x % 2 == 0 else impar.append(x) for x in numeros]

    print(f"{numeros}\n{par}\n{impar}")


if __name__ == "__main__":
    main()
