Description
===========

#### Production

Multiple Linux servers with [MySQL 5.6](http://www.mysql.com/), configured in
a master-slave replication configuration.


Instructions
===========

#### Getting Started
If you're new to MySQL, the [Manual](http://dev.mysql.com/doc/refman/5.6/en/index.html)
documentation will step you through the basics of configuration, connecting,
user, and  permission management.

By default, the "root" MySQL user can only connect from localhost (127.0.0.1).
You will need to connect to the server and use the MySQL client in order to
allow "root" to connect from external servers.

As a part of your server configuration, your server will be configured to run
nightly backups leveraging
[Holland](https://github.com/holland-backup/holland#readme).  Backups will be
stored in the directory /var/lib/mysqlbackups directory on the master node.
#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH. We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).
#### Additional Notes
All write operations should be performed on the Master node. Read operations
can be performed against any servers in this deployment. By default, all new
and existing databases will be replicated across the members of this
deployment.


Requirements
============
* A Heat provider that supports the following:
  * OS::Heat::RandomString
  * OS::Heat::ResourceGroup
  * OS::Heat::SoftwareConfig
  * OS::Heat::SoftwareDeployment
  * OS::Nova::KeyPair
  * OS::Nova::Server
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `mysql_user`: User to create within MySQL (Default: mysql_user)
* `mysql_database`: Database to create within MySQL.  User defined in "MySQL User" will have full access to this database (Default: mysql_db)
* `server_flavor`: Flavor of Cloud Server to be used for all servers in this stack (Default: 4 GB General Purpose v1)
* `server_count`: Number of secondary web nodes (Default: 0)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `mysql_public_ip`: Master IP
* `mysql_password`: MySQL Root Password
* `mysql_user_password`: MySQL Password
* `mysql_user`: MySQL User
* `ssh_private_key`: SSH Private Key
* `secondary_ips`: Secondary Node IPs

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.
