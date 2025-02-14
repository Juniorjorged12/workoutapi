from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated [str,Field(description = 'Nome do centro de treinamento', example = 'CT King', max_length = 20)]
    endereco: Annotated [str,Field(description = 'Endeceço do CT', example = 'rua X Quadra 2', max_length = 60)]
    proprietario: Annotated [str,Field(description = 'Nome do proprietario do CT', example = 'Marcos', max_length = 30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated [str,Field(description = 'Nome do centro de treinamento', example = 'CT King', max_length = 20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description = 'identificador da Centro de Treinamento')]

