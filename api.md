# APIs

<details>
  <summary> General </summary>
  
* Ensure that adequate authentication, session management, and authorization of all web services are in place.
* Validate all parameters that transit from a lower to higher trust level.
* Design in effective security controls for all API types, including cloud and serverless APIs.
</details>

<details>
  <summary> Top API risks </summary>
  
From the [OWASP 2023 Top 10 API Security Risks](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)

1. [**Broken Object Level Authorization**](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/) (BOLA): APIs tend to expose endpoints that handle object identifiers, creating a wide attack surface of Object Level Access Control issues. Failures in this mechanism typically lead to unauthorized information disclosure, modification, or destruction of data.

    To prevent:
     * Implement a proper authorization mechanism that relies on the user policies and hierarchy.
     * Use the authorization mechanism to check if the logged-in user has access to perform the requested action on the record in every function that uses an input from the client to access a record in the database.
     * Prefer the use of random and unpredictable values as GUIDs for record IDs.
     * Write tests to evaluate the vulnerability of the authorization mechanism. Do not deploy changes that fail the tests.
  
2. [**Broken Authentication**](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/): Authentication mechanisms are often implemented incorrectly, allowing attackers to compromise authentication tokens or to exploit implementation flaws to assume another user's identity. Compromising authentication integrity  compromises API security overall.

    To prevent:
     * Use the [OWASP Authentication Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).
     * Ensure all possible flows to authenticate to the API are known (mobile/web/deep links that implement one-click authentication).
     * Understand what and how authentication mechanisms are used. OAuth is not authentication, and neither are API keys.
     * Use standard, vetted libraries for authentication, token generation, and password storage. Don't reinvent the wheel.
     * Implement anti-brute-force mechanisms to mitigate credential stuffing, dictionary attacks, and brute force attacks on your authentication endpoints. This mechanism should be stricter than the regular rate limiting mechanisms on your APIs.
     * Treat credential-recovery endpoints as login endpoints in terms of brute force, rate limiting, and lockout protections.
     * Implement multi-factor authentication (MFA) where possible.
     * Require re-authentication for sensitive operations (e.g. changing account owner email address or MFA phone number).
     * Implement account lockouts or captchas to prevent brute-force attacks against specific users. Implement weak-password checks.
     * Do not use API keys for user authentication. They should only be used to authenticate API clients.

3. [**Broken Object Property Level Authorization**](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/): The lack of or improper authorization validation at the object property level leads to information exposure or manipulation by unauthorized parties. This is the root cause of other API risks, such as Excessive Data Exposure and Mass Assignment.
  
    To prevent:
     * When exposing an object using an API endpoint, ensure the user _should_ have access to the object's exposed properties.
     * Avoid using generic methods such as to_json() and to_string(). Instead, specify the object properties that must be returned.
     * If possible, avoid using functions that automatically bind a client's input into code variables, internal objects, or object properties ("Mass Assignment").
     * Allow changes only to the object's properties that should be updated by the client.
     * Implement a schema-based response validation mechanism as an extra layer of security. Define and enforce data returned by all API methods.
     * Minimize returned data structures, according to the business/functional requirements for the endpoint.
  
4. [**Unrestricted Resource Consumption**](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/): Satisfying API requests requires resources such as network bandwidth, CPU, memory, and storage. Other resources such as emails/SMS/phone calls or biometrics validation are made available by service providers via API integrations, and paid for per request. Successful attacks can lead to a denial of service and increased operational costs.

    To prevent:
     * Use a solution that makes it easy to limit memory, CPU, number of restarts, file descriptors, and processes such as Containers / Serverless code (e.g. Lambdas).
     * Define and enforce a maximum size of data on all incoming parameters and payloads, such as maximum length for strings, maximum number of elements in arrays, and maximum upload file size.
     * Implement a rate limit on how often a client can interact with the API within a defined timeframe (tuned based on business needs).
     * Limit how many times or throttle how often a client can execute a single operation (e.g. validate an OTP, or request password recovery without visiting the one-time URL).
     * Add proper server-side validation for query string and request body parameters, especially one that controls the number of records to be returned.
     * Configure spending limits for all service providers/API integrations. When setting spending limits is not possible, billing alerts should be configured.

5. [**Broken Function Level Authorization**](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/): Complex access control policies with different hierarchies, groups, and roles, and an unclear separation between administrative and regular functions, tend to lead to authorization flaws. By exploiting these issues, attackers can gain access to other users’ resources and/or administrative functions.

    To prevent:
     * Have a consistent and easy-to-analyze authorization module that is invoked from all business functions. This is usually provided by one or more components external to the application code.
     * Deny all access by default, requiring explicit grants to specific roles for access to every function.
     * Review your API endpoints against function level authorization flaws, while keeping in mind the business logic of the application and group hierarchy.
     * Ensure all administrative controllers inherit from an administrative abstract controller that implements authorization checks based on the user's group/role.
     * Ensure that administrative functions inside a regular controller implement authorization checks based on the user's group and role.

