<!--
.. title: Openstack swift和Owncloud对接
.. slug: openstack-swift-and-owncloud
.. date: 2018-03-11 23:03:21 UTC+08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

## Swift的几个相关概念
### Proxy
提供HTTP API给client，用来存储，查询，下载文件。Client只会跟proxy通信，存储节点对client是不可见的。
### Account
Swift中的account并不是认证的概念，可以理解为一块存储区域，主要记录了container的信息。
### Container
Container中主要记录了Object的相关信息。
### Object
记录实际文件的存储位置等信息。
### 存储节点
安装了account server，container server和object server（三者中的一个或者多个）的服务器。
## Swift的网络规划需求
 ### 网络平面
Swift的业务网络平面至少包含`Outward-facing network`,即proxy对外提供API的网络，`Cluster-facing network`,即proxy面向存储节点的网络。
### 对于网卡的需求
Swiftstack建议proxy至少要支持20Gbps的转发能力[^1]，即考虑`Outward-facing`5Gbps, `Cluster-facing`15Gbps(因为一般是配置3个副本)。

## Openstack Swift的安装
根据Openstack的版本参考官方文档[^2]即可，但因Owncloud不支持`Keystone v3`需要按如下步骤配置`Keystone v2`[^3]。
* `keystone.conf` 中配置`default_domain_id `
```
[identity] 

default_domain_id  = xxxxxxxx32ea5xxxxx2b6f93
```

* 同步keystone配置文件和数据库

```shell
su -s /bin/sh -c "keystone-manage --config-file /etc/keystone/keystone.conf db_sync" keystone
```
## Owncloud上的配置
Owncluod上的配置参见官方文档[^4]，其中：
*   **Bucket**对应于swift中就是`container`
*   **Username**对应于Openstack上租户的用户名
*   **Password** 对应于Openstack上租户的密码
*   **Tenant name**对应于Openstack上的租户 
*   **Identity Endpoint URL**, 即keystone的URL

另外要注意的是虽然在页面上`Service name`并不是必填项，但实际操作中发现此处不填是无法正常使用的，应配置为`swift`,`Region`也按配置openstack swift时创建的region名称来配置。


[^1]: [SwiftStack](https://www.swiftstack.com/docs/admin/hardware.html#networked-nodes-architecture)
[^2]: [OpenStack Installation Guide for Ubuntu](https://docs.openstack.org/mitaka/install-guide-ubuntu/swift.html)
[^3]: [https://ask.openstack.org/en/question/93199/how-to-enable-keystone-v2-on-mitaka/](https://ask.openstack.org/en/question/93199/how-to-enable-keystone-v2-on-mitaka/)
[^4]: [ownCloud 10.0.7 Server Administration Manual](https://doc.owncloud.org/server/10.0/admin_manual/configuration/files/external_storage/openstack.html)

