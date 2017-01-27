# This repository

This repo is a fork of https://github.com/google/guava - with no intention of
merging back. This is about demonstrating how Google uses a "sparse checkout"
with their gigantic Monorepo (86TB of history, 9 million unique files).

Guava uses Maven - which is the point. Google uses Blaze internally (which was
open sourced as Bazel).

Refs:
[1](https://trunkbaseddevelopment.com/monorepos/)
[2](http://paulhammant.com/2014/01/06/googlers-subset-their-trunk/)
[3](http://paulhammant.com/2015/05/20/turning-bazel-back-into-blaze-for-monorepo-nirvana/)

# Doing a 'quick' experiment with this repo/branch

Initial setup:

```
git clone git@github.com:paul-hammant/googles-monorepo-demo.git
cd googles-monorepo-demo
```

To run the experiment:

```
git config core.sparsecheckout true
echo '/mr' > .git/info/sparse-checkout
echo '/README.md' >> .git/info/sparse-checkout
echo '/pom*' >> .git/info/sparse-checkout
echo '/guava/' >> .git/info/sparse-checkout
echo '/guava-testlib/' >> .git/info/sparse-checkout
mr/checkout.sh
mvn install
```

The huge 'samples' directory isn't in the checkout (yes yes, it is in the
clone, relax). It isn't in the root POM's modules either - which is what we
wanted.

# Making your own Maven setup like this

In your repo, all pom.xml files need to be renamed to pom-template.xml:

```
find . -name pom.xml -type f | while read a; do n=$(echo $a | sed -e 's/pom.xml/pom-template.xml/'); git mv $a $n; done
```

You'll need to checkin the `mr` directory we have above. You'll also want to
add `pom.xml` to `.gitignore` - they're not under source control any more,
`pom-template.xml` is instead.
