<!-- 04_branching_parallel_universes.md -->

# Chapter 4: Branching: Parallel Universes

## The Fear of Experimentation

Imagine you're writing a novel. You've drafted ten chapters, and they're good—really good. But you have an idea for a radical restructuring that might make the story even better. It would require rewriting several chapters, changing the narrative perspective, and altering the ending. It could be brilliant. Or it could be a disaster.

What do you do?

Without version control, you'd probably save a copy: "Novel_BACKUP_before_big_changes.docx." Then you'd start editing the original, heart pounding, hoping you're making the right choice. If it doesn't work, you'll have to manually compare the backup with your changes and try to piece together a hybrid version. It's risky, scary, and stressful.

With Git, you simply create a branch.

A branch is a parallel version of your project where you can experiment freely. Make radical changes. Try wild ideas. If it works, great—merge it back into the main version. If it doesn't, simply delete the branch. The original is completely untouched. No backup files needed. No stress.

This chapter will teach you to think in branches, and once you do, you'll approach your work with a newfound freedom. The fear of permanent mistakes evaporates. Experimentation becomes safe.

## What Is a Branch?

In Git, a branch is a movable pointer to a commit. That's it. It's not a copy of your files (that would waste space). It's just a lightweight reference that says, "This is where I am in the history."

By default, when you create a repository, you start on a branch called `main` (or `master` in older Git versions). Every commit you make advances the `main` branch pointer forward. Think of it like a bookmark that automatically moves as you add pages to a book.

When you create a new branch, you're creating a second bookmark. Now you have two pointers, and they can move independently. You can make commits on one branch without affecting the other. Later, you can merge the branches back together if you want.

### A Visual Example

Let's say you've made three commits on `main`:

```
A---B---C  (main)
```

Each letter represents a commit. `main` points to commit C, the most recent.

Now you create a new branch called `experiment`:

```
A---B---C  (main, experiment)
```

Both branches point to the same commit (C). They're identical at this moment.

You switch to the `experiment` branch and make two more commits:

```
A---B---C  (main)
         \
          D---E  (experiment)
```

Now `main` still points to C, but `experiment` has moved forward to E. The commits D and E exist only on the `experiment` branch. If you switch back to `main`, you won't see those commits—your files will look like they did at commit C.

This is parallel development. Two versions of your project coexisting, both rooted in the same history.

## Creating and Switching Branches

Let's make this concrete with our book club notes project from Chapter 3.

### Viewing Current Branches

First, check what branches exist:

```bash
git branch
```

You'll see:

```
* main
```

The asterisk indicates you're currently on the `main` branch. This is the only branch that exists right now.

### Creating a New Branch

Let's say you want to experiment with reorganizing your reading list. Create a new branch:

```bash
git branch reading-list-redesign
```

This creates a new branch called `reading-list-redesign` but doesn't switch to it yet. Check again:

```bash
git branch
```

Output:

```
* main
  reading-list-redesign
```

Two branches now exist, but you're still on `main` (indicated by the asterisk).

### Switching Branches

To work on the new branch, switch to it:

```bash
git checkout reading-list-redesign
```

Or, in newer Git versions, you can use the clearer command:

```bash
git switch reading-list-redesign
```

(Both commands do the same thing. Use whichever you prefer. I'll use `git switch` going forward as it's more intuitive.)

You'll see: `Switched to branch 'reading-list-redesign'`

Verify:

```bash
git branch
```

Output:

```
  main
* reading-list-redesign
```

You're now on the `reading-list-redesign` branch.

### The Shortcut: Create and Switch in One Command

Creating a branch and immediately switching to it is so common that Git provides a shortcut:

```bash
git switch -c new-branch-name
```

Or with the older command:

```bash
git checkout -b new-branch-name
```

The `-c` flag (or `-b` for checkout) means "create and switch."

## Working on a Branch

Now that you're on the `reading-list-redesign` branch, any commits you make will advance this branch, leaving `main` untouched.

### Making Changes

Open `reading-list.txt` and restructure it:

