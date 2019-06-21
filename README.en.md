# 📃 PACOS

![(PACOS.png)]

Parallel Application Communication Optimization System based on Topology Mapping

Home page：<https://king-ofwolf.github.io/PACOS>

Github Address: <https://github.com/King-ofwolf/PACOS>

Author：Wang Shengling

[中文 README](README.md)

## 📣 Introduction

[PACOS] is a parallel application communication performance optimization system based on topology mapping. It can calculate the mapping between the parallel application communication topology data file and the system network topology data file. Sequence, which integrates [TreeMatch], [TopoMapping], [MPIPP] Three algorithms, as well as algorithm recommendation functions and data visualization functions.

## ✨ Characteristic

* Provides an interactive interface that provides researchers with a simple and convenient way to perform parallel application communication performance optimization related work
* Provide algorithm recommendation function, recommend appropriate algorithm based on network structure and optimization options
* Provide data visualization capabilities to visualize parallel application communication topology data, system network topology data, and mapping schemes

## ⏳ Version

### V2.0

> Support Python2.7
> Add TreeMatch,MPIPP,TopoMapping Algorithms

## 🔰 Installation

**Install with git**
```bash
$ git clone https://github.com/King-ofwolf/PACOS.git
$ cd PACOS
$ sudo apt-get install qt4-dev-tools qt4-doc qt4-qtconfig qt4-demos qt4-designer libqwt5-qt4 libqwt5-qt4-dev
$ sudo pip2 install -r requirements.txt
```
**Install with zip**

Download source code zip file at the master branch of <https://github.com/King-ofwolf/PACOS>, its name is PACOS-master.zip

