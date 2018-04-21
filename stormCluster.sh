#!/bin/bash

source "/home/huawei2/.profile"

if [ "$1" == "start-nimbus" ]
then
	zkServer start >/dev/null &
	storm nimbus >/dev/null &
	storm ui >/dev/null &
fi

if [ "$1" == "start-supervisor" ]
then
	zkServer start >/dev/null &
	storm supervisor >/dev/null &
fi

if [ "$1" == "stop-nimbus" ]
then
	kill -9 "$(jps | grep 'nimbus' | awk '{print $1}')"
	kill -9 $(jps | grep 'core' | awk '{print $1}')
	zkServer stop
	#sudo rm -rf $(cd "$ZOOKEEPER/data"; ls | grep "version" | xargs realpath )

	if [ "$2" == "clean" ]
	then
		sudo rm -rf "/CNN"
		sudo rm -rf "$STORM/data/nimbus/indox"
		echo  "$STORM/data/nimbus/indox"
	fi
fi

if [ "$1" == "stop-supervisor" ]
then
	kill -9 $(jps | grep 'Supervisor' | awk '{print $1}')
	zkServer stop
	#sudo rm -rf $(cd "$ZOOKEEPER/data"; ls | grep "version" | xargs realpath )

	if [ "$2" == "clean" ]
	then
		sudo rm -rf "/CNN"
		sudo rm -rf "$STORM/data"
		sudo rm -rf "$STORM/logs"
	fi
fi
