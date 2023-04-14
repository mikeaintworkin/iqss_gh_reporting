#!/bin/main
# export GITHUB_TOKEN=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
# export GH_REPO=hmdc/DevOpsProjects

# https://docs.github.com/en/issues/trying-out-the-new-projects-experience/using-the-api-to-manage-projects
# 4103595 | hmdc/DevOpsProjects
# 10829206 | Releases
# 8487501 | OnDeck
# 8931645 | Waiting
# 8309430 | WIP (proposed limit = 10)
# 8610335 | Pending Review
# 13317183 | Review (test in dev) 
# 13317275 | Pending QA
# 13317280 | QA
# 8309431 | Done
# 14345046 | Ready (e.g. deferred for now)
# 8840819 | [OFF THE BOARD (OTB)] ICEBOX (NEW)
# 9837518 | [OTB] RShiny
# 8840813 | [OTB] CentOS 6 EOL Priority (Sarah)
# 8840823 | [OTB] RCE EOL Priority (Sarah,Mike)
# 10825872 | [OTB] Sid RCE Next Generation
# 10643309 | [OTB] IQSS Service Catalog
# 16597272 | [OTB] Heroku Alternative
# 

#exec gh api --preview inertia "projects/4103595/columns" > ../wrk/projects_4103595_columns.txt
exec gh api --preview inertia "projects/columns/10829206/cards" > ../wrk/projects_4103595_10829206_cards-$(date '+%Y_%m_%d-%H_%M_%S').json

