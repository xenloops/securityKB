# Cryptographic Storage

## Definitions
* Pseudo-Random Number Generator (PRNG) - an algorithm that generates apparently random numbers that might be predictable.
* Cryptographically-Secure Pseudo-Random Number Generator (CSPRNG) - an algorithm that generates random numbers that may be used in cryptographic processes.

<details>
  <summary>
    Cryptographic Storage: General
  </summary>
  
* Ensure all cryptographic modules fail securely and to handle errors properly.
* Use a suitable random number generator.
* Securely manage key access.
</details>

<details>
  <summary>
    Cryptographic Storage: Data Classification
  </summary>
  
* Create a privacy impact assessment for every application to classify the data protection needs of any stored data correctly.
* Store the following data encrypted while at rest:
  * Private data  (e.g. personally identifiable information (PII), sensitive personal information, data subject to the GDPR).
  * Protected Health Information (PHI) (e.g. medical records, medical device details, de-anonymized research records).
* Financial data (e.g. financial accounts, defaults or credit history, tax records, pay history, beneficiaries, de-anonymized market or research records).
</details>

<details>
  <summary>
    Cryptographic Storage: Algorithms
  </summary>
  
* **Never** use custom written cryptographic algorithms.
* Ensure that cryptographic modules fail securely and errors are handled in a way that does not enable Padding Oracle attacks.
* Use well vetted, industry proven, government-approved cryptographic algorithms, modes, and libraries.
* Configure encryption initialization vector, cipher configuration, and block modes securely using the latest guidance.
* Create applications such that random number, encryption or hashing algorithms, key lengths, rounds, ciphers, or modes 
can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic best-practice changes.
* Avoid known insecure block modes (e.g. ECB), padding modes (e.g. PKCS#1 v1.5), ciphers with small block sizes (e.g. Triple-DES, Blowfish), 
and weak hashing algorithms (e.g. MD5, SHA1). If required for backward compatibility, upgrade the obsolete system or use approved workarounds.
* Use nonces, initialization vectors, and other single-use numbers only once with a given encryption key.
* Generate nonces using a method appropriate for the algorithm used.
* Verify encrypted data via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered.
* Ensure that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns 
to avoid leaking information.
</details>

<details>
  <summary>
    Cryptographic Storage: Randomization
  </summary>
  
* Generate random values using the cryptographic module's approved cryptographically secure random number generator when these random values are intended to be not guessable.
* Generate random GUIDs using the GUID v4 algorithm and a CSPRNG.
* Generate random values with proper entropy even when the application is under heavy load.
</details>

<details>
  <summary>
    Cryptographic Storage: Secret Management
  </summary>
  
* Use a secrets management solution such as a key vault to securely create, store, control access, to and destroy secrets.
* Never expose key material to the application; instead use an isolated security module like a vault for cryptographic operations.
</details>

<details>
  <summary>
    Cryptographic Storage: Example security user stories
  </summary>
  
* As a user, I want my sensitive and regulated data to be encrypted while at rest.
* As a user, I want the application to use only proven or government approved cryptographic algorithms.
* As a user, I want the application to store encryption keys securely with access tightly controlled.
</details>
