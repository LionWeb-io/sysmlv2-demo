from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Optional, cast
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name
from lionweb.model.impl.dynamic_node import DynamicNode
from .language import get_language, get_owningmembership, get_membership, get_import, get_documentation, get_comment, get_annotation, get_textualrepresentation, get_dependency, get_membershipimport, get_namespaceimport, get_subclassification, get_specialization, get_featuremembership, get_redefinition, get_subsetting, get_featuretyping, get_typefeaturing, get_featureinverting, get_featurechaining, get_referencesubsetting, get_conjugation, get_multiplicity, get_intersecting, get_unioning, get_disjoining, get_differencing, get_endfeaturemembership, get_elementfiltermembership, get_expression, get_function, get_package, get_librarypackage, get_invocationexpression, get_featurereferenceexpression, get_operatorexpression, get_literalstring, get_literalexpression, get_literalboolean, get_literalinteger, get_nullexpression, get_metadataaccessexpression, get_metadatafeature, get_metaclass, get_selectexpression, get_featurechainexpression, get_collectexpression, get_literalinfinity, get_literalrational, get_multiplicityrange, get_featurevalue, get_bindingconnector, get_association, get_invariant, get_booleanexpression, get_predicate, get_returnparametermembership, get_parametermembership, get_resultexpressionmembership, get_datatype, get_interaction, get_itemflowend, get_itemflow, get_itemfeature, get_successionitemflow, get_associationstructure, get_aliasidscontainer, get_featuring, get_relationship, get_element, get_annotatingelement, get_behavior, get_class, get_classifier, get_type, get_namespace, get_step, get_feature, get_succession, get_connector, get_structure
from lionweb.model.reference_value import ReferenceValue
from lionweb.model import Node


class VisibilityKind(Enum):
    private = 'private'
    protected = 'protected'
    public = 'public'


class FeatureDirectionKind(Enum):
    in_ = 'in'
    inout = 'inout'
    out = 'out'


class IRelationship(Node, ABC):
    pass


class AliasIdsContainer(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_aliasidscontainer()

    @property
    def aliasIds(self) ->str:
        return cast(str, get_property_value_by_name(self, 'aliasIds'))

    @aliasIds.setter
    def aliasIds(self, value: str):
        property_ = self.get_classifier().require_property_by_name('aliasIds')
        self.set_property_value(property=property_, value=value)


class IElement(Node, ABC):
    pass


class Membership(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_membership()

    @property
    def membershipOwningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'membershipOwningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @membershipOwningNamespace.setter
    def membershipOwningNamespace(self, membershipOwningNamespace: 'INamespace'
        ):
        reference = self.get_classifier().get_reference_by_name(
            'membershipOwningNamespace')
        if self.membershipOwningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            membershipOwningNamespace, membershipOwningNamespace.name))

    @property
    def memberElementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'memberElementId'))

    @memberElementId.setter
    def memberElementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'memberElementId')
        self.set_property_value(property=property_, value=value)

    @property
    def memberShortName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'memberShortName'))

    @memberShortName.setter
    def memberShortName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'memberShortName')
        self.set_property_value(property=property_, value=value)

    @property
    def memberElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'memberElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @memberElement.setter
    def memberElement(self, memberElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('memberElement'
            )
        if self.memberElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(memberElement,
            memberElement.name))

    @property
    def memberName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'memberName'))

    @memberName.setter
    def memberName(self, value: str):
        property_ = self.get_classifier().require_property_by_name('memberName'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def visibility(self) ->VisibilityKind:
        return cast(VisibilityKind, get_property_value_by_name(self,
            'visibility'))

    @visibility.setter
    def visibility(self, value: VisibilityKind):
        property_ = self.get_classifier().require_property_by_name('visibility'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class OwningMembership(Membership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_owningmembership()

    @property
    def ownedMemberElementId(self) ->str:
        return cast(str, get_property_value_by_name(self,
            'ownedMemberElementId'))

    @ownedMemberElementId.setter
    def ownedMemberElementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'ownedMemberElementId')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedMemberShortName(self) ->str:
        return cast(str, get_property_value_by_name(self,
            'ownedMemberShortName'))

    @ownedMemberShortName.setter
    def ownedMemberShortName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'ownedMemberShortName')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedMemberName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'ownedMemberName'))

    @ownedMemberName.setter
    def ownedMemberName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'ownedMemberName')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedMemberElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedMemberElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @ownedMemberElement.setter
    def ownedMemberElement(self, ownedMemberElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedMemberElement')
        if self.ownedMemberElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedMemberElement, ownedMemberElement.name))


class INamespace(Node, ABC):
    pass


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
    def importedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'importedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @importedElement.setter
    def importedElement(self, importedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'importedElement')
        if self.importedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(importedElement,
            importedElement.name))

    @property
    def importOwningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'importOwningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @importOwningNamespace.setter
    def importOwningNamespace(self, importOwningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'importOwningNamespace')
        if self.importOwningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            importOwningNamespace, importOwningNamespace.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class IAnnotatingElement(Node, ABC):
    pass


