# Security Scan Triage Guide for Development Teams

## Understand what you’re looking at:

   * SAST (Static Application Security Testing) scans source code looking for issues without running the app. Like linting, but for security.
   * SCA (Software Composition Analysis) looks at a project's dependencies, licenses, and versions for known vulnerabilities. There should be no false positives with this (though frequently there is disagreement on whether to include test or dev-only dependencies).
   * DAST (Dynamic Application Security Testing) tests a running app like an external attacker would. Fewer false positives than SAST, but less context on the code.

## Initial Sanity Check

Before diving in:

   * Review everything, but keep an eye out for duplicates and false positives.
   * Prioritize by severity (but don't just go by CVSS score; also perform some kind of [risk rating](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)):
     * **Critical**: Probably actively being exploited in the wild, with low probability of false positives. Address immediately.
     * **High**: Can lead to compromise without much effort. Address quickly.
     * **Medium**: Important, but weigh against business impact and exploit likelihood.
     * **Low**: Fix when convenient unless it’s a stepping stone for a bigger exploit.
     * **Info**: Usually code quality issues, without much security ramification. Should be safe to ignore.

Map to exploitable reality:

   * Is this actually reachable in your app’s execution path?
   * Is it gated by strong authentication or input validation?
   * Would fixing it break something more critical?

## Triage Steps for SAST Findings

Confirm the issue:

   * Look at the flagged code.
   * Ask: "If I were an attacker, could I abuse this?"

Validate the context:

   * Is the data input controlled by a user?
   * Is it sanitized or escaped before it hits the dangerous sink/output?

Mark false positives. Mature organizations have a Security Center of Excellence with a findings review board. If a finding doesn't look exploitable:
    
   1. Mark it as proposed not exploitable (or similar verbiage for the tool).
   2. Document why you think it’s not exploitable (with code evidence).
   3. Route the finding for the appropriate review (this step may wait until all findings are addressed).

If the finding is valid:

   1. Assign to the owning developer.
   2. Add the vulnerability to the sprint or hotfix queue based on severity.

If not fixable immediately:

   1. Add compensating controls (input validation, feature flag limits, logging).
   2. Create a tracking ticket with a risk acceptance note.

## Triage Steps for SCA Findings

Check CVE details:

  1. What’s the exploit scenario?
  2. Is it actually in the code path you use?
  3. Check for a safe upgrade path:

     * Does a patch or minor upgrade exist without breaking API compatibility?
     * Weigh patch vs. mitigation; if patching breaks builds, is there a configuration change or feature disable that removes exposure?

Mark as false positive if the vulnerable feature/module isn’t included in your build (and you can prove it).

Track high-risk dependencies: add automated monitoring so regressions don’t creep back in.

## DAST-Specific Differences

  * SAST/SCA flag potential problems; DAST shows live exploitability.
  * If DAST confirms a SAST/SCA finding, raise the finding's priority immediately.
  * DAST false positives happen less often, but context can be vague -— retrace the attack scenario in your code.

## Documentation

Always log:

  * Vulnerability ID (CVE, CWE, etc.)
  * Severity & exploitability assessment
  * Decision (fix now, backlog, accept risk)
  * Evidence for false positives
  * Owner and expected resolution date

## Feedback Loop

  * Update scan rules or suppressions for recurring false positives —- but only with strong evidence.
  * Feed fixes back into secure coding guidelines.
  * Schedule regular review of "accepted risk" items.

## Golden Rules

  * Don’t dismiss findings on internally facing projects. Internal systems get breached too.
  * Don’t blindly trust the scanner’s severity ratings. A “Medium” with high exposure can be more dangerous than a “High” behind five layers of controls.
  * Fix root causes, not just the specific instance.

