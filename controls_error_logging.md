# Exception Handling and Logging

<details>
  <summary>
    Exceptions and Logging: General
  </summary>
  
  * Focus on creating high quality logs rather than high volume.
  * Avoid collecting or logging sensitive information unless specifically required.
  * Handle all logged information securely and protect it per its data classification.
  * Store logs with a well-defined lifetime that is as short as possible.
  * Delete expired logs securely.
  * Do not disclose unnecessary information in logs and errors.
  * Ensure logs are clear, easily monitored, and analyzed either locally or sent to a remote monitoring system.
</details>

<details>
  <summary>
    Exceptions and Logging: Content
  </summary>
  
  * Do not log credentials or payment details. 
  * Log any session tokens in an irreversible, hashed form.
  * Do not log any sensitive data as defined under governing laws or relevant policy.
  * Log relevant security events, e.g.:
    * Successful authentication events
    * Failed authentication events
    * Access control failures
    * Deserialization failures
    * Input validation failures
  * Include necessary information in log events that facilitate a detailed investigation of the timeline when an event happens.
</details>

<details>
  <summary>
    Exceptions and Logging: Log Protection
  </summary>
  
  * Protect logs from modification, deletion, and unauthorized access and disclosure.
  * Appropriately encode user-supplied data to prevent log injection.
  * Protect all events from injection when viewed in log viewing software.
  * Synchronize logging systems to keep accurate time. Consider logging in UTC to assist with post-incident forensic analysis.
</details>

<details>
  <summary>
    Exceptions and Logging: Exception handling
  </summary>
  
  * Show generic error messages, potentially with a unique ID which support personnel can use to investigate.
  * Use consistent exception handling across the codebase to account for expected and unexpected error conditions.
  * Define a "last resort" error handler is defined which will catch all unhandled exceptions.
</details>
