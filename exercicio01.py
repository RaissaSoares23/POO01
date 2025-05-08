from biblioteca import ContaBancaria

conta01 = ContaBancaria( 333,"Raissa", 1)
print(conta01.nome)


conta01.AtivarConta()
conta01.Depositar(100)
conta01.AjustarLimite(100)
conta01.Sacar(150)
conta01.VerificarSaldo()
