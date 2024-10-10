from Cliente import Cliente
from Conta import Conta

if __name__ == "__main__":
    c1 = Cliente("João", "114444-2222")
    conta = Conta(c1.nome, 1222)  # Agora você pode acessar 'nome' diretamente

    conta.deposita(145)
    conta.saque(50)
    conta.extrato()

    print(conta.titular, "Numero: ", conta.numero, "Seu saldo: ", conta.saldo)
    print(c1)
    print(c1.nome, "e", c1.telefone)
