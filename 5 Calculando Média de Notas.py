def calcula_media(notas):
    if len(notas) == 0:
        return 0  # Evita divisão por zero se a lista estiver vazia
    soma = sum(notas)
    media = soma / len(notas)
    return media


notas = [8.5, 9.0, 7.5, 6.0, 10.0]
media = calcula_media(notas)
print(f"A média das notas é {media:.2f}")

