# 0x0C. Web server
Completed by **Erick Otieno Awino**
* **What is the main role of a web server:** The primary role of a web server is to store, process, and deliver requested information or webpages to end users.
* **What is a child process:** A child process is a process created by another process, i.e the parent process. A child process can start and stop without affecting the parent process. A child process is dependent on the parent process. When a parent process dies, a child process is orphaned.
* **Why web servers usually have a parent process and child processes:** Web servers typically use a parent-child process model to handle incoming client requests efficiently and to enhance the overall stability and performance of the server.
* **What are the main HTTP requests?** The main HTTP requests include GET (Retrieve data from the specified resource); POST (Submit data to be processed to a specified resource.); PUT (Update a resource or create a new resource if it does not exist at the specified URL); PATCH (Partially update a resource.); DELETE (Delete the specified resource.); HEAD(Retrieve the headers of a resource, without the actual body content.); OPTIONS(Retrieve information about the communication options available for the target resource.); TRACE(Perform a message loop-back test, which can be useful for debugging.); CONNECT( Establish a tunnel to the server identified by the target resource.), and TRACE (Perform a message loop-back test, which can be useful for debugging.).
* **What DNS stands for:** DNS is an abbreviation of Domain Name System.
* **What is DNS main role?** A DNS makes the internet accessible by translating the human-readable domain names into IP addresses that computers use to locate and communicate with one another on a network.

## Types of DNS Record
* **A (Address Record)**: Associates a domain name with an IPv4 address.
Example:
`www    IN    CNAME    example.com`
* **CNAME**: Creates an alias for a domain name. It is often used to map a subdomain to the canonical domain.
Example:
`www    IN    CNAME    example.com`
* **TXT (Text) Record**: Allows the addition of arbitrary text to a DNS record. It is commonly used for various purposes such as domain verification for services like SPF (Sender Policy Framework) and DKIM (DomainKeys Identified Mail).
Example:
`example.com.    IN    TXT    "v=spf1 include:_spf.example.com ~all"`
* **MX (Mail Exchange) Record**: Specifies mail servers responsible for receiving email on behalf of a domain. It points to the domain names of mail servers and their associated priority values.
Example:
 `example.com.    IN    MX    10    mailserver1.example.com.`
`example.com.    IN    MX    20    mailserver2.example.com.`

