import git
repo = git.Repo.init("e:/test/test2")
repo.remotes.origin.fetch()
print("master:",repo.commit('master'))
print("origin/master:",repo.commit('origin/master'))
if repo.commit('master') != repo.commit('origin/master'):
    print("need update")

