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

1. **Broken Object Level Authorization** (BOLA): APIs tend to expose endpoints that handle object identifiers, creating a wide attack surface of Object Level Access Control issues. Consider using object level authorization checks in every function that accesses a data source using an ID from the user.
2. **Broken Authentication**: Authentication mechanisms are often implemented incorrectly, allowing attackers to compromise authentication tokens or to exploit implementation flaws to assume another user's identity. Compromising authentication integrity  compromises API security overall.
3. **Broken Object Property Level Authorization**: The lack of or improper authorization validation at the object property level leads to information exposure or manipulation by unauthorized parties. This is the root cause of other API risks, such as Excessive Data Exposure and Mass Assignment.
4. **Unrestricted Resource Consumption**: Satisfying API requests requires resources such as network bandwidth, CPU, memory, and storage. Other resources such as emails/SMS/phone calls or biometrics validation are made available by service providers via API integrations, and paid for per request. Successful attacks can lead to a denial of service and increased operational costs.
5. **Broken Function Level Authorization**: Complex access control policies with different hierarchies, groups, and roles, and an unclear separation between administrative and regular functions, tend to lead to authorization flaws. By exploiting these issues, attackers can gain access to other users’ resources and/or administrative functions.
6. **Unrestricted Access to Sensitive Business Flows**: APIs vulnerable to this risk expose a business flow -- such as making a transaction or posting a comment -- without compensating for how the functionality could harm the business if used excessively in an automated manner. This doesn't necessarily come from implementation bugs.
7. **Server Side Request Forgery** (SSRF) flaws can occur when an API fetches a remote resource without validating a user-supplied URI. This enables an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall or a VPN.
8. **Security Misconfiguration**: APIs and supporting systems typically contain complex configurations intended to make the APIs more customizable. Misconfiguring or not following security best practices may allow different types of attacks.
9. **Improper Inventory Management**: APIs tend to expose more endpoints than traditional web applications, making it essential to maintain documentation. A proper inventory of hosts and deployed API versions is also important to mitigate issues such as deprecated API versions and exposed debug endpoints.
10. **Unsafe Consumption of APIs**: Data received from third-party APIs tends to be trusted more than user input, and so is usually subject to weaker security standards. In order to compromise APIs, attackers may go after integrated third-party services instead of trying to compromise the target API directly.

</details>






















