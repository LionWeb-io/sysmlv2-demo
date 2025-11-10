import { allSuperTypesOf, Classifier, Language } from "@lionweb/core"
import { generatePlantUmlForLanguage } from "./PlantUML-generator"


export const focusedDiagram = (sysMLv2Language: Language): string => {

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

    return generatePlantUmlForLanguage(sysMLv2Language, interestingEntities)
}

