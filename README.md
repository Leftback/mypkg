## mypkg
ロボットシステム学課題２のリポジトリ

# メモリの使用量
## 概要
これはROS2のパッケージで,システムの使用メモリ量を毎秒パブリッシュするノード（mem_usage_publisher）を提供します。
## 使用方法
1.リポジトリをクローン
```
https://github.com/Leftback/mypkg
```
2.ワークスペースをセットアップ
```
mkdir -p ~/ros2_ws/src
```
```
cd ~/ros2_ws/src
```
```
ln -s /path/to/mypkg .
```
3.ビルド
```
cd ~/ros2_ws
```
```
colcon build
```
4.環境設定
```
source install/setup.bash
```
5.パブリッシャーノードの起動
```
ros2 run mypkg mem_usage_publisher
```


## 実行例

# 環境
## 必要なソフトウェア

## テスト環境

## ライセンス


