from fastapi import Request, Depends, Form
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND

from project.main import app, templates
from project.database.base import get_db
from project.models import ToDo
from project.config import settings


@app.get('/')
def index_page(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'todo_list': todos}
                                      )


@app.post('/add')
def add_todo(title: str = Form(...), db_session: Session = Depends(get_db)):
    new_todo = ToDo(title=title)
    db_session.add(new_todo)
    db_session.commit()

    url = app.url_path_for('index_page')
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@app.get('/update/{todo_id}')
def get_update(todo_id: int, db_session: Session = Depends(get_db)):
    todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.is_complete = not todo.is_complete
    db_session.commit()

    url = app.url_path_for('index_page')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@app.get('/delete/{todo_id}')
def delete_todo(todo_id: int, db_session: Session = Depends(get_db)):
    todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
    db_session.delete(todo)
    db_session.commit()

    url = app.url_path_for('index_page')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)
