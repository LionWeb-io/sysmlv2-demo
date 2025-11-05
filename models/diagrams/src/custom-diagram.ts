import { allSuperTypesOf, Classifier, inheritsFrom, Language } from "@lionweb/core"
import { Template } from "littoral-templates"
import { generateForEntity, generateForRelationsOf } from "./PlantUML-generator"


export const focusedDiagram = (sysMLv2Language: Language): Template => {

    const allSubTypesOf = (superClassifier: Classifier) =>
        sysMLv2Language.entities
            .filter((entity) => entity instanceof Classifier)
            .map((entity) => entity as Classifier)
            .filter((subClassifier) => allSuperTypesOf(subClassifier).indexOf(superClassifier) > -1)

    const entity = (target: string) => {
        const candidate = sysMLv2Language.entities.find(({name}) => name === target)
        if (candidate === undefined) {
            throw new Error(`no entity named "${target}"`)
        }
        return candidate
    }

    const interestingNames = [ "INamespace", "Membership" ]
    const interestingEntities = interestingNames.map(entity)
        .concat(allSubTypesOf(entity("Membership") as Classifier))

    return [
        `@startuml`,
        `hide empty members`,
        ``,
        interestingEntities.map(generateForEntity),
        ``,
        interestingEntities.map(generateForRelationsOf),
        ``,
        `@enduml`
    ]
}

