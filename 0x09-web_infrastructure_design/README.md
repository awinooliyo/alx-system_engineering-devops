Web Infrastructure Tasks

## 0. Simple Web Stack

### Specifics About This Infrastructure

- **What a server is.** <br />
    A server is a piece of computer hardware or software that provides functionality for other programs or devices, called "clients".

- **The role of the domain name.** <br />
    Helps users find their way around the Internet.
    Domain name - a string of text that maps to a numeric IP address, used to access a website from client software.
- **The type of DNS record ```www``` is in ```www.foobar.com```.**
    ```www.foobar.com``` uses an A record. This can be checked by running ```dig www.foobar.com```.
    Note: the results might be different but for the infrastructure in this design, an A record is used.
    Address Mapping record (A Record) - also known as a DNS host record, stores a hostname and its corresponding IPv4 address.
- **The role of the web server.** <br />
    Serves web pages to clients upon their request, it does this over the protocol HTTP.
- **The role of the application server.** <br />
    Provides its clients with access to what is commonly called business logic, which generates dynamic content;that is, it’s code that transforms data to provide the specialized functionality offered by a business, service, or application.
- **The role of the database.** <br />
    To maintain a collection of organized information that can easily be accessed, updated and managed.
- **What the server uses to communicate with the client (computer of the user requesting the website).** <br />
    Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

    ### Issues with this infrastructure

- **SPOF (Single Point Of Failure).** <br />
    Failure of the server causes whole network to collapse

- **Downtime when maintenance needed.** <br />
    When the system is not being productive due to required maintenance work (like deploying new code web server needs to be restarted).
- **Cannot scale if too much incoming traffic.** <br />
    It is a bit unwieldy when it comes to scaling your site for higher loads.

## 1. Distributed web infrastructure

### Specifics About This Infrastructure

- **The distribution algorithm the load balancer is configured with and how it works.** <br />
    The HAProxy load balancer is configured with the Round Robin distribution algorithm. A client request is forwarded to each server in turn. The algorithm instructs the load balancer to go back to the top of the list and repeats again.

- **The setup enabled by the load-balancer.** <br />
    The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. This is because it consists of at least two nodes and not all nodes are going to be active. The passive (failover) server serves as a backup that's ready to take over as soon as the active (primary) server gets disconnected or is unable to serve. Different from an Active-Active setup which is made up of at least two nodes, both actively running the same kind of service simultaneously.

- **How a database Primary-Replica (Master-Slave) cluster works.** <br />
    A Primary-Replica setup configures one server to act as the Primary server and the other server to act as a Replica of the Primary server. However, the Primary server is capable of performing read/write requests whilst the Replica server is only capable of performing read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.

- **What is the difference between the Primary node and the Replica node in regard to the application.** <br />
    The Primary node is responsible for all the write operations the site needs whilst the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.

    ### Issues with this infrastructure

- **SPOF (Single Point Of Failure).** <br />
    Failure of the server causes whole network to collapse

- **Security issues.** <br />
    Prone to malware and interception by third parties to gather data passed between the two systems (no firewall, no HTTPS).
- **No monitoring.** <br />

    You cannot assess the health and performance of your servers in real-time.

    ## 2. Secured and monitored web infrastructure

### Specifics About This Infrastructure

- **What firewalls are for.** <br />
    They monitor and filter incoming and outgoing network traffic based on an organization's previously established security policies.

- **Why is the traffic served over HTTPS** <br />
    HTTPS is a more advanced and secure version of the HTTP protocol. It includes SSL, which is a part of the HTTPS protocol that performs encryption of the data.
    SSL certificate - authenticates the website’s identity and establishes a secured channel for communication between the website and the client.

- **What monitoring is used for.** <br />
    Tracking the health, metrics, and performance of your web servers, so you can ensure high-level functioning.

- **How the monitoring tool is collecting data.** <br />
    Web servers are monitored for user load, security and speed.
    Application servers are monitored for server availability and responsiveness.
    Storage servers are monitored for availability, capacity, delay and data loss.

    ### Issues with this infrastructure

- **Terminating SSL at the load balancer level is an issue.** <br />
    The traffic between the load-balancer and the server is unencrypted and, therefore, is vulnerable to data theft, session hijacking, and man-in-the-middle (MitM) attacks

- **Having only one MySQL server capable of accepting writes is an issue.** <br />
    Some transactions committed on the master may not be available on the slave if the master fails.
- **Having servers with all the same components (database, web server and application server) might be a problem.** <br />
    Your web site and database will share the same server resources (disk usage, memory, CPU). As a result, your database and web site will run slower than they would if they did not share resources with each other.


