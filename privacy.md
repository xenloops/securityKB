# Privacy and Data Security

Protecting data is a core concern of information security.  Some information must be handled especially carefully, including:

* **Personally Identifiable Information (PII)** such as government-issued ID number, birth date, etc. (anything that can uniquely identify a person)
* **Protected Health Information (PHI)** like health history, drug test results, physician notes, etc.
* **Intellectual Property (IP)**, including patent filings, project documentation, etc.

Privacy risks may have serious consequences for an organisation, including:
* Perceived and/or actual harm to privacy
* Failure to meet public expectations on the use and protection of personal information
* Costs of redesigning or retro-fitting systems
* Withdrawal of support from key supporting organisations
* Legal action by governmental regulators
* Compensation claims from individuals
* Increased insurance costs

<details>
  <summary> General </summary>
  
* Categorize all data processed, transmitted, or stored properly.
* Protect sensitive data in transit and at rest as appropriate.
* Follow best practices pertaining to infrastructure
* Apply each data category's protection requirements in the architecture, including:
  * Encryption
  * Integrity
  * Confidentiality
  * Secure retention
* Encrypt database connection strings.
* Ensure applications follow best practices for data security, including input sanitization and output encoding.
</details>

<details>
  <summary> Legal issues and regulations </summary>

  Many countries and U.S. states have data privacy laws, with stringent requirements and dire consequences. Among the most famous:
  
  * [General Data Protection Regulation (GDPR)](https://gdpr.eu) governs the personal information belonging to people in the European Union.
  * [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) governs the personal information of California residents.
  
</details>

# Social Media Privacy

Privacy settings on social media sites can be confusing. The following are distilled down to the bare minimum settings to control (IMHO).

<details>
  <summary> LinkedIn </summary>

  To get to the appropriate settings, go to the Me menu > Settings & Privacy.

  ## Account preferences:
  ### Profile Information
  * Personal demographic information -- Check to ensure LI isn't storing your data (unless you trust Microsoft with it)
  ### General preferences
  *  Feed preferences > Show political content -- For sanity's sake, turn off (is this really where you want to see such dreg?)
  ### Syncing options
  * Sync contacts > Remove all -- Unless you trust Microsoft with them
  * Partners & services -- Check that you really trust Microsoft with connecting to other services

  ## Sign in & Security:
  ### Account access
  * Where you're signed in -- It doesn't hurt to check the active sessions list periodically. Make sure all the entries (usually one for each LI tab open) are yours. End any sessions you don't recognize. (I had sessions still open that I last accessed two months ago -- if anyone knows of a course in managing browser tabs, I'd like to hear about it.)
  * Two-step verification -- Turn on and use an authenticator app to make logging in more secure (and admittedly yes, slightly less convenient). Don't bother with SMS as a method, as this is susceptible to SIM swapping attacks.

  ## Visibility: 

  Change settings as desired. Of course, part of the point of LI is that people can find you and learn about your work history. But there are things you might not want to share, for example:
  ### Visibility of your profile & network
  * Who can see your email address (recommend limiting to connections or no one)
  * Who can see members you follow
  * Page owners exporting your data (recommend turning off)
  * Profile discovery and visibility off LinkedIn (recommend turning off)
  
  ### Visibility of your LinkedIn activity
  * Manage active status (recommend setting to No one, unless you're ok with people seeing you're actively on LI)

  ## Data privacy:

  ### How LinkedIn uses your data
  Special thanks to the EU for passing the GDPR!
  * Get a copy of your data -- Not a bad idea to look through periodically.
  * Search history -- Only visible to LI, but if your search results aren't showing you what you want, it might be a good time to clear it here.
  * Demographic info -- This is sensitive info. Why give it to a company if it's not required?
  * Social, economic, and workplace research -- Turn off. You won't benefit from the collection of your data.
  * Data for Generative AI Improvement -- Turn off. You won't benefit from the collection of your data.

  ### Messaging experience
  * Read receipts and typing indicators -- Turn off.

    [Work in progress]

</details>

