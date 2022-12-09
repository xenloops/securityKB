# API and Web Services

<details>
  <summary>
    API and Web Services: General
  </summary>
  
  * Ensure that adequate authentication, session management, and authorization of all web services are in place.
  * Validate all parameters that transit from a lower to higher trust level.
  * Design in effective security controls for all API types, including cloud and serverless APIs.
</details>

<details>
  <summary>
    API and Web Services: Generic Web Service Security
  </summary>
  
  * Use the same encodings and parsers across all application components to avoid parsing attacks that exploit different parsing behavior.
  * Limit access to administration and management functions to authorized administrators.
  * Verify API URLs do not expose sensitive information, such as the API key, session tokens etc.
  * Make authorization decisions at the URI (enforced at the controller or router) and at the resource level (enforced by model-based permissions).
  * Reject requests containing unexpected or missing content types with appropriate headers (HTTP response 406 Unacceptable or 415 Unsupported Media Type).
</details>

<details>
  <summary>
    API and Web Services: RESTful Web Services
  </summary>
  
  * Disable RESTful HTTP methods that are not valid for the user or action (e.g. DELETE or PUT on protected resources).
  * Validate JSON schema before accepting.
  * Protect RESTful web services that utilize cookies from Cross-Site Request Forgery via the use of at least one of the following: 
    * Triple or double submit cookie pattern
    * CSRF nonces
    * ORIGIN request header checks
  * Use anti-automation controls for REST services to protect against excessive calls, especially if the API is unauthenticated.
  * Confirm the incoming Content-Type is the expected one, such as application/xml or application/JSON.
  * Verify that the message headers and payload are trustworthy and not modified in transit. 
  * Require strong encryption for transport as it provides both confidentiality and integrity protection. 
  * Use per-message digital signatures to provide additional assurance for high-security applications (but also have additional complexity).
</details>

<details>
  <summary>
    API and Web Services: SOAP Web Service
  </summary>
  
  * Validate XSD schema to ensure a properly formed XML document, followed by validation of each input field before any processing of the data.
  * Sign message payloads using WS-Security to ensure reliable transport between client and service.
</details>

<details>
  <summary>
    API and Web Services: GraphQL and other Web Service Data Layer
  </summary>
  
  * Use query whitelisting or depth limiting and amount limiting to prevent GraphQL or data layer expression denial of service (DoS)
  * Use query cost analysis for advanced scenarios.
  * Use GraphQL or other data layer authorization logic at the business logic layer instead of the GraphQL layer.
</details>

<details>
  <summary>
    API and Web Services: Example security user stories
  </summary>
  
  * As a user, I want the application to have adequate authentication, session management, and authorization on all web services that have access to my data.
</details>
