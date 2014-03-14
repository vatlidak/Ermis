
# Service description

Ermis (aka [Hermes](http://en.wikipedia.org/wiki/Hermes), the Greek god of transition) is a Django web service providing 
a Gateway to submit requests related to LB aliases. A user can create, delete, update and list LB alias information 
without the need to use the Drupal LBWeb. Ermis is accessible through LDAP using your CERN \<username, password\>, or 
with Kerberos provided that you have a valid ticket.


# API documentation


## List LB alias

List all registered LB aliasies. 

### Specification
* _Protocol_: HTTPS
* _Port_: 443
* _URL_: **aiermis.cern.ch/krb/api/lbalias/list** (Kerberos)
* _URL_: **aiermis.cern.ch/ldap/api/lbalias/list ** (LDAP)
* _Method_: GET
* _Authorization_: A valid kerberos ticket or a valid CERN <username,password>


### Return codes

* 200 (OK) -- Information successfully returned.
* 400 (Bad Request) -- Authentication OK but couldn't find information about aliases.
* 404 (Not Found) -- Authentication OK but couldn't find URL.
    * Check spelling of URL
* 401 (Authentication Failure) -- Apache couldn't authenticate with kerberos or LDAP. Your request never reached Django server.
    * Check that you have a valid Kerberos ticket.
    * Check that you properly spelled your \<username, password\>.
* 405 (Method not allowed) -- HTTP verb is not allowed.
    * Verify if your client is issuing a GET request
* 500 (Internal Server Error) -- Something is wrong in the server
    * Open a support call. See 'Bugs'.


### Examples

Some cURL magic:

`curl -k --negotiate  -X GET https://:@aiermis.cern.ch/krb/api/lbalias/list`

`curl -k  -X GET https://aiermis.cern.ch/ldap/api/lbalias/list -u vatlidak`



## Create LB alias 

Registers an LB alias and assignes a type; either external or internal.

### Specification
* _Protocol_: HTTPS
* _Port_: 443
* _URL_: **aiermis.cern.ch/krb/api/lbalias/add** (Kerberos)
* _URL_: **aiermis.cern.ch/ldap/api/lbalias/add ** (LDAP)
* _Method_: POST
* _Authorization_: A valid kerberos ticket or a valid CERN <username,password>

### Return codes

* 201 (Created) -- Alias registration succesful.
* 401 (Authentication Failure) -- Apache couldn't authenticate with kerberos or LDAP. Your request never reached Django server.
    * Check that you have a valid Kerberos ticket.
    * Check that you properly spelled your \<username, password\>.
* 400 (Bad request) -- Authentication OK but couldn't registed alias.
    * Verify that you are *not* trying to register an existing alias.
    * Verify that you have valid dictionary key values.
* 404 (Not Found) -- Authentication OK but couldn't find URL.
    * Check spelling of URL
* 405 (Method not allowed) -- HTTP verb is not allowed.
    * Verify if your client is issuing a POST request
* 500 (Internal Server Error) -- Something is wrong in the server
    * Open a support call. See 'Bugs'.


### Examples

`curl -k --negotiate -H "Content-Type: application/json" -X POST -d '{"alias_name":"higgs-alias-2", "type":"external"}' -L https://:@aiermis.cern.ch/krb/api/lbalias/add `

`curl -k  -H "Content-Type: application/json" -X POST -d '{"alias_name":"higgs-alias-3", "type":"external"}' -L https://aiermis.cern.ch/ldap/api/lbalias/add  -u vatlidak`



## Updates LB alias 

Updates an LB alias and assignes a new type; either external or internal.

### Specification
* _Protocol_: HTTPS
* _Port_: 443
* _URL_: **aiermis.cern.ch/krb/api/lbalias/update** (Kerberos)
* _URL_: **aiermis.cern.ch/ldap/api/lbalias/update ** (LDAP)
* _Method_: PUT
* _Authorization_: A valid kerberos ticket or a valid CERN <username,password>

### Return codes

* 200 (OK) -- Alias registration succesful.
* 401 (Authentication Failure) -- Apache couldn't authenticate with kerberos or LDAP. Your request never reached Django server.
    * Check that you have a valid Kerberos ticket.
    * Check that you properly spelled your \<username, password\>.
* 400 (Bad request) -- Authentication OK but couldn't update alias.
    * Verify that you are not trying to update an existing alias.
    * Verify that you have valid dictionary key values.
* 404 (Not Found) -- Authentication OK but couldn't find URL.
    * Check spelling of URL
* 405 (Method not allowed) -- HTTP verb is not allowed.
    * Verify if your client is issuing a PUT request
* 500 (Internal Server Error) -- Something is wrong in the server
    * Open a support call. See 'Bugs'. 


### Examples

`curl -k --negotiate -H "Content-Type: application/json" -X PUT -d '{"type":"internal"}' -L https://:@aiermis.cern.ch/krb/api/lbalias/update/higgs-alias-1`

`curl -k  -H "Content-Type: application/json" -X PUT -d '{"type":"external"}' -L https://aiermis.cern.ch/ldap/api/lbalias/update/higgs-alias-1 -u vatlidak`




## Deletes LB alias

Removes an LB alias.

### Specification
* _Protocol_: HTTPS
* _Port_: 443
* _URL_: **aiermis.cern.ch/krb/api/lbalias/delete** (Kerberos)
* _URL_: **aiermis.cern.ch/ldap/api/lbalias/delete ** (LDAP)
* _Method_: DELETE
* _Authorization_: A valid kerberos ticket or a valid CERN <username,password>

### Return codes

* 204 (DELETED) -- Alias successfully removed.
* 401 (Authentication Failure) -- Apache couldn't Authenticate with kerberos or LDAP. Your request never reached Django server.
    * Check that you have a valid Kerberos ticket.
    * Check that you properly spelled your \<username, password\>.
* 400 (Bad request) -- Authentication OK but couldn't remove alias.
    * Verify that you are not trying to remove an existing alias.
* 404 (Not Found) -- Authentication OK but couldn't find URL.
    * Check spelling of URL
* 405 (Method not allowed) -- HTTP verb is not allowed.
    * Verify that your client is issuing a DELETE request
* 500 (Internal Server Error) -- Something is wrong in the server
    * Open a support call. See 'Bugs'.





### Examples

`curl -k --negotiate  -X DELETE   https://:@aiermis.cern.ch/krb/api/lbalias/delete/higgs-alias-5`

`curl -k   -X DELETE   https://aiermis.cern.ch/ldap/api/lbalias/delete/higgs-alias-1 -u vatlidak`


### Notes

There is currently a bug in django-piston package. The only way to circumvent it is to manually install 
the most up-to-date python module. 



# Bugs

Bug reports are welcome. Open a [JIRA ticket](https://its.cern.ch/jira/) (project AI) providing a detailed
description of the problem and assign it to Vaggelis Atlidakis. 

# Version

This server is running Ermis Gateway **v@@ERMISVERSION@@**.


# Source code

The source code can be downloaded from the [Central GIT Service](https://git.cern.ch/web/?p=ai-ermis.git)
