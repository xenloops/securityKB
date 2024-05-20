# Cookies

## Session Management

Cookies are frequently used for session management, owing to their ability to limit effective token duration and impose usage constraints. If an attaker is able to extract the data within the session cookie and put it to use while the original session is still open, they will be able to hijack the user's session. 

Many protections exist to prevent this type of attack. 

### Minimal essential protections

* **Use a strong, standard encryption algorithm.** Transmit session data only over encrypted channels (see below). This should go without saying, but as we're still in the infancy of protecting sensitive data, it must be explicitly stated. There is no excuse for transmitting anything related to authentication or session in the clear, and any organizations failing this practice deserve to be put out of business. The encryption must be a current industry standard, not e.g. SSL 3.0 or Ivan's Good Enough Crypto.
* **Use unguessable IDs.** Any value employed as a session token, user ID, or any kind of value used as part of a session identifier must:
  * Use crypographically strong randomization (e.g. ```java.security.SecureRandom``` rather than ```java.util.Random```).
  * Use long enough values to ensure uniqueness, like [UUIDs/GUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier). Anything less than this, and you might as well be partying like it's 1999 -- and prepare to have your servers boarded.
  * Refrain from simply incrementing the value from the previously used one. If User A (an attacker) can see that they were issued SessionID #4506, they're likely to try changing their cookie to SessionID 4507, 4508, 4509, etc. until they can access another user's active session. Don't be an idiot; randomize IDs (see above).
* **Validate on the server.** Validate the integrity and authenticity of tokens on the server side; don't rely on client-side validation, which may be under an attacker's control.
* **Do not store sensitive data in the cookie.** Use session tokens or JSON Web Tokens in the cookie instead of data like user IDs.
* **Invalidate unused sessions.** Once an authenticated user clicks the Logout button (the site does have one, doesn't it?), the session is no longer valid.
* **Timeout stale sessions.** If an authenticated user hasn't done anything for a specified duration, assume they've moved on or gotten distracted, and invalidate their session. The duration depends on the context; timeout for an admin user, or for a banking site, should be far shorter than that for a product rating site.
* **Renew the session with any change in privilege level.** If an authenticated user who has been e.g. viewing their account balance wants to submit a funds transfer, consider making them reauthenticate before going through with it. Sure, it's less convenient, but so are angry customers who have lost thousands of dollars through no fault of their own (except they chose a bank whose security was lacking).
* **Provide log out functionality.** Give users a log out button, which invalidates the session on the server and deletes the cookie from the client.
* **Invalidate tokens when replaced.** Create a completely new token when a new one is issued, and invalidate the old token.


### Cookie protections

* The ```Secure``` attribute instructs web browsers to transmit a cookie _only_ through an encrypted channel.
* The ```HttpOnly``` attribute forces browsers to not allow scripts (e.g. JavaScript or VBscript) to access cookies via the DOM ```document.cookie``` object.
* The ```SameSite``` attribute prevents browsers from sending a cookie with requests to other sites.
* The ```Domain``` and ```Path``` attributes define to where a browser may send the cookie;
  * ```Domain``` restricts the cookie to the specified domain and its subdomains.
  * ```Path``` restricts the cookie to the specified directory and its subdirectories (unless a subdomain is specified).
* Cookie lifespan attributes (it's best _not_ to use these unless needed):
  * The ```Max-Age``` attribute (takes precedence) sets a cookie to be persistent until the specified number of seconds elapses.
  * The ```Expires``` attribute persists a cookie until the date and time specified.
  * Note: these allow cookies to be persistent until the specified time, which defeats the purpose of closed sessions (see above). Use short timeouts where possible.
 
Here's an example of a secured authentication cookie:

```Set-Cookie: sessionId=7c65bd77-f96b-4b0a-bf21-0005526bcc82; Secure; HttpOnly; SameSite=Strict; Domain=www.secure.org```

# References

* [(OWASP) Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#introduction)
* [(OWASP) Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
* [(OWASP) Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [(OWASP) Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [(Mozilla) Using HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#security)
* [(Microsoft) Prevent Cross-Site Request Forgery (XSRF/CSRF) attacks in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery#authentication-fundamentals)
