using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using LionWeb.Core;
using LionWeb.Core.M2;
using LionWeb.Core.M3;
using LionWeb.Core.Serialization;
using LionWeb.Generator;
using LionWeb.Generator.GeneratorExtensions;
using LionWeb.Generator.Names;

var baseDir = Path.GetFullPath(args[0]);
Console.WriteLine($"baseDir: {baseDir}");

var sysml2Dir = Path.GetFullPath(Path.Combine([baseDir, "..", ".."]));
Console.WriteLine($"sysml2Dir: {sysml2Dir}");

var lionWebVersion = LionWebVersions.v2023_1;

List<Language> dependentLanguages = [];

var typesLanguage = await Deserialize(lionWebVersion, $"{sysml2Dir}/types_lionweb.json", dependentLanguages);
dependentLanguages.Add(typesLanguage);
var kermlLanguage = await Deserialize(lionWebVersion, $"{sysml2Dir}/kerml_lionweb_lionweb.json", dependentLanguages);
dependentLanguages.Add(kermlLanguage);
var sysmlLanguage = await Deserialize(lionWebVersion, $"{sysml2Dir}/SysML_lionweb_lionweb.json", dependentLanguages);
dependentLanguages.Add(sysmlLanguage);

var namespaceMappings = new Dictionary<Language, string>
{
    { typesLanguage, "LionWeb.Demo.SysMl2.Languages.Types" },
    { kermlLanguage, "LionWeb.Demo.SysMl2.Languages.KerMl" },
    { sysmlLanguage, "LionWeb.Demo.SysMl2.Languages.SysMl2" },
};

var primitiveTypeMappings = new Dictionary<PrimitiveType, Type>
{
    { typesLanguage.FindByKey<PrimitiveType>("types-Boolean"), typeof(bool) },
    { typesLanguage.FindByKey<PrimitiveType>("types-Integer"), typeof(int) },
    { typesLanguage.FindByKey<PrimitiveType>("types-Real"), typeof(decimal) },
    { typesLanguage.FindByKey<PrimitiveType>("types-String"), typeof(string) },
    { typesLanguage.FindByKey<PrimitiveType>("types-UnlimitedNatural"), typeof(decimal) }
};

var outputDir = Path.GetFullPath(Path.Combine([baseDir, "..", "SysML2.Languages"]));
Console.WriteLine($"outputDir: {outputDir}");

foreach (var language in dependentLanguages)
{
    var languageNamespace = namespaceMappings[language];
    var generator = new GeneratorFacade
    {
        Names = new Names(language, languageNamespace)
        {
            NamespaceMappings = namespaceMappings, PrimitiveTypeMappings = primitiveTypeMappings
        },
        LionWebVersion = lionWebVersion
    };

    generator.PersistFilePerType(outputDir, false,
        (_, file) => Console.WriteLine($"Wrote output to {file}"));
}

return;

async Task<DynamicLanguage> Deserialize(IVersion2023_1 lwVersion, string filePath, List<Language> depLang)
{
    await using var jsonFile = new FileStream(filePath, FileMode.Open);

    var deserializer = new LanguageDeserializerBuilder()
        .WithLionWebVersion(lwVersion)
        .WithCompressedIds(new(KeepOriginal: true))
        .WithDependentLanguages(depLang)
        .Build();

    var nodes = await JsonUtils.ReadNodesFromStreamAsync(jsonFile, deserializer);

    return nodes.Cast<DynamicLanguage>().Single();
}