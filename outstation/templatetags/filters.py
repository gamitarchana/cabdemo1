from django import template

register = template.Library()

@register.filter()
def parseInt(value):
    return int(value)

@register.filter(name="item")
def item(l, i):
    #print("---item---")
    #print(l)
    i = int('0' + i)
    #print(l[i])
    try:
        #print(l[i])
        return l[i]
    except:
        return None

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
