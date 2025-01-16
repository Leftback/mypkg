#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash

# ログファイルを別途保存
LOGFILE=/tmp/mypkg.log
timeout 15 ros2 run mypkg mem_usage_publisher > $LOGFILE 2>&1

# 結果を出力
cat $LOGFILE
grep '使用メモリ:' $LOGFILE || exit 1

