# Graficos de vendas

#Biblioteca para a criação de graficos
import matplotlib.pyplot as plt

#dados para grafico
meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
vendas = [10, 20, 10, 15, 23]
vendas2 = [2, 3, 4, 6, 3]

#criando o grafico
plt.plot(meses, vendas, color="g", linestyle="--", marker="o" )
plt.plot(meses, vendas, color="r", linestyle="-", marker="x" )

#Dados do grafico
plt.title("evolução das vendas")
plt.xlabel("Meses")
plt.ylabel("Vendas")
plt.grid(True)
plt.show()
