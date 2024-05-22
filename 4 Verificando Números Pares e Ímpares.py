# Função para verificar se um número é par ou ímpar
def verifica_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Testando a função
numero = int(input("Digite um número: "))
resultado = verifica_par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")
