# About the tool

Veracode Fix is a remediation solution that helps development teams to get AI/LLM-generated code patches, review the suggested patches, and apply them directly to flaws in their source code without writing any code themselves. This serves to "shift left" (to continue to overuse a buzzterm) AppSec; developers do not have to access the Veracode site directly to run scans and triage findings.

Fix is available in Veracode Scan, an IDE plugin. The general workflow:

* Developer builds project/solution.
* Plugin packages the project code into an artifact (e.g. ZIP file).
* Plugin uploads the artifact to Veracode servers for analysis.
* Plugin downloads the results and displays them in the IDE.

## Limitations

Veracode Fix resolves findings found by Pipeline Scan, but doesn't resolve findings found by Upload and Scan.

### Supported languages

* C#
* COBOL
* Go
* Java
* JavaScript and TypeScript
* Kotlin
* PHP
* Python
* Ruby
* Scala

### Integrations

* CLI (for automation)
* IDEs
  * Eclipse
  * JetBrains
  * Visual Studio 2019 and 2022
  * Visual Studio Code
* GitHub Action


# Installation

Veracode Scan must be installed to use Fix.

## Visual Studio IDE plugin



## Visual Studio Code IDE plugin

# Sources

* [Vendor documentation](https://docs.veracode.com/r/About_Veracode_Fix)
* 
