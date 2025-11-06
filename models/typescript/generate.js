import { generateApiFromLanguages } from "@lionweb/class-core-generator"
import { deserializeLanguages } from "@lionweb/core"
import { readFileAsJson } from "@lionweb/utilities"
import { setEOLStyleFromOS } from "littoral-templates-node"

// read the JSON for the SysMLv2 *types* language, and deserialize it as a Language object:
const typesLanguage = deserializeLanguages(readFileAsJson("../types_lionweb.json"))[0]

// read the JSON for the SysMLv2 language (that relies on the types language), and deserialize it as a Language object:
const sysMlV2Language = deserializeLanguages(readFileAsJson("../SysML_lionweb_lionweb.json"), typesLanguage)[0]

// tweak the language’s name, to have more standard file and class names:
sysMlV2Language.name = "SysMLv2"
// tweak the name of the language’s Classifier concept, to deconflict from LionCore’s own Classifier meta-concept:
sysMlV2Language.entities.forEach((entity) => {
    if (entity.name === "Classifier") {
        entity.name = "SysMLv2Classifier"
    }
})

// ensure that line endings are generated OS-compliant:
await setEOLStyleFromOS()

// generate a complete API for both the SysMLv2 language and its accompanying types language:
generateApiFromLanguages([sysMlV2Language, typesLanguage], "src")

