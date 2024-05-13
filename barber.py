from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Barbearia(App):
    def __init__(self):
        super().__init__()
        self.barbearia = BarbeariaModel()

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.output_label = Label(text="Bem-vindo à Barbearia!")
        layout.add_widget(self.output_label)

        self.input_nome = TextInput(hint_text="Nome do cliente")
        layout.add_widget(self.input_nome)

        self.input_horario = TextInput(hint_text="Horário do agendamento (8-18)")
        layout.add_widget(self.input_horario)

        agendar_button = Button(text="Agendar", on_press=self.agendar_cliente)
        layout.add_widget(agendar_button)

        mostrar_button = Button(text="Mostrar Agendamentos", on_press=self.mostrar_agendamento)
        layout.add_widget(mostrar_button)

        return layout

    def agendar_cliente(self, instance):
        nome_cliente = self.input_nome.text
        horario_agendamento = int(self.input_horario.text)

        if nome_cliente and horario_agendamento:
            mensagem = self.barbearia.agendar_cliente(nome_cliente, horario_agendamento)
            self.output_label.text = mensagem
        else:
            self.output_label.text = "Por favor, insira o nome do cliente e o horário."

    def mostrar_agendamento(self, instance):
        agendamentos = self.barbearia.mostrar_agendamento()
        self.output_label.text = agendamentos


class BarbeariaModel:
    def __init__(self):
        self.horario_abertura = 8
        self.horario_fechamento = 18
        self.limite_clientes = 10
        self.clientes_agendados = []
        self.horario_almoco_inicio = 12
        self.horario_almoco_fim = 13

    def agendar_cliente(self, cliente, horario):
        if len(self.clientes_agendados) < self.limite_clientes and self.horario_abertura <= horario < self.horario_almoco_inicio or \
                self.horario_almoco_fim < horario <= self.horario_fechamento:
            self.clientes_agendados.append((cliente, horario))
            return f"Cliente {cliente} agendado para as {horario}h"
        else:
            return "Desculpe, não podemos agendar neste horário."

    def mostrar_agendamento(self):
        if self.clientes_agendados:
            agendamentos = "Agendamentos:\n"
            for cliente, horario in self.clientes_agendados:
                agendamentos += f"{cliente}: {horario}h\n"
            return agendamentos
        else:
            return "Não há agendamentos."


if __name__ == "__main__":
    Barbearia().run()
