from django import template

register = template.Library()


@register.simple_tag
def mediapath(format_string):
    return f'/media/{format_string}'


@register.filter
def mediapath_filter(text):
    return f'/media/{text}'
