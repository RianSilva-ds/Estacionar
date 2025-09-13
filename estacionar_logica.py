
import datetime
import math

class Carro:
    def __init__(self, placa, cor, modelo):
        self.placa = placa.upper()
        self.cor = cor
        self.modelo = modelo
        self.horarioEntrada = datetime.datetime.now()

    def exibir(self):
        entrada_formatada = self.horarioEntrada.strftime('%H:%M')
        print(f"Placa: {self.placa} | Modelo: {self.modelo} | Cor: {self.cor} | Entrada: {entrada_formatada}")

class Estacionamento:
    def __init__(self):
        self.carrosEstacionados = []

    def cadastrarCarro(self):
        placa = input("Digite a placa: ").upper()
        if self.buscarCarro(placa):
            print("Carro já cadastrado!")
            return

        cor = input("Digite a cor do veículo: ")
        modelo = input("Digite o modelo do veículo: ")

        carro = Carro(placa, cor, modelo)
        self.carrosEstacionados.append(carro)
        print("Carro cadastrado com sucesso!")

    def removerCarro(self):
        placa = input("Digite a placa: ").upper()
        carro = self.buscarCarro(placa)
        if carro:
            carro.exibir()
            valor, tempo = self.calcularValor(carro.horarioEntrada)
            print(f"\nValor total a ser pago: R${valor:.2f}")
            print(f"Tempo de permanência: {tempo}")
            self.carrosEstacionados.remove(carro)
            print("Carro removido com sucesso!")
        else:
            print("Carro não encontrado.")

    def buscarCarro(self, placa):
        for carro in self.carrosEstacionados:
            if carro.placa == placa:
                return carro
        return None

    def calcularValor(self, horarioEntrada):
        horaSaida = datetime.datetime.now()
        tempoPermanencia = horaSaida - horarioEntrada
        totalSegundos = int(tempoPermanencia.total_seconds())

        horas, minutos = divmod(totalSegundos, 3600)
        minutos = minutos // 60

        if totalSegundos <= 1800:
            valor = 7.00
        elif totalSegundos <= 10800:
            valor = 13.00
        else:
            horasExtras = math.ceil((totalSegundos - 10800) / 3600)
            valor = 13.00 + (horasExtras * 2.00)

        tempoFormatado = f"{horas} hora(s) e {minutos} minuto(s)"
        return valor, tempoFormatado
    
def menu():
    estacionamento = Estacionamento()

    while True:
        print("\n=== Sistema de Estacionamento ===")
        print("1 - Cadastrar carro")
        print("2 - Consultar carros")
        print("3 - Remover carro / Calcular valor")
        print("4 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            estacionamento.cadastrarCarro()
        elif opcao == "2":
            estacionamento.consultarCarros()
        elif opcao == "3":
            estacionamento.removerCarro()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()