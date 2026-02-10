from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_namespace_import
from .import_ import Import
if TYPE_CHECKING:
    from .i_namespace import INamespace


class NamespaceImport(Import):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_namespace_import()

    @property
    def importedNamespace(self) ->'Optional["INamespace"]':
        res = get_only_reference_value_by_reference_name(self,
            'importedNamespace')
        if res:
            return cast('INamespace', res.referred)
        else:
            return None

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: '"INamespace"'):
        reference = self.get_classifier().get_reference_by_name(
            'importedNamespace')
        if self.importedNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            importedNamespace, importedNamespace.name))
