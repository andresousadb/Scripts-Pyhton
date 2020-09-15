from Modularizacao.moeda_v3.utilidadesCeV import moeda
from Modularizacao.moeda_v3.utilidadesCeV import dado

p = dado.leiadinheiro('Digite o preco: R$')
moeda.resumo(p,20,12)
