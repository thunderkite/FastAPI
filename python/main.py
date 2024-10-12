from fastapi import FastAPI # Импортируем FastAPI
from fastapi.templating import Jinja2Templates # Импортируем Jinja2Templates для работы с HTML-шаблонами
from fastapi.responses import HTMLResponse # Это тип ответа, который возвращает HTML-страницу
from starlette.requests import Request # Импортируем Request для работы с запросами
from fastapi.staticfiles import StaticFiles # Импортируем StaticFiles для работы с файлами css и js

app = FastAPI() # Инициализируем FastAPI

app.mount("/static", StaticFiles(directory="static"), name="static") # Создаем маршрут "/static" и указываем путь к папке с файлами css и js

# Путь к папке с HTML шаблонами
templates = Jinja2Templates(directory="templates") # Указываем путь к папке с HTML шаблонами

@app.get("/", response_class=HTMLResponse) # Создаем маршрут "/" и указываем тип ответа HTMLResponse
async def home(request: Request): # Функция, которая принимает запрос request и возвращает HTML-шаблон
    return templates.TemplateResponse("index.html", {"request": request}) # Рендерим HTML-шаблон

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Для запуска сервера
if __name__ == "__main__": # Проверяем, что мы запускаем этот файл как main.py
    import uvicorn # Импортируем uvicorn для запуска сервера
    uvicorn.run(app, host="0.0.0.0", port=5000) # Запускаем сервер на порту 5000