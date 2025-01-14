#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

timeout 15 ros2 run mypkg mem_usage_publisher > /tmp/mypkg.log 2>&1
grep '使用メモリ:' /tmp/mypkg.log

