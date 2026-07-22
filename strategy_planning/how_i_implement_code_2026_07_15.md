Notes on how I implement code:

- I prefer to, when scoping out actual implementation given a spec or design, start with scaffolding
and then do implementation.
- when I implement software, I like to first figure out the main caller or how this change will
be used by whatever is calling or using it. That's generally a single function plugged into a flow,
a single class that's used in a `main.py`, or something like that.
- stub the files first and figure out how all the files will be imported into the core files.
- then I like to set up the core models and interfaces and boundaries. again just defining the classes,
no functionality or methods yet (besides any directly useful to show how a caller uses a class).
- then once that's approved, I'll write out (first in pseudocode, then real code) the expected test cases.
- then, I'll go to the main caller or endpoint and pick one specific use case or path or flow or unit of work,
and I'll flesh that out to completion. I'll write up its unit tests and also see which of the previous tests I designed
will now pass.
- I do that for each step, until the main caller is fully fleshed out.
