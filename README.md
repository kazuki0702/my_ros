# 2019 ロボットシステム学課題２
#　システム概要
入力された数字をヤードとして認識しメートルに変換する
フィートで入力された数字をパブリッシュして、それをサブスクライブしてメートルに変換するパッケージ
#手法
#インストール手順
$ cd ~/catkin_ws/src/
$ https://github.com/Takeshi-Kojima/My_ROS.git
$ cd ../
$ catkin_make
#実行方法
端末１
$ roscore
端末２
$ rosrun My_ROS pub_yard.py
端末３
$ rosrun My_ROS sub_yard.py
