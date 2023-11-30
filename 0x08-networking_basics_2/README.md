0x08. Networking basics #1
XXXXXXXXXXXXXXXXXXXXXXXXXX
## Learning Objectives

* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine's active network interfaces

### What is localhost/127.0.0.1

> "Localhost" is a hostname that refers to the current device or computer being used. It is commonly associated with the IP address "127.0.0.1." It's also the default name used to establish a connection with a computer using the loopback address network.

> When you access "localhost" in a web browser or use it in network communications, you are referring to the device you are currently using. It is often used for testing and development purposes. Any services or applications running on the device can be accessed through the localhost address.

> The IP address "127.0.0.1" is a loopback address that is reserved for the purpose of communication within the device itself. When a program or service communicates with "127.0.0.1," it is essentially sending data to itself. This loopback mechanism allows developers to test and debug applications locally without the need for an external network connection; it bypasses the local network interface hardware.

### What is 0.0.0.0

> The IP address "0.0.0.0" has a special meaning in networking. It is known as an "unspecified" or "wildcard" address.

> When a device is assigned the IP address "0.0.0.0," it typically indicates that the device does not have a specific assigned IP address or it is not yet configured with a valid IP address. It can also be used to represent all IP addresses on the local machine or on a particular network interface.

> In some cases, network administrators may use the IP address "0.0.0.0" to configure network services or applications to listen on all available network interfaces or to bind to any available IP address. This allows the services or applications to accept connections from any source IP address.

> Overall, the IP address "0.0.0.0" is a placeholder that represents various meanings depending on the context in which it is used, such as indicating the absence of a specific IP address or representing all available IP addresses.

### What is /etc/hosts

> The /etc/hosts file is a plain text file found in Unix-like operating systems (including Linux) that serves as a local DNS (Domain Name System) lookup table. It maps hostnames to IP addresses on the local machine.

> When a computer needs to communicate with another computer on a network, it typically uses the DNS to translate human-readable domain names (like www.example.com) into IP addresses (like 192.0.2.1). The /etc/hosts file provides a way to override or supplement the DNS lookup process by defining custom mappings between hostnames and IP addresses locally.

> By modifying the /etc/hosts file, you can define custom hostname-to-IP address mappings on your local machine. This can be useful for testing or development purposes, or for overriding DNS resolution for specific domains. When a program on the machine tries to access a hostname listed in the /etc/hosts file, it will use the associated IP address defined in the file instead of querying a DNS server.

### How to display your machine's active network interfaces

> ifconfig: This command displays information about all active network interfaces on your Linux machine, including their IP addresses, MAC addresses, and other details. However, newer Linux distributions often use the ip command instead of ifconfig.

> ip addr show: This command provides similar information as ifconfig but is considered more modern and is available on newer Linux systems.

>Telnet is a network protocol used on the internet or local area networks to provide a bidirectional interactive text-oriented communication session between two networked devices. It allows a user to connect to and interact with a remote system or device as if they were directly connected to it via a command-line interface (CLI). To initiate a Telnet session, you can typically use the following command in a terminal or command prompt:telnet <host> <port> for example telnet example.com 23. Once connected, you can interact with the remote system using command-line instructions specific to that system or application.

> The nc command, short for "netcat," is a versatile networking utility available on Unix-like operating systems (Linux, macOS, etc.) that allows for reading from and writing to network connections using TCP or UDP protocols. It's often referred to as the "Swiss Army knife of networking" due to its flexibility in handling various network-related tasks. nc can be used for a variety of purposes, including: (1) Port Scanning: It can check for open ports on a remote system, (2) Creating Network Connections: It can establish TCP or UDP connections to remote systems, and (3) Transferring Files: It can transfer files between systems.

>The cut command is a Unix/Linux utility used for extracting sections or columns of text from files or standard input (stdin). It's particularly useful for manipulating text data by selecting specific fields or portions based on delimiters such as spaces, tabs, or characters. The basic syntax for the cut command is: cut OPTION... [FILE]
