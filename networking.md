# Networking

Networking controls protect the overall technnical infrastructure from many kinds of intrusions. 

<details>
  <summary> General </summary>
  
* Centralize management and governance of core network functions (e.g. virtual network/subnet provisioning and IP addressing).
* 
</details>

<details>
  <summary> Network segmentation </summary>
  
  Segmenting the network segregates logical business units and helps limit the damage from successful attacks.
  
  * Segment larger address spaces into subnets using CIDR-based principles.
  * Don't assign Allow rules with broad IP address ranges (for example, allow 0.0.0.0 through 255.255.255.255).
  * Adopt Zero Trust approaches that validate trust at the time of access; don't rely on perimeter controls. Employees can access their organization's resources from anywhere on various devices and apps.
  * 
</details>

<details>
  <summary> Network Security Appliances </summary>
  
  Network security groups and user-defined routing can provide a certain measure of network security at the network and transport layers of the OSI model. In some situations, other security controls need to be implemented at high levels of the stack, including:

  * Firewalling
  * Intrusion detection/intrusion prevention
  * Vulnerability management
  * Application control
  * Network-based anomaly detection
  * Web filtering
  * Antivirus
  * Botnet protection

</details>

<details>
  <summary> Perimeter Network (DMZ) </summary>
  
  A DMZ is a physical or logical network segment that provides an extra layer of security between assets and the internet. Consider using a DMZ for all high-security deployments to enhance the level of network security and access control. Specialized network access control devices on the edge of a perimeter network allow only desired traffic into the network. The network security devices sit between the internet and internal network and have an interface on both networks. The perimeter network is where many controls are used, including:
  
  * Distributed denial of service (DDoS) protection
  * Intrusion detection/intrusion prevention systems (IDS/IPS)
  * Firewall rules and policies
  * Web filtering
  * Network antimalware 
  
  
* Deploy perimeter networks for security zones. 
</details>

<details>
  <summary>  </summary>
  
* 
</details>
