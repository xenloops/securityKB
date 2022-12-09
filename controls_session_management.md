# Session Management

<details>
  <summary>
    Session Management: General
  </summary>
  
  * Ensure sessions are unique to each individual and cannot be guessed or shared.
  * Invalidate sessions when no longer required and time out during a period of inactivity.
  * Never reveal session tokens in the application (e.g. in URL parameters or error messages).
  * Ensure a valid session or require re-authentication for sensitive actions.
</details>

<details>
  <summary>
    Session Management: Session Binding
  </summary>
  
  * Generate a new session token upon user authentication.
  * Create session tokens using at least 64 bits of entropy.
  * Store session tokens only in the browser using secure cookies.
  * Generate session tokens using approved cryptographic algortihms.
</details>

<details>
  <summary>
    Session Management: Session Logout and Timeout
  </summary>
  
  * Invalidate the session token upon logout and expiration, such that the back button or a downstream relying party cannot resume an authenticated session
  * If allowing users to remain logged in, re-authenticate periodically both when actively used or after an idle period.
  * Terminate a user's active sessions after a successful password change across the application, federated login, and any relying parties.
  * Allow users to view and log out of any or all currently active sessions and devices.
</details>

<details>
  <summary>
    Session Management: Tokens
  </summary>
  
  * Do not accept OAuth and refresh tokens as presense of the subscriber.
  * Allow users to terminate trust relationships with linked applications.
  * Use session tokens rather than static API secrets and keys.
  * Protect stateless session tokens with the following controls:
    * Digital signatures
    * Encryption
</details>

<details>
  <summary>
    Session Management: Cookies
  </summary>
  
  * On cookie-based session tokens:
    * Set the "Secure" attribute
    * Set the "HttpOnly" attribute
    * Use the "SameSite" attribute
    * Use the "__Host-" prefix
    * Set the path attribute to the most restrictive path possible
</details>

<details>
  <summary>
    Session Management: Re-Authentication from a Federation or Assertion
  </summary>
  
  * Relying parties (RP) must specify the maximum authentication time
  * Credential Service Providers (CSP) must re-auth a user if the session times out.
  * CSPs must inform RPs of the last authentication event.
</details>

<details>
  <summary>
    Session Management: Example security user stories
  </summary>
  
  * As a user, I want the application to use session state to ensure my use is unique and protected.
  * As a user, I want the application to follow security best practices for session use, generation, management, and destruction.
  * As a user, I want the session to timeout after a period of inactivity.
  * As a user, I want cookie-based sessions to have all the appropriate security settings set.
  * As a user, I want token-based sessions to use digital signatures, encryption, and other measures to ensure my session cannot be tampered with.
</details>
