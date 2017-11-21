import git
repo = git.Repo.init("e:/test/test2")
w = "master"
r = "origin/master"
repo.remotes.origin.fetch("master")
repo.git.checkout(w)
print("master:",repo.commit(w))
print("origin/master:",repo.commit(r))
if repo.commit(w) != repo.commit(r):
    print("need update")
    print("process update.....")
else:
    print("It's up to date")
    repo.git.merge(r)

