# Clean Code Principles

Source: [Clean Code: A Handbook of Agile Software Craftsmanship, by Robert Martin](https://www.goodreads.com/book/show/3735293-clean-code)

This is intended to serve as a quick checklist of clean code principles to adhere to.

## Meaningful names

- Use intention-revealing names. If a name requires a comment, then the name doesn't reveal intent.
- Avoid disinformation. If a container holding accounts is not actually a list, don't call it `accountsList` (something like `accountGroup` or `accounts` is better).
- Make meaningful distinctions. For example, having 3 classes, `Product`, `ProductInfo`, and `ProductData` are not distinct. Give them unique names. Ditto for a class called `Customer` and another called `CustomerObject`.
- Avoid noisy words in names, such as "variable", "manager", "processor", "table", "info", and "data". In these scenarios, you can probably pick a more clear synonym.
- Pick one word per concept.  For example, it's confusing to have "fetch", "retrieve", and "get" all mean "obtain something". Pick one word, and stick with it.

## Functions

- "The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that".
- Functions should do one thing. They should do it well. They should do it only.
- If we can describe the function as a brief "TO" paragraph (e.g., "To (do task), we (step 1), then (step 2), then (step 3)"), then it is good.
- If a function is doing more than one thing, you can extract another function from it with a name that is not merely a restatement of its implementation.
- Make sure that the statements within a function are all at the same level of abstractions.
- Read code from top to bottom. We want every function to be followed by those at the next level of abstraction. We want to be able to read the program as though it were a set of "TO" paragraphs.
- Avoid too many switch statements. They're OK if used once, are used to create polymorphic objects, and are hidden behind inheritance. Use polymorphism where possible.
- "You know you are working on clean code when each routine turns out to be pretty much what you expected". The smaller and more focused a function is, the easier it is to choose a descriptive name.
- Minimize the number of function arguments where possible. If a function needs more than 2-3 arguments, see if you can wrap some arguments into a class.
- Have no side effects. If your function promises to do one thing but also does other hidden things, this can cause unexpected bugs and dependencies.
- Functions should either do something, or answer something, but not both. Either your function should change the state of the object, or it should return some information about that object. Doing both leads to confusion.
- Prefer custom exceptions to returning error codes.
- Extract the bodies of try/catch blocks into functions of their own. Should be "try{ func() } except { other_func() }".
- A function that handles errors should do nothing else.
- Don't repeat yourself.

## 