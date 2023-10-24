# Application

Basically, an application (*app* for short) is a digital program that runs on the Operative System of a device and has a set of features useful to the user.

Applications may either be **desktop applications** or **mobile applications**, the main difference being the device the application is intended for. Furthermore, the set of technologies used to build the application determines the type of application:

- A **native app** is an application written explicitly for a type of device (e.g. *desktop*, *mobile*) in a language that compiles to code that the device **natively** understands, e.g. `java/kotlin` -> `Android`, `swift` -> `iOS`.
- A **hybrid app** is an application written using web technologies, that either are *interpreted* or *cross-compiled* to different operative systems. 

> [!note] Internet Connectivity
> 
> Native and hybrid applications may or may not use an internet connection, depending on the features offered by the application, but it is not required by the type of application itself.

Another type of application, vastly used, are **web applications**. They run in a browser and need internet connectivity to access them. The main difference with native and hybrid applications is that most of the computation happens in a **server**, that sends the user (**client**) a web page tailored to his use.

Usually, web applications reload the web page at each user interaction, to let the server update the user interface. Certain web applications, instead, let the client update the user interface without reloading the entire page: they are called **single page applications**. Instead of asking for the whole page, the client asks the server for just the data, so that it can update the interface with the given data.

Web applications, similarly to hybrid apps, have the ability to be *installed* on the device to reduce loading times and to provide offline features; these are called **progressive web applications**.