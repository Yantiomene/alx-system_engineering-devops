# Postmortem

In this module, we will be debugging a http 500 internal Apache server error:

Here is the error:
```
root@c1cea22c50e0:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 13 Oct 2023 11:38:21 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9–1ubuntu4.21
Connection: close
Content-Type: text/html
```

I used the `strace` and the `tmux` command to find out that the error was a mispelling of the path of this **/var/www/html/wp-includes/class-wp-locale.phpp** in this settings file **/var/www/html/wp-settings.php**

so all i have to do was to replace lines containing this error with the good spelling which i did using a puppet manifest file
```
root@c1cea22c50e0:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 13 Oct 2023 13:33:31 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9–1ubuntu4.21
Connection: close
Content-Type: text/html

root@c1cea22c50e0:~# puppet apply debug_apache.pp
Notice: Compiled catalog for c1cea22c50e0.ec2.internal in environment production in 0.20 seconds
Notice: /Stage[main]/Main/Exec[replace_class_name]/returns: executed successfully
Notice: Finished catalog run in 0.31 seconds

root@c1cea22c50e0:~# curl -sI 127.0.0.1
HTTP/1.1 200 OK
Date: Fri, 13 Oct 2023 13:34:01 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9–1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@c1cea22c50e0:~#
```


A full details of the step can be found in this [article](https://medium.com/@yan2016tiomene/how-to-fix-the-http-500-internal-apache-server-error-using-strace-and-tmux-2a8f4722667d)
