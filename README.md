# TP_git_Emie_Pul
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

linux@Linux:~$ cd Documents
linux@Linux:~/Documents$ git clone https://github.com/maemieP/TP_git_Emie
fatal: destination path 'TP_git_Emie' already exists and is not an empty directory.
linux@Linux:~/Documents$ git clone https://github.com/maemieP/TP_git_Emie_Pul
Cloning into 'TP_git_Emie_Pul'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
linux@Linux:~/Documents$ cd TP_git_Emie_Pul
linux@Linux:~/Documents/TP_git_Emie_Pul$ git checkout -b manageTask
Switched to a new branch 'manageTask'
linux@Linux:~/Documents/TP_git_Emie_Pul$ touch taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ nano taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git add taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git commit -m "fonction pour ajouter une nouvelle tache"
[manageTask a4beda1] fonction pour ajouter une nouvelle tache
 1 file changed, 3 insertions(+)
 create mode 100644 taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ nano taskTouch.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git add taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git commit -m "fonction pour suprimer les taches"
On branch manageTask
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	taskTouch.py

nothing added to commit but untracked files present (use "git add" to track)
linux@Linux:~/Documents/TP_git_Emie_Pul$ nano taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git add taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ 
linux@Linux:~/Documents/TP_git_Emie_Pul$ git add taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git commit -m "fonction pour suprimer une tache"
[manageTask bd7abce] fonction pour suprimer une tache
 1 file changed, 7 insertions(+)
linux@Linux:~/Documents/TP_git_Emie_Pul$ nano taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git add taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git commit -m "fonction pour marquer la fin d'une tache"
[manageTask 8448220] fonction pour marquer la fin d'une tache
 1 file changed, 7 insertions(+)
linux@Linux:~/Documents/TP_git_Emie_Pul$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
linux@Linux:~/Documents/TP_git_Emie_Pul$ git merge manageTask
Updating 3d4f5b7..8448220
Fast-forward
 taskTool.py | 17 +++++++++++++++++
 1 file changed, 17 insertions(+)
 create mode 100644 taskTool.py
linux@Linux:~/Documents/TP_git_Emie_Pul$ git push origin main
Username for 'https://github.com': maemieP
Password for 'https://maemieP@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/maemieP/TP_git_Emie_Pul/'
linux@Linux:~/Documents/TP_git_Emie_Pul$ git push origin main
Username for 'https://github.com': emiepulcherie@yahoo.com
Password for 'https://emiepulcherie@yahoo.com@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/maemieP/TP_git_Emie_Pul/'
linux@Linux:~/Documents/TP_git_Emie_Pul$ git config --global user.name
EmiePul
linux@Linux:~/Documents/TP_git_Emie_Pul$ git config --global user.name "maemieP"
linux@Linux:~/Documents/TP_git_Emie_Pul$ git config --global user.email "emiepulcherie@yahoo.com"
linux@Linux:~/Documents/TP_git_Emie_Pul$ git config --global user.name
maemieP
linux@Linux:~/Documents/TP_git_Emie_Pul$ git push origin main
Username for 'https://github.com': maemieP
Password for 'https://maemieP@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/maemieP/TP_git_Emie_Pul/'
linux@Linux:~/Documents/TP_git_Emie_Pul$ git push main
fatal: 'main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
linux@Linux:~/Documents/TP_git_Emie_Pul$ git push origin main
Username for 'https://github.com': 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
Password for 'https://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@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/maemieP/TP_git_Emie_Pul/'
linux@Linux:~/Documents/TP_git_Emie_Pul$ 

