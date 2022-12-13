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
    * Protect against logins across multiple accounts from same IP
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
  
  * Never store credentials in the clear.
  * Store salted and hashed version of password.
  * Use a currently approved hash algorithm for passwords (ref. NIST)
  * Use a salt at least 32 bits long, unique to each credential, chosen arbitrarily to prevent salt collisions.
  * If using PBKDF2, use at least 100,000 iterations for the hash.
  * If using bcrypt, use as large a work factor as the server performance allows (at least 13).
  * Perform an additional iteration of salting, using a secret value known only to the verifier component. Store the secret salt separate from the password hashes.
  * Do not store secrets in source code or code repositories.
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
    Authentication: Lookup-Secret Verifiers
  </summary>
  
  * Verifiers are OTPs, and must be discarded after use.
  * Allow lookup secrets to be used only once.
  * Use unpredictable values.
  * Verify that lookup secrets have sufficient randomness (at least 112 bits of entropy) or are salted with a unique and random 32-bit salt and hashed with an approved one-way hash.
</details>

<details>
  <summary>
    Authentication: Out-of-Band Verifiers
  </summary>
  
  These are usually codes sent via another route than the standard authentication method, e.g. temporary code sent to a known email to verify the user that they then enter along with their login.
  
  * Use strong methods like mobile push, secure email, or another secure method for sending authentication codes.
  * Avoid SMS or PSTN; these are insecure and unencrypted.
  * Expire verifiers after a short time.
  * Expire verifiers after one use.
  * Secure the channel between the authenticator and verifier.
  * Ensure the verifier keeps only a hashed version on the authentication code.
  * Generate authentication codes using a secure random number generator, using at least 20 bits of entropy (e.g. a six digit number).
</details>

<details>
  <summary>
    Authentication: One-Time Verifiers
  </summary>

  These are typically codes that appear in a soft or hard token and change every minute. The user must enter the current code during login.
  
  * Change OTPs after a short time; typically one minute.
  * Protect symmetric keys used to verify OTPs, by using a hardware security module or secure operating system-based key storage.
  * Use approved cryptographic algorithms in OTP generation, seeding, and verification.
  * Allow a time-based OTP to be used only once within the validity period.
  * Alert user and log attempts to use a OTP more than once.
  * Enable revocation for physical OTP generators in case of loss. Close sessions for revoked devices immediately.
  * Use biometric authenticators only in conjunction with other factors.
</details>

<details>
  <summary>
    Authentication: Services
  </summary>
  
  * Ensure integration secrets do not rely on static passwords.
  * Do not use the credentials of default accounts.
</details>

<details>
  <summary>
    Authentication: Example security user stories
  </summary>
  
  * As a user, I want the application to have strong password policies in place for my account.
  * As a user, I want to change my password and be forced to enter my old one first.
  * As a user, I want the application to allow passwords longer than 64 characters so I can use phrases.
  * As a user, I want to use multi-factor authentication.
  * As a user, I do not want the application to perform mutli-factor over text messages (SMS).
  * As a user, I want to use my own token generator for multi-factor authentication.
  * As a user, I want the application to store my password hashed and salted to the current security standards and practices.
  * As a user, I want the application to follow password management, resets, storage, and utilization best practices.
</details>
