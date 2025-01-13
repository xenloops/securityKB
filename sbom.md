# Software Bill of Materials (SBOM)

An SBOM is a comprehensive, structured inventory that lists the software components, dependencies, and related metadata used in a software system. It is similar to a bill of materials for a physical product but focuses on the digital components that make up a software system.

## Typical SBOM contents

* Component Name: The name of each software component, library, or module.
* Version Information: The version number of each component to identify specific releases.
* Licensing Information: Details about the licenses governing each component, such as MIT, Apache, or GPL.
* Supplier Information: The source or author of the component (e.g., open source, vendor, or internal team).
* Dependency Information: Relationships between components, including direct and transitive (nested) dependencies.
* Vulnerability Data: Known vulnerabilities (e.g., CVEs) associated with each component, where applicable.
* File Integrity Data: Hashes or checksums of files to verify integrity and authenticity.

## Purpose of an SBOM

An SBOM serves several critical functions:

* Transparency: Provides visibility into the software components used, their origins, and associated risks.
* Cybersecurity: Helps identify vulnerabilities and manage risk by tracking dependencies and their vulnerabilities.
* Compliance: Ensures compliance with licensing requirements and regulatory standards, such as those set by the FDA for medical devices.
* Incident Response: Speeds up response to security incidents by allowing organizations to quickly determine if affected components are part of their software.
* Software Supply Chain Management: Assists in understanding and managing risks in the software supply chain.
* Regulatory Compliance: Increasingly required by regulations, such as the U.S. Executive Order on Improving the Nation's Cybersecurity, and standards like the FDA's cybersecurity guidance for medical devices.
* Risk Mitigation: Identifies outdated, vulnerable, or unlicensed components to reduce cybersecurity and legal risks.
* Trust and Collaboration: Provides confidence to customers, regulators, and partners by demonstrating a clear understanding of software composition.

## Common SBOM Formats

* CycloneDX: A lightweight SBOM format focused on application security.
* SPDX (Software Package Data Exchange): An open standard maintained by the Linux Foundation.
* SWID (Software Identification Tags): An ISO standard commonly used for tracking installed software.


## The SBOM process

Beyond giving teams useful insight into a project's development, generating an SBOM for a regulated project requires precision and adherence to regulatory expectations. These expectations may differ depending on the regulatory agency and region, so be sure to get expert advice on the particular needs of the project.


1. Understand SBOM Requirements for Submission

  * Familiarize yourself with regulatory guidance on cybersecurity, including the requirements for SBOM documntation.
  * Ensure the SBOM includes:
      * All software components (open source, commercial, and proprietary).
      * Dependencies, including nested/indirect ones.
      * Versions, licenses, and associated vulnerabilities (CVEs).
      * Known exploitability status and remediation steps.

2. Prepare the Tools Environment

  * Standardize Component Management: Ensure that all software components are sourced consistently and documented within your configuration management system or package manager.
  * Integrate Checkmarx into CI/CD Pipelines: Enable automated scans at key stages of development to continuously capture component metadata.
  * Verify Development Tools: Ensure the development, build, or security scanning (i.e. SCA) tools used can output metadata needed for SBOM generation.

3. Scan Source Code and Dependencies

  * Scan the entire codebase, including:
       * Source code repositories.
       * Third-party libraries.
       * Containerized environments (if applicable).
   * Omit any of the following from the scan, unless there's a good reason to include:
       * Test code
       * Non-code directories in the repositories
       * Helper utilities that do not get deployed
   * Include Transitive Dependencies: Configure the tool to capture transitive (nested) dependencies. This step is critical for a complete SBOM.
   * Automate Recurring Scans: Schedule periodic scans to maintain an up-to-date SBOM throughout the project lifecycle.

4. Generate the SBOM

   * Use the tools's reporting/exporting feature to extract dependency and vulnerability data in a standardized SBOM format.
   * Validate Component Metadata: Ensure the exported SBOM includes:
       * Component name, version, and supplier.
       * Dependency relationships (direct and indirect).
       * Vulnerability mappings and licenses.

5. Validate and Augment the SBOM

   * Cross-Check Against Build Artifacts:
       * Compare the SBOM against build manifests or package managers (e.g., npm, Maven, Pip) to ensure all components are accounted for.
       * Validate the SBOM against any container images if your medical device includes containerized applications.
   * Resolve Discrepancies: Address any missing or incorrect metadata in collaboration with the development team.
   * Add Security Metadata: Include known vulnerabilities, their severity, exploitability, and mitigation details.

6. Perform SBOM Quality Assurance

   * Automated Validation:
       * Use tools like SPDX validators or CycloneDX CLI to check for schema compliance.
       * Ensure the SBOM meets internal and regulatory quality standards.
    * Manual Review:
       * Conduct a manual review to ensure completeness and correctness, focusing especially on high-risk components.

7. Prepare SBOM for Submission

    * Generate Final SBOM Report:
       * Ensure the SBOM includes all required elements (e.g., file hashes, authorship, and timestamps).
       * Include a narrative description of the SBOM generation process for transparency.
     * Document Validation Process: Provide evidence of validation steps taken to ensure SBOM accuracy.
     * Export in Regulatory-Preferred Format: Provide the SBOM in a format acceptable to the regulatory agency (consult with regulatory experts if necessary).

8. Maintain SBOM Throughout the Product Lifecycle

   * Monitor Vulnerabilities: Use the SCA tool to continuously monitor for new vulnerabilities in SBOM components and update the SBOM accordingly.
   * Version Control: Store SBOM versions in a secure, version-controlled repository for traceability.
   * Periodically Update: Update the SBOM or rescan after any software updates, patches, or component changes.

9. Ensure Regulatory Compliance

   * Map SBOM to Requirements: Cross-reference the SBOM against submission guidelines to confirm compliance.
   * Engage Cybersecurity Experts: Consult cybersecurity professionals to ensure the SBOM aligns with expectations for managing software-related risks.

This process emphasizes automation, traceability, and regulatory alignment to streamline SBOM generation and validation with minimal manual labor.
   
