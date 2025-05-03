# Лабораторная работа 4 — CORS + Static + JS

## 📌 Что реализовано

- FastAPI-сервер с включенным CORS
- Статический HTML с JS
- POST-запросы на API
- `GET /` → отдает HTML
- `POST /api/submit` → принимает JSON от формы

## ▶ Как запустить

1. Установи зависимости:
   ```
   pip install fastapi uvicorn
   ```

2. Запусти сервер:
   ```
   uvicorn main:app --reload
   ```

3. Перейди в браузере:
   ```
   http://127.0.0.1:8000/
   ```

## ✅ Как выложить на GitHub

```bash
git init
git add .
git commit -m "lab4 — CORS и frontend"
git branch -M main
git remote add origin https://github.com/ТВОЙ_ЛОГИН/lab4-cors.git
git push -u origin main
```
