#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

timeout 10 ros2 run mypkg mem_usage_publisher > /tmp/mypkg.log
cat /tmp/mypkg.log | grep '使用メモリ:'