```
Book Club Reading List
======================

📚 COMPLETED READS
------------------
✓ "The Great Gatsby" by F. Scott Fitzgerald
  Date: January 2024
  Rating: 4.5/5
  Discussion Leader: Jennifer

📖 UPCOMING READS
------------------
→ "To Kill a Mockingbird" by Harper Lee
  Scheduled: February 2024
  Discussion Leader: Sarah
  
→ "1984" by George Orwell
  Scheduled: March 2024
  Discussion Leader: TBD

→ "Pride and Prejudice" by Jane Austen
  Scheduled: April 2024
  Discussion Leader: Mike

💡 SUGGESTED FOR FUTURE
------------------------
• "The Handmaid's Tale" by Margaret Atwood
• "Brave New World" by Aldous Huxley
• "The Catcher in the Rye" by J.D. Salinger
• "Beloved" by Toni Morrison
```

This is a more visual, organized format. Save the file.

### Committing on the Branch

Stage and commit as usual:

```bash
git add reading-list.txt
git commit -m "Redesign reading list with better visual organization"
```

You've now made a commit on the `reading-list-redesign` branch. This commit does not exist on `main`.

### Switching Back to Main

Switch back to `main`:

```bash
git switch main
```

Now open `reading-list.txt`. It looks exactly like it did before your redesign! The emojis, the new sections—all gone. This isn't a bug; it's the feature. You're on `main`, where that commit doesn't exist.

Check your commit history:

```bash
git log --oneline
```

You won't see the "Redesign reading list" commit. It's not on `main`.

Switch back to `reading-list-redesign`:

```bash
git switch reading-list-redesign
```

Open `reading-list.txt` again. Your redesign is back! Check the log:

```bash
git log --oneline
```

Now you see the redesign commit.

This is branching in action. Two versions of your project, each with its own history, and you can switch between them instantly.

## Why This Is Revolutionary

Let's pause and appreciate what just happened. You made significant changes to a file, and you can switch between the original and the modified version instantly, without manually creating backups, without fear of losing anything.

### Traditional Workflow Pain Points

Without branches, experimenting is risky:

1. **The Backup Dance**: Copy entire folders or files with names like "BACKUP_before_changes."
2. **Decision Anxiety**: Every change feels permanent. What if this is wrong?
3. **Merge Hell**: If the experiment works, you have to manually copy changes from the backup into the main version, paragraph by paragraph.
4. **Lost Ideas**: Sometimes you don't experiment at all because it's too risky or tedious.

### The Branching Workflow

With branches:

1. **No Backup Needed**: The original is automatically safe on the `main` branch.
2. **Freedom to Fail**: Make bold changes knowing you can always delete the branch.
3. **Easy Merging**: Git can automatically merge the branch back into `main` (usually).
4. **Parallel Experimentation**: Work on multiple experiments simultaneously, each on its own branch.

## Real-World Branching Scenarios for Non-Developers

Let's explore practical ways non-developers can use branches:

### Scenario 1: The Writer

**Situation**: You're writing a memoir. Chapter 7 covers a difficult topic, and you're considering two different tones: reflective or humorous.

**Branching Solution**:

```bash
git switch -c chapter7-reflective
# Write the chapter in a reflective tone, commit
git switch main
git switch -c chapter7-humorous
# Write the chapter in a humorous tone, commit
```

Now you have three branches:
- `main`: The chapter as originally drafted (or not written yet)
- `chapter7-reflective`: The reflective version
- `chapter7-humorous`: The humorous version

Share both versions with your writing group. Based on feedback, merge the one that resonates.

### Scenario 2: The Designer

**Situation**: You're designing a logo. You have a strong concept, but you want to try a few variations (different color schemes, different fonts) without losing the original.

**Branching Solution**:

```bash
git switch -c logo-blue-scheme
# Create blue color variation, commit
git switch main
git switch -c logo-red-scheme
# Create red color variation, commit
git switch main
git switch -c logo-modern-font
# Try a modern font, commit
```

Present all variations to the client. They choose one, and you merge that branch.

### Scenario 3: The Marketer

**Situation**: You're drafting a campaign email. You want to test different subject lines and call-to-action text to see which performs better.

**Branching Solution**:

```bash
git switch -c email-subject-direct
# Use direct subject line: "Save 50% Today Only"
git switch main
git switch -c email-subject-curious
# Use curiosity-gap subject line: "You Won't Believe This Deal"
```

Send each version to a test segment of your email list. Analyze open rates and click-through rates. Merge the winner.

### Scenario 4: The Event Planner

**Situation**: You're planning a conference schedule. You have two possible arrangements: morning workshops vs. afternoon workshops.

**Branching Solution**:

