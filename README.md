Verificador de CPF
Este é um sistema de verificação de CPF, que solicita a entrada de um CPF (com ou sem '.' e '-') e realiza o cálculo para verificar se é válido ou não.

Utilização
Para usar o sistema, basta executar o arquivo e inserir o CPF desejado. O sistema irá calcular se o CPF é válido ou não e exibirá a resposta na tela. Caso queira gerar um CPF para teste, pode-se usar a função gerador_cpf, basta apagar a linha que recebe o input do usuário e substituí-la pela chamada da função.

Funcionamento
O sistema realiza as seguintes ações:

Recebe a entrada do CPF e remove os '.' e '-'
Verifica se a entrada consiste apenas de números repetidos
Realiza o cálculo dos primeiros 9 dígitos e os dois dígitos verificadores do CPF
Compara o CPF gerado pelo cálculo com o CPF inserido pelo usuário
Exibe a resposta na tela, informando se o CPF é válido ou inválido.
Considerações
Este sistema é apenas uma demonstração básica da verificação de CPF, e não deve ser usado em aplicações reais sem a devida validação e testes. A implementação de validação de CPF pode variar de acordo com o contexto de utilização, por isso, é importante sempre consultar a documentação e regulamentações específicas do país ou região onde o sistema será utilizado.
