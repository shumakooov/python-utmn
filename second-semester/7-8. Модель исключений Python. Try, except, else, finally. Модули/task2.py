# img/2.7-8.2.png

class CyrillicError(Exception):
    pass

class CapitalError(Exception):
    pass

def name_validation(name):
    if not isinstance(name, str):
        raise TypeError("Параметр должен быть строкой")
    
    if not all('а' <= char.lower() <= 'я' for char in name):
        raise CyrillicError("Значение должно состоять только из кириллических букв")
    
    if not name[0].isupper() or any(char.isupper() for char in name[1:]):
        raise CapitalError("Значение должно начинаться с заглавной буквы, а остальные должны быть строчными")
    
    return name
