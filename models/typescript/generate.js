import { generateApiFromLanguages } from "@lionweb/class-core-generator"
import { defaultSimplisticHandler, deserializeLanguagesWithHandler } from "@lionweb/core"
import { readFileAsJson } from "@lionweb/utilities"

const typesLanguage = deserializeLanguagesWithHandler(readFileAsJson("../types_lionweb.json"), defaultSimplisticHandler)[0]

const sysMlV2Language = deserializeLanguagesWithHandler(readFileAsJson("../SysML_lionweb_lionweb.json"), defaultSimplisticHandler, typesLanguage)[0]
sysMlV2Language.name = "SysMLv2"

sysMlV2Language.entities.forEach((entity) => {
    if (entity.name === "Classifier") {
        entity.name = "SysMLv2Classifier"
    }
})

generateApiFromLanguages([sysMlV2Language, typesLanguage], "src")

