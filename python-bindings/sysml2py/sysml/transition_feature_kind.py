from enum import Enum


class TransitionFeatureKind(Enum):
    trigger = 'trigger'
    guard = 'guard'
    effect = 'effect'
