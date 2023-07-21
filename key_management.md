# Key Management / PKI

Implementing cryptographic key management in a secure manner is not the easiest thing. Create a plan for an organization's  overall cryptographic strategy to guide developers working on different applications and ensure that each application's cryptographic capability meets minimum requirements and best practices. Identify the cryptographic and key management requirements for each application and map all components that process or store cryptographic key material. Document and harmonize rules and practices for:

  * Key lifecycle management (generation, distribution, destruction)
  * Key storage
  * Key agreement
  * Key compromise, recovery, and zeroization


<details>
  <summary> Key Management Lifecycle Best Practices </summary>

References in this section:
   * [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final)
   * [NIST SP 800-133](https://csrc.nist.gov/pubs/sp/800/133/r2/final)
   * 

### Key generation

   * Cryptographic keys must be generated within a cryptographic module with at least FIPS 140-2 compliance. The module in which a key is generated is the key-generating module.
   * Any random value required by the key-generating module must be generated within that module; that is, a random value generator must be implemented within a cryptographic module with at least a FIPS 140-2 compliance generating the key.
   * Prefer hardware cryptographic modules over software cryptographic modules.

### Key distribution

Transport generated keys using secure channels and used by their associated cryptographic algorithm within at least a FIPS 140-2 compliant cryptographic module. For additional detail for the recommendations in this section refer to NIST SP 800-133.

### Key storage

  * Understand where cryptographic keys are stored within the application and in any memory devices.
  * Keys must be protected on both volatile and persistent memory, ideally processed within secure cryptographic modules.
  * Never store keys in plaintext format.
  * Store keys in a cryptographic vault, such as a hardware security module (HSM) or isolated cryptographic service.
  * If storing keys in offline devices/databases, encrypt the keys using Key Encryption Keys (KEKs) prior to the export of the key material. KEK length (and algorithm) should be equivalent to or greater in strength than the keys being protected.
  * Ensure that keys have integrity protections applied while in storage (consider dual purpose algorithms that support encryption and a Message Authentication Code MAC).
  * Ensure that standard application level code never reads or uses cryptographic keys directly; instead use key management libraries.
  * Perform all work in the vault such as key access, encryption, decryption, signing, etc.

### Escrow and Backup

   * Data encrypted with lost cryptographic keys will never be recovered. Therefore, it is essential that the application incorporate a secure key backup capability, especially those that support encryption for long-term data stores.
   * When backing up keys, ensure that the database that is used to store the keys is encrypted using at least a FIPS 140-2 validated module. It is sometimes useful to escrow key material for use in investigations and for re-provisioning of key material to users in the event that the key is lost or corrupted.
   * Never escrow keys used for performing digital signatures, but consider the need to escrow keys that support encryption. Oftentimes, escrow can be performed by the Certificate Authority (CA) or key management system that provisions certificates and keys, however in some instances separate APIs must be implemented to allow the system to perform escrow for the application.

### Accountability and Audit

Accountability involves the identification of those that have access to, or control of, cryptographic keys throughout their lifecycles. Accountability can be an effective tool to help prevent key compromises and to reduce the impact of compromises once they are detected.

   * Although it is preferred that no humans are able to view keys, as a minimum, the key management system should account for all individuals who are able to view cryptographic keys.
   * Account for all individuals authorized to access or control any cryptographic keys, whether in plaintext or encrypted form.

Accountability provides significant advantages by:

   * Aiding in the determination of when the compromise could have occurred and what individuals could have been involved.
   * Protecting against compromise, because individuals with access to the key know that their access to the key is known.
   * Recovering from a detected key compromise to know where the key was used and what data or other keys were protected by the compromised key.

Certain principles have been found to be useful in enforcing the accountability of cryptographic keys. These principles might not apply to all systems or all types of keys. Some of the principles that apply to long-term keys controlled by humans include:

   * Uniquely identifying keys.
   * Identifying the key user.
   * Identifying the dates and times of key use, along with the data that is protected.
   * Identifying other keys that are protected by a symmetric or private key.

Two types of audit should be performed on key management systems:

   * The security plan and the procedures that are developed to support the plan should be periodically audited to ensure that they continue to support the Key Management Policy.
   * The protective mechanisms employed should be periodically reassessed with respect to the level of security that they provide and are expected to provide in the future, and that the mechanisms correctly and effectively support the appropriate policies.

Consider new technology developments and attacks. Frequently review the actions of the humans that use, operate, and maintain the system to verify that they continue to follow established security procedures.

Strong cryptographic systems can be compromised by lax and inappropriate human actions. Review highly unusual events as possible indicators of attempted attacks on the system.

### Key Compromise and Recovery

Key compromise has the following implications:

   * The unauthorized disclosure of a key used to provide confidentiality means that all information encrypted by that key will be exposed to unauthorized entities.
   * The disclosure of a Certificate Authorities's private signature key means that an adversary can create fraudulent certificates and Certificate Revocation Lists (CRLs).
   * The compromise of key integrity means that the key is incorrect -- either that the key has been modified (either deliberately or accidentally) or that another key has been substituted. The substitution or modification of a key used to provide integrity calls into question the integrity of all information protected by the key. This information could have been provided by, or changed by, an unauthorized entity that knows the key. The substitution of a public or secret key that will be used (at a later time) to encrypt data could allow an unauthorized entity (who knows the decryption key) to decrypt data that was encrypted using the encryption key.
   * A compromise of a key's usage or application association means that the key could be used for the wrong purpose (e.g., for key establishment instead of digital signatures) or for the wrong application, and could result in the compromise of information protected by the key.
   * A compromise of a key's association with the owner or other entity means that the identity of the other entity cannot be assured (i.e., one does not know who the other entity really is) or that information cannot be processed correctly (e.g., decrypted with the correct key).
   * A compromise of a key's association with other information means that there is no association at all, or the association is with the wrong "information". This could cause the cryptographic services to fail, information to be lost, or the security of the information to be compromised.

The following procedures are usually involved:

   * Limit the time a symmetric or private key is in plaintext form.
   * Prevent humans from viewing plaintext symmetric and private keys.
   * Restrict plaintext symmetric and private keys to physically protected containers. This includes key generators, key-transport devices, key loaders, cryptographic modules, and key-storage devices.
   * Use integrity checks to ensure that the integrity of a key or its association with other data has not been compromised. For example, wrap keys (i.e., encrypt them) in such a manner that unauthorized modifications to the wrapping or to the associations will be detected.
   * Employ key confirmation (see NIST SP 800-57 Part 1 Section 4.2.5.5) to help ensure that the proper key was, in fact, established.
   * Establish an accountability system that keeps track of each access to symmetric and private keys in plaintext form.
   * Provide a cryptographic integrity check on the key (e.g., using a MAC or a digital signature).
   * Use trusted timestamps for signed data. Destroy keys as soon as they are no longer needed.
   * Create a compromise-recovery plan, especially in the case of a CA compromise.

#### Compromise-recovery plan

A compromise-recovery plan is essential for restoring cryptographic security services in the event of a key compromise. A Document the compromise-recovery plan and make it easily accessible. The compromise-recovery plan should contain:

   * The identification and contact info of the personnel to notify.
   * The identification and contact info of the personnel to perform the recovery actions.
   * The re-key method.
   * An inventory of all cryptographic keys and their use (e.g., the location of all certificates in a system).
   * The education of all appropriate personnel on the recovery procedures.
   * An identification and contact info of all personnel needed to support the recovery procedures.
   * Policies that key-revocation checking be enforced (to minimize the effect of a compromise).
   * The monitoring of the re-keying operations (to ensure that all required operations are performed for all affected keys).
   * Any other recovery procedures, which may include:
       * Physical inspection of the equipment.
       * Identification of all information that may be compromised as a result of the incident.
       * Identification of all signatures that may be invalid, due to the compromise of a signing key.
       * Distribution of new keying material, if required.

</details>


### Trust Stores

Design controls to secure the trust store against injection of third-party root certificates. The access controls are managed and enforced on an entity and application basis.
    Implement integrity controls on objects stored in the trust store.
    Do not allow for export of keys held within the trust store without authentication and authorization.
    Setup strict policies and procedures for exporting key material from applications to network applications and other components.
    Implement a secure process for updating the trust store.

### Cryptographic Key Management Libraries

Use only reputable crypto libraries that are well maintained and updated, as well as tested and validated by third-party organizations (e.g., NIST/FIPS). These include:

   * 



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

A summary of the uses of the following algorithms:

| Service     | Hash function | Symmetric | Asymmetric | MAC | Digital Signature |
|--|:--:|:--:|:--:|:--:|:--:|
| Data authentication                    | X |   |   | X | X |
| Data confidentiality                   |   | X |   |   |   |
| Integrity                              | X |   |   | X | X |
| Digital signatures                     | X |   | X |   |   |
| Key generation                         | X |   | X |   |   |
| Key exchange                           |   | X |   |   |   |
| Non-repudiation                        |   |   | X |   | X |
| Deterministic random number generation | X | X |   |   |   |
| Pseudo-random number generation        |   |   | X |   |   |

### Cryptographic hash functions

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

### Symmetric-key algorithms

Symmetric-key algorithms (also known as secret-key algorithms) transform data in a way that is fundamentally difficult to undo without knowledge of a secret key. The key is called "symmetric" because the same key is used for both encryption and decryption.

Symmetric keys are often known by more than one entity; however, the key must not be disclosed to entities that are not authorized access to the data protected by that algorithm and key. Symmetric key algorithms can be used, for example:

  * To provide data confidentiality.
  * To provide authentication and integrity services in the form of MACs; the same key is used to generate the MAC and to validate it. MACs normally employ either a symmetric key-encryption algorithm or a cryptographic hash function as their cryptographic primitive.
  * As part of the key-establishment process.
  * To generate deterministic random numbers.

### Asymmetric-key algorithms

Asymmetric-key algorithms, commonly known as public-key algorithms, use two related keys (i.e., a key pair) to perform their functions: a public key and a private key. The public key may be known by anyone; the private key must be kept secret and under control of the entity that "owns" the key pair. Although the public and private keys of a key pair are related, knowledge of the public key does not reveal the private key. Asymmetric algorithms are used:

  * To compute digital signatures
  * To establish cryptographic keying material
  * To prove non-repudiation
  * To generate random numbers

### Message Authentication Codes (MACs)¶

MACs provide data authentication and integrity. A MAC is a cryptographic checksum on the data that is used in order to provide assurance that the data has not changed and that the MAC was computed by the expected entity.

Although message integrity is often provided using non-cryptographic techniques known as error detection codes, these codes can be altered. Using an approved cryptographic mechanism, such as a MAC with is more complex, alleviates this problem.

A MAC can also provide the recipient with assurance that the originator of the data is a key holder (i.e., an entity authorized to have the key). MACs are often used to authenticate the originator to the recipient when only those two parties share the MAC key.

### Digital Signatures

Digital signatures are used to provide authentication, integrity, and non-repudiation. Digital signatures are used in conjunction with hash functions and are computed on data of any length (up to a limit that is determined by the hash function).

[FIPS 186](https://csrc.nist.gov/publications/detail/fips/186/4/final) specifies algorithms that are approved for the computation of digital signatures.

### Key Encryption Keys

Symmetric key-wrapping keys are used to encrypt other keys using symmetric-key algorithms. Key-wrapping keys are also known as key-encrypting keys.

</details>


<details>
  <summary> Key Strength </summary>

[NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final) Key Management makes recommendations on key strength for specific algorithm implementations. Also, consider these best practices:

  * Establish what the application's minimum computational resistance to attack should be. Take into consideration the sophistication of likely adversaries and for how long data must be protected where stored and if exposed. Identifying the computational resistance to attack will inform engineers of the minimum length of the cryptographic key required to protect data over the life of that data. Consult [NIST SP 800-131a](https://csrc.nist.gov/publications/detail/sp/800-131a/rev-2/final) for additional guidance on determining the appropriate key lengths for the algorithm of choice.
   * When encrypting keys for storage or distribution, always encrypt the key with another key of equal or greater cryptographic strength.
   * When moving to elliptic curve-based algorithms, choose a key length that meets or exceeds the comparative strength of other algorithms in use within the system. Refer to  Table 2 in [NIST SP 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final).
   * Formulate a strategy for the overall organization's cryptographic strategy to guide developers working on different applications and ensure that each application's cryptographic capability meets minimum requirements and best practices.

</details>

<details>
  <summary> Key Use </summary>

According to NIST, in general, a key should be used for only one purpose (e.g., encryption, authentication, key wrapping, random number generation, or digital signatures). The reasons for this:

  * The use of the same key for two different cryptographic processes may weaken the security provided by one or both of the processes.
  * Limiting the use of a key limits the damage that could be done if the key is compromised.
  * Some uses of keys interfere with each other. For example, the length of time the key is required for each use and purpose. Retention requirements of the data may differ for different data types.

</details>


<details>
  <summary> Miscellany </summary>

### Memory Management Considerations

Keys stored in memory for a long time can become "burned in". This can be mitigated by splitting the key into components that are frequently updated. NIST SP 800.57).

Loss or corruption of the memory media on which keys and/or certificates are stored, and recovery planning, according to NIST SP 800.57.

Plan for the recovery from possible corruption of the memory media necessary for key or certificate generation, registration, and/or distribution systems, subsystems, or components as recommended in NIST SP 800.57.

### Algorithm lifetime

The NSA released a report, Commercial National Security Algorithm Suite 2.0 which lists the cryptographic algorithms that are expected to be remain strong even with advances in quantum computing.

### Perfect Forward Secrecy

Ephemeral keys can provide perfect forward secrecy protection, which means a compromise of the server's long term signing key does not compromise the confidentiality of past sessions. Refer to the [OWASP TLS cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html).

### Cryptographic Module Topics

According to NIST SP800-133, cryptographic modules are the set of hardware, software, and/or firmware that implements security functions (including cryptographic algorithms and key generation) and is contained within a cryptographic module boundary to provide protection of the keys.
  
</details>

<details>
  <summary> Sources </summary>

  * [OWASP Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)
  * [NIST SP 800-57 Part 1: Recommendation for Key Management](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)

Reviewed 7 July 2023

</details>

## Public Key Infrastructure best practices

Public Key Infrastructure (PKI) is a framework of policies, procedures, hardware, software, and standards used to manage digital certificates and encryption keys. Following these best practices is essential for ensuring the security and effectiveness of PKI implementations:

    Use Strong Cryptography: Choose strong cryptographic algorithms, key lengths, and encryption methods. Keep up to date with the latest security standards and avoid using deprecated or weak algorithms.

    Secure Key Management: Properly manage private keys to prevent unauthorized access. Use Hardware Security Modules (HSMs) or other secure key storage methods to protect private keys from theft or tampering.

    Certificate Lifecycle Management: Implement a well-defined certificate lifecycle management process, including issuance, renewal, and revocation. Regularly audit certificates and remove expired or unused certificates.

    Authentication and Authorization: Utilize certificates for strong authentication and authorization purposes. Ensure that only authorized individuals have access to private keys and sensitive operations.

    Certificate Revocation: Maintain an updated Certificate Revocation List (CRL) or use Online Certificate Status Protocol (OCSP) for real-time certificate validation. Promptly revoke compromised or compromised private keys.

    Secure Communication: Use secure communication channels when transmitting certificate requests, revocation information, and other sensitive data. Implement encryption and secure protocols such as HTTPS and TLS.

    Separation of Duties: Distribute PKI administrative tasks among different individuals or roles to prevent unauthorized control over the entire infrastructure.

    Backup and Recovery: Regularly back up the PKI components, including keys, certificates, and configuration data. Ensure that there is a reliable recovery plan in place in case of system failure or data loss.

    Secure Hardware and Software: Keep the PKI infrastructure's hardware and software up to date with the latest security patches and firmware updates to prevent vulnerabilities.

    Monitoring and Logging: Implement comprehensive monitoring and logging for all PKI-related activities and events. This helps detect suspicious behavior and facilitates auditing and incident response.

    Physical Security: Ensure that physical access to PKI components, especially HSMs and root CA servers, is restricted and protected against unauthorized access.

    Root CA Protection: Protect the root CA with extreme care, as it forms the foundation of the entire PKI. Store the root CA offline or in a highly secure environment.

    Regular Audits and Reviews: Conduct regular security audits and reviews of the PKI infrastructure to identify potential weaknesses or vulnerabilities.

    Compliance with Standards: Ensure that your PKI complies with relevant industry standards and regulations (e.g., X.509, RFC 5280, etc.).

    Education and Training: Train employees and administrators on PKI best practices, security protocols, and the importance of protecting private keys.

By adhering to these best practices, organizations can establish a robust and secure PKI infrastructure that enables secure digital communication, authentication, and data protection.


