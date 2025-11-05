import { writeFileSync } from "fs"
import { defaultSimplisticHandler, deserializeLanguagesWithHandler } from "@lionweb/core"
import { LionWebJsonChunk } from "@lionweb/json"
import { generatePlantUmlForLanguage, readFileAsJson } from "@lionweb/utilities"

const typesLanguage = deserializeLanguagesWithHandler(readFileAsJson("../types_lionweb.json") as LionWebJsonChunk, defaultSimplisticHandler)[0]
const sysMlV2Language = deserializeLanguagesWithHandler(readFileAsJson("../SysML_lionweb_lionweb.json") as LionWebJsonChunk, defaultSimplisticHandler, typesLanguage)[0]

writeFileSync("artifacts/types.puml", generatePlantUmlForLanguage(typesLanguage))
writeFileSync("artifacts/sysml.puml", generatePlantUmlForLanguage(sysMlV2Language))

