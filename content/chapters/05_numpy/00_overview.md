# The scientific Python ecosystem

Python has an excellent eco-system of scientific computing tools. What do we
mean when we say "scientific computing"? There's no one definition, but we
roughly mean those parts of computing that allow us to compute on scientific
data. This is the kind of data that represents images or time-series (but can
represent many other things!). It's also often called "numerical computing",
because these data are often stored as numbers. A common structure for numerical
computing is that of an array. An array is an ordered collection of items that
are stored such that a user can access one or more items in the array. The
[`numpy`](https://numpy.org/) Python library provides an implementation of
an array data structure that is both powerful and light-weight.

What do we mean by "ecosystem"? This means that many different individuals and
organizations develop software that interoperates to perform the various
scientific computing tasks that they need to perform. Tools compete for users
and developers' attention and mind-share, but more often they might coordinate.
No one entity manages this coordination. In that sense, the collection of
software tools that exists in Python is more like an organically evolving
ecosystem than a centrally-managed organization. One place in which the
ecosystem comes together as a community is an annual conference called
Scientific Computing in Python, which takes place in Austin, Texas once a year
every summer.


## Further reading

For a description of the Python scientific, see Fernando Perez, Brian Granger
and John Hunter's paper from 2011 [@Perez2010-nn]. This paper describes in some
detail how Python has grown from a general-purpose programming language into a
flexible and powerful tool that covers many of the uses that scientists have,
through a distributed, eco-system of development.