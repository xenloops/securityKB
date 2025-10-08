# The OWASP Top 10 Application Security Risks

## A01: Broken Access Control

Application neglects to check who's allowed to do what. Attackers can bypass controls (e.g. by forced browsing or modifying URLs/tokens) to access data or perform actions they shouldn't. Akin to leaving the keys in an unlocked car.

## A02: Cryptographic Failures

The absence, misuse, or meglect of cryptography (e.g. outdated algorithm, bad key management, poor choice of mode) exposes sensitive data. Was called "Sensitive Data Exposure" but now we focus on the root problem: people making bad choices in crypto. If you treat encryption like black magic, expect things to go very wrong.

## A03: Injection

Now groups injection types such as SQL, NoSQL, command, and others under one category. Input from untrusted sources gets inserted into queries/commands, and the application doesn't discern between data and code, allowing attackers to execute arbitrary code. Even Cross-Site Scripting (XSS) is now folded in here, because even after two decades, it’s still a thing. 

## A04: Insecure Design

Design flaws (not implementation ones) are baked in early; this is a failure to perform threat modeling, insecure patterns, or secure defaults. You can code flawlessly, but if your app is fundamentally badly planned, attackers will find the holes. This is an architectural category rather than bugs in the code.

## A05: Security Misconfiguration

The server, framework, or platform is left with default creds, wide permissions, unpatched features, etc. These settings are everywhere and often forgotten. A big neon sign to attackers of sloppy work.

A06: Vulnerable and Outdated Components

Using libraries, frameworks, or modules that have known vulnerabilities or are no longer maintained. Because patching is boring (until you're breached). One vulnerable component is enough to screw up everything else. 

A07: Identification and Authentication Failures

When the system can’t reliably check who someone is, or allows bad authentication flows. Weak passwords, lack of MFA, sessions not invalidated—all those nasty bits. If attackers can pretend to be someone else, rest assured they will. 

A08: Software and Data Integrity Failures

Assuming that updates, data, or external resources are safe without verifying. Includes insecure deserialization, untrusted CI/CD pipelines, or software supply chain attacks. If someone can tamper under the hood, your safety checks go out the window. 

A09: Security Logging and Monitoring Failures

No decent logging? No alerting? No monitoring? That means breaches happen in the dark, and you’re utterly unprepared. Detecting, investigating, and responding to attacks depends on this stuff—but many apps treat it as afterthought. 

A10: Server-Side Request Forgery (SSRF)

Your server is tricked into making unintended requests (e.g. internal network, cloud metadata endpoints). Attackers use SSRF to breach internal systems not directly exposed to the outside. It’s sneaky, dangerous, and often overlooked until it's too late. 

