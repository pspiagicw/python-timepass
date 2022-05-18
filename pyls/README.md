Welcome to my first post.
Today we will make a simple project.
We will make a ls clone in python.
If you don't know what is ls.
Just google it.If you are on windows 
the similar command is dir.
We are naming it pyls


## Approach

I will not give the code in anyway in this article.
If you get stuck for an hour or longer.
Then just skim through my code.


## Introduction

This project is aimed at python beginners but anyone programming language can be used.
Just a little work is required to find alternative to the modules and packages.

## Prerequisite

You should know basic python and comfortable using modules.
We will also use basic git in this project.
You should also know how to create a python project as a directory layout.
You if you don't know any of them.Just search for them right here in DEVTO.
My recommendation is Dead Simple Python Lesson 1 which how to layout your project.

## Getting Started

Start by making a directory for you project.Then create a git repository inside it.This is optional
but for a more professional feel.We would be adding features in form of git branches and merging them.
If you are not comfortable with it,No Problem you can still follow just skip all the git stuff.

## Main Course

After you make a directory structure you create a main python file.
For the first step we will just print the contents of current directory.
For a hint you can use os.listdir for it.If you want more documentation google it.

If you can print the contents of current directory then let's make a git commit out of it.
Make a git commit and give a message like 'initial-commit'.
Moving forward let's add a feature in our program.


Create a git branch called hidden-files.If you didn't understand from the name we are adding support for hidden files.
For now just make it ignore hidden files.
If you don't know what are hidden files.They are file which have name starting with a '.'.

If it works then merge the branch with the master branch.

Let's add support for commandline arguments.This is done by the argparse module in python.
Make separate file for parsing the arguments.For now we will only support directory name.
Again for the same create a separate branch or it.

I should explain this point.What I mean by directory name.With that I mean that when 'pyls' is run without any arguments.
Then it should print current directory's contents.But when given given a directory name which is in the current directory.
It should print that directory's contents.

If it works then again merge the branch with the master branch.
One thing I would like to touch is the use of docstrings in each and every function.
This is a very weird thing to do.But I am trying to write good code and thus I am following it too.

The next idea I think we should tacke is the '--all' argument which prints the hidden files too.
Again for this we should create a separate branch and thus merge after working.

The above point is quite easy.

But the next idea is not so easy.
We are going to build the '--long' argument which means we have to get stats of each and every file.
This stats include read/write/execute permissions and even last-modified-date.

Again use git branches.

This was a big one.For a hint you can work with os.path and os.stat along with stat module for getting information about the file)
I think this is enough for using on a daily basis.

## Extensions
If you are up to the task.You can write multiple extensions to pyls

 - Color support: You can have color support for pyls.
 - More Options: Just look at man ls and try to implement things that you think you can do.
 - Recursive: This is one which requires recursion which is a little higher concept for beginners.(Just Google It)
Think of more extensions and implement them.
Give your feedback and give your opinions on my writing.You feedback is appreciated.
Send me your code and we will discuss them.
Send me ideas for future posts share links to such posts on the internet.








