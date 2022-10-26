# Authentication Controls

Authentication establishes or confirms a user or component as authentic and that the claims made are correct, resistant to impersonation, 
altercation, and interception.

<details>
  <summary>
    Authoritative Sources 
  </summary>
  
  * [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
  * [NIST approved hash functions](https://csrc.nist.gov/projects/hash-functions)
  * [NIST Random Number Generation](https://csrc.nist.gov/publications/detail/sp/800-90a/rev-1/final)
</details>

<details>
  <summary>
    Definitions 
  </summary>
  
  * **Memorized secrets** include passwords, PINs, patterns, image selections and passphrases. 
  * **One-time password (OTP)**: a secret used once to login, e.g. a code sent by SMS.
  * **Something you know**: a memorized secret required to authenticate.
  * **Something you have**: something you can hold, e.g. housekey, ATM card, Yubikey.
  * **Something you are**: a biometric unique to a person, e.g. DNA, fingerprint, retina, voice, etc.
  * **Single factor**: Something required for authentication. Usually a passphrase or PIN.
  * **Second factor**: Something additional to a single factor required to authenticate.
  * **Multi-factor authentication (MFA)** Required use of more than one factor to authenticate. Examples include a PIN and key card,
  or passphrase and fingerprint. _Note:_ a password combined with a secret question does _not_ constitute MFA, since both are "things you know."
</details>

<details>
  <summary>
    Authentication: Passwords
  </summary>
  
  * Require user-entered passwords to have the following qualities:
    * Be at least 12 characters, allowing for longer (e.g. up to 64).
    * Allow special characters, e.g.:
      * Spaces (without truncation)
      * The full Unicode set, including e.g. emoji and Kanji
      * Do not limit the number of special characters permitted.
  * Require system-generated initial passwords to have the following qualities:
    * Be securely randomly generated.
    * Be at least 6 characters.
    * Expire after a specified time.
    * Not allowed to become permanent.
  * Allow users to change their password.
    * Force entry of current and new passwords for change.
  * Force user to choose a different password if it is a well-known breached password.
  * Display the user's password strength during creation.
  * Avoid forcing password rotation.
  * Allow pasting of passwords, secure browser storage, and password manager autotype functionality.
  * Mask password entry.
    * Allow user to temporarily unmask their password as entered or display most recently typed character.
</details>

<details>
  <summary>
    Authentication: General
  </summary>
  
  * Give no indication whether a username or password is valid.
  * Use anti-automation controls, e.g.:
    * Block most common breached password guessing
    * Rate limits on attempts
    * Increase delays between allowed attempts
    * Restrict IP address ranges
    * CAPTCHAs
  * Use weak authenticators (e.g. SMS or email) only for secondary authentication or to approve transactions.
  * Send authentication detail changes to user's verified contact method, including:
    * Incorrect login attempt (only first time in a period, to avoid spamming users)
    * Password or other detail changes
    * Address or email/phone changes
    * Logins from new devices and IP addresses
  * Prefer push notifications to email/SMS.
  * Do not send sensitive information in notifications.
  * Use controls against phishing attacks, e.g.:
    * Multi-factor authentication
    * Client-side certificates
  * Use mutually-authenticated encryption between a credential service provider (CSP) and authentication verifier if distinct systems.
  * Protect against replay attacks by enforcing use of OTPs, cryptographic authenticators, or lookup codes.
  * Disable or remove shared or default accounts.
</details>

<details>
  <summary>
    Authentication: Credential Storage
  </summary>
  
  * Store salted and hashed version of password.
  * Use a currently approved hash algorithm for passwords (ref. NIST)
  * Use a salt at least 32 bits long, unique to each credential, chosen arbitrarily to prevent salt collisions.
  * If using PBKDF2, use at least 100,000 iterations for the hash.
  * If using bcrypt, use as large a work factor as the server performance allows (at least 13).
  * Perform an additional iteration of salting, using a secret value known only to the verifier component. Store the secret salt separate from the password hashes.
</details>

<details>
  <summary>
    Authentication: Credential Recovery
  </summary>
  
  * Never send the following to recover a login:
    * An initial or recovery secret in cleartext
    * Secret questions or password hints
    * The current password
  * Use a secure recovery mechanism, e.g. soft token or mobile push.
  * If OTP or MFA factors are lost, require evidence of identity proofing at the same level as during enrollment.
</details>

<details>
  <summary>
    Authentication: Lookup Secret Verifiers
  </summary>
  
  Verifiers are OTPs, and must be discarded after use.
  * Allow lookup secrets to be used only once.
  * Use unpredictable values.
  * Verify that lookup secrets have sufficient randomness (at least 112 bits of entropy) or are salted with a unique and random 32-bit salt and hashed with an approved one-way hash.
</details>

<details>
  <summary>
    Authentication: 
  </summary>
  
  * 
</details>

<details>
  <summary>
    Authentication: 
  </summary>
  
  * 
</details>

<details>
  <summary>
    Authentication: 
  </summary>
  
  * 
</details>

