# This repository

Is a hacky composite of three repos from https://github.com/hazelcast/

I it hacky because those three are now subdirectories of this one, with their
history deleted and committed again as revision #1. It serves as a testbed for
Maven and Monorepo hacking in the style of Google's Blaze Monorepo. Refs:
[1](https://trunkbaseddevelopment.com/monorepos/)
[2](http://paulhammant.com/2014/01/06/googlers-subset-their-trunk/)
[3](http://paulhammant.com/2015/05/20/turning-bazel-back-into-blaze-for-monorepo-nirvana/)

# Doing a 'quick' experiment with this repo/branch

To run the experiment:

```
git clone git@github.com:paul-hammant/maven-monorepo-experiment.git --no-checkout
cd maven-monorepo-experiment
git config core.sparsecheckout true
echo '/*' > .git/info/sparse-checkout
echo '!samples' >> .git/info/sparse-checkout
git checkout trick-maven-monorepo
find . -name "pom-template.xml" | python writepom.py
mvn install
```

The huge 'samples' directory isn't in the checkout (yes yes, it is in the clone, relax). It isn't in the
root POM's modules either - which is what we wanted.

The see what happened to the pom:

```
diff pom-template.xml pom.xml
```

# Making your own Maven setup like this

In your repo, all pom.xml files need to be renamed pom-template.xml:

```
find . -name pom.xml -type f | while read a; do n=$(echo $a | sed -e 's/pom.xml/pom-template.xml/'); git mv $a $n; done
```

You'll need to checkin `writepom.py` to the root of your repo.

Then refer to the experiment script above.
