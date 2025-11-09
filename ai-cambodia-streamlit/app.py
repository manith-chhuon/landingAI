import streamlit as st
import streamlit.components.v1 as components
import os

# Page config
st.set_page_config(
    page_title="AI in Cambodia",
    page_icon="🤖",
    layout="wide"
)

# Read file content
def read_file(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "templates", filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Read HTML and CSS files
def read_html_file():
    html_content = read_file("index.html")
    css_content = read_file("style.css")
    
    # Insert CSS into HTML
    html_with_css = html_content.replace(
        '<link rel="stylesheet" href="style.css">',
        f'<style>{css_content}</style>'
    )
    return html_with_css

# Display the HTML content
def main():
    # Display the HTML content
    html_content = read_html_file()
    components.html(html_content, height=3000, scrolling=False)

if __name__ == "__main__":
    main()