## Apache NiFi
Apache NiFi is a software project from the Apache Software Foundation designed to automate the flow of data between software systems.

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/apache/apache_nifi)

## NOTES

NiFi does not perform user authentication over HTTP.

Single User authentication password must be at least 12 characters.


## Errors
When changing existing deployment from HTTPS to HTTP, errors may occur, for example^
```
Caused by: java.lang.illeglegstateexception: Flow Controller TLS Configuration is Invalid
```
Due to the imperfection of the docker entrypoint script, try to set empty variables:
```
nifi.security.keystorePasswd=
nifi.security.keyPasswd=
nifi.security.truststore=
nifi.security.truststoreType=
nifi.security.truststorePasswd=
```
