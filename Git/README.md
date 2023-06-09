<div>
<h1 align="center"; style="font-size:30px">
  <br>
  <a href="https://hpai.bsc.es/"> 
      <img src="../Images/Logos/Git-Icon-1788C.png" alt="UB Logo" width="25%">
</a>

<h1 align = "center">
    Git 👥📤
</h1>

<h2 align="center">
  Marc Herranz i Alié
</h2>

<br></br>

</div>

## 🧪 What is Git ?

---

Git is a version control system used for software development and other types of projects created in 2005. In plain words, Git allows multiple developers to work on the same code independently and keep track of changes made to it over time. This tool is widely used in the software development industry and has become essential for developers. It provides a way for teams to collaborate on code, keep track of changes, and maintain a history of a project's development.
<br>
By means of a system of commits, it can track changes to the repository, which is a collection of files and folders that make up the project. A commit is a snapshot of the repository at a specific point in time. Developers can create new commits to record changes they have made to the code.
<br>
Git also allows developers to create branches, which are separate lines of development that can be merged back into the main project when they are complete.
(Mouat, pg 3)

<br>

<p align = "center">
  <img src="../Images/pics/docker-vm-architecture.png" alt="VM vs Containerized Architecture" width="400">
  <p align = "center">
    <i>VM vs Containerized Architecture</i>
  </p>  
</p>

(How can be Git used) -> Git Bash, Plug-ins in IDEs, etc.

<br>

## 🧑🏼‍💻 What is the difference between Git and GitHub ?

---

Git and GitHub are related but distinct concepts. Git is a version control system, while GitHub is a web-based platform that provides hosting for Git repositories, as well as other collaboration tools for software development.

In other words, while Git is the tool used for version control of local repositories, GitHub is the web-based platform used for developers for sharing personal code, developing others code, or keeping track of changes in code in a more user-friendly interface.

With Git, you can track changes to files in their local repository, create new branches, and merge changes between branches. It is a distributed version control system, which means that developers can work on their own local copies of a repository and then merge their changes with other developers when they are ready.

GitHub, on the other hand, is a web-based platform that provides hosting for Git repositories. Developers can use GitHub to store their repositories online and collaborate with others on the same project. GitHub provides a number of features that make collaboration easier, such as pull requests, issue tracking, and code review tools. It is worth mentioning that to interact with GitHub repositories, you use Git commands like _git pull_ or _git push_.

<p align = "center">
  <img src="../Images/pics/git-github-relation.png" alt="GitHub and Git version" width="600">
  <p align = "center">
    <i>GitHub and Git version</i>
  </p>  
</p>

<br>

## 🏛 Basic commands

---

Given the multiple Git commands available along with their corresponding flags and options, it is recommended to refer to the [official documentation](https://git-scm.com/docs) for further clarification.

We can distinguish commands hinging on their scope. Some are used for snapshoting code and their changes (e.g. status, add, reset), other are usd for branching or merging (e.g. checkout, stash, switch), and some are for simple inspection and comparison (e.g. show, diff, log). Let's explore the basic functionalities of git commands by means of examples.

<br>

## _Setup and Config_

<br>

> ### git config

This command is used to configure several options that Git uses. One common use is done right before starting a project for setting the name and mail of the Git user. These configuration names are dot limited strings composed of a section (user, core, etc.) and a key (email, name, editor, etc.). These values can be displayed, modified, or even have their scope modified. In general, the command can be written in the following form:

```git
git config <level> <section.key> <value>
```

If the _\<value>_ is not set, it will simply display the current _<section.key>_ value. Regarding the most important sections and their corresponding names, these are user.name, user.email which are used to know who did what when commiting, branching, or merging code; core.editor that is used to set the editor for Git comments; color.ui, color.branch or color.diff to set the color of some git actions or commands; merge.tool; and alias.ci, among many other.

The main levels for config options are **--local** that is the default one and that is applied to the context repository that git config gets invoked in. These values are stored in the directory .git/config. Next level is **--global** that is user-specific so values are applied to an operating system user. Their values are stored in a user's home directory C:\Users\\.gitconfig on Windows. Finally, we have **--system**, which sets the values for different users in the same machine, and stored the values in C:\ProgramData\Git\config on Windows OS.

<p align = "center">
  <img src="./pic/1.png" alt="git config section.key values" width="550">
  <p align = "center">
    <i>git config section.key values</i>
  </p>  
</p>

<br>

> ### git config

This command is used to configure several options that Git uses. One common use is done right before starting a project for setting the name and mail of the Git user. These configuration names are dot limited strings composed of a section (user, core, etc.) and a key (email, name, editor, etc.). These values can be displayed, modified, or even have their scope modified. In general, the command can be written in the following form:

```git
git config <level> <section.key> <value>
```

If the _\<value>_ is not set, it will simply display the current _<section.key>_ value. Regarding the most important sections and their corresponding names, these are user.name, user.email which are used to know who did what when commiting, branching, or merging code; core.editor that is used to set the editor for Git comments; color.ui, color.branch or color.diff to set the color of some git actions or commands; merge.tool; and alias.ci, among many other.

The main levels for config options are **--local** that is the default one and that is applied to the context repository that git config gets invoked in. These values are stored in the directory .git/config. Next level is **--global** that is user-specific so values are applied to an operating system user. Their values are stored in a user's home directory C:\Users\\.gitconfig on Windows. Finally, we have **--system**, which sets the values for different users in the same machine, and stored the values in C:\ProgramData\Git\config on Windows OS.

<p align = "center">
  <img src="./pic/1.png" alt="git config section.key values" width="550">
  <p align = "center">
    <i>git config section.key values</i>
  </p>  
</p>




> git init, git add . , git commit -a, git commit -m, git pull, git push, git checkout, git
> branch, git cherry-pick, git fetch, git stash push, git stash pop, git revert, git reset, git clone, git diff, git log, git status, git reset, git merge, git remote,

- <ins>Flexibility:</ins> Easy to manage and scale applications, allowing you to quickly spin up new instances of your containers and distribute them across multiple hosts.

<br>

## 📗 Bibliography

---

- Mouat, A. _Using Docker: Developing and Deploying Software with Containers_. (1st ed.). O'Reilly, 2015

<br>

## 🎓 License

---

This repository and thereby all its content is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<br>

## Further Issues and questions ❓

---

If you have issues or questions, don't hesitate to contact Marc Herranz i Alié at [mherranz98@gmail.com](mailto:mherranz98@gmail.com).
