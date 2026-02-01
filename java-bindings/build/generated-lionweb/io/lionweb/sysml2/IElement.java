package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;
import java.lang.String;

public interface IElement extends Node {
  void setOwningMembership(ReferenceValue value);

  ReferenceValue getOwningMembership();

  void setOwningNamespace(ReferenceValue value);

  ReferenceValue getOwningNamespace();

  void setOwningRelationship(ReferenceValue value);

  ReferenceValue getOwningRelationship();

  String getElementId();

  void setElementId(String value);

  int addToOwnedRelationship(IRelationship child, int index);

  void setOwner(ReferenceValue value);

  ReferenceValue getOwner();

  int addToOwnedElement(ReferenceValue referenceValue, int index);

  int addToDocumentation(ReferenceValue referenceValue, int index);

  int addToOwnedAnnotation(ReferenceValue referenceValue, int index);

  int addToTextualRepresentation(ReferenceValue referenceValue, int index);

  String getDeclaredShortName();

  void setDeclaredShortName(String value);

  String getDeclaredName();

  void setDeclaredName(String value);

  String getShortName();

  void setShortName(String value);

  String getName();

  void setName(String value);

  String getQualifiedName();

  void setQualifiedName(String value);

  Boolean getIsImpliedIncluded();

  void setIsImpliedIncluded(Boolean value);

  Boolean getIsLibraryElement();

  void setIsLibraryElement(Boolean value);

  int addToAliasIdsContainer(AliasIdsContainer child, int index);
}