class Comment(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_comment()

    @property
    def locale(self) ->str:
        return cast(str, get_property_value_by_name(self, 'locale'))

    @locale.setter
    def locale(self, value: str):
        property_ = self.get_classifier().require_property_by_name('locale')
        self.set_property_value(property=property_, value=value)

    @property
    def body(self) ->str:
        return cast(str, get_property_value_by_name(self, 'body'))

    @body.setter
    def body(self, value: str):
        property_ = self.get_classifier().require_property_by_name('body')
        self.set_property_value(property=property_, value=value)

    def add_to_annotated_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotating_relationship(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotatingRelationship'),
            ReferenceValue(new_element, new_element.name))

    def add_to_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Documentation(Comment):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_documentation()

    @property
    def documentedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'documentedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @documentedElement.setter
    def documentedElement(self, documentedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'documentedElement')
        if self.documentedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            documentedElement, documentedElement.name))


class Annotation(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_annotation()

    @property
    def annotatingElement(self) ->Optional['IAnnotatingElement']:
        res = get_only_reference_value_by_reference_name(self,
            'annotatingElement')
        if res:
            return cast(IAnnotatingElement, res.referred)
        else:
            return None

    @annotatingElement.setter
    def annotatingElement(self, annotatingElement: 'IAnnotatingElement'):
        reference = self.get_classifier().get_reference_by_name(
            'annotatingElement')
        if self.annotatingElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            annotatingElement, annotatingElement.name))

    @property
    def annotatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'annotatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @annotatedElement.setter
    def annotatedElement(self, annotatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'annotatedElement')
        if self.annotatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(annotatedElement,
            annotatedElement.name))

    @property
    def owningAnnotatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningAnnotatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningAnnotatedElement.setter
    def owningAnnotatedElement(self, owningAnnotatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningAnnotatedElement')
        if self.owningAnnotatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningAnnotatedElement, owningAnnotatedElement.name))

    @property
    def owningAnnotatingElement(self) ->Optional['IAnnotatingElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningAnnotatingElement')
        if res:
            return cast(IAnnotatingElement, res.referred)
        else:
            return None

    @owningAnnotatingElement.setter
    def owningAnnotatingElement(self, owningAnnotatingElement:
        'IAnnotatingElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningAnnotatingElement')
        if self.owningAnnotatingElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningAnnotatingElement, owningAnnotatingElement.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class TextualRepresentation(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_textualrepresentation()

    @property
    def language(self) ->str:
        return cast(str, get_property_value_by_name(self, 'language'))

    @language.setter
    def language(self, value: str):
        property_ = self.get_classifier().require_property_by_name('language')
        self.set_property_value(property=property_, value=value)

    @property
    def body(self) ->str:
        return cast(str, get_property_value_by_name(self, 'body'))

    @body.setter
    def body(self, value: str):
        property_ = self.get_classifier().require_property_by_name('body')
        self.set_property_value(property=property_, value=value)

    @property
    def representedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'representedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @representedElement.setter
    def representedElement(self, representedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'representedElement')
        if self.representedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            representedElement, representedElement.name))

    def add_to_annotated_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotating_relationship(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotatingRelationship'),
            ReferenceValue(new_element, new_element.name))

    def add_to_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Dependency(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_dependency()

    def add_to_client(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('client'), ReferenceValue(new_element,
            new_element.name))

    def add_to_supplier(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('supplier'), ReferenceValue(
            new_element, new_element.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class MembershipImport(Import):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_membershipimport()

    @property
    def importedMembership(self) ->Optional['Membership']:
        res = get_only_reference_value_by_reference_name(self,
            'importedMembership')
        if res:
            return cast(Membership, res.referred)
        else:
            return None

    @importedMembership.setter
    def importedMembership(self, importedMembership: 'Membership'):
        reference = self.get_classifier().get_reference_by_name(
            'importedMembership')
        if self.importedMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            importedMembership, importedMembership.name))


class NamespaceImport(Import):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_namespaceimport()

    @property
    def importedNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'importedNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'importedNamespace')
        if self.importedNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            importedNamespace, importedNamespace.name))


