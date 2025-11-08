AI Landing — Flask + Vercel

What this is

- A minimal AI-focused landing page built with Python (Flask).
- Designed to be deployed to Vercel using the `@vercel/python` builder.

Files

- `app.py` — Flask app (WSGI) that serves `templates/index.html` and a `/contact` POST endpoint.
- `templates/index.html` — Static landing page markup.
- `static/style.css` — Simple styles.
- `requirements.txt` — Python dependencies.
- `vercel.json` — Vercel configuration to build the Python app.

Local run (Windows PowerShell)

1. Create and activate a virtual env (optional, recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run locally:

```powershell
python app.py
```

Open http://localhost:8000 in your browser.

Deploy to Vercel

1. Install Vercel CLI (requires Node.js/npm):

```powershell
npm install -g vercel
```

2. From project directory, login and deploy:

```powershell
vercel login
vercel --prod
```

Vercel will use `vercel.json` to detect the `@vercel/python` builder and deploy the Flask app.

Notes & next steps

- The contact form currently returns a JSON success message. In production, forward form submissions to your email, CRM, or serverless function.
- You can replace content in `templates/index.html` and style in `static/style.css`.
- To pin a specific Python version on Vercel, create a `runtime.txt` with e.g. `python-3.9.18` (check Vercel docs for supported versions).
