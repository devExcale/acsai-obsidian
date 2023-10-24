# Authentication

Authentication is the process of establishing confidence in user identities that are presented electronically to an information system.

![authentication-architecture](assets/authentication-architecture.png)

## Authentication Requirements

The following are the two basic requirements that an authentication system must implement to ensure authentication.

1. Identify information system users, processes acting on behalf of users, or devices.

2. Authenticate (or verify) the identities of those users, processes, or devices, as a prerequisite to allowing access to organizational information systems.

Moreover, additional requirements can be derived to improve security.

3. Use multifactor authentication for access to privileged accounts and for network access

4. Employ replay-resistant authentication mechanisms (i.e. tokens can't be used more than once)

5. Prevent reuse of identifiers for a defined period

6. Disable identifiers after a defined period of inactivity

7. Enforce a minimum password complexity and change of characters when new passwords are created

8. Prohibit password reuse for a specified number of generations

9. Allow temporary password use for logons with an immediate change to a permanent password.

10. Store and transmit only cryptographically-protected passwords.

11. Obscure feedback of authentication information.

## Password-based Authentication

In a password-based authentication system, the user provides a name (**user ID**), which uniquely identifies the user, and a **password**, which is checked against the one stored in the system.

Popular password vulnerabilities:

- **Offline Dictionary Attack:** a list of password is checked against a single user ID, hoping that the user's password is included in the list;

- **Popular Password Attack:** similar to the offline dictionary attack, a list of popular passwords is checked against the user ID;

- **Workstation Hijacking:** TK

- **Exploiting Multiple Password Use:** TK

### Storing Passwords

When creating a password, the password must be stored in a database so that it can be checked against when the user tries to authenticate. Passwords are **not** stored ai-is (*cleartext*), but instead a [hash function](Cybersecurity/Tools/Hash%20Functions.md) is used to convert the password into a fixed-size string (*hash code*) that can't be reversed.

Moreover, to prevent some types of attack (e.g. offline dictionary attack), a so-called *salt* is appended to the password before the hashing, to ensure that two users using the same password will result in different hash codes.

![Storing a new password](assets/pwd_hash_loading.png)

When the user tries to authenticate, the inputted password is converted into the hash code via the hash function. The resulting hash code is checked against the stored hash code: if the hash codes match the user is correctly authenticated, otherwise the password is not the original one.

![Verifying an input password](assets/pwd_hash_verifying.png)