class Specialization(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_specialization()

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def general(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'general')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @general.setter
    def general(self, general: 'IType'):
        reference = self.get_classifier().get_reference_by_name('general')
        if self.general:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(general, general
            .name))

    @property
    def specific(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'specific')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @specific.setter
    def specific(self, specific: 'IType'):
        reference = self.get_classifier().get_reference_by_name('specific')
        if self.specific:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(specific,
            specific.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Subclassification(Specialization):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_subclassification()

    @property
    def superclassifier(self) ->Optional['IClassifier']:
        res = get_only_reference_value_by_reference_name(self,
            'superclassifier')
        if res:
            return cast(IClassifier, res.referred)
        else:
            return None

    @superclassifier.setter
    def superclassifier(self, superclassifier: 'IClassifier'):
        reference = self.get_classifier().get_reference_by_name(
            'superclassifier')
        if self.superclassifier:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(superclassifier,
            superclassifier.name))

    @property
    def owningClassifier(self) ->Optional['IClassifier']:
        res = get_only_reference_value_by_reference_name(self,
            'owningClassifier')
        if res:
            return cast(IClassifier, res.referred)
        else:
            return None

    @owningClassifier.setter
    def owningClassifier(self, owningClassifier: 'IClassifier'):
        reference = self.get_classifier().get_reference_by_name(
            'owningClassifier')
        if self.owningClassifier:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningClassifier,
            owningClassifier.name))

    @property
    def subclassifier(self) ->Optional['IClassifier']:
        res = get_only_reference_value_by_reference_name(self, 'subclassifier')
        if res:
            return cast(IClassifier, res.referred)
        else:
            return None

    @subclassifier.setter
    def subclassifier(self, subclassifier: 'IClassifier'):
        reference = self.get_classifier().get_reference_by_name('subclassifier'
            )
        if self.subclassifier:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(subclassifier,
            subclassifier.name))


class IType(Node, ABC):
    pass


class IFeaturing(Node, ABC):
    pass


class FeatureMembership(OwningMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featuremembership()

    @property
    def ownedMemberFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedMemberFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @ownedMemberFeature.setter
    def ownedMemberFeature(self, ownedMemberFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedMemberFeature')
        if self.ownedMemberFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedMemberFeature, ownedMemberFeature.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def type(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'type')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @type.setter
    def type(self, type: 'IType'):
        reference = self.get_classifier().get_reference_by_name('type')
        if self.type:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(type, type.name))

    @property
    def feature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'feature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @feature.setter
    def feature(self, feature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('feature')
        if self.feature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(feature, feature
            .name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class IFeature(Node, ABC):
    pass


class Subsetting(Specialization):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_subsetting()

    @property
    def subsettedFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'subsettedFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @subsettedFeature.setter
    def subsettedFeature(self, subsettedFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'subsettedFeature')
        if self.subsettedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(subsettedFeature,
            subsettedFeature.name))

    @property
    def subsettingFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'subsettingFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @subsettingFeature.setter
    def subsettingFeature(self, subsettingFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'subsettingFeature')
        if self.subsettingFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            subsettingFeature, subsettingFeature.name))

    @property
    def owningFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'owningFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @owningFeature.setter
    def owningFeature(self, owningFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('owningFeature'
            )
        if self.owningFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningFeature,
            owningFeature.name))


class Redefinition(Subsetting):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_redefinition()

    @property
    def redefiningFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'redefiningFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @redefiningFeature.setter
    def redefiningFeature(self, redefiningFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'redefiningFeature')
        if self.redefiningFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            redefiningFeature, redefiningFeature.name))

    @property
    def redefinedFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'redefinedFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @redefinedFeature.setter
    def redefinedFeature(self, redefinedFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'redefinedFeature')
        if self.redefinedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(redefinedFeature,
            redefinedFeature.name))


class FeatureTyping(Specialization):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featuretyping()

    @property
    def typedFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'typedFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @typedFeature.setter
    def typedFeature(self, typedFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('typedFeature')
        if self.typedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(typedFeature,
            typedFeature.name))

    @property
    def type(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'type')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @type.setter
    def type(self, type: 'IType'):
        reference = self.get_classifier().get_reference_by_name('type')
        if self.type:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(type, type.name))

    @property
    def owningFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'owningFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @owningFeature.setter
    def owningFeature(self, owningFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('owningFeature'
            )
        if self.owningFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningFeature,
            owningFeature.name))


