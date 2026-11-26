from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Balbhadra Solutions")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# NIC 62020 — Computer consultancy and computer facilities management activities
SERVICES = [
    {
        "icon": "💻",
        "title": "IT Strategy & Consulting",
        "tags": ["Strategy", "Advisory"],
        "description": "End-to-end technology roadmaps, digital transformation advisory, and IT governance frameworks tailored to your business goals.",
    },
    {
        "icon": "🖥️",
        "title": "Computer Facilities Management",
        "tags": ["Infrastructure", "Operations"],
        "description": "Full lifecycle management of your IT infrastructure — servers, networks, storage, and data centres — keeping systems available 24/7.",
    },
    {
        "icon": "☁️",
        "title": "Cloud Migration & Management",
        "tags": ["Cloud", "DevOps"],
        "description": "Seamless migration to public, private, or hybrid cloud environments with ongoing cost optimisation and performance monitoring.",
    },
    {
        "icon": "🔒",
        "title": "Cybersecurity Advisory",
        "tags": ["Security", "Compliance"],
        "description": "Risk assessments, vulnerability management, and compliance consulting (ISO 27001, GDPR) to safeguard your digital assets.",
    },
    {
        "icon": "🛠️",
        "title": "Software & Systems Integration",
        "tags": ["Integration", "Development"],
        "description": "Custom software consulting, ERP/CRM implementation guidance, and seamless integration of enterprise systems.",
    },
    {
        "icon": "📊",
        "title": "IT Support & Helpdesk Services",
        "tags": ["Support", "Managed Services"],
        "description": "Dedicated L1–L3 technical support, remote monitoring, and managed helpdesk solutions to minimise downtime.",
    },
]

STATS = [
    {"value": "200+", "label": "Clients Served"},
    {"value": "15+", "label": "Years of Expertise"},
    {"value": "98%", "label": "Client Retention Rate"},
    {"value": "50+", "label": "Certified Consultants"},
]

NIC_INFO = {
    "nic2": "62 — Computer programming, consultancy and related activities",
    "nic4": "6202 — Computer consultancy and computer facilities management activities",
    "nic5": "62020 — Computer consultancy and computer facilities management activities",
    "activity": "Services",
}


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "services": SERVICES,
            "stats": STATS,
            "nic": NIC_INFO,
        },
    )


@app.get("/privacy")
async def privacy(request: Request):
    return templates.TemplateResponse(request, "privacy.html", {})


@app.get("/terms")
async def terms(request: Request):
    return templates.TemplateResponse(request, "terms.html", {})

