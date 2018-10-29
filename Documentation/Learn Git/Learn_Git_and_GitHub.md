# Learn Git and GitHub Basics

> So you want to Learn Git and GitHub? Awesome! Git is a very verbose method of version control and makes sharing projects between small teams a breeze. 

## What is Git 

Git is an implementation of Version control. Version control is the task of keeping a software system consisting of many versions and configurations well organized. 

[You can find it and download it for free here](https://git-scm.com/)

### What Can I do with Git?
With Git you can
- Make commits, which are short messages documenting milestones in software development. 
- Pull a repository (project folder) from a remote location like GitHub.
- Push a repository with the commits you have made to a remote location.

### What kind of files can I use Git with?
You can use Git with any kind of files that have lines. This includes .txt, .py, .c, .md and many, many more. It is noted that many common file types are not supported like .pdf or .docx. Git can recognize if they are there but can't track changes line by line.

### How do I use git?
Whenever and however you use Git you should follow these steps:

- Git Pull: Pull the latest version from remote from the server. In our case the server is GitHub.
- Git Add (Command Line Only): Add the files for a commit. The GitHub desktop app can do this automatically.
- Git Commit: Log the changes and optionally leave a message of what was changed
- Git Push: Send the changes to remote with the commit messages. 

For Example via the Command Line:

- `git pull https://github.com/RIT-Space-Exploration/Rovers` 

- *** some changes ***

- `git add -A` - Add all the files that were changed. You can specify specific files instead of `-A` if necessary

- `git commit` - Makes a commit. It will open up vi to make the changes just hit `i`, type the changes, an then `:wq` to write them and quit. 

- `git push` - pushes the changes to remote.

All of this can be done in the GitGUI or GitHub Desktop App via buttons.

### What do I use Git with?
Many programming applications have Git built in. There are some tools to make using Git easier. They include Git GUI, GitHub Desktop App (Highly recommended if you are using GitHub) and of course; the command line. 

- [GitHub Desktop App](https://desktop.github.com/) - makes cloning GitHub repositories, making commits and pushing changes super easy!
- [Git Bash](https://git-scm.com/) - Git through the command line. It comes with Git when you install it for windows. It allows you to use Unix commands on Windows. Linux and Mac users won't have this issue. I *highly recommend* windows users add Git Bash to their path when installing. This allows you to right click anywhere and open a terminal window there instead of navigating from root.

### That's it?
Well, not exactly. Git is a whole lot more powerful than that. There are many more commands like clone, rm (remove), merge, init, diff and many, *many* more. You can (*and should!*) read all about those [here](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html).

## What is GitHub
GitHub is a web-based hosting service for version control using Git. You're going to need at GitHub accounts. GitHub accounts are free but you should definitely get the student pack for unlimited repository space while you're at it. 

[GitHub Education Link](https://education.github.com/pack)


## SPEX & GitHub
If you want to join the SPEX GitHub send your GitHub account to your project lead. 
[RIT SPEX GitHub](https://github.com/RIT-Space-Exploration/)

### What Are Branches
Sometime there are different paths for a project that will meet up later. To keep these changes separate we use branches. This is also very useful for isolating different versions of software that are in testing before committing to the master branch (the original). 

### Should I Just Commit My Changes To Master?

# **NO!** 

For any non-trivial task, a feature branch should be created. A feature branch will track the changes to a project specific to one feature. Once it has been verified and tested it can then be merged back onto master. 

# Bibliography

Repository: The folder, files, and any subsequent folders or files for a project. 

Commit: records changes to the repository via the changes in line data. 

Version Control: task of keeping a software system consisting of many versions and configurations well organized

Git: implementation of Version control

GitHub: web-based hosting service for version control using Git

Branch: A branch is a parallel version of a repository. It is contained within the repository, but does not affect the primary or master branch allowing you to work freely without disrupting the "live" version.

# Other Resources

[Git](https://git-scm.com/)
[Git Commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html)
[GitHub Help](https://help.github.com/)
[GitHub Education Link](https://education.github.com/pack)
