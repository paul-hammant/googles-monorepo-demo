# Demo of a expanding/contracting monorepo for mortals

This repo is a fork of https://github.com/google/guava - with no intention of
merging back. This is about demonstrating how Google uses a "sparse checkout" (Git and Subversion language)
with their gigantic Monorepo (86TB of history, 9 million unique files).

Guava uses Maven - which is why I chose it. (you can do expanding/contracting monorepos with Maven too). 
Google uses Blaze internally (which wasopen sourced as Bazel - with the expand/contract feature missing).

* Main blog entry, documenting this: [Maven In A Google Style Monorepo](https://paulhammant.com/2017/01/27/maven-in-a-google-style-monorepo/) (2017)
* Google knowhow for the edification of the masses [Googlers Subset their Trunk](http://paulhammant.com/2014/01/06/googlers-subset-their-trunk/) (2014)
* On the piece left out of Bazel: [Turning Bazel back into Blaze for monorepo nirvana](http://paulhammant.com/2015/05/20/turning-bazel-back-into-blaze-for-monorepo-nirvana/)
* A **bigger** (more convincing) version of this demo: [Further Experiments With Expanding/Contracting Monorepos](https://paulhammant.com/2017/02/08/further-experiments-with-expanding-contracting-monorepos/) (2017)
* The monorepos page on the site I put together with friends: [trunkbaseddevelopment.com/monorepos/](https://trunkbaseddevelopment.com/monorepos/)
* Same site, but the **expandable/contractable** page: [trunkbaseddevelopment.com/expanding-contracting-monorepos](https://trunkbaseddevelopment.com/expanding-contracting-monorepos/)

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
