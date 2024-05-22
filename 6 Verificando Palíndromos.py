def eh_palindromo(palavra):
    palavra = palavra.lower()  # Converte para minúsculas
    return palavra == palavra[::-1]  

palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
