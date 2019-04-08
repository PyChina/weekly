Title: Postgres Weekly : Issue 229
Slug: pgw-229
Date: 2019-04-04 15:32
Tags: Weekly,Pycoder,Zh 


原文: [Postgres Weekly Issue 299: April 3, 2019](https://postgresweekly.com/issues/299)

![...](https://res.cloudinary.com/cpress/image/upload/w_1280,e_sharpen:60/ssoylsgxn7il7w6zynuj.jpg)

- [Postgres 获得 'Generated Column' 支持](https://postgresweekly.com/link/61543/web)
    + Peter Eisentraut


It's always great to see Postgres gaining support for an SQL-standard feature and this commit begins with a simple example of how one type of generated column will work in the future. MySQL 5.7 introduced a similar feature and SQL Server calls them computed columns.


- [用 pg_dump / pg_restore 进行 Postgres 升级 ](https://postgresweekly.com/link/61546/web)
    + Jobin Augustine, Vallarapu, et al.


Last time they looked at using pg_dumpall, now it’s pg_dump and pg_restore’s turn under the spotlight.


- [在 PostgreSQL 数据库中监控的度量标准](https://postgresweekly.com/link/61548/web)
    + InfluxData 
    + sponsor

There are several key metrics you’ll want to keep track of when it comes to database performance, and they’re not all database-specific.


(`是也乎:`

![...](https://copm.s3.amazonaws.com/2e860b79.jpg)

这种很搭的赞助商才对味儿

)


- [2019 年 PostgreSQL 趋势报告](https://postgresweekly.com/link/61549/web)
    + ScaleGrid


A multi-cloud DBaaS provider surveyed users at last month’s PostgresConf and shares the results here. AWS comes in as the most popular cloud platform to host Postgres on and cost is the biggest reason to choose Postgres.


- [就等 PostgreSQL 12: REINDEX CONCURRENTLY](https://postgresweekly.com/link/61550/web)
    + Hubert depesz Lubaczewski


In Postgres 12, the REINDEX command (which rebuilds an index from a table’s current data) gains an option to have it build the index in the background and switch it into play upon completion.


- [用 TimescaleDB 为 PostgreSQL 的 Azure 数据库就物联网和时间序列工作负载提供动力](https://postgresweekly.com/link/61552/web)
    + Sunil Kamath (Microsoft)


A new partnership with Timescale that introduces support for TimescaleDB (a Postgres extension that focuses on time-series support) on Azure for customers building IoT and time-series workloads.


- [如何将大规模并行 Postgres 数据库迁移进 Kubernetes ](https://postgresweekly.com/link/61553/web)
    + Oz Basarir (Pivotal)

- [Pgpool-II 4.1 中的语句级负载平衡](https://postgresweekly.com/link/61554/web)
    + PgPool


- [Migra: Like diff But For Postgres Schemas](https://postgresweekly.com/link/61556/web)
    + Robert Lechte

Written in Python and can be used from your own Python scripts or the command line.

(`是也乎:`

哈, Python 喜欢干的事儿...

)


- [ActiveRecordExtended 1.0: Adds Additional Postgres Functionality to Ruby's Active Record](https://postgresweekly.com/link/61557/web)
    + George Protacio-Karaszi


Active Record, as commonly used in Ruby on Rails apps to interact with databases, is naturally database agnostic but Postgres has so many extra querying features it’s a shame not to be able to use them. This gem adds things like array and JSON querying, CTEs, and unions to the mix.


- [repmgr 4.3 发布](https://postgresweekly.com/link/61559/web)
    + 2ndQuadrant 

A popular tool for replication and failover management that includes several usability improvements in this release.




## 社区/活动
> 🗓 Upcoming Postgres Events



- [pgconf.de 2019 (May 10 in Leipzig, Germany)](https://postgresweekly.com/link/61560/web)
    + 德国 (May 10 in Leipzig, Germany)

The latest edition of the highly successful German-speaking PostgreSQL conference.

- [PGDay.IT 2019 (May 16 in Bologna, Italy)](https://postgresweekly.com/link/61561/web)
    + 意大利 (May 16 in Bologna, Italy)

- [PGCon 2019 (May 28 in Ottawa, Canada)](https://postgresweekly.com/link/61562/web)
    + 加拿大 (May 28 in Ottawa, Canada) 

An annual conference for users and developers to meet and discuss all things Postgres.

- [Postgres Vision 2019 (June 24 in Boston, MA)](https://postgresweekly.com/link/61563/web)
    + USA (June 24 in Boston, MA)


## 是也乎

- 190404 [Zoom.Quiet](http://zoomquiet.org/) 用时 13 分钟 完成快译.
- 190404 [Zoom.Quiet](http://zoomquiet.org/) 用时 3 分钟 完成格式转抄.

 
