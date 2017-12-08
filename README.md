Python Language Repository (Data Structure, Algorithm)

Configure Java Environment on Linux (ubuntu Linux distribution)


vim .profile


export JAVA_HOME=/usr/jdk1.7.0_80

export PATH=$JAVA_HOME/bin:$PATH


Useful Blog,Article etc...

https://www.ibm.com/developerworks/cn/linux/management/configuration/index.html  --- About Linux Profile's article

http://www.tutorialspoint.com/java/io/outputstream_write.htm  ------- Java API Examples website.

http://blog.csdn.net/liuzhenwen/article/details/28078625 -- Hadoop Hive Integrated with HBase.

https://developers.google.com/fonts/docs/getting_started. ---- Google Font Blog (Useful website)


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

http://www.importnew.com/15141.html --- importnew SpringMVC 入门教程

https://github.com/hehaiyangwork   -- Maven-Demo SpringMVC 很好的一个例子

http://www.imooc.com/article/15638  -- Spring boot + mybatis + Vue.js + ElementUI 实现数据的增删改查(1)

http://blog.csdn.net/qq_31065001/article/details/64912687  Spring Boot JSP应用实例

http://www.cnblogs.com/best/p/5638827.html  -- 非常详细的Eclipse环境下，Spring+Maven+Mybatis配置教程

http://www.ncnynl.com/  创客智造

http://www.oracle.com/technetwork/articles/dsl/python-091105.html   Oracle Offical Document for Python access Oracle 11g

https://www.youtube.com/watch?v=0XL1NBUv2NU  Youtube DataStructure Training Video.

https://www.youtube.com/watch?v=YWnBbNj_G-U  Youtube DataStructure and Algorithms in one Video.

https://www.youtube.com/watch?v=-1nwZznnsCs&list=PLIgVNMF8pXSHr9FRzRrxH_AW8oTbJLfhg  Objective-C 培训视频（台湾版）

http://www.cnblogs.com/hehaiyang/p/4745897.html   Oracle SQL 外链接
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



=====================================================================================
https://segmentfault.com/a/1190000006178770 -- WebPack 入门指南
