from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse

from fastapi_infra.adapter.input.service import PersonNameService
from fastapi_infra.adapter.output.model import PersonNameDTO, PersonNameResponseDTO, PersonFullNameResponseDTO, \
    PersonFullNameDTO

app = FastAPI()

person_service = PersonNameService()


@app.get("/", response_class=RedirectResponse)
async def index():
    return "/docs"


@app.get("/random_name",
         description="Rota para gerar um nome aleatório",
         response_model=PersonNameResponseDTO)
async def random_name():
    person_name = await person_service.get_random_person_name()
    return PersonNameResponseDTO(
        data=PersonNameDTO(
            name=person_name.name,
            variations=person_name.variations,
            genre=person_name.genre,
        )
    )


@app.get("/random_full_name",
         description="Rota para gerar nome completo aleatório",
         response_model=PersonFullNameResponseDTO)
async def full_name(size: int = Query(description="Tamanho do nome", default=2, ge=2, le=5)):
    person_full_name = await person_service.get_random_full_name(size)

    return PersonFullNameResponseDTO(
        data=PersonFullNameDTO(
            first_name=person_full_name.first_name,
            last_name=person_full_name.last_name,
            full_name=person_full_name.full_name,
        )
    )
