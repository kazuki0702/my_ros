# 2019 ロボットシステム学課題２
# システム概要
入力されたヤードの値をメートルに変換するパッケージ  
入力されたヤード値をrostopicとしてパブリッシュして、それをサブスクライブしてメートルに変換する
# 手法
# インストール手順
```
$ cd ~/catkin_ws/src/
$ https://github.com/yoshimura/My_ROS.git
$ cd ../
$ catkin_make
```    
# 実行
端末１  
`$ roscore`  
端末２  
`$ rosrun My_ROS pub_yard.py`  
端末３  
`$ rosrun My_ROS sub_yard.py`
## YouTube
https://youtu.be/ogLRQPR76P0
## LICENSE  
This repository is licensed under the GPLv3 license, see LICENSE.
