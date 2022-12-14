# Data Protection

<details>
  <summary> Definitions </summary>
  
  Cyber security is mainly concerned with the following essential ingredients:
  
* **Confidentiality**: Protect data from unauthorized observation or disclosure, both in transit and when stored.
* **Integrity**: Protect data from being created, altered or deleted by unauthorized attackers.
* **Availability**: Ensure data is available to authorized users per requirements.
</details>

<details>
  <summary> General </summary>
  
* Prevent sensitive data from being cached in server components such as load balancers and application caches.
* Protect all cached or temporary copies of sensitive data stored on the server from unauthorized access.
* Overwrite cached sensitive data after its authorized use.
* Minimize the number of parameters in a request, such as hidden fields, Ajax variables, cookies, and header values.
* Detect and alert on abnormal numbers of requests by IP, user, total per hour or day, or other appropriate criteria.
* Perform regular backups of important data and test restoration.
* Store backups securely.
</details>

<details>
  <summary> Client-Side </summary>
  
* Set sufficient anti-caching headers so that sensitive data is not cached in browsers.
* Do not cache sensitive data in client-side storage.
* Clear authenticated data from client-side storage after the client or session is terminated.
</details>

<details>
  <summary> Sensitive and Private Data </summary>
  
* Use the HTTP message body or headers to send sensitive data to the server.
* Ensure query string parameters from any HTTP verb do not contain sensitive data.
* Allow users to remove or export their data on demand.
* Provide users with clear language regarding collection and use of supplied personal information and provide opt-in consent for the use of that data before it is used.
* Identify all sensitive data created and processed by the application, and have a policy in place on how to deal with sensitive data.
* Audit accesses to sensitive data collected under relevant data protection directives or where logging of access is required.
* Overwrite sensitive information in memory as soon as it is no longer required using zeroes or random data.
* Encrypt sensitive or private information that requires it.
* Overwrite old or out-of-date data according to data retention requirements.
</details>

<details>
  <summary> Example security user stories </summary>
  
* As a user, I want the application to protect my sensitive data from being cached or temporary copies kept that may lead to exposure.
* As a user, I want the application to make regular backups of my sensitive data for which recovery is tested regularly.
* As a user, I want the application to ensure sensitive data is transmitted securely.
</details>
