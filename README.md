# leetcode_mysolution


# 记录在另一台电脑上同步并新建代码测试版本过程、(可以见Typora_Record仓库，更为实用)

## 前言

在Git中，分支（Branch）是用于并行开发和管理不同版本代码的关键功能。通过分支，你可以在同一项目中同时处理多个版本或特性开发，而不会干扰主分支上的稳定代码。

### 示例操作流程

假设你在B电脑上进行如下操作：

1. **创建一个新分支**：

   ```
   git checkout -b feature-x
   ```

2. **在`feature-x`分支上进行代码修改**：

   对代码进行修改后，添加并提交更改：

   ```
   git commit -m "Implement feature-x"
   ```

3. **推送`feature-x`分支到远程仓库**：

   ```
   git push origin feature-x
   ```

4. **切换回主分支**：

   ```
   git checkout main
   ```

5. **将`feature-x`分支合并到主分支**：

   ```
   git merge feature-x
   ```

6. **推送合并后的主分支到远程仓库**：

   ```
   git push origin main
   ```

## 使用Vs code & Git hub 

### 先下载 Git

- `git config --global user.name "你的名字"`
  `git config --global user.email "你的邮箱"`

  配置全局信息这样在提交新版本代码时能辨认出是谁提交的 

   - 然后是

     `ssh-keygen -t rsa -C "1790584259@qq.com"`

     生成ssh密钥

     在c盘中找到相关文件"C:\Users\yubin\.ssh\id_rsa.pub"  **记得打开文件扩展名显示与隐藏文件可见**

     全选在github上添加ssh公共密钥

   - 同时在c盘该文件夹新建一个没有后缀的config文件

     `Host github.com
     HostName ssh.github.com  
     User git
     Port 443
     PreferredAuthentications publickey
     IdentityFile ~/.ssh/id_rsa`

### 然后拷贝A电脑上已经上传了的代码

- 在想要拷贝的文件夹中直接输入cmd（省略cd）
- 或者在vscode中直接在该文件夹处新建一个终端然后git clone "复制的ssh地址"

### (可选) 克隆好了就新建一个.gitignore用于忽略不想要追踪的文件夹

- 例子

   `\# 为了在github上管理我的solution`

  `Assets/`

  `Contents/`

  `Solutions/`

  `Templates/`

  `README.md`

  `LICENSE`  

  `\# 修改后也需要 git add git commit`

### 远程仓库

1. **远程仓库（Remote Repository）**：一个存储在服务器上的Git仓库，通常用来与本地仓库进行同步。
2. **本地仓库（Local Repository）**：开发者在自己电脑上使用的Git仓库。
3. **克隆（Clone）**：从远程仓库复制整个仓库到本地。执行此操作的命令是`git clone`。
4. **推送（Push）**：将本地仓库的更改上传到远程仓库。执行此操作的命令是`git push`。
5. **拉取（Pull）**：从远程仓库获取最新的更改并合并到本地仓库。执行此操作的命令是`git pull`。
6. **获取（Fetch）**：从远程仓库获取最新的更改，但不自动合并到本地分支。执行此操作的命令是`git fetch`。

### 连接远程仓库

#### 步骤 1: 确认是否已添加远程仓库

首先，检查当前的远程仓库配置：

```
git remote -v
```

如果没有任何输出，表示远程仓库尚未配置。如果输出中没有 `origin`，或者URL不正确，需要重新配置远程仓库。

#### 步骤 2: 添加或修改远程仓库

假设你的GitHub仓库URL是 `git@github.com:yourusername/your-repo.git`，请按以下步骤操作：

1. **添加远程仓库**

   ```
   git remote add origin git@github.com:yourusername/your-repo.git
   ```

2. **修改远程仓库URL（如果已经存在但URL错误）**

   ```
   git remote set-url origin git@github.com:yourusername/your-repo.git
   ```

#### 步骤 3: 确认远程仓库配置

再次检查远程仓库配置：

```
git remote -v
```

你应该看到如下输出：

```
origin  git@github.com:yourusername/your-repo.git (fetch)
origin  git@github.com:yourusername/your-repo.git (push)
```

#### 步骤 4: 确保你有正确的访问权限

确认你已经在GitHub上设置了SSH密钥，并且添加了正确的SSH密钥到GitHub账户。你可以使用以下命令测试连接：

```
ssh -T git@github.com
```

如果连接成功，你会看到一条欢迎信息。如果连接失败，请确保你在GitHub上添加了正确的SSH公钥。

#### 步骤 5: 推送本地分支到远程仓库

确保你在本地的分支是你希望推送的分支（例如 `main`），然后运行以下命令推送：

```
 git push -u origin main
```

### 后续操作

已经在GitHub上创建了一个仓库，并希望将本地项目推送到远程仓库，以下是完整的操作流程：

1. **初始化本地仓库（如果还没有）**：

   ```
   git init
   ```

2. **添加所有文件到暂存区**：

   ```
   git add .
   ```

3. **提交更改**：

   ```
   git commit -m "Initial commit"
   ```

4. **添加远程仓库**：

   ```
   git remote add origin git@github.com:yourusername/your-repo.git
   ```

5. **推送更改到远程仓库**：

   ```python
   git push -u origin main
   ```

### 后续

[这是本次实验的库](https://github.com/chunyangW/leetcode_mysolution)

