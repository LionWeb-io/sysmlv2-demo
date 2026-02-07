package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IImport extends Node, IRelationship {
  VisibilityKind getVisibility();

  void setVisibility(VisibilityKind value);

  Boolean getIsRecursive();

  void setIsRecursive(Boolean value);

  Boolean getIsImportAll();

  void setIsImportAll(Boolean value);

  void setImportedElement(ReferenceValue value);

  ReferenceValue getImportedElement();

  void setImportOwningNamespace(ReferenceValue value);

  ReferenceValue getImportOwningNamespace();
}
