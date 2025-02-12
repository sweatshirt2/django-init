from django.template import Library


register = Library()


@register.filter
def has_votes(choices):
    return any(choice.votes > 0 for choice in choices)
