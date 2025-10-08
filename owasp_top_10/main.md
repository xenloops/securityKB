# The OWASP Top 10 Application Security Risks

## Broken Access Control (2021: A01)

Software neglects to check who's allowed to do what. Attackers can bypass controls (e.g. by forced browsing or modifying URLs/tokens) to access data or perform actions they shouldn't. Akin to leaving the keys in an unlocked car.

## Cryptographic Failures (2021: A02)

The absence, misuse, or meglect of cryptography (e.g. outdated algorithm, bad key management, poor choice of mode) exposes sensitive data. Was called "Sensitive Data Exposure" but now we focus on the root problem: people making bad choices in crypto. If you treat encryption like black magic, expect things to go very wrong.

## Injection (2021: A03)

Now groups injection types such as SQL, NoSQL, command, and others under one category. Input from untrusted sources gets inserted into queries/commands, and the application doesn't discern between data and code, allowing attackers to execute arbitrary code. Even Cross-Site Scripting (XSS) is now folded in here, because even after two decades, it’s still a thing. 

## Insecure Design (2021: A04)

Design flaws (not implementation ones) are baked in early; this is a failure to perform threat modeling, insecure patterns, or secure defaults. You can code flawlessly, but if your app is fundamentally badly planned, attackers will find the holes. This is an architectural category rather than bugs in the code.

## Security Misconfiguration (2021: A05)

The server, framework, or platform is left with default creds, wide permissions, unpatched features, etc. These settings are everywhere and often forgotten. A big neon sign to attackers of sloppy work.

## Vulnerable and Outdated Components (2021: A06)

Using libraries, frameworks, or modules that have known vulnerabilities or are no longer maintained. Devs are lazy (like everyone), and don't want to build a car if they can download one from the dealer's web site. Patching is boring (until you're breached), so this isn't likely to be solved soon. Remember, an **application accepts the risk of all its third-party components**.

## Identification and Authentication Failures (2021: A07)

The system doesn’t reliably check who someone is, or allows bad authentication flows. Weak passwords, lack of MFA, sessions not invalidated, etc. If attackers can pretend to be someone else, they _will_.

## Software and Data Integrity Failures (2021: A08)

Assuming that updates, data, or external resources are safe without verifying. Includes insecure deserialization, untrusted CI/CD pipelines, or software supply chain attacks. If someone can tamper under the hood, safety checks are useless.

## Security Logging and Monitoring Failures (2021: A09)

No decent logging? No alerting? No monitoring? That means breaches happen in the dark, leaving everyone unprepared. Detecting, investigating, and responding to attacks depends on this, but many apps treat it as afterthought.

## Server-Side Request Forgery (SSRF) (2021: A10)

The server is tricked into making unintended requests (e.g. internal network, cloud metadata endpoints). The problem occurs when at least part of a remote resource URL is under user control and the application neglects to validate it. Attackers use SSRF to breach internal systems not directly exposed to the outside.

