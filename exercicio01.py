from biblioteca import ContaBancaria

conta01 = ContaBancaria( 333,"Raissa", 1)
print(conta01.nome)


conta01.AtivarConta()
conta01.Depositar(1000)
conta01.AjustarLimite(1000)
conta01.Sacar(1500)
conta01.VerificarSaldo()