class TypeFeaturing(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_typefeaturing()

    @property
    def featureOfType(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureOfType')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureOfType.setter
    def featureOfType(self, featureOfType: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureOfType'
            )
        if self.featureOfType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureOfType,
            featureOfType.name))

    @property
    def featuringType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'featuringType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @featuringType.setter
    def featuringType(self, featuringType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('featuringType'
            )
        if self.featuringType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featuringType,
            featuringType.name))

    @property
    def owningFeatureOfType(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureOfType')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @owningFeatureOfType.setter
    def owningFeatureOfType(self, owningFeatureOfType: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureOfType')
        if self.owningFeatureOfType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureOfType, owningFeatureOfType.name))

    @property
    def type(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'type')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @type.setter
    def type(self, type: 'IType'):
        reference = self.get_classifier().get_reference_by_name('type')
        if self.type:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(type, type.name))

    @property
    def feature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'feature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @feature.setter
    def feature(self, feature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('feature')
        if self.feature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(feature, feature
            .name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class FeatureInverting(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featureinverting()

    @property
    def featureInverted(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'featureInverted')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureInverted.setter
    def featureInverted(self, featureInverted: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'featureInverted')
        if self.featureInverted:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureInverted,
            featureInverted.name))

    @property
    def invertingFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'invertingFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @invertingFeature.setter
    def invertingFeature(self, invertingFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'invertingFeature')
        if self.invertingFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(invertingFeature,
            invertingFeature.name))

    @property
    def owningFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'owningFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @owningFeature.setter
    def owningFeature(self, owningFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('owningFeature'
            )
        if self.owningFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningFeature,
            owningFeature.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class FeatureChaining(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featurechaining()

    @property
    def chainingFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'chainingFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @chainingFeature.setter
    def chainingFeature(self, chainingFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'chainingFeature')
        if self.chainingFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(chainingFeature,
            chainingFeature.name))

    @property
    def featureChained(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureChained'
            )
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureChained.setter
    def featureChained(self, featureChained: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'featureChained')
        if self.featureChained:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureChained,
            featureChained.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class ReferenceSubsetting(Subsetting):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_referencesubsetting()

    @property
    def referencedFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'referencedFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @referencedFeature.setter
    def referencedFeature(self, referencedFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'referencedFeature')
        if self.referencedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencedFeature, referencedFeature.name))

    @property
    def referencingFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'referencingFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @referencingFeature.setter
    def referencingFeature(self, referencingFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'referencingFeature')
        if self.referencingFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencingFeature, referencingFeature.name))


