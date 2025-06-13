# Software Composition Analysis

## What is SCA?

Software Composition Analysis tells you what libraries a software project depends upon (or "uses"). It then looks up those libraries (or dependencies) and their versions to find whether they have any known vulnerabilities (or CVEs). SCA is basically a glorified database lookup engine, though some scanners also attempt to figure out whether your project is calling vulnerable functions inside those dependencies.

## What is an SBOM?

A Software Bill of Materials is derived from output from an SCA scan. It lists the dependencies in a project, and often includes vulnerability data. Organizations in regulated indistries often have a requirement to produce an SBOM with commentary regarding each vulnerabilty (including any controls in place or plans to remediate the vulnerability).

## When should we get an SCA scan done?

Potentially, when the project has finished changing the dependencies it uses. However, new vulnerabilities are discovered in the wild every day, so the vulnerabilities may change if the scan is performed early in development. A good rule of thumb is if a scan is more than two weeks old, it's probably outdated.

## Why do dependencies we don't use get reported?

SCA scanning tools don't always know which dependencies are used in production. Updates to those libraries and frameworks used only in development or test environments that never get promoted to production can probably be delayed or  ignored (if the organization's policy allows).

If a dependency is reported as being in the project and no one on the team thinks it's used, find and remove the reference. If the project still compiles, runs, and tests well, the dependency indeed wasn't needed.

## Why do we care about transitive dependencies?

Vulnerabilities in libraries that are not called directly by a project are _transitive_, or dependencies of direct dependencies (or of their dependencies, and so on). We always want to reduce risk to a project wherever possible, and transitive dependencies bring their own risk to the table. A project team usually has no say in when a dependency upgrades its dependencies (unless  it's a large organization with sway over the maintainers), so if there is no update to the a dependency that has no CVEs there may be no way to remediate those findings. Choices at that point include contact the maintainers, wait for the update (a.k.a. accept the risk), place a control that mitigaes the risk, or remove/replace the dependency.