```bash
git switch -c schedule-morning-workshops
# Create schedule with workshops in the morning, commit
git switch main
git switch -c schedule-afternoon-workshops
# Create schedule with workshops in the afternoon, commit
```

Share both schedules with speakers and get feedback. Choose the one that works best for everyone.

## Merging Branches

Once you've completed your experiment and decided it's good, you'll want to merge it back into `main`. Merging combines the changes from two branches.

### Fast-Forward Merge: The Simple Case

Let's merge our `reading-list-redesign` branch into `main`. First, switch to the branch you want to merge *into* (the target):

```bash
git switch main
```

Now merge the other branch:

```bash
git merge reading-list-redesign
```

If no changes were made to `main` since you branched off, Git performs a "fast-forward" merge. This simply moves the `main` pointer forward to match `reading-list-redesign`. Easy.

You'll see:

```
Updating a7b3c2d..f9e8d7c
Fast-forward
 reading-list.txt | 24 ++++++++++++++----------
 1 file changed, 14 insertions(+), 10 deletions(-)
```

Check `reading-list.txt` on `main`—it now has your redesign. Check the log:

```bash
git log --oneline
```

The redesign commit is now part of `main`'s history.

### Deleting Merged Branches

Once a branch is merged, you often don't need it anymore. Delete it:

```bash
git branch -d reading-list-redesign
```

The branch pointer is deleted, but the commits remain—they're now part of `main`. The history is preserved.

### Three-Way Merge: The Complex Case

Sometimes both branches have new commits since they diverged. This requires a "three-way merge." Git compares three points: the common ancestor, the tip of branch A, and the tip of branch B.

**Example**: Let's create a scenario.

First, make a commit on `main`:

```bash
git switch main
# Edit january-meeting.txt, add a line: "Location: Sarah's house"
git add january-meeting.txt
git commit -m "Add meeting location"
```

Now create and switch to a new branch:

```bash
git switch -c add-february-notes
```

Create a new file `february-meeting.txt`:

```
Book Club - February Meeting
=============================

Book: "To Kill a Mockingbird"
Date: February 12, 2024
Attendees: Sarah, Mike, Jennifer, Tom, Lisa

Discussion Points:
- Racial injustice themes
- Scout's character growth
- Atticus as a moral compass
```

Commit it:

```bash
git add february-meeting.txt
git commit -m "Add February meeting notes"
```

Now both branches have unique commits:

```
        (main with location update)
       /
A---B---C---D
         \
          E  (add-february-notes with new file)
```

Merge:

```bash
git switch main
git merge add-february-notes
```

Git will create a merge commit—a special commit with two parents, combining both branches:

```
        D (main)
       / \
A---B---C   F (merge commit)
         \ /
          E (add-february-notes)
```

If Git can automatically merge (no conflicting changes to the same file), it will. You might see a text editor open asking for a merge commit message. The default message is fine; save and close.

If Git can't automatically merge (both branches edited the same part of the same file), you get a merge conflict. We'll address that next.

## Handling Merge Conflicts

A merge conflict occurs when Git doesn't know which change to keep. This happens when both branches modified the same line(s) of the same file.

### Creating a Conflict

Let's deliberately create one for practice.

Create a branch and edit a file:

```bash
git switch -c update-reading-list-v1
# Open reading-list.txt, change the first line to: "Book Club Master Reading List"
git add reading-list.txt
git commit -m "Update reading list title to Master Reading List"
```

Switch back to `main` and edit the same line differently:

```bash
git switch main
# Open reading-list.txt, change the first line to: "Book Club Official Reading List"
git add reading-list.txt
git commit -m "Update reading list title to Official Reading List"
```

Now try to merge:

```bash
git merge update-reading-list-v1
```

You'll see:

