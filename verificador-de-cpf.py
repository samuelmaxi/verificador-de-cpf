"""
Sistema que solicita um CPF(com ou sem '.' e '-')
e realiza o calculo de validação
ao final ele verifica se é valido ou não.
"""
import sys, random

def gerador_cpf():
    nove_digitos = ''
    for i in range(11):
        nove_digitos += str(random.randint(0,9))
    return nove_digitos

# Para usar a função apague a proxima linha e subistituias por essa:
# cpf_enviado_usuario = gerador_cpf().replace('.', '', 2).replace('-','')
cpf_enviado_usuario = input('CPF (123.456.789-10): ').replace('.', '', 2).replace('-','')
nove_digitos = cpf_enviado_usuario[:9]

entrada_repetida = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
if entrada_repetida:
    print('Você enviou caracteres repetidos')
    sys.exit()

contagem_regressiva_1 = 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contagem_regressiva_1 
    contagem_regressiva_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

contagem_regressiva_2 = 11
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contagem_regressiva_2
    contagem_regressiva_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = dez_digitos + str(digito_2)

if cpf_gerado_pelo_calculo == cpf_enviado_usuario:
    print(f'CPF: {cpf_gerado_pelo_calculo} é valido')
else:
    print(f'{cpf_gerado_pelo_calculo} CPF inválido')