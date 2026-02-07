from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_import
from lionweb.model.impl.dynamic_node import DynamicNode
from .visibility_kind import VisibilityKind
if TYPE_CHECKING:
    from .i_element import IElement
    from .i_namespace import INamespace
    from .owning_membership import OwningMembership
    from .i_relationship import IRelationship
    from .documentation import Documentation
    from .annotation import Annotation
    from .textual_representation import TextualRepresentation


class Import(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_import()

    @property
    def visibility(self) ->VisibilityKind:
        return cast(VisibilityKind, get_property_value_by_name(self,
            'visibility'))

    @visibility.setter
    def visibility(self, value: VisibilityKind):
        property_ = self.get_classifier().require_property_by_name('visibility'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isRecursive(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isRecursive'))

    @isRecursive.setter
    def isRecursive(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isRecursive')
        self.set_property_value(property=property_, value=value)

    @property
    def isImportAll(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImportAll'))

    @isImportAll.setter
    def isImportAll(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isImportAll')
        self.set_property_value(property=property_, value=value)

    @property
    def importedElement(self) ->'Optional["IElement"]':
        res = get_only_reference_value_by_reference_name(self,
            'importedElement')
        if res:
            return cast('IElement', res.referred)
        else:
            return None

    @importedElement.setter
    def importedElement(self, importedElement: '"IElement"'):
        reference = self.get_classifier().get_reference_by_name(
            'importedElement')
        if self.importedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(importedElement,
            importedElement.name))

    @property
    def importOwningNamespace(self) ->'Optional["INamespace"]':
        res = get_only_reference_value_by_reference_name(self,
            'importOwningNamespace')
        if res:
            return cast('INamespace', res.referred)
        else:
            return None

    @importOwningNamespace.setter
    def importOwningNamespace(self, importOwningNamespace: '"INamespace"'):
        reference = self.get_classifier().get_reference_by_name(
            'importOwningNamespace')
        if self.importOwningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            importOwningNamespace, importOwningNamespace.name))

    @property
    def ownedRelatedElement(self) ->'List["IElement"]':
        res = self.get_children('ownedRelatedElement')
        return res

    def add_to_owned_related_element(self, new_element: '"IElement"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'ownedRelatedElement'), new_element)

    @property
    def owningRelatedElement(self) ->'Optional["IElement"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast('IElement', res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: '"IElement"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def relatedElement(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'relatedElement')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_related_element(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    @property
    def target(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'target')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_target(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    @property
    def source(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'source')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_source(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->'Optional["OwningMembership"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast('OwningMembership', res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: '"OwningMembership"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningNamespace(self) ->'Optional["INamespace"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast('INamespace', res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: '"INamespace"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def owningRelationship(self) ->'Optional["IRelationship"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast('IRelationship', res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: '"IRelationship"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedRelationship(self) ->'List["IRelationship"]':
        res = self.get_children('ownedRelationship')
        return res

    def add_to_owned_relationship(self, new_element: '"IRelationship"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'ownedRelationship'), new_element)

    @property
    def owner(self) ->'Optional["IElement"]':
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast('IElement', res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: '"IElement"'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    @property
    def ownedElement(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'ownedElement')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_owned_element(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    @property
    def documentation(self) ->'List["Documentation"]':
        res = get_reference_value_by_name(self, 'documentation')
        return [(cast('Documentation', r.referred) if r else None) for r in res
            ]

    def add_to_documentation(self, new_element: '"Documentation"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedAnnotation(self) ->'List["Annotation"]':
        res = get_reference_value_by_name(self, 'ownedAnnotation')
        return [(cast('Annotation', r.referred) if r else None) for r in res]

    def add_to_owned_annotation(self, new_element: '"Annotation"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def textualRepresentation(self) ->'List["TextualRepresentation"]':
        res = get_reference_value_by_name(self, 'textualRepresentation')
        return [(cast('TextualRepresentation', r.referred) if r else None) for
            r in res]

    def add_to_textual_representation(self, new_element:
        '"TextualRepresentation"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('textualRepresentation'),
            ReferenceValue(new_element, new_element.name))

    @property
    def declaredShortName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'declaredShortName'))

    @declaredShortName.setter
    def declaredShortName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'declaredShortName')
        self.set_property_value(property=property_, value=value)

    @property
    def declaredName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'declaredName'))

    @declaredName.setter
    def declaredName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'declaredName')
        self.set_property_value(property=property_, value=value)

    @property
    def shortName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'shortName'))

    @shortName.setter
    def shortName(self, value: str):
        property_ = self.get_classifier().require_property_by_name('shortName')
        self.set_property_value(property=property_, value=value)

    @property
    def name(self) ->str:
        return cast(str, get_property_value_by_name(self, 'name'))

    @name.setter
    def name(self, value: str):
        property_ = self.get_classifier().require_property_by_name('name')
        self.set_property_value(property=property_, value=value)

    @property
    def qualifiedName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'qualifiedName'))

    @qualifiedName.setter
    def qualifiedName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'qualifiedName')
        self.set_property_value(property=property_, value=value)

    @property
    def isImpliedIncluded(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImpliedIncluded')
            )

    @isImpliedIncluded.setter
    def isImpliedIncluded(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isImpliedIncluded')
        self.set_property_value(property=property_, value=value)

    @property
    def isLibraryElement(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isLibraryElement'))

    @isLibraryElement.setter
    def isLibraryElement(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isLibraryElement')
        self.set_property_value(property=property_, value=value)

    @property
    def aliasIdsContainer(self) ->'List["AliasIdsContainer"]':
        res = self.get_children('aliasIdsContainer')
        return res

    def add_to_alias_ids_container(self, new_element: '"AliasIdsContainer"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'aliasIdsContainer'), new_element)