6. [**Unrestricted Access to Sensitive Business Flows**](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/): APIs vulnerable to this risk expose a business flow -- such as making a transaction or posting a comment -- without compensating for how the functionality could harm the business if used excessively in an automated manner. This doesn't necessarily come from implementation bugs.

    To prevent, the mitigation planning should be done in two layers:
     * Business: identify the business flows that might harm the business if they are excessively used.
     * Engineering: choose the right protection mechanisms to mitigate the business risk.

    Some of the protection mechanisms are more simple while others are more difficult to implement. The following methods are used to slow down automated threats:
     * Device fingerprinting: denying service to unexpected client devices (e.g headless browsers) tends to make threat actors use more sophisticated solutions, thus more costly for them.
     * Human detection: using captcha or advanced biometric solutions (e.g. typing patterns).
     * Non-human patterns: analyze the user flow to detect non-human patterns (e.g. the user accessed the "add to cart" and "complete purchase" functions in less than one second).
     * Consider blocking IP addresses of Tor exit nodes and well-known proxies.
     * Secure and limit access to APIs that are consumed directly by machines (such as developer and B2B APIs). They tend to be an easy target for attackers because they often don't implement all the required protection mechanisms.

7. [**Server Side Request Forgery**](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/) (SSRF) flaws can occur when an API fetches a remote resource without validating a user-supplied URI. This enables an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall or a VPN.
  
    To prevent:
     * Isolate the resource fetching mechanism in your network. These features are usually aimed to retrieve remote resources and not internal ones.
     * Whenever possible, use "allow" lists of:
       * Remote origins users are expected to download resources from
       * URL schemes and ports
       * Accepted media types for a given functionality
     * Disable HTTP redirections.
     * Use a well-tested and -maintained URL parser to avoid issues caused by URL parsing inconsistencies.
     * Validate and sanitize all client-supplied data.
     * Do not send raw responses to clients.
  
8. [**Security Misconfiguration**](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/): APIs and supporting systems typically contain complex configurations intended to make the APIs more customizable. Misconfiguring or not following security best practices may allow different types of attacks.

    To prevent:
    The API life cycle should include:
     * A repeatable hardening process leading to fast and easy deployment of a properly locked-down environment.
     * A task to review and update configurations across the entire API stack. The review should include: orchestration files, API components, and cloud services (e.g. S3 bucket permissions).
     * An automated process to continuously assess the effectiveness of the configuration and settings in all environments.

    Further measures:
     * Ensure that all API communications from the client and any downstream/upstream components are over an encrypted communication channel (TLS), regardless of whether an internal or public-facing API.
     * Be specific about which HTTP verbs each API supports; disable all other HTTP verbs.
     * APIs expecting to be accessed from browser-based clients (e.g., by a web app front-end) should at least:
       * Implement a proper Cross-Origin Resource Sharing (CORS) policy
       * Include applicable security headers
       * Restrict incoming content types/data formats to those that meet the business and functional requirements.
     * Ensure all servers in the HTTP server chain (e.g. load balancers, reverse and forward proxies, and back-end servers) process incoming requests in a uniform manner to avoid desync issues.
     * Define and enforce all API response payload schemas, including error responses, to prevent exception traces and other valuable information from being sent back to attackers.
  
9. [**Improper Inventory Management**](https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/): APIs tend to expose more endpoints than traditional web applications, making it essential to maintain documentation. A proper inventory of hosts and deployed API versions is also important to mitigate issues such as deprecated API versions and exposed debug endpoints.
  
    To prevent:
     * Inventory all API hosts and document important aspects of each one of them, focusing on the API environment (e.g. production, staging, test, development), who should have network access to the host (e.g. public, internal, partners) and API version.
     * Inventory integrated services and document important aspects such as their role in the system, what data is exchanged (data flow), and their sensitivity.
     * Document all aspects of your API such as authentication, errors, redirects, rate limiting, cross-origin resource sharing (CORS) policy, and endpoints, including their parameters, requests, and responses.
     * Generate documentation automatically by adopting open standards. Include the documentation build in your CI/CD pipeline.
     * Make API documentation available only to those authorized to use the API.
     * Use external protection measures such as API security specific solutions for all exposed versions of your APIs, not just for the current production version.
     * Avoid using production data with non-production API deployments. If this is unavoidable, give these endpoints the same security treatment as the production ones.
     * When newer versions of APIs include security improvements, perform a risk analysis to inform the mitigation actions required for the older versions. For example, whether it is possible to backport the improvements without breaking API compatibility or if you need to take the older version out quickly and force all clients to move to the latest version.

10. [**Unsafe Consumption of APIs**](https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/): Data received from third-party APIs tends to be trusted more than user input, and so is usually subject to weaker security standards. In order to compromise APIs, attackers may go after integrated third-party services instead of trying to compromise the target API directly.

    To prevent:
     * When evaluating service providers, assess their API security posture.
     * Ensure all API interactions happen over a secure communication channel (TLS).
     * Always validate and properly sanitize data received from integrated APIs before using it.
     * Maintain an "allow" list of well-known locations integrated APIs may redirect yours to: do not blindly follow redirects.
  
</details>

<details>
  <summary> Best practices </summary>

</details>




















