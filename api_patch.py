
from fastapi import Request

@app.post("/api/submit")
async def handle_form(request: Request):
    data = await request.json()
    return {"message": "Данные получены", "data": data}
