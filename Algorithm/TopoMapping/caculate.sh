#!/bin/bash
# @Author: kingofwolf
# @Date:   2018-12-03 16:20:39
# @Last Modified by:   kingofwolf
# @Last Modified time: 2019-03-13 17:35:33

#python ParMapper -t <taskgraph file> --tsize <task number> -n <netgraph file> --ct <core total number> --nnode <node number> --ncore <core number>
case $1 in
	#debug
	(-128)
		echo "python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf128.APHiD --tsize 128 -n ../examples/netgraph/TimeCostDataFile_128-7-20.txt --ct 128 --nnode 7 --ncore 20"
		python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf128.APHiD --tsize 128 -n ../examples/netgraph/TimeCostDataFile_128-7-20.txt --ct 128 --nnode 7 --ncore 20
		:;;
	(-240)
		echo "python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf240.APHiD --tsize 240 -n ../examples/netgraph/TimeCostDataFile_240-10-24.txt --ct 240 --nnode 10 --ncore 24"
		python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf240.APHiD --tsize 240 -n ../examples/netgraph/TimeCostDataFile_240-10-24.txt --ct 240 --nnode 10 --ncore 24
		:;;
	(-256)
		echo "python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf256.APHiD --tsize 256 -n ../examples/netgraph/TimeCostDataFile_256-11-24.txt --ct 256 --nnode 11 --ncore 24"
		python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf256.APHiD --tsize 256 -n ../examples/netgraph/TimeCostDataFile_256-11-24.txt --ct 256 --nnode 11 --ncore 24
		:;;
	(-320)
		echo "python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf320.APHiD --tsize 320 -n ../examples/netgraph/TimeCostDataFile_320-14-24.txt --ct 320 --nnode 14 --ncore 24"
		python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf320.APHiD --tsize 320 -n ../examples/netgraph/TimeCostDataFile_320-14-24.txt --ct 320 --nnode 14 --ncore 24
		:;;
	(-480)
		echo "python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf480.APHiD --tsize 480 -n ../examples/netgraph/TimeCostDataFile_480-20-24.txt --ct 480 --nnode 20 --ncore 24"
		python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf480.APHiD --tsize 480 -n ../examples/netgraph/TimeCostDataFile_480-20-24.txt --ct 480 --nnode 20 --ncore 24
		:;;
	(-512)
		echo "python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf512.APHiD --tsize 512 -n ../examples/netgraph/TimeCostDataFile_512-22-24.txt --ct 512 --nnode 22 --ncore 24"
		python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf512.APHiD --tsize 512 -n ../examples/netgraph/TimeCostDataFile_512-22-24.txt --ct 512 --nnode 22 --ncore 24
		:;;
	(-640)
		echo "python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf640.APHiD --tsize 640 -n ../examples/netgraph/TimeCostDataFile_640-27-24.txt --ct 640 --nnode 27 --ncore 24"
		python ./ParMapper.py --debug -t ../examples/taskgraph/CloverLeaf640.APHiD --tsize 640 -n ../examples/netgraph/TimeCostDataFile_640-27-24.txt --ct 640 --nnode 27 --ncore 24
		:;;

	#caculate 24cores
	(128)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf128.APHiD --tsize 128 -n ../examples/netgraph/TimeCostDataFile_128-6-24.txt --ct 128 --nnode 6 --ncore 24"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf128.APHiD --tsize 128 -n ../examples/netgraph/TimeCostDataFile_128-6-24.txt --ct 128 --nnode 6 --ncore 24
		:;;
	(240)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf240.APHiD --tsize 240 -n ../examples/netgraph/TimeCostDataFile_240-10-24.txt --ct 240 --nnode 10 --ncore 24"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf240.APHiD --tsize 240 -n ../examples/netgraph/TimeCostDataFile_240-10-24.txt --ct 240 --nnode 10 --ncore 24
		:;;
	(256)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf256.APHiD --tsize 256 -n ../examples/netgraph/TimeCostDataFile_256-11-24.txt --ct 256 --nnode 11 --ncore 24"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf256.APHiD --tsize 256 -n ../examples/netgraph/TimeCostDataFile_256-11-24.txt --ct 256 --nnode 11 --ncore 24
		:;;
	(320)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf320.APHiD --tsize 320 -n ../examples/netgraph/TimeCostDataFile_320-14-24.txt --ct 320 --nnode 14 --ncore 24"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf320.APHiD --tsize 320 -n ../examples/netgraph/TimeCostDataFile_320-14-24.txt --ct 320 --nnode 14 --ncore 24
		:;;
	(480)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf480.APHiD --tsize 480 -n ../examples/netgraph/TimeCostDataFile_480-20-24.txt --ct 480 --nnode 20 --ncore 24"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf480.APHiD --tsize 480 -n ../examples/netgraph/TimeCostDataFile_480-20-24.txt --ct 480 --nnode 20 --ncore 24
		:;;
	(512)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf512.APHiD --tsize 512 -n ../examples/netgraph/TimeCostDataFile_512-22-24.txt --ct 512 --nnode 22 --ncore 24"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf512.APHiD --tsize 512 -n ../examples/netgraph/TimeCostDataFile_512-22-24.txt --ct 512 --nnode 22 --ncore 24
		:;;
	(640)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf640.APHiD --tsize 640 -n ../examples/netgraph/TimeCostDataFile_640-27-24.txt --ct 640 --nnode 27 --ncore 24"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf640.APHiD --tsize 640 -n ../examples/netgraph/TimeCostDataFile_640-27-24.txt --ct 640 --nnode 27 --ncore 24
		:;;

	#caculate 20croes
	(128-20)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf128.APHiD --tsize 128 -n ../examples/netgraph/TimeCostDataFile_128-7-20.txt --ct 128 --nnode 7 --ncore 20"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf128.APHiD --tsize 128 -n ../examples/netgraph/TimeCostDataFile_128-7-20.txt --ct 128 --nnode 7 --ncore 20
		:;;
	(240-20)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf240.APHiD --tsize 240 -n ../examples/netgraph/TimeCostDataFile_240-12-20.txt --ct 240 --nnode 12 --ncore 20"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf240.APHiD --tsize 240 -n ../examples/netgraph/TimeCostDataFile_240-12-20.txt --ct 240 --nnode 12 --ncore 20
		:;;
	(256-20)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf256.APHiD --tsize 256 -n ../examples/netgraph/TimeCostDataFile_256-13-20.txt --ct 256 --nnode 13 --ncore 20"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf256.APHiD --tsize 256 -n ../examples/netgraph/TimeCostDataFile_256-13-20.txt --ct 256 --nnode 13 --ncore 20
		:;;
	(320-20)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf320.APHiD --tsize 320 -n ../examples/netgraph/TimeCostDataFile_320-16-20.txt --ct 320 --nnode 16 --ncore 20"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf320.APHiD --tsize 320 -n ../examples/netgraph/TimeCostDataFile_320-16-20.txt --ct 320 --nnode 16 --ncore 20
		:;;
	(480-20)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf480.APHiD --tsize 480 -n ../examples/netgraph/TimeCostDataFile_480-24-20.txt --ct 480 --nnode 24 --ncore 20"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf480.APHiD --tsize 480 -n ../examples/netgraph/TimeCostDataFile_480-24-20.txt --ct 480 --nnode 24 --ncore 20
		:;;
	(512-20)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf512.APHiD --tsize 512 -n ../examples/netgraph/TimeCostDataFile_512-26-20.txt --ct 512 --nnode 26 --ncore 20"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf512.APHiD --tsize 512 -n ../examples/netgraph/TimeCostDataFile_512-26-20.txt --ct 512 --nnode 26 --ncore 20
		:;;
	(640-20)
		echo "python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf640.APHiD --tsize 640 -n ../examples/netgraph/TimeCostDataFile_640-32-20.txt --ct 640 --nnode 32 --ncore 20"
		python ./ParMapper.py -t ../examples/taskgraph/CloverLeaf640.APHiD --tsize 640 -n ../examples/netgraph/TimeCostDataFile_640-32-20.txt --ct 640 --nnode 32 --ncore 20
		:;;
esac
