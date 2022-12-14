from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()  # Створення основної програми
# Визнаення шляху до статчних файлів, завдяки методу mount
# Який приймає неповний шлях до папки, повний шлях до папки і назву шаблону,
# за якою до нього можна буде звертатись
app.mount('/static', StaticFiles(directory='project/static'), 'static')
templates = Jinja2Templates(directory='project/templates')

from project.routes import index_page
