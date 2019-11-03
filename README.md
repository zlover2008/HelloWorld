# HelloWorld
A new repository.
I'm practicing the branch, I create a readme-edit branch, and watch how it works.

只需要进行下面几步就能把本地项目上传到Github

1、在本地创建一个版本库（即文件夹），通过git init把它变成Git仓库；
2、把项目复制到这个文件夹里面，再通过git add .把项目添加到仓库；
3、再通过git commit -m "注释内容"把项目提交到仓库；
4、在Github上设置好SSH密钥后，新建一个远程仓库，通过git remote add origin https://github.com/guyibang/TEST2.git将本地仓库和远程仓库进行关联；
5、最后通过git push -u origin master把本地仓库的项目推送到远程仓库（也就是Github）上；（若新建远程仓库的时候自动创建了README文件会报错，解决办法看上面）。

一定要注意,如果你在创建github仓库时，初始化了一个readme.md文件,远程仓库不是空的，则需要先将远程仓库与本地仓库同步,使用命令:git pull --rebase origin master.将远程文件拉回本地仓库,然后再执行:git push origin master,就能成功了.

原文链接：https://blog.csdn.net/vir_lee/article/details/80464408
