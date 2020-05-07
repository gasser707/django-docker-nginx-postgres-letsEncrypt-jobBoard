# ConcordiaAce
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://aceconcordia.ca)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) (Except Templates) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[https://concordia-ace.ca/](https://concordia-ace.ca/)

Job board made for Concordia University, Montreal, Canada, Co-op ACE program. 
# Features

| Security        | Job Ranking & Matching          | Media servicing  | User Notification  | Other Job Board Services  | Data  | CI/CD  |
| ------------- |:-------------:| :-----:|:-----:| :-----:|-----:|-----:|
| Google Captcha      | Candidate-Employer preference ranking system| Nginx file servicing | [django-notifications-hq](https://pypi.org/project/django-notifications-hq/) | Login as Admin, Candidate or Employer | Postgres Db| Prod Ready easy Docker-Compose setup
| Email activation|  ["hospital-resident" matching algorithm](https://pypi.org/project/matching/)      |   [Dynamic Plyr video player](https://github.com/sampotts/plyr)  | Email notification| Post/review/edit jobs, interview invite, job matching | | Persistent Volumes and storage mount, django migrations
| Nginx-Sendfile Firewall |  |   Dynamic upload forms | Annoncements | Apply to jobs | | Test media and db volumes, 95% Code shared between prod and test docker-compose setups
| uuid protected dynamic file paths |  |    Secured resume caching and reuse| | Search and filter jobs
| Email password reset |  | Sendfile + auth protected media| | Search and filter candidates
| Let's Encrypt SSL with autorenewal | |  | | Full Admin Control (approval, permission assignment, etc.)
| | |  | | Google Map,  PDF Concatination
# Licensing
- All python/django code are created by us and available under MIT licence
- html template license was purchased for single app use for Concordia ACE website on http://preview.themeforest.net/item/oficiona-job-board-html-template/full_screen_preview/23042674 License must be re-purchased for other project. Permission to reuse template not under MIT license. 


