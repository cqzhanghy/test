import git
repo = git.Repo.init("e:/test/test2")
print("master:",repo.commit('master'))
print("origin/master:",repo.commit('origin/master'))
