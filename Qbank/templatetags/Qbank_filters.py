from django.template import Library
from django.template.defaultfilters import stringfilter

"""'register' is a module level variable that is a 'template.Library' instance in which tags and filters are registered"""
register = Library()

# Thia line registers customise filters with the register instance
@register.filter(name = 'repl_space_underscore')
@stringfilter

# fucntion to replace white spaces with underscore
def repl_space_underscore(string_to_convert):

    return string_to_convert.replace(' ','_')
    
