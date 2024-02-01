# 0x10. HTTPS SSL
The two main roles of HTTPS (Hypertext Transfer Protocol Secure)and SSL(Secure Socket Layer) are:
* **Encryption**: The HTTP/SSL encrypt data exchanged between the server and clients to prevent access by unauthorized third parties. They also provide data integrity, ensuring that information transmitted between client and server remains unchanged during tranfer to prevent attacks.
* **Authentification**: HTTP/SSL helps in authenticating the identity of the server to the client. When a user connects to a website using HTTPS, the server presents a digital SSL certificate that is verified by the client's browser. The cerificate confirms the identity of the server to help the users to trust that they're connecting to the legitimate website and not a malicuous alternative.

Encryption of the traffic is critical in information security. It plays a critical role in:
* Confidentiality by ensuring that information transmitted such as credit card details, credentials, and financial data is protected from unauthorized access.
* Data integrity during transit by ensuring same information is sent and received without being altered.
* Authentification by verifying the identitiesof the parties involved.
* Protection against eavesdropping
* Security in public networks.
* Preventing man-in-the-middle attacks.
* Preserving user trust and confidence in websites and other online services.

**SSL Termination** refers to the process of decrypting encrypted SSL/TLS traffic at a network device before it reaches the web server. It occurs in an intermediary point, usually a load balancer or a reverse proxy. The process entails:
* Client connection - the client initiates a connection toa web server using HTTPS protocol.
* Intermediary Device (SSL Termination Point) - An intermediary device intercepts the incoming SSL/TLS-encrypted traffic before it gets to the server.
* SSL/TLS Decrption - the intermediary device decrypts the traffic using private key associated with the SSL/TLS certificate.
* Plain HTTP Traffic - the traffic is converted to plain HTTP. Here, the communication between the intermediary device and the web server occurs in unencrypted form.
* Communication with web server - the intermediary device forwards the unencrypted HTTP traffic to web server. The latter processes the request and generates a response.
* SSL/TLS Encryption (Optional) - if need be, the intermediary device may re-encrypt the response using SSL/TLS before sending it back to the client depending on the configuration and security requirements.

Task done by **Erick O. Awino**
