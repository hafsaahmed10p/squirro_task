from fastapi import FastAPI
from app.api import document_handlers, search_handlers, answer_handlers
from app.middlewares.exception import ExceptionHandlerMiddleware

app = FastAPI(title="Squirro Document Search Task")
app.add_middleware(ExceptionHandlerMiddleware)
 

app.include_router(document_handlers.router)
app.include_router(search_handlers.router)
app.include_router(answer_handlers.router)

