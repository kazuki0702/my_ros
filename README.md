# 2019 ロボットシステム学課題２
# システム概要
入力されたヤードの値をメートルに変換するパッケージ  
入力されたヤード値をrostopicとしてパブリッシュして、それをサブスクライブしてメートルに変換する
# 手法
# インストール手順
```
$ cd ~/catkin_ws/src/
$ https://github.com/kazuki0702/my_ros.git
$ cd ../
$ catkin_make
```    
# 実行
端末１  
`$ roscore`  
端末２  
`$ rosrun my_ros pub_yard.py`  
端末３  
`$ rosrun my_ros sub_yard.py`
## YouTube
https://youtu.be/ogLRQPR76P0
## LICENSE  
This repository is licensed under the BSD-3-Clause license, see LICENSE.
## 一緒にやった人
* 小関　隆　https://github.com/KosekiTakashi  
* 木村　慧士　https://github.com/kimurasatoshi  
* 小島　健　https://github.com/Takeshi-Kojima  

