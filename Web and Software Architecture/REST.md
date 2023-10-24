# REST

The **REpresentational State Transfer** is an architectural style for distributed system, it states how the transfer of resources should happen between two hosts via HTTP.

## Resource

A resource is a set of values that have names (*i.e. information*), such as a document, image, a person's information. A resource may vary over time.

A representation of a resource is the state (value) of the resource at any given time, it is composed of *data* and *metadata*. The format of the data is called *media type*.

## Uniform Resource Identifier

Resources are identified by a **Uniform Resource Identifier** (*URI*), which is a unique sequence of characters that identify a logical or physical resource.

### URI Best Practices

- Resources are represented by nouns
- Singular nouns represent a single resource (e.g. `.../users/admin`)
- Plural nouns represent a collection of resources (e.g. `.../users/`)
- Slashes are used to express hierarchy; trailing slashed may be used on non-leaf resources
- Hyphens (-) are preferred to underscores (*lower-kebab-case*)
- Use lowercase letters
- Media type is specified in the headers, so file extensions must be omitted
- Query parameters may be used to filter (e.g. `/managed-devices/?region=IT`)

URIs are used to uniquely identify the resources, and not the actions that can be performed upon them. Different actions can be executed on a resource through supported methods:

- **Get a device's information:** `GET http://example.com/managed-devices/{id}`

- **Insert a device:** `PUT http://example.com/managed-devices/{id}`

- **Delete a device:** `DELETE http://example.com/managed-devices/{id}`

## RESTful System Constraints

A RESTful system must match some criteria, to be considered RESTful.

It must have a **client-server** paradigm.

- The separation of concerns and roles is enforced: the client is lightweight and handles user-interaction, the server handles data storage and intensive computations.
- Improved portability: the client can be a hybrid or web app.
- Improved scalability: the server can be improved or multiple servers can be deployed without the client knowing. 

It must be **stateless**.

- There's no context stored in the server, each request coming from the client must contain all the information necessary to understand it.
- Session state is kept entirely on the client, the server keeps only the resources states.

Resources must be **cacheable**: the client could later reuse a resource representation (data) with no problems, the caching time period can be specified in the response.