```
Auto-merging reading-list.txt
CONFLICT (content): Merge conflict in reading-list.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Git couldn't decide whether the title should be "Master" or "Official."

### Resolving the Conflict

Open `reading-list.txt`. You'll see something like:

```
<<<<<<< HEAD
Book Club Official Reading List
=======
Book Club Master Reading List
>>>>>>> update-reading-list-v1
======================
...
```

Git has marked the conflict:
- `<<<<<<< HEAD`: The start of your current branch's version (main)
- `=======`: The divider between the two versions
- `>>>>>>> update-reading-list-v1`: The end of the other branch's version

**Your job**: Decide what the final version should be. You can:

1. Keep your version (delete everything from `<<<<<<< HEAD` to `>>>>>>>` except your version)
2. Keep their version (delete everything except their version)
3. Write something new that combines both or replaces both

Let's combine them:

```
Book Club Official Master Reading List
======================
...
```

Remove all the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). Save the file.

Stage the resolved file:

```bash
git add reading-list.txt
```

Complete the merge with a commit:

```bash
git commit -m "Merge update-reading-list-v1 with combined title"
```

Conflict resolved! The branches are merged.

### Aborting a Merge

If you encounter a conflict and decide you don't want to deal with it right now, you can abort:

```bash
git merge --abort
```

This cancels the merge and returns everything to how it was before you started.

## Visualizing Branches

As your branching becomes more complex, visualizing the branch structure helps. Use:

```bash
git log --oneline --graph --all
```

This shows a ASCII-art graph of your commits and branches:

```
*   f7e6d5c (HEAD -> main) Merge update-reading-list-v1 with combined title
|\  
| * c9d8e7f (update-reading-list-v1) Update reading list title to Master Reading List
* | b6a5c4d Update reading list title to Official Reading List
|/  
* a7b3c2d Add February meeting notes
...
```

The graph shows branches diverging and merging. It's a visual history of your parallel work.

## Branching Strategies for Non-Developers

You don't need complex branching strategies like software teams use. Here are simple approaches:

### Strategy 1: Feature Branches

Create a branch for each new feature or section:

- `main`: Stable, complete work
- `chapter-7-draft`: Working on chapter 7
- `new-logo-design`: Experimenting with a new logo
- `updated-timeline`: Revising project timeline

When a feature is done, merge it into `main` and delete the branch.

### Strategy 2: Experiment Branches

Keep `main` as your official version. Create branches for experiments:

- `main`: Your approved, final work
- `experiment-new-intro`: Trying a different introduction
- `experiment-shorter-format`: Testing a condensed format

If an experiment works, merge it. If not, delete it. `main` remains untouched.

### Strategy 3: Collaboration Branches

If working with others, each person can have their own branch:

- `main`: The combined, approved work
- `sarahs-edits`: Sarah's contributions
- `mikes-revisions`: Mike's revisions

Everyone works independently, then merges their work into `main` when ready.

## Best Practices for Branching

### 1. Use Descriptive Branch Names

Bad: `new-branch`, `test`, `branch2`  
Good: `update-contact-info`, `redesign-homepage`, `draft-chapter-5`

### 2. Keep Branches Short-Lived

Don't let branches linger for months. The longer a branch exists, the more `main` diverges, and the harder merging becomes. Finish your work, merge, delete.

### 3. Merge Regularly

If your branch will exist for a while, periodically merge `main` into your branch to stay up-to-date:

```bash
git switch your-branch
git merge main
```

This prevents your branch from drifting too far.

### 4. Don't Fear Branching

Branches are free (computationally). Creating a branch takes milliseconds and uses almost no disk space. Create them liberally. Experiment. The worst that happens is you delete the branch.

## The Psychology of Fearless Experimentation

Branches fundamentally change how you approach creative work. Without them, you're conservative. You play it safe. Bold ideas feel risky because they might permanently damage your work.

With branches, you're liberated. That wild idea? Try it on a branch. That complete restructuring? Branch. That controversial redesign? Branch. If it works, you merge and look like a genius. If it fails, you delete the branch and no one ever knows. There's no downside to trying.

This psychological shift is profound. You become more creative, more willing to take risks, more innovative—because the safety net is always there. Branching doesn't just protect your work; it unlocks your potential.

## Summary: Your Parallel Universes

You now understand Git's most powerful feature: branching. You can create parallel versions of your project, experiment freely, and merge the results back together. You can work on multiple ideas simultaneously without confusion. You can collaborate without stepping on toes.

Branches transform Git from a simple versioning system into a creativity tool. They make experimentation safe, failure cheap, and success easy to achieve.

In the next chapter, we'll expand beyond your local computer. You'll learn to push your repository to the cloud, enabling backup, collaboration, and access from anywhere. But you've already mastered the core of Git. Everything else is building on this foundation.

Practice branching. Create branches for every new idea. Merge them or delete them. Get comfortable with the workflow. Soon, you'll think in branches naturally, and your work will never be the same.

Welcome to the multiverse.
