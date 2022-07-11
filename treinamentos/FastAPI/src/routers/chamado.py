from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

fake_db = []


class ChamadoModelo(BaseModel):
    titulo: str
    descricao: str | None = None
    data: str
    status: str
    tipo_problema: str

    class Config:
        schema_extra = {
            "example": {
                "titulo": "Titulo do chamado",
                "descricao": "Descricao do chamado",
                "data": "06/07/2022",
                "status": "Aguardando",
                "tipo_problema": "Internet",
            }
        }


@router.get("/chamado/", tags=["Chamado"])
def get_chamado():
    return {
        "message": "Dados buscados com sucesso",
        "error": None,
        "data": fake_db,
    }


@router.post("/chamado/", tags=["Chamado"])
def post_chamado(data: ChamadoModelo):
    fake_db.append(data)
    return {
        "message": "Dados buscados com sucesso",
        "error": None,
        "data": data,
    }
