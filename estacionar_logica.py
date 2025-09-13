
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