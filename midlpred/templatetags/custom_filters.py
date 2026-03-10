from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return float(value) * arg

@register.filter
def get_item(dictionary, key):
    """Récupérer un élément d'un dictionnaire"""
    if isinstance(dictionary, dict):
        return dictionary.get(key, '')
    return ''  # Retourner une chaîne vide si ce n'est pas un dictionnaire

@register.filter
def format_percent(value):
    """Formater un pourcentage"""
    try:
        return f"{float(value) * 100:.2f}%"
    except (ValueError, TypeError):
        return "0.00%"

@register.filter
def get_class_color(class_name):
    """Retourner une couleur CSS selon la classe"""
    colors = {
        'FORME': 'primary',
        'PHYSIO': 'success',
        'OTHER': 'warning',
        'MOTILITY': 'info'
    }
    return colors.get(class_name, 'secondary')

@register.filter
def get_class_icon(class_name):
    """Retourner une icône selon la classe"""
    icons = {
        'FORME': 'fas fa-shapes',
        'PHYSIO': 'fas fa-heartbeat',
        'OTHER': 'fas fa-question-circle',
        'MOTILITY': 'fas fa-running'
    }
    return icons.get(class_name, 'fas fa-dna')