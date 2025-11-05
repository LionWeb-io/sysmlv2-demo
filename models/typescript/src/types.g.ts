/*
 * language's metadata:
 *     name:    types
 *     version: 1
 *     key:     types
 *     id:      types
 */


import {
    Classifier,
    EnumerationLiteral,
    Language,
    PrimitiveType
} from "@lionweb/core";

import {
    LionWebId
} from "@lionweb/json";

import {
    DeltaReceiver,
    ILanguageBase,
    NodeBaseFactory
} from "@lionweb/class-core";


export class typesBase implements ILanguageBase {

    private readonly _language: Language = new Language("types", "1", "types", "types");
    get language(): Language {
        this.ensureWiredUp();
        return this._language;
    }

    public readonly _Boolean = new PrimitiveType(this._language, "Boolean", "types-Boolean", "types-Boolean");
    get Boolean(): PrimitiveType {
        this.ensureWiredUp();
        return this._Boolean;
    }

    public readonly _Integer = new PrimitiveType(this._language, "Integer", "types-Integer", "types-Integer");
    get Integer(): PrimitiveType {
        this.ensureWiredUp();
        return this._Integer;
    }

    public readonly _Real = new PrimitiveType(this._language, "Real", "types-Real", "types-Real");
    get Real(): PrimitiveType {
        this.ensureWiredUp();
        return this._Real;
    }

    public readonly _UnlimitedNatural = new PrimitiveType(this._language, "UnlimitedNatural", "types-UnlimitedNatural", "types-UnlimitedNatural");
    get UnlimitedNatural(): PrimitiveType {
        this.ensureWiredUp();
        return this._UnlimitedNatural;
    }

    public readonly _String = new PrimitiveType(this._language, "String", "types-String", "types-String");
    get String(): PrimitiveType {
        this.ensureWiredUp();
        return this._String;
    }

    private _wiredUp: boolean = false;
    private ensureWiredUp() {
        if (this._wiredUp) {
            return;
        }
        this._language.havingEntities(this._Boolean, this._Integer, this._Real, this._UnlimitedNatural, this._String);
        this._wiredUp = true;
    }

    factory(_receiveDelta?: DeltaReceiver): NodeBaseFactory {
        return (classifier: Classifier, _id: LionWebId) => {
            const {language} = classifier;
            throw new Error(`can't instantiate ${classifier.name} (key=${classifier.key}): classifier is not known in language ${language.name} (key=${language.key}, version=${language.version})`);
        }
    }

    enumLiteralFrom<EnumType>(enumerationLiteral: EnumerationLiteral): EnumType {
        const {enumeration} = enumerationLiteral;
        const {language} = enumeration;
        throw new Error(`enumeration with key ${enumeration.key} is not known in language ${language.name} (key=${language.key}, version=${language.version})`);
    }

    public static readonly INSTANCE = new typesBase();
}


export type Boolean = string;

export type Integer = string;

export type Real = string;

export type UnlimitedNatural = string;

export type String = string;

