# About the tool

Veracode Fix is a remediation solution that helps development teams to get AI/LLM-generated code patches, review the suggested patches, and apply them directly to flaws in their source code without writing any code themselves. This serves to "shift left" (to continue to overuse a buzzterm) AppSec; developers do not have to access the Veracode site directly to run scans and triage findings.

Fix is available in Veracode Scan, an IDE plugin. The general workflow:

* Developer builds project/solution.
* Plugin packages the project code into an artifact (e.g. zip file). The developer can also do this manually.
* Plugin uploads the artifact to Veracode servers for analysis.
* Plugin downloads the results and displays them in the IDE.

## Limitations

Veracode Fix resolves findings found by Pipeline Scan, but doesn't resolve findings found by Upload and Scan.

### Project size

The packaged artifact (e.g. the zip file) must not exceed the total file size limit of 200 MB.

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
  * Visual Studio 2019 (v16.11.40+) and 2022 (v17.11.4+)
  * Visual Studio Code
* GitHub Actions


# Installation

Veracode Scan must be installed to use Fix.

## Visual Studio IDE plugin

TODO _Draft notes, will be refined._

1. Create an API credentials file. Vendor recommends using Single-Sign On (SSO) with Just-in-Time (JIT) provisioning for human user accounts.
2. Install the extension from the Visual Studio Marketplace (in IDE: Extensions menu > Manage Extensions, search for Veracode Scan).
3. Click Install button.
4. Close Visual Studio.
5. When the VSIX Installer prompts, click Modify.
6. If using SSO, browse and authenticate to Veracode's site.
7. Start Visual Studio and open a project.
8. The Veracode Scan options are available under the Tools menu. Select Open Veracode Scan.
9. The Scan window prompts to Authenticate (select the Commercial region).
10. A new browser window opens with the auth code.
11. Allow Veracode to access the information it requires.
12. In Visual Studio, scroll down in the Veracode window. Click Install Agent at the bottom.
13. The Veracode window will automatically advance to its Scan and Review tab.
14. To see results, a scan must be run on a successfully built project.
15. Build the project and resolve any errors that appear.
16. Click the Scan project text at the top of the Veracode window.
17. Wait for the Scanning... messages to be replaced with results.
18. 


## Visual Studio Code IDE plugin



# Sources

* [Vendor documentation](https://docs.veracode.com/r/About_Veracode_Fix)
* 
