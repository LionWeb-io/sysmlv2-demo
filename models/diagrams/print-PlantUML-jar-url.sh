#!/bin/sh

readonly plantUmlVersion="1.2024.8"
readonly jarFile="plantuml-$plantUmlVersion.jar"

echo "URL to download the required PlantUML JAR file:"
echo "https://github.com/plantuml/plantuml/releases/download/v$plantUmlVersion/$jarFile"
# (Somehow, I'm not getting cURL to work correctly — at least not under macOS...)

echo

echo "NOTE: after downloading, copy the downloaded JAR from the downloads directory to this directory, e.g. by executing the following on the command-line:"
echo "  $ mv ~/Downloads/$jarFile ./"

