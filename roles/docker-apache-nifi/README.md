## Apache apache_nifi
Apache apache_nifi is a software project from the Apache Software Foundation designed to automate the flow of data between software systems. 

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/apache/apache_nifi)


## Errors
When changing existing deployment from HTTPS to HTTP, errors may occur, for example^
```
Caused by: java.lang.illeglegstateexception: Flow Controller TLS Configuration is Invalid
```
Due to the imperfection of the docker entrypoint script. Delete `conf` directory and restart. Or try to set empty variables:
```
nifi.security.keystorePasswd=
nifi.security.keyPasswd=
nifi.security.truststore=
nifi.security.truststoreType=
nifi.security.truststorePasswd=
```
