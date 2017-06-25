Python Language Repository (Data Structure, Algorithm)

Configure Java Environment on Linux (ubuntu Linux distribution)


vim .profile


export JAVA_HOME=/usr/jdk1.7.0_80

export PATH=$JAVA_HOME/bin:$PATH


Useful Blog,Article etc...

https://www.ibm.com/developerworks/cn/linux/management/configuration/index.html  --- About Linux Profile's article

http://www.tutorialspoint.com/java/io/outputstream_write.htm  ------- Java API Examples website.

http://blog.csdn.net/liuzhenwen/article/details/28078625 -- Hadoop Hive Integrated with HBase.


http://blog.csdn.net/zxcvg/article/details/18600335  --- Flume-ng+Kafka+storm的学习笔记 (非常好的文章)

http://www.cnblogs.com/lijingchn/p/5574476.html  --- Linux中安装配置Hadoop集群

http://blog.csdn.net/high2011/article/details/52425430  --- 编写Hive UDF，详实的资料

http://blog.csdn.net/high2011/article/details/52539071  --- 编写Hive UDF 获取当前日期

http://blog.csdn.net/tswisdom/article/details/41522069  --- Zookeeper 系列

http://www.cnblogs.com/luxiaoxun/p/5272384.html  --- 一个轻量级分布式RPC框架--NettyRpc  Simple Dubbo Framework 

http://www.cnblogs.com/bigdataZJ/p/spring1.html   --- Spring in Action 实战，不错的一个博客

http://blog.csdn.net/congcong68/article/details/41113239  ---- Dubbo Zookeeper Spring Integration Article

http://blog.csdn.net/wangpeng047/article/details/9627527  ---- JUnit 系列文章，其中还有Spring Maven，Hibernate的使用

https://www.w3cschool.cn/junit/   ---- w3cschool.cn JUnit Training Course.

https://www.ibm.com/developerworks/cn/linux/l-assembly/  -- IBM Assembly Language Guide

http://www.cnblogs.com/pwc1996/p/4839131.html  ---- cnblog, Spring+SpringMVC+MyBaitis Configuration

http://www.cnblogs.com/eggbucket/archive/2012/02/02/2335697.html   ---- junit4 详解

http://www.cnblogs.com/fingertouch/archive/2013/05/02/3054721.html  --- Linux 下写汇编程序

https://segmentfault.com/a/1190000006178770 -- WebPack 入门指南
=====================================================================================
 设置Git的user name和email：

$ git config --global user.name "xuhaiyan"

$ git config --global user.email "haiyan.xu.vip@gmail.com"


二、生成SSH密钥过程：
1.查看是否已经有了ssh密钥：cd ~/.ssh
如果没有密钥则不会有此文件夹，有则备份删除
2.生存密钥：

    $ ssh-keygen -t rsa -C “haiyan.xu.vip@gmail.com”
    按3个回车，密码为空。


    Your identification has been saved in /home/tekkub/.ssh/id_rsa.
    Your public key has been saved in /home/tekkub/.ssh/id_rsa.pub.
    The key fingerprint is:
    ………………


最后得到了两个文件：id_rsa和id_rsa.pub


3.添加密钥到ssh：ssh-add 文件名
需要之前输入密码。
4.在github上添加ssh密钥，这要添加的是“id_rsa.pub”里面的公钥。



