from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi_infra.port.input.person_name_service import PersonNameService
from fastapi_infra.port.output.dto import PersonNameDTO, PersonNameResponseDTO

app = FastAPI()

person_service = PersonNameService()


@app.get("/", response_class=RedirectResponse)
async def index():
    return "/docs"


@app.get("/random-name", response_model=PersonNameResponseDTO)
async def index():
    person_name = await person_service.get_random_person_name()
    return PersonNameResponseDTO(
        data=PersonNameDTO(
            name=person_name.name,
            variations=person_name.variations
        )
    )
