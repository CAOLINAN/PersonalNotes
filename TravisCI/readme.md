# [Travis CI](https://travis-ci.org/)简介

Travis CI是一个自动化测试和部署代码的工具。提供的是持续集成服务(Continuous Integration，简称 CI),绑定到github上面的项目，只要有新代码就自动抓取。提供测试环境，执行测试，完成构建，还能部署到服务器中。

# 需求

1、github账户
2、github项目
3、项目中包含可运行的代码
4、项目包含构建测试脚本

# 内网版本
	
私有项目用 Gitlab ，持续化用 Jenkins，Drone CI或者Gitlab CI

# .travis.yml

Travis 要求项目的根目录下面，必须有一个.travis.yml文件。这是配置文件，指定了 Travis 的行为。该文件必须保存在 Github 仓库里面，一旦代码仓库有新的 Commit，Travis 就会去找这个文件，执行里面的命令。

文件采用 YAML 格式

