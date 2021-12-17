def main():
    temperaturas = [
        int(input(f"Insira a temperatura do {x+1}o mês: ")) for x in range(12)
    ]

    temp_media = sum(temperaturas) / len(temperaturas)

    meses_ext = {
        "1": "Janeiro",
        "2": "Fevereiro",
        "3": "Março",
        "4": "Abril",
        "5": "Maio",
        "6": "Junho",
        "7": "Julho",
        "8": "Agosto",
        "9": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro",
    }

    temp_superior = [
        f"{i+1} - {meses_ext[str(i+1)]}: {x}°C" for i, x in enumerate(temperaturas) if x > temp_media
    ]

    print(",\n".join(temp_superior))


if __name__ == "__main__":
    main()
