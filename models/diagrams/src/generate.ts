import { writeFileSync } from "fs"
import { asString } from "littoral-templates"
import { setEOLStyleFromOS } from "littoral-templates-node"
import { defaultSimplisticHandler, deserializeLanguagesWithHandler } from "@lionweb/core"
import { LionWebJsonChunk } from "@lionweb/json"
import { generatePlantUmlForLanguage, languageAsText, readFileAsJson } from "@lionweb/utilities"

import { focusedDiagram } from "./custom-diagram"

const typesLanguage = deserializeLanguagesWithHandler(readFileAsJson("../types_lionweb.json") as LionWebJsonChunk, defaultSimplisticHandler)[0]
const sysMLv2Language = deserializeLanguagesWithHandler(readFileAsJson("../SysML_lionweb_lionweb.json") as LionWebJsonChunk, defaultSimplisticHandler, typesLanguage)[0]
const kerMLlanguage = deserializeLanguagesWithHandler(readFileAsJson("../kerml_lionweb_lionweb.json") as LionWebJsonChunk, defaultSimplisticHandler, typesLanguage)[0]

setEOLStyleFromOS()

writeFileSync("artifacts/types.puml", generatePlantUmlForLanguage(typesLanguage))
writeFileSync("artifacts/types.txt", languageAsText(typesLanguage))

writeFileSync("artifacts/kerml.puml", generatePlantUmlForLanguage(kerMLlanguage))
writeFileSync("artifacts/kerml.txt", languageAsText(kerMLlanguage))

writeFileSync("artifacts/sysml.puml", generatePlantUmlForLanguage(sysMLv2Language))
writeFileSync("artifacts/sysml.txt", languageAsText(sysMLv2Language))

writeFileSync("artifacts/sysml_focused.puml", asString(focusedDiagram(sysMLv2Language)))