class Conjugation(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_conjugation()

    @property
    def originalType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'originalType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @originalType.setter
    def originalType(self, originalType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('originalType')
        if self.originalType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(originalType,
            originalType.name))

    @property
    def conjugatedType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'conjugatedType'
            )
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @conjugatedType.setter
    def conjugatedType(self, conjugatedType: 'IType'):
        reference = self.get_classifier().get_reference_by_name(
            'conjugatedType')
        if self.conjugatedType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(conjugatedType,
            conjugatedType.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Multiplicity(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_multiplicity()

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Intersecting(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_intersecting()

    @property
    def intersectingType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self,
            'intersectingType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @intersectingType.setter
    def intersectingType(self, intersectingType: 'IType'):
        reference = self.get_classifier().get_reference_by_name(
            'intersectingType')
        if self.intersectingType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(intersectingType,
            intersectingType.name))

    @property
    def typeIntersected(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self,
            'typeIntersected')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @typeIntersected.setter
    def typeIntersected(self, typeIntersected: 'IType'):
        reference = self.get_classifier().get_reference_by_name(
            'typeIntersected')
        if self.typeIntersected:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(typeIntersected,
            typeIntersected.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Unioning(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_unioning()

    @property
    def unioningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'unioningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @unioningType.setter
    def unioningType(self, unioningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('unioningType')
        if self.unioningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(unioningType,
            unioningType.name))

    @property
    def typeUnioned(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'typeUnioned')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @typeUnioned.setter
    def typeUnioned(self, typeUnioned: 'IType'):
        reference = self.get_classifier().get_reference_by_name('typeUnioned')
        if self.typeUnioned:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(typeUnioned,
            typeUnioned.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Disjoining(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_disjoining()

    @property
    def typeDisjoined(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'typeDisjoined')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @typeDisjoined.setter
    def typeDisjoined(self, typeDisjoined: 'IType'):
        reference = self.get_classifier().get_reference_by_name('typeDisjoined'
            )
        if self.typeDisjoined:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(typeDisjoined,
            typeDisjoined.name))

    @property
    def disjoiningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'disjoiningType'
            )
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @disjoiningType.setter
    def disjoiningType(self, disjoiningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name(
            'disjoiningType')
        if self.disjoiningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(disjoiningType,
            disjoiningType.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Differencing(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_differencing()

    @property
    def differencingType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self,
            'differencingType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @differencingType.setter
    def differencingType(self, differencingType: 'IType'):
        reference = self.get_classifier().get_reference_by_name(
            'differencingType')
        if self.differencingType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(differencingType,
            differencingType.name))

    @property
    def typeDifferenced(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self,
            'typeDifferenced')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @typeDifferenced.setter
    def typeDifferenced(self, typeDifferenced: 'IType'):
        reference = self.get_classifier().get_reference_by_name(
            'typeDifferenced')
        if self.typeDifferenced:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(typeDifferenced,
            typeDifferenced.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class IClassifier(Node, ABC):
    pass


class EndFeatureMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_endfeaturemembership()


class ElementFilterMembership(OwningMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_elementfiltermembership()

    @property
    def condition(self) ->Optional['Expression']:
        res = get_only_reference_value_by_reference_name(self, 'condition')
        if res:
            return cast(Expression, res.referred)
        else:
            return None

    @condition.setter
    def condition(self, condition: 'Expression'):
        reference = self.get_classifier().get_reference_by_name('condition')
        if self.condition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(condition,
            condition.name))


class IStep(Node, ABC):
    pass


class Expression(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_expression()

    @property
    def function(self) ->Optional['Function']:
        res = get_only_reference_value_by_reference_name(self, 'function')
        if res:
            return cast(Function, res.referred)
        else:
            return None

    @function.setter
    def function(self, function: 'Function'):
        reference = self.get_classifier().get_reference_by_name('function')
        if self.function:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(function,
            function.name))

    @property
    def result(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'result')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @result.setter
    def result(self, result: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('result')
        if self.result:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(result, result.name)
            )

    @property
    def isModelLevelEvaluable(self) ->bool:
        return cast(bool, get_property_value_by_name(self,
            'isModelLevelEvaluable'))

    @isModelLevelEvaluable.setter
    def isModelLevelEvaluable(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isModelLevelEvaluable')
        self.set_property_value(property=property_, value=value)

    def add_to_behavior(self, new_element: 'IBehavior'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('behavior'), ReferenceValue(
            new_element, new_element.name))

    def add_to_parameter(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('parameter'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class IClass(Node, ABC):
    pass


class IBehavior(Node, ABC):
    pass


class Function(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_function()

    def add_to_expression(self, new_element: 'Expression'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('expression'), ReferenceValue(
            new_element, new_element.name))

    @property
    def result(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'result')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @result.setter
    def result(self, result: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('result')
        if self.result:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(result, result.name)
            )

    @property
    def isModelLevelEvaluable(self) ->bool:
        return cast(bool, get_property_value_by_name(self,
            'isModelLevelEvaluable'))

    @isModelLevelEvaluable.setter
    def isModelLevelEvaluable(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isModelLevelEvaluable')
        self.set_property_value(property=property_, value=value)

    def add_to_step(self, new_element: 'IStep'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('step'), ReferenceValue(new_element,
            new_element.name))

    def add_to_parameter(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('parameter'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Package(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_package()

    def add_to_filter_condition(self, new_element: 'Expression'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('filterCondition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class LibraryPackage(Package):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_librarypackage()

    @property
    def isStandard(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isStandard'))

    @isStandard.setter
    def isStandard(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isStandard'
            )
        self.set_property_value(property=property_, value=value)


class InvocationExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_invocationexpression()

    def add_to_argument(self, new_element: 'Expression'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('argument'), ReferenceValue(
            new_element, new_element.name))


class FeatureReferenceExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featurereferenceexpression()

    @property
    def referent(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'referent')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @referent.setter
    def referent(self, referent: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('referent')
        if self.referent:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(referent,
            referent.name))


class OperatorExpression(InvocationExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_operatorexpression()

    @property
    def operator(self) ->str:
        return cast(str, get_property_value_by_name(self, 'operator'))

    @operator.setter
    def operator(self, value: str):
        property_ = self.get_classifier().require_property_by_name('operator')
        self.set_property_value(property=property_, value=value)


class LiteralExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_literalexpression()


class LiteralString(LiteralExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_literalstring()

    @property
    def value(self) ->str:
        return cast(str, get_property_value_by_name(self, 'value'))

    @value.setter
    def value(self, value: str):
        property_ = self.get_classifier().require_property_by_name('value')
        self.set_property_value(property=property_, value=value)


class LiteralBoolean(LiteralExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_literalboolean()

    @property
    def value(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'value'))

    @value.setter
    def value(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('value')
        self.set_property_value(property=property_, value=value)


class LiteralInteger(LiteralExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_literalinteger()

    @property
    def value(self) ->int:
        return cast(int, get_property_value_by_name(self, 'value'))

    @value.setter
    def value(self, value: int):
        property_ = self.get_classifier().require_property_by_name('value')
        self.set_property_value(property=property_, value=value)


class NullExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_nullexpression()


class MetadataAccessExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_metadataaccessexpression()

    @property
    def referencedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'referencedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @referencedElement.setter
    def referencedElement(self, referencedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'referencedElement')
        if self.referencedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencedElement, referencedElement.name))


class MetadataFeature(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_metadatafeature()

    @property
    def metaclass(self) ->Optional['Metaclass']:
        res = get_only_reference_value_by_reference_name(self, 'metaclass')
        if res:
            return cast(Metaclass, res.referred)
        else:
            return None

    @metaclass.setter
    def metaclass(self, metaclass: 'Metaclass'):
        reference = self.get_classifier().get_reference_by_name('metaclass')
        if self.metaclass:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(metaclass,
            metaclass.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_annotated_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotating_relationship(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotatingRelationship'),
            ReferenceValue(new_element, new_element.name))

    def add_to_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))


class IStructure(Node, ABC):
    pass


class Metaclass(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_metaclass()

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class SelectExpression(OperatorExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_selectexpression()


class FeatureChainExpression(OperatorExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featurechainexpression()

    @property
    def targetFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'targetFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @targetFeature.setter
    def targetFeature(self, targetFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('targetFeature'
            )
        if self.targetFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(targetFeature,
            targetFeature.name))


class CollectExpression(OperatorExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_collectexpression()


class LiteralInfinity(LiteralExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_literalinfinity()


class LiteralRational(LiteralExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_literalrational()

    @property
    def value(self) ->float:
        return cast(float, get_property_value_by_name(self, 'value'))

    @value.setter
    def value(self, value: float):
        property_ = self.get_classifier().require_property_by_name('value')
        self.set_property_value(property=property_, value=value)


class MultiplicityRange(Multiplicity):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_multiplicityrange()

    @property
    def lowerBound(self) ->Optional['Expression']:
        res = get_only_reference_value_by_reference_name(self, 'lowerBound')
        if res:
            return cast(Expression, res.referred)
        else:
            return None

    @lowerBound.setter
    def lowerBound(self, lowerBound: 'Expression'):
        reference = self.get_classifier().get_reference_by_name('lowerBound')
        if self.lowerBound:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(lowerBound,
            lowerBound.name))

    @property
    def upperBound(self) ->Optional['Expression']:
        res = get_only_reference_value_by_reference_name(self, 'upperBound')
        if res:
            return cast(Expression, res.referred)
        else:
            return None

    @upperBound.setter
    def upperBound(self, upperBound: 'Expression'):
        reference = self.get_classifier().get_reference_by_name('upperBound')
        if self.upperBound:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(upperBound,
            upperBound.name))

    def add_to_bound(self, new_element: 'Expression'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('bound'), ReferenceValue(new_element,
            new_element.name))


class FeatureValue(OwningMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featurevalue()

    @property
    def featureWithValue(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'featureWithValue')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureWithValue.setter
    def featureWithValue(self, featureWithValue: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'featureWithValue')
        if self.featureWithValue:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureWithValue,
            featureWithValue.name))

    @property
    def value(self) ->Optional['Expression']:
        res = get_only_reference_value_by_reference_name(self, 'value')
        if res:
            return cast(Expression, res.referred)
        else:
            return None

    @value.setter
    def value(self, value: 'Expression'):
        reference = self.get_classifier().get_reference_by_name('value')
        if self.value:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(value, value.name))

    @property
    def isInitial(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isInitial'))

    @isInitial.setter
    def isInitial(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isInitial')
        self.set_property_value(property=property_, value=value)

    @property
    def isDefault(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDefault'))

    @isDefault.setter
    def isDefault(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDefault')
        self.set_property_value(property=property_, value=value)


class IConnector(Node, ABC):
    pass


class BindingConnector(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_bindingconnector()

    def add_to_related_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_association(self, new_element: 'Association'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('association'), ReferenceValue(
            new_element, new_element.name))

    def add_to_connector_end(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('connectorEnd'), ReferenceValue(
            new_element, new_element.name))

    @property
    def sourceFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'sourceFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @sourceFeature.setter
    def sourceFeature(self, sourceFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('sourceFeature'
            )
        if self.sourceFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(sourceFeature,
            sourceFeature.name))

    def add_to_target_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('targetFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))


class Association(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_association()

    def add_to_related_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def sourceType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'sourceType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @sourceType.setter
    def sourceType(self, sourceType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('sourceType')
        if self.sourceType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(sourceType,
            sourceType.name))

    def add_to_target_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('targetType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_association_end(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('associationEnd'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))


class ISuccession(Node, ABC):
    pass


class BooleanExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_booleanexpression()

    @property
    def predicate(self) ->Optional['Predicate']:
        res = get_only_reference_value_by_reference_name(self, 'predicate')
        if res:
            return cast(Predicate, res.referred)
        else:
            return None

    @predicate.setter
    def predicate(self, predicate: 'Predicate'):
        reference = self.get_classifier().get_reference_by_name('predicate')
        if self.predicate:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(predicate,
            predicate.name))


class Invariant(BooleanExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_invariant()

    @property
    def isNegated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNegated'))

    @isNegated.setter
    def isNegated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isNegated')
        self.set_property_value(property=property_, value=value)


class Predicate(Function):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_predicate()


class ParameterMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_parametermembership()

    @property
    def ownedMemberParameter(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedMemberParameter')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @ownedMemberParameter.setter
    def ownedMemberParameter(self, ownedMemberParameter: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedMemberParameter')
        if self.ownedMemberParameter:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedMemberParameter, ownedMemberParameter.name))


class ReturnParameterMembership(ParameterMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_returnparametermembership()


class ResultExpressionMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_resultexpressionmembership()

    @property
    def ownedResultExpression(self) ->Optional['Expression']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedResultExpression')
        if res:
            return cast(Expression, res.referred)
        else:
            return None

    @ownedResultExpression.setter
    def ownedResultExpression(self, ownedResultExpression: 'Expression'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedResultExpression')
        if self.ownedResultExpression:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedResultExpression, ownedResultExpression.name))


class DataType(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_datatype()

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Interaction(Association):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_interaction()

    def add_to_step(self, new_element: 'IStep'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('step'), ReferenceValue(new_element,
            new_element.name))

    def add_to_parameter(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('parameter'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class ItemFlowEnd(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_itemflowend()

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class ItemFlow(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_itemflow()

    def add_to_item_type(self, new_element: 'IClassifier'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('itemType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def targetInputFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'targetInputFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @targetInputFeature.setter
    def targetInputFeature(self, targetInputFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'targetInputFeature')
        if self.targetInputFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            targetInputFeature, targetInputFeature.name))

    @property
    def sourceOutputFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self,
            'sourceOutputFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @sourceOutputFeature.setter
    def sourceOutputFeature(self, sourceOutputFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name(
            'sourceOutputFeature')
        if self.sourceOutputFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            sourceOutputFeature, sourceOutputFeature.name))

    def add_to_item_flow_end(self, new_element: 'ItemFlowEnd'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('itemFlowEnd'), ReferenceValue(
            new_element, new_element.name))

    @property
    def itemFeature(self) ->Optional['ItemFeature']:
        res = get_only_reference_value_by_reference_name(self, 'itemFeature')
        if res:
            return cast(ItemFeature, res.referred)
        else:
            return None

    @itemFeature.setter
    def itemFeature(self, itemFeature: 'ItemFeature'):
        reference = self.get_classifier().get_reference_by_name('itemFeature')
        if self.itemFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(itemFeature,
            itemFeature.name))

    def add_to_interaction(self, new_element: 'Interaction'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('interaction'), ReferenceValue(
            new_element, new_element.name))

    def add_to_related_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_association(self, new_element: 'Association'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('association'), ReferenceValue(
            new_element, new_element.name))

    def add_to_connector_end(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('connectorEnd'), ReferenceValue(
            new_element, new_element.name))

    @property
    def sourceFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'sourceFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @sourceFeature.setter
    def sourceFeature(self, sourceFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('sourceFeature'
            )
        if self.sourceFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(sourceFeature,
            sourceFeature.name))

    def add_to_target_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('targetFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_behavior(self, new_element: 'IBehavior'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('behavior'), ReferenceValue(
            new_element, new_element.name))

    def add_to_parameter(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('parameter'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))


class ItemFeature(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_itemfeature()

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class SuccessionItemFlow(ItemFlow):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_successionitemflow()

    @property
    def transitionStep(self) ->Optional['IStep']:
        res = get_only_reference_value_by_reference_name(self, 'transitionStep'
            )
        if res:
            return cast(IStep, res.referred)
        else:
            return None

    @transitionStep.setter
    def transitionStep(self, transitionStep: 'IStep'):
        reference = self.get_classifier().get_reference_by_name(
            'transitionStep')
        if self.transitionStep:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(transitionStep,
            transitionStep.name))

    def add_to_trigger_step(self, new_element: 'IStep'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('triggerStep'), ReferenceValue(
            new_element, new_element.name))

    def add_to_effect_step(self, new_element: 'IStep'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('effectStep'), ReferenceValue(
            new_element, new_element.name))

    def add_to_guard_expression(self, new_element: 'Expression'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('guardExpression'), ReferenceValue(
            new_element, new_element.name))

    def add_to_related_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_association(self, new_element: 'Association'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('association'), ReferenceValue(
            new_element, new_element.name))

    def add_to_connector_end(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('connectorEnd'), ReferenceValue(
            new_element, new_element.name))

    @property
    def sourceFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'sourceFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @sourceFeature.setter
    def sourceFeature(self, sourceFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('sourceFeature'
            )
        if self.sourceFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(sourceFeature,
            sourceFeature.name))

    def add_to_target_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('targetFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))


class AssociationStructure(Association):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_associationstructure()

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Featuring(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_featuring()

    @property
    def type(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'type')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @type.setter
    def type(self, type: 'IType'):
        reference = self.get_classifier().get_reference_by_name('type')
        if self.type:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(type, type.name))

    @property
    def feature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'feature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @feature.setter
    def feature(self, feature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('feature')
        if self.feature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(feature, feature
            .name))

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Relationship(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_relationship()

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Element(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_element()

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class AnnotatingElement(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_annotatingelement()

    def add_to_annotated_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotating_relationship(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotatingRelationship'),
            ReferenceValue(new_element, new_element.name))

    def add_to_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('annotation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Behavior(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_behavior()

    def add_to_step(self, new_element: 'IStep'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('step'), ReferenceValue(new_element,
            new_element.name))

    def add_to_parameter(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('parameter'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Class(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_class()

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Classifier(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_classifier()

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Type(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_type()

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Namespace(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_namespace()

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Step(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_step()

    def add_to_behavior(self, new_element: 'IBehavior'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('behavior'), ReferenceValue(
            new_element, new_element.name))

    def add_to_parameter(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('parameter'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Feature(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_feature()

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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


class Succession(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_succession()

    @property
    def transitionStep(self) ->Optional['IStep']:
        res = get_only_reference_value_by_reference_name(self, 'transitionStep'
            )
        if res:
            return cast(IStep, res.referred)
        else:
            return None

    @transitionStep.setter
    def transitionStep(self, transitionStep: 'IStep'):
        reference = self.get_classifier().get_reference_by_name(
            'transitionStep')
        if self.transitionStep:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(transitionStep,
            transitionStep.name))

    def add_to_trigger_step(self, new_element: 'IStep'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('triggerStep'), ReferenceValue(
            new_element, new_element.name))

    def add_to_effect_step(self, new_element: 'IStep'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('effectStep'), ReferenceValue(
            new_element, new_element.name))

    def add_to_guard_expression(self, new_element: 'Expression'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('guardExpression'), ReferenceValue(
            new_element, new_element.name))

    def add_to_related_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_association(self, new_element: 'Association'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('association'), ReferenceValue(
            new_element, new_element.name))

    def add_to_connector_end(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('connectorEnd'), ReferenceValue(
            new_element, new_element.name))

    @property
    def sourceFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'sourceFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @sourceFeature.setter
    def sourceFeature(self, sourceFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('sourceFeature'
            )
        if self.sourceFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(sourceFeature,
            sourceFeature.name))

    def add_to_target_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('targetFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))


class Connector(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_connector()

    def add_to_related_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_association(self, new_element: 'Association'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('association'), ReferenceValue(
            new_element, new_element.name))

    def add_to_connector_end(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('connectorEnd'), ReferenceValue(
            new_element, new_element.name))

    @property
    def sourceFeature(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'sourceFeature')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @sourceFeature.setter
    def sourceFeature(self, sourceFeature: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('sourceFeature'
            )
        if self.sourceFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(sourceFeature,
            sourceFeature.name))

    def add_to_target_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('targetFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    def add_to_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_redefinition(self, new_element: 'Redefinition'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_subsetting(self, new_element: 'Subsetting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->Optional['FeatureMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast(FeatureMembership, res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        'FeatureMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->Optional['IType']:
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast(IType, res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: 'IType'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    def add_to_owned_typing(self, new_element: 'FeatureTyping'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    def add_to_featuring_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_type_featuring(self, new_element: 'TypeFeaturing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    def add_to_chaining_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_feature_inverting(self, new_element: 'FeatureInverting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_chaining(self, new_element: 'FeatureChaining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->Optional['ReferenceSubsetting']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast(ReferenceSubsetting, res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        'ReferenceSubsetting'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def featureTarget(self) ->Optional['IFeature']:
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast(IFeature, res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: 'IFeature'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    def add_to_related_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('relatedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_target(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('target'), ReferenceValue(new_element,
            new_element.name))

    def add_to_source(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('source'), ReferenceValue(new_element,
            new_element.name))

    @property
    def owningRelatedElement(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelatedElement')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owningRelatedElement.setter
    def owningRelatedElement(self, owningRelatedElement: 'IElement'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelatedElement')
        if self.owningRelatedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelatedElement, owningRelatedElement.name))

    @property
    def isImplied(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImplied'))

    @isImplied.setter
    def isImplied(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isImplied')
        self.set_property_value(property=property_, value=value)

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))


class Structure(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_structure()

    def add_to_owned_subclassification(self, new_element: 'Subclassification'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubclassification'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature_membership(self, new_element: 'FeatureMembership'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_owned_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_input(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    def add_to_output(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    def add_to_end_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->Optional['Conjugation']:
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast(Conjugation, res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: 'Conjugation'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    def add_to_inherited_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->Optional['Multiplicity']:
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast(Multiplicity, res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: 'Multiplicity'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    def add_to_unioning_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_intersecting(self, new_element: 'Intersecting'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    def add_to_intersecting_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_unioning(self, new_element: 'Unioning'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_disjoining(self, new_element: 'Disjoining'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    def add_to_feature_membership(self, new_element: 'FeatureMembership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_differencing_type(self, new_element: 'IType'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_differencing(self, new_element: 'Differencing'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    def add_to_directed_feature(self, new_element: 'IFeature'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_specialization(self, new_element: 'Specialization'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    def add_to_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_import(self, new_element: 'Import'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    def add_to_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    def add_to_owned_member(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    def add_to_imported_membership(self, new_element: 'Membership'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def owningMembership(self) ->Optional['OwningMembership']:
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast(OwningMembership, res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: 'OwningMembership'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningRelationship(self) ->Optional['IRelationship']:
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast(IRelationship, res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: 'IRelationship'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def owningNamespace(self) ->Optional['INamespace']:
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast(INamespace, res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: 'INamespace'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def owner(self) ->Optional['IElement']:
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast(IElement, res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: 'IElement'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    def add_to_owned_element(self, new_element: 'IElement'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    def add_to_documentation(self, new_element: 'Documentation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_owned_annotation(self, new_element: 'Annotation'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    def add_to_textual_representation(self, new_element:
        'TextualRepresentation'):
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
