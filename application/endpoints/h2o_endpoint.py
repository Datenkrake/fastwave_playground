
#region imports
from fastapi import FastAPI, APIRouter


# https://github.com/arnavdas88/fastwave
from h2o_wave import Q, ui
from faker import Faker
from fastwave import H2O_WaveUI

app = FastAPI()
fake = Faker()

router = APIRouter(
    prefix="/router",
    tags=["H2O Wave GUI"],
    responses={404: {"description": "/h2o/ not found"}},
)


@router.get("/hello")
@H2O_WaveUI(app, name="hello")
async def hello(q:Q):
    # The header shown on all the app's pages
    q.page['header'] = ui.header_card(
        box='1 1 5 1', title='Hello Wave',
        subtitle='Hello World example', 
        icon='WavingHand', color='card'
    )

    # The main card of the app
    q.page['main'] = ui.form_card(
        box='1 2 5 4',
        items=[
            ui.text(content=fake.paragraph(nb_sentences=5, variable_nb_sentences=False)) for _ in range(10)
        ]
    )

    # Save the page
    await q.page.save()