from django import template
 
register = template.Library()
 
@register.filter(name='saludo')
def saludo(valor):
    return f"<h1 style='background:#ffc107; color:white;'> Bienvenido, {valor} </h1>"
