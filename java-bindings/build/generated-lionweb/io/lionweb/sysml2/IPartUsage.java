package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IPartUsage extends Node, IItemUsage {
  int addToPartDefinition(ReferenceValue referenceValue, int index);
}
