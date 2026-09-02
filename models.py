class RegistoAlimentar:
    # Representa um alimento registado numa determinada refeição.

    def __init__(
        self,
        id_registo,
        data,
        refeicao,
        alimento,
        quantidade,
        quantidade_por_unidade,
        unidade_medida,
        calorias_por_unidade,
        proteinas_por_unidade,
        hidratos_carbono_por_unidade,
        gorduras_por_unidade
    ):
        self.id = id_registo
        self.data = data
        self.refeicao = refeicao
        self.alimento = alimento
        self.quantidade = quantidade
        self.quantidade_por_unidade = quantidade_por_unidade
        self.unidade_medida = unidade_medida
        self.calorias_por_unidade = calorias_por_unidade
        self.proteinas_por_unidade = proteinas_por_unidade
        self.hidratos_carbono_por_unidade = hidratos_carbono_por_unidade
        self.gorduras_por_unidade = gorduras_por_unidade

    def quantidade_total(self):
        # Calcula a quantidade total consumida.
        return self.quantidade * self.quantidade_por_unidade

    def calcular_nutrientes(self):
        # Calcula os valores nutricionais totais.
        return {
            "calorias": self.quantidade * self.calorias_por_unidade,
            "proteinas": self.quantidade * self.proteinas_por_unidade,
            "hidratos_carbono": self.quantidade * self.hidratos_carbono_por_unidade,
            "gorduras": self.quantidade * self.gorduras_por_unidade
        }

    def para_dicionario(self):
        # Converte o objeto para dicionário, para guardá-lo em JSON.
        return {
            "id": self.id,
            "data": self.data,
            "refeicao": self.refeicao,
            "alimento": self.alimento,
            "quantidade": self.quantidade,
            "quantidade_por_unidade": self.quantidade_por_unidade,
            "unidade_medida": self.unidade_medida,
            "calorias_por_unidade": self.calorias_por_unidade,
            "proteinas_por_unidade": self.proteinas_por_unidade,
            "hidratos_carbono_por_unidade": self.hidratos_carbono_por_unidade,
            "gorduras_por_unidade": self.gorduras_por_unidade
        }

    @classmethod
    def de_dicionario(cls, dados):
        # Converte um dicionário num objeto RegistoAlimentar.
        return cls(
            dados["id"],
            dados["data"],
            dados["refeicao"],
            dados["alimento"],
            dados["quantidade"],
            dados["quantidade_por_unidade"],
            dados["unidade_medida"],
            dados["calorias_por_unidade"],
            dados["proteinas_por_unidade"],
            dados["hidratos_carbono_por_unidade"],
            dados["gorduras_por_unidade"]
        )

class ObjetivosNutricionais:
    # Representa os objetivos nutricionais do utilizador.

    def __init__(
        self,
        calorias,
        proteinas,
        hidratos_carbono,
        gorduras
    ):
        self.calorias = calorias
        self.proteinas = proteinas
        self.hidratos_carbono = hidratos_carbono
        self.gorduras = gorduras

    def para_dicionario(self):
        # Converte os objetivos para dicionário.
        return {
            "calorias": self.calorias,
            "proteinas": self.proteinas,
            "hidratos_carbono": self.hidratos_carbono,
            "gorduras": self.gorduras
        }

    @classmethod
    def de_dicionario(cls, dados):
        # Converte um dicionário num objeto ObjetivosNutricionais.
        return cls(
            dados["calorias"],
            dados["proteinas"],
            dados["hidratos_carbono"],
            dados["gorduras"]
        )

    