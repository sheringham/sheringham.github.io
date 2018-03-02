<!--
.. title: ubuntu 14通过service networking restart重启网络失败
.. slug: ubuntu-14-service-networking-restart-not-working
.. date: 2018-03-02 19:52:54 UTC+08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->


之前就遇到过启动Debian或者Ubuntu虚拟机并修改网络后使用`service netwoking restart`出现如下报错的失败的问题，当时觉得反正虚拟机启动也快，就直接重启解决。


```
# service  networking restart
stop: Job failed while stopping
start: Job is already running: networking
```


今天启动Ubuntu 14.04虚拟机后又遇到类似的问题，发现原因是不支持使用这种方式重启网络。

```
# tail -f /var/log/upstart/networking.log
Stopping or restarting the networking job is not supported.
Use ifdown & ifup to reconfigure desired interface.
```

于是采用如下的方式去重启除loopback之外的所有网卡即可解决。


```
# ifdown --exclude=lo -a && sudo ifup --exclude=lo -a

```


