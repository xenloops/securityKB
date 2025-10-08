# The OWASP Top 10 Application Security Risks

## Broken Access Control 

Software neglects to check who's allowed to do what. Attackers can bypass controls (e.g. by forced browsing or modifying URLs/tokens) to access data or perform actions they shouldn't. Akin to leaving the keys in an unlocked car.

_(2021: A01, 2017: A05)_

## Cryptographic Failures

The absence, misuse, or meglect of cryptography (e.g. outdated algorithm, bad key management, poor choice of mode) exposes sensitive data. Was called "Sensitive Data Exposure" but now we focus on the root problem: people making bad choices in crypto. If you treat encryption like black magic, expect things to go very wrong.

_(2021: A02, 2017: A03)_

## Injection

Now groups injection types such as SQL, NoSQL, command, and others under one category. Input from untrusted sources gets inserted into queries/commands, and the application doesn't discern between data and code, allowing attackers to execute arbitrary code. Even Cross-Site Scripting (XSS) is now folded in here, because even after two decades, it’s still a thing. 

_(2021: A03, 2017: A01)_

## Insecure Design

Design flaws (not implementation ones) are baked in early; this is a failure to perform threat modeling, insecure patterns, or secure defaults. You can code flawlessly, but if your app is fundamentally badly planned, attackers will find the holes. This is an architectural category rather than bugs in the code.

_(2021: A04)_

## Security Misconfiguration

The server, framework, or platform is left with default creds, wide permissions, unpatched features, etc. These settings are everywhere and often forgotten. A big neon sign to attackers of sloppy work.

_(2021: A05, 2017: A04/A06)_

## Vulnerable and Outdated Components

Using libraries, frameworks, or modules that have known vulnerabilities or are no longer maintained. Devs are lazy (like everyone), and don't want to build a car if they can download one from the dealer's web site. Patching is boring (until you're breached), so this isn't likely to be solved soon. Remember, an **application accepts the risk of all its third-party components**.

_(2021: A06, 2017: A09)_

## Identification and Authentication Failures

The system doesn’t reliably check who someone is, or allows bad authentication flows. Weak passwords, lack of MFA, sessions not invalidated, etc. If attackers can pretend to be someone else, they _will_.

_(2021: A07, 2017: A02)_

## Software and Data Integrity Failures

Assuming that updates, data, or external resources are safe without verifying. Includes insecure deserialization, untrusted CI/CD pipelines, or software supply chain attacks. If someone can tamper under the hood, safety checks are useless.

_(2021: A08)_

## Security Logging and Monitoring Failures

No decent logging? No alerting? No monitoring? That means breaches happen in the dark, leaving everyone unprepared. Detecting, investigating, and responding to attacks depends on this, but many apps treat it as afterthought.

_(2021: A09, 2017: A10)_

## Server-Side Request Forgery (SSRF)

The server is tricked into making unintended requests (e.g. internal network, cloud metadata endpoints). The problem occurs when at least part of a remote resource URL is under user control and the application neglects to validate it. Attackers use SSRF to breach internal systems not directly exposed to the outside.

_(2021: A10)_
