from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama

#Создание экземпляра FastAPI
app = FastAPI()

# Определение модели данных для входящего запроса
class Input(BaseModel):
    input: str

# Инициализация модели
llm_model = Llama.from_pretrained(
	repo_id="bartowski/gemma-2-9b-it-GGUF",
	filename="gemma-2-9b-it-IQ2_XS.gguf",
)

# Эндпоинт, принимающий сообщение пользователя и возвращающий ответ
@app.post("/generate/")
async def generate_response(user_input: Input):
    response = llm_model(user_input.input, max_tokens=30)
    return {"response": response['choices'][0]['text']}