Or click to [download](https://github.com/King-ofwolf/PACOS/archive/master.zip)
```bash
$ unzip PACOS-master.zip
$ cd PACOS-master
$ sudo apt-get install qt4-dev-tools qt4-doc qt4-qtconfig qt4-demos qt4-designer libqwt5-qt4 libqwt5-qt4-dev
$ sudo pip2 install -r requirements.txt
```
## 📝 Usage

### Local Environment and Startup Method
> python 2.7

Run this command at the root directory of source code 
```bash
$ python System_windows.py
```
to open the system graphical interface
![(graphical interface.png)]

### Interface operation mode

Control name | Control graphic
--------|-------
[Open]()|![(Open.png)]
[File Type]()|![(File Type.png)]
[Configuration]()|![(Configuration.png)]
[Ensure]()|![(Ensure.png)]
[Play]()|![(Play.png)]
[File Parsing]()|![(File Parsing.png)]
[Parsing State]()|![(Parsing State Done.png)] ![(Parsing State Wrong.png)]
[Start Calculation]()|![(Start Calculation.png)]

#### &diams;Data file input：

- Communication topology file input：

![(Communication topology input.png)]

> 1. Click the [Open]()![(Open.png)] button, select the file you want to enter in the file browser that pops up / enter the address of the file in the input box.
> >If the file type to be input is the directory structure, you need to select **Dir** from the [File Type]()![(File Type.png)] drop-down menu after the input box.
> 
> 2. Select the corresponding type in the [File Type]()![(File Type.png)] drop-down menu depending on the file type entered.
> 3. Click the [Configuration]()![(Configuration.png)] button, enter the corresponding information in the pop-up configuration window, and click [Ensure]()![(Ensure.png)]

- Network topology file input：

![(Net topology input.png)]

> 1. Click the [Open]()![(Open.png)] button, select the file you want to enter in the file browser that pops up / enter the address of the file in the input box.
> 2. Select the corresponding type in the [File Type]()![(File Type.png)] drop-down menu depending on the file type entered.
> 3. Click the [Configuration]()![(Configuration.png)] button, enter the corresponding information in the pop-up configuration window, and click [Ensure]()![(Ensure.png)]

#### &diams;File parsing and visualization

> Click the [File Parsing]()![(File Parsing.png)] button. If the parsing is successful, the green Done is displayed in the [Parsing Status]()![(Parsing State Done.png)], otherwise an error message is displayed and the red Wrong is displayed![(Parsing State Wrong.png)].
> After the analysis is successful, click the [Play]()![(Play.png)] button to view the data after the data is visualized.
> > Network topology diagram currently only supports files in .txt format for visualization

![(CommGraph visiualization.png)]

#### &diams;Algorithm configuration and algorithm recommendation

After the file input and configuration are completed and parsed successfully, the algorithm can be configured. After the configuration is complete, the algorithm will be automatically recommended and the recommended algorithm will be checked.
> - [Optimization Options](): Determine algorithm recommendation, performance is priority performance, efficiency is priority efficiency
> - [Debug Mode](): Check to enable system debugging mode, debugging information will be output to the log file

If the selected algorithm is the TreeMatch algorithm, the corresponding configuration items are corresponding.
> - [-b]() binding constraint file
> - [-d]() cancel topology optimization
> - [-m]() optimization target (evaluation metric) Select the corresponding optimization target (SUM_COM/MAX_COM/HOP_BYTE) from the drop-down menu

#### &diams;Algorithm calculation and result display

Although the algorithm recommendation function automatically recommends the algorithm and selects the corresponding algorithm according to the network structure and the optimization option selected by the user, the user can still check other algorithms. Click [Start Calculation]()![(Start Calculation.png)], the system will calculate the algorithm according to the input data and parameters. The system is unavailable during the calculation process. After the calculation is finished, the result display interface will pop up.
> Results display interface includes scatter plots, map sequences, visualizations, and algorithm runtime
> - Scatter plot: the abscissa is the task serial number and the ordinate is the node serial number
> - Mapping sequence: the first column is the task serial number, and the second column is the node serial number
> - Visualization: The tree diagram is a network structure. The leaf nodes are nodes 0-n from top to bottom, and the number group on the node is the task sequence number assigned to the current node.

![(Result visualization.png)]

### Quick sample data input 

In order to facilitate the development test, add the [Sample]() menu in the menu bar of the system, All  the corresponding configuration items will be completed and you only have to click to select the corresponding algorithm and the corresponding sample. Directly click on two [File Parsing]()![(File Parsing.png)] after the button is completed, you can click the [Start Calculation]()![(Start Calculation.png)] button to perform algorithm calculation.

## 🔖 Sample data

> Sample data belongs to the directory names examples

For more detailed documentation, please visit

* [中文文档](README.md)
* [English Documentation](README.en.md)

## 😉 Author

PACOS mainly developed by the following developers

* [@King-ofwolf]

## 💡 Development
Waiting for update...
### Code structure
### Code base management
### Automatic code compilation


[PACOS]:https://github.com/King-ofwolf/PACOS
[TreeMatch]:http://treematch.gforge.inria.fr/
[TopoMapping]:https://dl.acm.org/citation.cfm?id=3079104
[MPIPP]:https://dl.acm.org/citation.cfm?id=1183451
[@King-ofwolf]:https://github.com/King-ofwolf/

[(PACOS.png)]:Layout/png/1208066.png
[(graphical interface.png)]:Layout/img/main.png
[(Open.png)]:Layout/img/open.png
[(File Type.png)]:Layout/img/file_type.png
[(Configuration.png)]:Layout/img/settings.png
[(Ensure.png)]:Layout/img/ensure.png
[(Play.png)]:Layout/img/play.png
[(File Parsing.png)]:Layout/img/file_analysis.png
[(Parsing State Done.png)]:Layout/img/analysis_done.png
[(Parsing State Wrong.png)]:Layout/img/analysis_wrong.png
[(Start Calculation.png)]:Layout/img/caculate.png
[(Communication topology input.png)]:Layout/img/task_input_line.png
[(Net topology input.png)]:Layout/img/net_input_line.png
[(CommGraph visiualization.png)]:Layout/img/TaskGraph.png
[(Result visualization.png)]:Layout/img/result_show.png

