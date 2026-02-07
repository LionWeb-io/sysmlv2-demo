package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface INamespace extends Node, IElement {
  int addToMembership(ReferenceValue referenceValue, int index);

  int addToOwnedImport(ReferenceValue referenceValue, int index);

  int addToMember(ReferenceValue referenceValue, int index);

  int addToOwnedMember(ReferenceValue referenceValue, int index);

  int addToImportedMembership(ReferenceValue referenceValue, int index);

  int addToOwnedMembership(ReferenceValue referenceValue, int index);
}
