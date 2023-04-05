# Azure Cloud

Azure.... 

<details>
  <summary> General </summary>
  
* 
</details>

<details>
  <summary> Networking </summary>
  
  In addition to the advice given in the Networking section, the following should be practiced (see [this Microsoft page](https://learn.microsoft.com/en-us/azure/security/fundamentals/network-best-practices#adopt-a-zero-trust-approach) for more information):
  
  * Create network access controls between subnets. By default, there are no network access controls between the subnets that you create on an Azure virtual network. 
  * Use a [network security group (NSG)](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group) to protect against unsolicited traffic into Azure subnets.
  * Avoid small virtual networks and subnets to ensure simplicity and flexibility. Using small subnets adds limited security value, and mapping a network security group to each subnet adds overhead. 
  * Simplify network security group rule management by defining [Application Security Groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups).
  * Employ [Azure AD Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) to implement automated access control decisions based on required conditions.
  * To lock down inbound traffic, enable port access only after workflow approval. See [just-in-time VM access in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/security-center/security-center-just-in-time).
  * By default, a virtual machine on an Azure virtual network can connect to any other VM on the same virtual network, even those on different subnets. Configure the next-hop address to reach specific destinations where needed.
  * Configure [user-defined routes](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#custom-routes) for security appliances on a virtual network.
  * Employ Azure virtual network security appliances found in the Azure Marketplace (search for "security" and "network security").
  * Use Azure native controls such as [Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/overview) and [Azure Web Application Firewall](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview) for a fully stateful firewall as a service, built-in high availability, unrestricted cloud scalability, FQDN filtering, and support for OWASP core rule sets.
  * If using a hybrid approach with cross-premises connections, be sure to use a site-to-site VPN or [Azure ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction).
  * Use load balancing appropriate to the use case to improve a site's availability and performance. Options include [internal](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-portal) and [external](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-portal) load balancers, [Azure Application Gateway](https://learn.microsoft.com/en-us/azure/application-gateway/overview), and [Azure Traffic Manager](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-overview) for geographic load balancing.
  * Disable RDP/SSH access to VMs from the internet to avoid brute-force attacks.
  * Deny access for critical Azure service resources from the internet using [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview). Exposing a virtual network to the internet is no longer necessary to consume Azure PaaS Services.
</details>

<details>
  <summary> Data protection </summary>
  
  In addition to the advice given in the encryption and Data Protection sections, the following should be practiced (see [this Microsoft page](https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices) for more information):
  
  * Use [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) to safeguard cryptographic keys and secrets that cloud applications and services use.
    * Use Azure RBAC predefined roles.
    * Control what users have access to.
    * Store certificates in your key vault.
    * Verify key vault and key vault object recovery from accidental or malicious deletion.
  * Use a [secure privileged access management workstation](https://4sysops.com/archives/understand-the-microsoft-privileged-access-workstation-paw-security-model/) to protect sensitive accounts, tasks, and data.
  * Use Azure Disk Encryption to protect data at rest ([for Linux VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disk-encryption-overview) or [for Windows VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disk-encryption-overview)).
  * Use a VPN or [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction), and interact with Azure Storage through the Azure portal.
  * Deploy [Azure Information Protection](https://learn.microsoft.com/en-us/azure/information-protection/what-is-information-protection) to classify, label, and protect documents and emails. This can be done automatically via rules and conditions, or users can classify manually.
  * 
</details>

<details>
  <summary>  </summary>
  
* 
</details>

<details>
  <summary>  </summary>
  
* 
</details>
