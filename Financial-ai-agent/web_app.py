from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from agent.agent import run_agent

app = FastAPI(title="Financial AI Agent")

app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request):
    form = await request.form()
    query = form.get("query", "Analyze Indian markets")

    agent_state = run_agent(query)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": agent_state.final_insight,
            "query": query
        }
    )
