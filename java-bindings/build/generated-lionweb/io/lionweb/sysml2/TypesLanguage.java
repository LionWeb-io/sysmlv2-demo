package io.lionweb.sysml2;

import io.lionweb.LionWebVersion;
import io.lionweb.language.Language;
import io.lionweb.language.PrimitiveType;

public class TypesLanguage extends Language {
  private static TypesLanguage INSTANCE;

  private TypesLanguage() {
    super(LionWebVersion.v2023_1);
    this.setName("types");
    this.setVersion("1");
    this.setID("types");
    this.setKey("types");
    createElements();
  }

  public static TypesLanguage getInstance() {
    if (INSTANCE == null) {
      INSTANCE = new TypesLanguage();
    }
    return INSTANCE;
  }

  public PrimitiveType getBoolean() {
    return this.requirePrimitiveTypeByName("Boolean");
  }

  public PrimitiveType getInteger() {
    return this.requirePrimitiveTypeByName("Integer");
  }

  public PrimitiveType getReal() {
    return this.requirePrimitiveTypeByName("Real");
  }

  public PrimitiveType getUnlimitedNatural() {
    return this.requirePrimitiveTypeByName("UnlimitedNatural");
  }

  public PrimitiveType getString() {
    return this.requirePrimitiveTypeByName("String");
  }

  private void createElements() {
    PrimitiveType _boolean = new PrimitiveType(this, "Boolean", "types-Boolean");;
    _boolean.setKey("types-Boolean");
    PrimitiveType integer = new PrimitiveType(this, "Integer", "types-Integer");;
    integer.setKey("types-Integer");
    PrimitiveType real = new PrimitiveType(this, "Real", "types-Real");;
    real.setKey("types-Real");
    PrimitiveType unlimitedNatural = new PrimitiveType(this, "UnlimitedNatural", "types-UnlimitedNatural");;
    unlimitedNatural.setKey("types-UnlimitedNatural");
    PrimitiveType string = new PrimitiveType(this, "String", "types-String");;
    string.setKey("types-String");
  }
}
