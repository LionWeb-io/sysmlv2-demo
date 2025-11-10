import {ILanguageBase, LionCore_builtinsBase} from "@lionweb/class-core";

import * as SysMLv2 from "./SysMLv2.g.js";
import * as Types from "./Types.g.js";

// ensure that all languages get wired up by triggering that through their first entity:
LionCore_builtinsBase.INSTANCE.String;
SysMLv2.SysMLv2Base.INSTANCE.Subclassification;
Types.TypesBase.INSTANCE.Boolean;

export const allLanguageBases: ILanguageBase[] = [
    SysMLv2.SysMLv2Base.INSTANCE,
    Types.TypesBase.INSTANCE
];

export {
    SysMLv2,
    Types
};

