# 版本控制 Git

代码管理工具，管理代码的版本迭代；多人协作工具。Git是一个分布式版本控制系统：每一台电脑都是一个服务器，每个用户都存在两个空间（仓库、用户代码区），代码交互是仓库与仓库之间的操作。

学习资料（book）：<https://git-scm.com/book/zh/v2>

## 代码托管仓库（GitHub、开源中国码云）

获取仓库：

- git init
- git clone 地址

## 仓库托管GitHub

1.登录GitHub官网<https://github.com

2.创建仓库：

![](.\image\创建仓库1.png)

3.填写仓库信息：

![](.\image\创建仓库2.png)

4.仓库基本情况

![](.\仓库基本情况.png)

在上面中，可以在clone or download下面复制链接，然后用git clone 地址 进行下载。

## 在pycharm中使用Git

用pycharm打开刚才clone的项目，显示如下：

![](.\image\pycharm git-1563204700117.png)

然后点击file-settings-verson control-github,然后点击登录

![](.\image\settings.png)

点击确定后，默认显示的都是黑色的颜色：

![](.\image\heise.png)

### 文件标识：

- 红色文件，代表未添加到版本控制中的文件
- 绿色文件，代表添加到版本控制中的文件，文件还未提交
- 蓝色文件，代表已经在版本控制中的文件发生了修改。

把文件添加到版本控制中

![](.\image\add.png)

提交文件到本地仓库

![1563205892221](.\image\commit.png)

将本地仓库与服务器仓库进行提交push，从远端服务器中获取pull

![](.\image\commit2.png)

这时，远端服务器就提交成功了。

### 忽略文件

注意：在项目中，有一个.gitignore文件，这个是忽略文件，里面填写的是忽视哪些文件，若用的是pycharm，则会在项目根目录创建一个.idea文件夹，这个是千万不能上传的（特别是团队协作时），所以要在忽略文件中添加进去。

![](.\image\忽略文件.png)

## 代码冲突

多个人同时修改相同文件，代码出现冲突后，用merger合并，要查看逻辑和变更的代码。

## 指令

- git status 查看当前工作状态,要在存在项目的根目录下操作

- git pull 更新，强制更新

- git push 推送代码到远端服务器，使用
- - git push origin（远端） master(分支)
  - git push set-upstream origin 分支名 将本地分支推送到远端，并建立关联

- git add 针对新文件、一存在的文件的修改，添加版本控制
- git add -A 添加所有变更的文件
- git commit 提交代码到本地仓库，需要添加描述信息
- git commit -m "描述信息"
- git log 查看提交历史
- git reset --hard versionid  强制还原，重置一个版本追踪记录，后面添加commit的ID（可以通过git log获取）

- git branch 分支操作（默认为master）
  - git branch -a 查看所有分支
  - git branch -b 分支名 创建一个新的分支

- git chechout 
- - git checkout 分支名  切换到指定分支
  - git checkout -b 分支名  创建并切换到指定分支

- git merge  分支名  合并分支到当前分支中，强制合并，会直接产生冲突，需要所有的冲突一次性解决。

- git fech（先将代码从服务器下载到本地的远端服务器映像中） + git merge = git pull（直接下载并合并）
- git rebase 分支名  交互式合并，功能和merge一样，如果合并冲突，需要解决，解决完成git rebase --continue，如果还有冲突，需要继续解决，git rebase --continue。
- git rebase --skip 当前问题全部解决完成，跳出这个区域
- git rebase --abort 合并出现冲突，不想继续解决，终止合并，代码还原。

在工作中最好使用git fech+git rebase

- git stash 代码的暂存，暂存时候可以执行分支，而不用commit
- git stash pop  切换回来，代码还在暂存区，想要获取，则用这个方式
- git stash drop 删除暂存



# SSH和HTTPS连接

https连接每次提交代码都会输入用户名和密码，但是通过ssh方式则不会，但是需要配置。

1.生成公钥和私钥，打开 Git Bash 终端，输入：

![](.\image\ssh2.png)

执行后在C:\Users\Administrator\.ssh文件夹下就生成了公钥和私钥。将公钥id_rsa.pub文件中的内容粘贴到GitHub中。

2.在GitHub中的setting中，找到SSH and GPG keys选项，将公钥的内容粘贴进去即可。

![](.\image\ssh1.png)

3.使用：如果有需要下载的，直接点击ssh链接即可，而不使用HTTPS方式。

![](.\image\ssh3.png)

