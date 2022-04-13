from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse

from fastapi_infra.adapter.input.dto import PersonNameResponseDTO, PersonFullNameResponseDTO, \
    PersonDocumentRespoonseDTO, DTOParser, PersonResponseDTO
from fastapi_infra.adapter.input.service import PersonService

description = """
Simple Mock data generation 👍

Made by developer to developers 😁

#### pt_br ✅
"""

meta_tags = [
    {
        "name": "docs",
        "description": "Swagger api para visualização de documentação da api"
    },
    {
        "name": "person",
        "description": "Recurso para gerar dados relacionados a pessoas físicas"
    }
]

app = FastAPI(
    title="MockGen",
    description=description,
    version="v0.2.0",
    contact={
        "name": "Jeff Kalffman",
        "email": "jefferson@kalffman.com",
    },
    openapi_tags=meta_tags
)

person_service = PersonService()
person_name_service = person_service.person_name_use_case
cpf_service = person_service.person_document_use_case

dto_parser = DTOParser()


@app.get("/",
         tags=["docs"],
         response_class=RedirectResponse)
async def index():
    return "/docs"


@app.get("/person",
         tags=["person"],
         description="Rota para gerar uma pessoa física com dados aleatórios",
         response_model=PersonResponseDTO)
async def random_person(name_size: int = Query(description="Tamanho do nome", default=2, ge=2, le=5),
                        mask: bool = Query(description="Habilita ou não o conteúdo mascarado", default=False)):
    person = await person_service.get_random_person(mask, name_size)

    return dto_parser.parse_to_dto(person)


@app.get("/person/random_name",
         tags=["person"],
         description="Rota para gerar um nome aleatório",
         response_model=PersonNameResponseDTO)
async def random_name():
    person_name = await person_name_service.get_random_person_name()

    return dto_parser.parse_to_dto(person_name)


@app.get("/person/random_full_name",
         tags=["person"],
         description="Rota para gerar nome completo aleatório",
         response_model=PersonFullNameResponseDTO)
async def full_name(name_size: int = Query(description="Tamanho do nome", default=2, ge=2, le=5)):
    person_full_name = await person_name_service.get_random_full_name(name_size)

    return dto_parser.parse_to_dto(person_full_name)


@app.get("/person/random_cpf",
         tags=["person"],
         description="Rota para gerar CPF aleatório",
         response_model=PersonDocumentRespoonseDTO)
async def random_cpf(mask: bool = Query(description="Habilita ou não o conteúdo mascarado", default=False)):
    document = await cpf_service.get_random_document(mask)

    return dto_parser.parse_to_dto(document)
