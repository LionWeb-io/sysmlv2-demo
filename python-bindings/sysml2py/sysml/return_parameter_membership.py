from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_return_parameter_membership
from .parameter_membership import ParameterMembership


class ReturnParameterMembership(ParameterMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_return_parameter_membership()
