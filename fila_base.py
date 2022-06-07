import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def insere_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def chama_cliente(self, caixa):
        ...

    @abc.abstractmethod
    def estatistica(self, dia, agencia, flag_detail):
        ...

    @abc.abstractmethod
    def atualiza_fila(self):
        ...

    def genha_senhas(self):
        self.busca_posicao_fila()
        self.gera_senha_atual()
        self.insere_cliente()
