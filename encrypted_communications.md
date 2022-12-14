# Encrypted Communications

<details>
  <summary> General </summary>
  
* Always use strong encryption, regardless of the sensitivity of the data being transmitted.
* Enable and order allowed algorithms and ciphers, prioritizing for strength.
* Disable deprecated or known insecure algorithms, ciphers, and configurations.
* Use the most recent versions of TLS review tools like SSLyze or TLS scanners periodically to sort the allowed algorithms and ciphers.
* Secure communications between all hosts in a system, including: 
  * Monitoring systems
  * Management tools
  * Remote access systems
  * Middleware
  * Databases
  * Directories
  * External systems
</details>

<details>
  <summary> Communication Security </summary>
  
* Use TLS for all client connectivity.
* Do not permit clients to fall back to insecure protocols.
</details>

<details>
  <summary> Server Communications Security </summary>
  
* Use trusted TLS certificates for connections to and from the server. 
* Where internally generated or self-signed certificates are used, configure the server to only trust specific internal CAs 
and specific self-signed certificates. 
* Reject all unexpected certificates.
* Use encrypted communications for all connections including for management ports, monitoring, authentication, API, 
web service calls, database, cloud, serverless, mainframe, external, and partner connections.
* Authenticate all encrypted connections with external systems that involve sensitive information or functionality.
* Enable proper certification revocation, such as with Online Certificate Status Protocol (OCSP) Stapling.
* Log backend TLS connection failures.
</details>

<details>
  <summary> Example security user stories </summary>
  
* As a user, I want the application to use TLS 1.2 or later for all client communications and does not fall back to an unencrypted 
or insecure, lower state.
* As a user, I want the application to encrypt all communication channels for inbound and outbound connections.
* As a user, I want the application to authenticate all external communication connections where my sensitive data is transmitted.
</details>
