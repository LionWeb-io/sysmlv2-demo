from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name
from lionweb.model.impl.dynamic_node import DynamicNode
from .language import get_language
from lionweb.model.reference_value import ReferenceValue
from lionweb.model import Node
