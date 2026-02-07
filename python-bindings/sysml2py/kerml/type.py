from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_type
from lionweb.model.impl.dynamic_node import DynamicNode
if TYPE_CHECKING:
    from .feature_membership import FeatureMembership
    from .i_feature import IFeature
    from .membership import Membership
    from .conjugation import Conjugation
    from .multiplicity import Multiplicity
    from .i_type import IType
    from .intersecting import Intersecting
    from .unioning import Unioning
    from .disjoining import Disjoining
    from .differencing import Differencing
    from .specialization import Specialization
    from .import_ import Import
    from .i_element import IElement
    from .owning_membership import OwningMembership
    from .i_relationship import IRelationship
    from .i_namespace import INamespace
    from .documentation import Documentation
    from .annotation import Annotation
    from .textual_representation import TextualRepresentation


class Type(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_type()

    @property
    def ownedFeatureMembership(self) ->'List["FeatureMembership"]':
        res = get_reference_value_by_name(self, 'ownedFeatureMembership')
        return [(cast('FeatureMembership', r.referred) if r else None) for
            r in res]

    def add_to_owned_feature_membership(self, new_element:
        '"FeatureMembership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    @property
    def ownedFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'ownedFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_owned_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedEndFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'ownedEndFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_owned_end_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def feature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'feature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def input(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'input')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_input(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    @property
    def output(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'output')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_output(self, new_element: '"IFeature"'):
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

    @property
    def inheritedMembership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'inheritedMembership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_inherited_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    @property
    def endFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'endFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_end_feature(self, new_element: '"IFeature"'):
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
    def ownedConjugator(self) ->'Optional["Conjugation"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast('Conjugation', res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: '"Conjugation"'):
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

    @property
    def inheritedFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'inheritedFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_inherited_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->'Optional["Multiplicity"]':
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast('Multiplicity', res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: '"Multiplicity"'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    @property
    def unioningType(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'unioningType')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_unioning_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedIntersecting(self) ->'List["Intersecting"]':
        res = get_reference_value_by_name(self, 'ownedIntersecting')
        return [(cast('Intersecting', r.referred) if r else None) for r in res]

    def add_to_owned_intersecting(self, new_element: '"Intersecting"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def intersectingType(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'intersectingType')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_intersecting_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedUnioning(self) ->'List["Unioning"]':
        res = get_reference_value_by_name(self, 'ownedUnioning')
        return [(cast('Unioning', r.referred) if r else None) for r in res]

    def add_to_owned_unioning(self, new_element: '"Unioning"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedDisjoining(self) ->'List["Disjoining"]':
        res = get_reference_value_by_name(self, 'ownedDisjoining')
        return [(cast('Disjoining', r.referred) if r else None) for r in res]

    def add_to_owned_disjoining(self, new_element: '"Disjoining"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    @property
    def featureMembership(self) ->'List["FeatureMembership"]':
        res = get_reference_value_by_name(self, 'featureMembership')
        return [(cast('FeatureMembership', r.referred) if r else None) for
            r in res]

    def add_to_feature_membership(self, new_element: '"FeatureMembership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    @property
    def differencingType(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'differencingType')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_differencing_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedDifferencing(self) ->'List["Differencing"]':
        res = get_reference_value_by_name(self, 'ownedDifferencing')
        return [(cast('Differencing', r.referred) if r else None) for r in res]

    def add_to_owned_differencing(self, new_element: '"Differencing"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    @property
    def directedFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'directedFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_directed_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedSpecialization(self) ->'List["Specialization"]':
        res = get_reference_value_by_name(self, 'ownedSpecialization')
        return [(cast('Specialization', r.referred) if r else None) for r in
            res]

    def add_to_owned_specialization(self, new_element: '"Specialization"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def membership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'membership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedImport(self) ->'List["Import"]':
        res = get_reference_value_by_name(self, 'ownedImport')
        return [(cast('Import', r.referred) if r else None) for r in res]

    def add_to_owned_import(self, new_element: '"Import"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    @property
    def member(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'member')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_member(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    @property
    def ownedMember(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'ownedMember')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_owned_member(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedMembership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'ownedMembership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_owned_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    @property
    def importedMembership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'importedMembership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_imported_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

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
    def ownedRelationship(self) ->'List["IRelationship"]':
        res = self.get_children('ownedRelationship')
        return res

    def add_to_owned_relationship(self, new_element: '"IRelationship"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'ownedRelationship'), new_element)

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
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

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
