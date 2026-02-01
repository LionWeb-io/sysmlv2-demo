from lionweb.language import Language, Concept, Containment, Enumeration, Interface, PrimitiveType, Property, Reference, LionCoreBuiltins
from lionweb.lionweb_version import LionWebVersion
from functools import lru_cache


@lru_cache(maxsize=1)
def get_language() ->Language:
    language = Language(lion_web_version=LionWebVersion.V2023_1, id='types',
        name='types', key='types', version='1')
    boolean = PrimitiveType(lion_web_version=LionWebVersion.V2023_1, id=
        'types-Boolean', name='Boolean', key='types-Boolean')
    language.add_element(boolean)
    integer = PrimitiveType(lion_web_version=LionWebVersion.V2023_1, id=
        'types-Integer', name='Integer', key='types-Integer')
    language.add_element(integer)
    real = PrimitiveType(lion_web_version=LionWebVersion.V2023_1, id=
        'types-Real', name='Real', key='types-Real')
    language.add_element(real)
    unlimited_natural = PrimitiveType(lion_web_version=LionWebVersion.
        V2023_1, id='types-UnlimitedNatural', name='UnlimitedNatural', key=
        'types-UnlimitedNatural')
    language.add_element(unlimited_natural)
    string = PrimitiveType(lion_web_version=LionWebVersion.V2023_1, id=
        'types-String', name='String', key='types-String')
    language.add_element(string)
    return language


def get_boolean() ->PrimitiveType:
    return get_language().get_primitive_type_by_name('Boolean')


def get_integer() ->PrimitiveType:
    return get_language().get_primitive_type_by_name('Integer')


def get_real() ->PrimitiveType:
    return get_language().get_primitive_type_by_name('Real')


def get_unlimitednatural() ->PrimitiveType:
    return get_language().get_primitive_type_by_name('UnlimitedNatural')


def get_string() ->PrimitiveType:
    return get_language().get_primitive_type_by_name('String')
