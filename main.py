from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/task/", response_class=HTMLResponse)
async def read_item(name, message):
    return f"""
    <html>
        <head>
            <title>Recruto task</title>
        </head>
        <body>
            <h2>Hello, {name}! {message} </h2>
        </body>
    </html>"""
