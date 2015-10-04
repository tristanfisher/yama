# YAMA
#### Y(et) A(nother) M(anagement) A(gent)

[![Build Status](https://travis-ci.org/tristanfisher/yama.svg?branch=master)](https://travis-ci.org/tristanfisher/yama)


### What does it do?

YAMA is the locally running agent for the [YAMS](https://github.com/tristanfisher/YAMS).  

Services provided:

* Heartbeat


### Communication

YAMA runs on the following ports:

| Port | Transport Protocol | Application Protocol | Usage                       |
|------|--------------------|----------------------|-----------------------------|
| 1112 | UDP/TCP            | YAMS Socket          | YAMS to Agent communication |


### Contributing

Please fork the repo, switch to the dev branch (or master/release for documentation), make your changes, and submit a pull request (`git rebase` first please).


#### Code

All code submissions should be done through pull requests.  If you're feeling extra nice (and want to increase the chances of a merge), include unittests.

If the change is large, please make sure that it is well-commented and be patient.


#### Documentation

If something is poorly explained and you feel it should be better, please either open a GitHub issue or make a pull request with documentation against the branch that contains the object you're writing about. 

e.g. "memory usage too high on branch dev" -> dev branch


#### Bug Hunters

If you find a bug in YAMA, please open a GitHub issue with the description of the bug, the version you're running, and any information you think may be helpful.

Please note that all fixes will be rolled forward into newer releases.


---
 
######*Tristan Fisher 2015*
