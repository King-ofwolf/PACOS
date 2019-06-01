
# 📃 PACOS
基于拓扑映射的并行应用通信性能优化系统
*(Parallel Application Communication Optimization System based on Topology Maping)*

Github 地址: <https://github.com/King-ofwolf/PACOS>
作者：汪圣灵

[English README](README.en.md)
## 📣 简介

[PACOS](https://github.com/King-ofwolf/PACOS) 是基于拓扑映射的并行应用通信性能优化系统，能够使用并行应用通信拓扑数据文件和系统网络拓扑数据文件计算生成两者的映射序列，其中集成了[TreeMatch](http://treematch.gforge.inria.fr/)、[TopoMapping](https://dl.acm.org/citation.cfm?id=3079104)、[MPIPP](https://dl.acm.org/citation.cfm?id=1183451)三种算法，以及算法推荐功能和数据可视化功能。

## ✨ 特性

* 提供交互式界面，为研究人员提供简单方便的途径来进行并行应用通信性能优化相关工作
* 提供算法推荐功能，能够根据网络结构和优化选项推荐合适的算法
* 提供数据可视化功能，能够将并行应用通信拓扑数据、系统网络拓扑数据、映射方案进行可视化

## ⏳ 版本

### V2.0

> 支持 Python2.7
> 添加了TreeMatch、MPIPP、TopoMapping算法

## 🔰 安装
**git源码安装**
```bash
$ git clone https://github.com/King-ofwolf/PACOS.git
$ cd PACOS
$ pip install -r requirements.txt
```
**zip源码安装**
在<https://github.com/King-ofwolf/PACOS>的master分支下载源码包，名字为PACOS-master.zip
```bash
$ unzip PACOS-master.zip
$ cd PACOS-master
$ pip install -r requirements.txt
```
## 📝 使用

### 本地环境
> python 2.7

## 🔖 样例数据

> 样例数据位于 examples 文件夹下

更多详细文档，请访问

* [中文文档](README.md)
* [English Documentation](README.en.md)

## 😉 Author

PACOS主要由以下开发者开发

* [@King-ofwolf](https://github.com/King-ofwolf/)

## 💡 开发
### 代码结构
### 代码库管理
### 代码自动编译


