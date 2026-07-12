# Subtrees are amazing

To say at least, way better than submodules afaik.
Subtrees shine when you need more control, i'd say, over the source code while maintaining a healthy relationship with the upstream.

## Wait, aren't `subtrees` and `submodules` the same thing?

Well, not quite you see, in fact they diverge a lot in various aspects, but regarding the goal, yes, pretty much the same.
The detail here is on how each one implements the solution, which to be fair each has it's use cases.

To begin with, the first main difference I can perceive is that a `submodule` is really a pointer to a commit in a given repo, eg a symlink to a commit.
While `subtree` in the other hand is like taking more control over it, basically copying the source code into your own repo but giving you full capability to pull/push isolated commits (that only affect the subtree) to the upstream.
Then you'll have that project code "bolted" into your codebase, so whenever they push updates/releases you can just `git subtree pull`, similarly use `push` to contribute patches you made to the upstream ([more on that later](# Contributing through a subtree)) and if they ever delete the repo you are fine since you have a literal copy.

## So what would be a good use case?

Well, let's say I have a project made in C, and it uses `libsqlite` for example, and for some unknown reason I need some patch/changes into this lib for it to work properly towards my project shenanigans with SQL.
Then we have a few options here:
1 Fork it and submit a PR that is very very unlikely to get accepted due it being a niche patch specifically for my project.
2 Fork it and maintain it, constantly pulling from upstream and having to worry on a second repo.
3 Fork it, patch and forget, completely ignoring upstream updates (are you a monster?).
4 Basically the second option but with a subtree.

So I guess there's no need to get in detail about 1 and 3...
About the second option, this is generally what you'd do, which is not wrong at all, however as this patch is niche into my project I could benefit much more from the fourth option.
For a quick perpective on how, imagine that I'd need to align the patch with types and logic contained in my project code, since a subtree is just another folder with code inside, once I pull it I can start doing whatever I need and use the definitions, functions, structs thata are already present in my codebase.
And what about the "maintaining it" part? Well, it depends a bit, because technically even with the second option you don't really *maintain* it, it really depends on how intrusive the patch would be, the real maintainece would be pulling from upstream and resolving merge conflicts once the patch is fully done (which can be automagically done by git, again depending on the circunstances of the patch made and incoming changes).
Other than that, maintaining it would be improving your patch against new updates from upstream, that if you ever bother to pull...

Another good example I can think of, would be in this same project where I now want to use another lib, let's take `libuv` for example, and the point here would be that I just want simplicity if they ever push a update/release or be secure if they ever happen to delete the repo.
Then using subtrees would be perfect, I just add the subtree into a `libs/libuv` folder and forget about it, and if they ever update i just pull this one subtree upstream and *vóila*, there it is the new version of the lib.

## Adding and managing subtrees

The commands are very simple, as git ever was.

First, it's recommended that we add the remote of the repo, for easy management so there is no need to memorize the repo url
```bash
git remote add lib_remote <URL>
```

Then we add the subtree
```bash
git subtree add --prefix=<local-folder-name> <remote-or-URL> <branch> --squash
```
> Here `--prefix` is the subtree folder, which must not exist as git will create it
> The `--squash` is optional, but very recommended as well so you dont add like 6k+ commits from a lib on top of your repo git history, it condenses down to a single commit, just notice that if you use it here you'll have to **ALWAYS** use it on subsequent pulls

If just copying it over once to have the code you're done, that's it all, so after you push this change the files from the subtree will appear normaly in your remote, no weird links pointing to another repo commit.
Then if the repo from the subtree ever gets an update you just pull it, simple.

## Contributing through a subtree

Pushing code back into the upstream is just as easy
```bash
git subtree push --prefix=<local-folder-name> <remote-or-URL> <branch>
```
> Git will then find the commits that affect the subtree and push these changes to the upstream remote.
> Why you have to specify the prefix (folder path) again?? Well, git is smart, but it doesn't know everything.

But this get tricky, because as far as I know, this only let's you push directly to the remote.
This is a dealbreaker in various cases of modern git hosts like github, gitlab, codeberg and generally any repository that you don't have write permission or due the PR workflow that a proposed change should undergo even if you can directly push.
There are a few solutions to that, for a repo where you have write access, ever noticed the branch option in the commands? Yeah, you know where this is going.
But for the ones where you don't and it, for example, follows the github contribution pattern; Even after you've created the subtree, go ahead and make a fork of the subtree repo, then back at your subtree, when pushing the code instead of specifying the remote handle, swap fro the url of your fork and the desired branch.

This feels like an workaround, and it is, but it's not Git fault.
Either way, those are the pros and cons right?

## An overview

Here's an table of comparision between `subtrees` and `submodules` (generated by Gemini).

| Feature       | Git Submodule                                                                         | Git Subtree                                                                         |
|---------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| File Storage  | Stored in a separate hidden git repo;<br>main repo only tracks a commit hash pointer. | Physically copied and fully tracked inside your main repository.                    |
| Cloning       | Requires extra steps (--recurse-submodules).                                          | One standard git clone.<br>Works out of the box.                                    |
| Local Editing | Tedious (must enter the submodule directory, checkout a branch, commit separately).   | Seamless. Edit files right there and commit normally with the rest of your project. |
| History bloat | Low impact.                                                                           | Can introduce minor bloat, mitigated entirely by using the <br>--squash flag.       |
