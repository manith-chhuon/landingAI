# AI in Cambodia - Streamlit Landing Page

A Streamlit-based landing page showcasing AI development and opportunities in Cambodia.

## Features
- Interactive dashboard layout
- Key statistics about AI growth in Cambodia
- Contact form for inquiries
- Resource directory of key organizations and events
- Responsive design

## Local Setup

1. Create a virtual environment (optional but recommended):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements:
```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app:
```powershell
streamlit run app.py
```

The app will open in your default web browser at http://localhost:8501

## Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy your app by connecting to your repository
5. Select main file as `app.py`

## Customization

To customize the content:
1. Edit text content in `app.py`
2. Modify the statistics in the DataFrame
3. Add more sections using Streamlit components
4. Adjust styling in the CSS section at the top of `app.py`

## Structure
- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## Contact Form Integration

The contact form currently shows a success message. To integrate with a backend:
1. Add a database connection (e.g., SQLite, PostgreSQL)
2. Or integrate with an email service
3. Modify the form submission handler in `app.py`