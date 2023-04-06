# Cloud Best Practices

The cloud represents a significant shift in capability and thinking from on-prem systems and networks. Although this shift brings its own set of challenges, many of the best practices learned from earlier models (e.g. single-user applications, web apps, mobile apps) do still apply, for example secure coding, data encryption, and secure networking. Below are some general best practices; see the pages on specific cloud vendors for specific guidance and components that help (e.g. [Azure](azure.md)).

* **Identity and Access Management (IAM)**: Implement a least-privilege access model, where users are granted the minimum permissions necessary to perform their tasks. Centralize identity management and implement multi-factor authentication (MFA) using an authenticator app to protect against unauthorized access.
* **Network Security**: Isolate enterprise resources from the public internet and implement security groups to control inbound and outbound traffic. Use firewalls to inspect and filter traffic between organization assets and the internet.
* **Data Encryption**: Protect data at rest and in transit using encryption. Encrypt storage accounts and virtual machine disks. Use a key vault to store and manage cryptographic keys and other secrets.
* **Monitoring and Logging**: Use built-in cloud monitoring to track and analyze the environment's health and performance. Configure alerts and notifications to detect and respond to security incidents. Collect, analyze, and archive log data from resources.
* **Disaster Recovery**: Implement a disaster recovery plan to ensure business continuity in case of an outage. Use recovery utilities to replicate and recover critical/essential applications and data in a different location.
* **Compliance and Governance**: Enforce compliance with organizational policies and industry regulations using tools available from the cloud vendor. Assess and monitor the security posture of the environment and implement security recommendations the tool gives.
* **Patch Management**: Keep resources up to date with the latest security patches and updates. Automate patch deployment (when possible) and compliance reporting.

Remember that security is an ongoing process, and includes regular reviews and updates to security measures to stay ahead of potential threats.
