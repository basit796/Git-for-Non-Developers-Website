// Git knowledge base for embeddings
// This contains the content that will be used to provide context to the agent

const gitKnowledge = [
    {
        id: 1,
        topic: "What is Git",
        content: "Git is a distributed version control system that tracks changes in files and coordinates work among multiple people. It was created by Linus Torvalds in 2005. Git allows you to save snapshots of your project at different points in time, making it easy to review history and revert changes if needed. Think of it as a sophisticated 'undo' system for your projects."
    },
    {
        id: 2,
        topic: "Git Repository",
        content: "A Git repository (or 'repo') is a directory that contains your project files along with a special .git folder. The .git folder stores all the version history and metadata. You can create a repository using 'git init' command. A repository can be local (on your computer) or remote (on platforms like GitHub, GitLab, or Bitbucket)."
    },
    {
        id: 3,
        topic: "Git Commit",
        content: "A commit is like taking a snapshot of your project at a specific moment. When you commit, you save the current state of your files along with a message describing what changed. Each commit has a unique identifier (SHA hash). To create a commit, you first stage your changes with 'git add', then commit with 'git commit -m \"your message\"'. Good commit messages are clear and describe what was changed and why."
    },
    {
        id: 4,
        topic: "Git Branch",
        content: "A branch in Git is like a parallel universe for your code. It allows you to work on new features or fixes without affecting the main codebase. The default branch is usually called 'main' or 'master'. You can create a new branch with 'git branch branch-name' and switch to it with 'git checkout branch-name'. Branches are lightweight and switching between them is fast."
    },
    {
        id: 5,
        topic: "Git Merge",
        content: "Merging is the process of combining changes from one branch into another. For example, after finishing a feature on a separate branch, you merge it back into the main branch. Use 'git merge branch-name' to merge. Sometimes, if the same part of a file was changed differently in both branches, you'll get a merge conflict that needs to be resolved manually."
    },
    {
        id: 6,
        topic: "Git Clone",
        content: "Cloning creates a complete copy of a remote repository on your local machine. Use 'git clone [url]' to clone a repository. This downloads all files, history, and branches. It's the typical way to start working on an existing project. After cloning, you have a full-featured local repository that can work independently."
    },
    {
        id: 7,
        topic: "Git Pull and Push",
        content: "Git pull downloads changes from a remote repository and merges them into your local branch. Use 'git pull' to update your local code. Git push uploads your local commits to a remote repository. Use 'git push' to share your changes with others. Always pull before pushing to avoid conflicts."
    },
    {
        id: 8,
        topic: "Staging Area",
        content: "The staging area (also called index) is like a preparation area for your next commit. You add changes to the staging area with 'git add'. This allows you to carefully choose which changes to include in your next commit. You can stage specific files, all files, or even specific parts of files. Check what's staged with 'git status'."
    },
    {
        id: 9,
        topic: "Git Status",
        content: "The 'git status' command shows the current state of your working directory and staging area. It tells you which files are modified, which are staged for commit, and which are untracked. It's one of the most commonly used Git commands and helps you understand what's happening in your repository."
    },
    {
        id: 10,
        topic: "Git Diff",
        content: "The 'git diff' command shows the differences between various commits, branches, or your working directory and staging area. Use 'git diff' to see unstaged changes, 'git diff --staged' to see staged changes, and 'git diff branch1 branch2' to compare branches. It's useful for reviewing changes before committing."
    },
    {
        id: 11,
        topic: "Git Log",
        content: "The 'git log' command displays the commit history of your repository. It shows commit hashes, authors, dates, and commit messages. Use 'git log --oneline' for a compact view, 'git log --graph' for a visual representation of branches, and 'git log -n 5' to show only the last 5 commits."
    },
    {
        id: 12,
        topic: "Git Remote",
        content: "A remote is a version of your repository hosted on the internet or network. The most common remote is called 'origin'. Use 'git remote -v' to list remotes, 'git remote add name url' to add a new remote, and 'git remote remove name' to remove one. Remotes enable collaboration with others."
    },
    {
        id: 13,
        topic: "Git Reset",
        content: "Git reset allows you to undo changes. 'git reset --soft' moves HEAD but keeps changes staged. 'git reset --mixed' (default) unstages changes but keeps them in working directory. 'git reset --hard' discards all changes (be careful!). You can reset to a specific commit with 'git reset commit-hash'."
    },
    {
        id: 14,
        topic: "Git Stash",
        content: "Git stash temporarily saves uncommitted changes so you can work on something else. Use 'git stash' to save changes, 'git stash pop' to reapply them, and 'git stash list' to see all stashes. It's useful when you need to quickly switch branches but aren't ready to commit your current work."
    },
    {
        id: 15,
        topic: "Git Ignore",
        content: "The .gitignore file specifies which files Git should ignore. Common examples include build artifacts, dependencies (node_modules), and sensitive information. Each line in .gitignore is a pattern. For example, '*.log' ignores all log files, and 'node_modules/' ignores the node_modules directory. Create this file in your repository root."
    }
];

module.exports = gitKnowledge;
