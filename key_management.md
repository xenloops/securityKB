# Key Management / PKI

Implementing cryptographic key management in a secure manner is not the easiest thing. Create a plan for an organization's  overall cryptographic strategy to guide developers working on different applications and ensure that each application's cryptographic capability meets minimum requirements and best practices. Identify the cryptographic and key management requirements for each application and map all components that process or store cryptographic key material. Document and harmonize rules and practices for:

  * Key lifecycle management (generation, distribution, destruction)
  * Key storage
  * Key agreement
  * Key compromise, recovery, and zeroization

<details>
  <summary> Cryptography selection </summary>

Cryptographic and key management algorithms to use within a given application depends on an understanding of the objectives of the application. If the application needs to store data securely, select an algorithm suite that supports data-at-rest encryption. Applications that need to transmit and receive data securely should use an algorithm suite that supports data-in-transit protection.

Developers often begin developing crypto and key management capabilities by examining what is available in a library -- instead, these features must be based on application and security objectives.

An analysis of the actual needs of the application should be conducted to determine the optimal key management approach. Begin by understanding the security objectives of the application, then use these to drive the selection of cryptographic protocols that are best suited to that application. For example, the application may require:

  * Confidentiality of data at rest and confidentiality of data in transit.
  * Authenticity of the end device.
  * Authenticity of data origin.
  * Integrity of data in transit.
  * Keys to create the data encryption keys.

Once the security needs of the application are fully understood, developers can determine what protocols and algorithms are required. Once the protocols and algorithms are understood, the team can begin to define the different types of keys that will support the application's objectives.

There are many key types and certificates to consider, like:

  * Encryption: Symmetric encryption keys, asymmetric encryption keys (public and private).
  * End-device authentication: Pre-shared symmetric keys, trusted certificates, trust anchors.
  * Integrity protection: Message Authentication Codes (MACs).
  * Data origin authentication: Hash MAC (HMAC).
  * Key Encryption Keys.

</details>

<details>
  <summary> Algorithms and Protocols </summary>

There are three basic classes of approved cryptographic algorithms, defined by the number of cryptographic keys that are used in conjunction with the algorithm: 

  * Hash functions (no key)
  * Symmetric-key algorithms (1 key)
  * Asymmetric-key algorithms (2 keys)

## Cryptographic hash functions

Many algorithms and schemes that provide a security service use a hash function as a component of the algorithm. Hash functions can be found in the following authoritative publications:

  * [FIPS 180](https://csrc.nist.gov/publications/detail/fips/180/4/final) Secure Hash Standard (SHS)
  * [FIPS 186](https://csrc.nist.gov/publications/detail/fips/186/5/final) Digital Signature Standard (DSS)
  * [FIPS 198](https://csrc.nist.gov/csrc/media/publications/fips/198/1/final/documents/fips-198-1_final.pdf) Keyed-Hash Message Authentication Code (HMAC)
  * Key-derivation functions/methods:
    * [NIST SP 800-56A](https://csrc.nist.gov/publications/detail/sp/800-56a/rev-3/final) Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography
    * [NIST SP 800-56B](https://csrc.nist.gov/publications/detail/sp/800-56b/rev-2/final) Pair-Wise Key-Establishment Using Integer Factorization Cryptography
    * [NIST SP 800-56C](https://csrc.nist.gov/publications/detail/sp/800-56c/rev-2/final) Key-Derivation Methods in Key-Establishment Schemes
    * [NIST SP 800-108](https://csrc.nist.gov/publications/detail/sp/800-108/rev-1/final) Key Derivation Using Pseudorandom Functions
  * [NIST SP 800-90A](https://csrc.nist.gov/publications/detail/sp/800-90a/rev-1/final) Random Number Generation Using Deterministic Random Bit Generators

Cryptographic hash functions do not require keys. Hash functions generate a relatively small digest (hash value) from an input of arbitrary length in a way that is fundamentally difficult to reverse (i.e., find an input that will produce a specific output). Hash functions are the building blocks for key management, for example:

  * To provide data authentication and integrity services -- the hash function is used with a key to generate a MAC.
  * To compress messages for digital signature generation and verification.
  * To derive keys in key-establishment algorithms.
  * To generate deterministic random numbers.

## Symmetric-key algorithms

Symmetric-key algorithms (also known as secret-key algorithms) transform data in a way that is fundamentally difficult to undo without knowledge of a secret key. The key is called "symmetric" because the same key is used for both encryption and decryption.

Symmetric keys are often known by more than one entity; however, the key must not be disclosed to entities that are not authorized access to the data protected by that algorithm and key. Symmetric key algorithms can be used, for example:

  * To provide data confidentiality.
  * To provide authentication and integrity services in the form of MACs; the same key is used to generate the MAC and to validate it. MACs normally employ either a symmetric key-encryption algorithm or a cryptographic hash function as their cryptographic primitive.
  * As part of the key-establishment process.
  * To generate deterministic random numbers.

## Symmetric-key algorithms

Asymmetric-key algorithms, commonly known as public-key algorithms, use two related keys (i.e., a key pair) to perform their functions: a public key and a private key. The public key may be known by anyone; the private key must be kept secret and under control of the entity that "owns" the key pair. Although the public and private keys of a key pair are related, knowledge of the public key does not reveal the private key. Asymmetric algorithms are used:

  * To compute digital signatures
  * To establish cryptographic keying material
  * To generate random numbers

## Message Authentication Codes (MACs)¶

MACs provide data authentication and integrity. A MAC is a cryptographic checksum on the data that is used in order to provide assurance that the data has not changed and that the MAC was computed by the expected entity.

Although message integrity is often provided using non-cryptographic techniques known as error detection codes, these codes can be altered. The use of an approved cryptographic mechanism, such as a MAC, can alleviate this problem.

In addition, a MAC can provide a recipient with assurance that the originator of the data is a key holder (i.e., an entity authorized to have the key). MACs are often used to authenticate the originator to the recipient when only those two parties share the MAC key.

## Digital Signatures

Digital signatures are used to provide authentication, integrity, and non-repudiation. Digital signatures are used in conjunction with hash functions and are computed on data of any length (up to a limit that is determined by the hash function).

[FIPS 186](https://csrc.nist.gov/publications/detail/fips/186/4/final) specifies algorithms that are approved for the computation of digital signatures.

## Key Encryption Keys

Symmetric key-wrapping keys are used to encrypt other keys using symmetric-key algorithms. Key-wrapping keys are also known as key-encrypting keys.

</details>

<details>
  <summary>  </summary>
  
</details>

<details>
  <summary>  </summary>
  
</details>

<details>
  <summary> Algorithm lifetime </summary>

The NSA released a report, Commercial National Security Algorithm Suite 2.0 which lists the cryptographic algorithms that are expected to be remain strong even with advances in quantum computing.


  
</details>

<details>
  <summary> Sources </summary>

  * [OWASP Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)
  * [NIST SP 800-57 Part 1: Recommendation for Key Management](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)

Reviewed 7 July 2023

</details>

