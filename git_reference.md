# Git

**Git** is an open source standard version control system. It is used for collaborative work on a repository, or code base.

A repo is like a folder that is shared with a remote server (Github is a common git server).

## Basic Process

A user can `clone` a repo, which means downloading a copy of it to their device.
- Clone this repo by using the following line in powershell:
- `git clone https://github.com/bvs7/Learn_Python.git`
- **When you clone a repo, a new folder will be created to contain it! Make sure your powershell has been navigated to a good place for this folder**
- After cloning the repo use `cd Learn_Python` to navigate the terminal to that repo.
- Then use `git status` to check that the repo has been cloned correctly.

Once there, you can make changes to the repo.

These changes are collected by the `git add` command.

Once changes are added, `git commit` is used to "commit" or confirm the changes.

To share these changes with the server repository, you can `git push` your commits to the server (usually called origin)

To get changes that others have made, you can use `git pull` to pull the commits from the server to your local repository

These commands can be performed from "git bash" a shell program (like command prompt) that should be navigated to the repo directory.

## Process Overview:

1) `git pull` - When you start working, use `git pull` to pull any changes made while you weren't here. The files in your repo will update with all new changes.
2) Make your changes
3) `git status` - Use this command to see what files you've changed
4) `git add [filename]` or `git add -A` - Add your changes with `git add` providing a filename adds a specific file, using -A adds all files that have changed
5) `git commit -m "[message]"` - Save the added changes as a commit. The message portion is a brief sentence to describe what the commit changed. For example: `git commit -m "Add git_reference.md for teaching git"`. You can also simply use `git commit`, which will open a text editor for you to enter the commit message. The commit finished when you save the commit message, then close the text editor
6) `git push` - Once you have finished making commits, use this command to push all of the changes you've made to the remote server repository. Once you've pushed, others can pull those changes into their repo.

## Merging

Say you forget to push or somebody else makes changes to the repo while you have commits that you haven't pushed on your local device. You will not be able to push your commits, and you will get an error message in the terminal when you try to do so. To fix this, you have to use `git pull` and merge your commits. When merging commits, any time two changes are made in the same place, you will have to resolve these changes, and choose which change is used. Once you have resolved all changes, you can use `git commit` to commit this merge, then `git push` to push your commits, which have been merged to commits you pulled.

## Best Practices

Good Practices when programming in a repo include the following:
- Make small commits: If your commit doesn't change much, it is easier to follow the code development.
- Commit often: This helps keep your commits managable, and lets your commits follow your workflow.
- Push working code: Usually, its best to have your code working before you push it. Otherwise you might cause problems for anyone who pulls the repo.
- Keep commits on focus: Try to keep the changes in each commit focused around a certain process

## Git Process Flow Chart

1) Open git bash to the appropriate directory (The directory called Learn_Python that was cloned)