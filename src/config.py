import os

# Параметры подключения к базе
DB_USER = os.getenv("DB_USER", "student")
DB_PASSWORD = os.getenv("DB_PASSWORD", "student_pass")
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "chat_db")

# Формируем строку подключения для psycopg2
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Параметры модели
# MODEL_NAME = "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
MODEL_NAME = "facebook/bart-large-mnli"
CANDIDATE_LABELS = ["бот", "человек"]

prompt_classifier = """
Это диалог между участниками
Твоя задача — определить, участвует ли в этом диалоге бот (автоматический AI-ассистент, чат-бот, программа)
Ответь только одно слово: 'бот' или 'человек'
"""