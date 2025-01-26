from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def truncate_html_content(value, length=100):
    
    soup = BeautifulSoup(value, "html.parser")
    text = soup.get_text()
    return text[:length] + ("..." if len(text) > length else "")