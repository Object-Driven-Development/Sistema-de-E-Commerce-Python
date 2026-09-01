import re

class Cliente:

    def __init__(self, nome, email, cpf):
        self.nome = nome
        self._email = None
        self.__cpf = None
        self.__saldo_cupom = 0.0

        self.email = email
        self.cpf = cpf

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str):
            raise ValueError("O e-mail deve ser um texto.")

        if "@" not in valor:
            raise ValueError("O e-mail deve conter o caractere '@'.")

        partes = valor.split("@")

        if len(partes) != 2 or not partes[0] or not partes[1]:
            raise ValueError(
                "O e-mail deve possuir texto antes e depois do '@'."
            )

        self._email = valor

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        if not isinstance(valor, str):
            raise ValueError("O CPF deve ser informado como texto.")

        digitos = re.sub(r'\D', '', str(valor))

        if len(digitos) != 11:
            raise ValueError("CPF inválido. Certifique-se de digitar os 11 números.")

        if len(set(digitos)) == 1:
            raise ValueError("CPF inválido.")

        primeiros_9 = [int(digito) for digito in digitos[:9]]

        soma_1 = sum(
            digito * peso
            for digito, peso in zip(primeiros_9, range(10, 1, -1))
        )

        resto_1 = (soma_1 * 10) % 11

        if resto_1 == 10:
            dv1 = 0
        else:
            dv1 = resto_1

        if dv1 != int(digitos[9]):
            raise ValueError("CPF inválido.")

        primeiros_10 = [int(digito) for digito in digitos[:10]]

        soma_2 = sum(
            digito * peso
            for digito, peso in zip(primeiros_10, range(11, 1, -1))
        )

        resto_2 = (soma_2 * 10) % 11

        if resto_2 == 10:
            dv2 = 0
        else:
            dv2 = resto_2

        if dv2 != int(digitos[10]):
            raise ValueError("CPF inválido.")

        self.__cpf = f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:9]}-{digitos[9:]}"
    @property
    def saldo_cupom(self):
        return self.__saldo_cupom
    @saldo_cupom.setter
    def saldo_cupom(self, valor):
        if valor <= 0:
            raise ValueError("O valor do cupom deve ser maior que zero.")

        self.__saldo_cupom += valor

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.__cpf}"

    def __repr__(self):
        return (
            f"Cliente(nome='{self.nome}', "
            f"email='{self._email}', "
            f"cpf='{self.__cpf}')"
        )