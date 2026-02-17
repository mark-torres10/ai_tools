---
id: rules.clean_code_principles
title: Clean Code Principles
description: Readability, maintainability, and design principles derived from established clean-code guidance.
when_to_use:
  - Refactoring for readability and maintainability.
  - Reviewing naming, function design, comments, and code organization.
  - Applying foundational code-quality principles across languages.
when_not_to_use:
  - Process-specific workflow operations (for example, server startup).
  - Toolchain configuration and package manager decisions.
scope:
  - coding
  - readability
  - maintainability
priority: 75
applies_to:
  task_types:
    - implementation
    - refactor
    - code_review
  file_globs:
    - "**/*.{py,ts,tsx,js,jsx,go,java,rs}"
dependencies: []
conflicts_with: []
tools_preferred:
  - ReadFile
  - ApplyPatch
owner: ai_tools
last_updated: 2026-02-17
---

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

## Comments

- Comments do not make up for bad code.
- Can comment when you're adding explanation of intent, or other contextual information that would be helpful for someone new to the codebase. Similarly, can flag notes that would be helpful to future developers wanting to develop/refactor that part of the code.
- Can add TODOs and other notes to future programmers.
- Can comment to amplify some line of code that seems inconsequential but actually is critical.
- Keep comments close to the code that it references.

## Formatting

- If one function calls another, they should be vertically close to each other.
- Groups of functions or variables used together should exist close together.
- we want function call dependencies to point in the downward direction. A function that is called should be below a function that does the calling.

## Objects and data structures

- The Law of Demeter: A method `f` of class `C` should only call the methods of (1) `C`, (2) an object created by `f`, (3) an object passed as an argument to `f`, or (4) an object held in an instance variable of `C`. The method should not invoke methods on objects that are returned by any of the allowed functions.
- Procedural code (code using data structures) makes it easy to add new functions without
changing the existing data structures. OO code, on the other hand, makes it easy to add
new classes without changing existing functions.

### Example of procedural code

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Square:
    def __init__(self, top_left: Point, side: float):
        self.top_left = top_left
        self.side = side

class Rectangle:
    def __init__(self, top_left: Point, height: float, width: float):
        self.top_left = top_left
        self.height = height
        self.width = width

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

class NoSuchShapeException(Exception):
    pass

class Geometry:
    PI = 3.141592653589793

    def area(self, shape):
        if isinstance(shape, Square):
            return shape.side * shape.side
        elif isinstance(shape, Rectangle):
            return shape.height * shape.width
        elif isinstance(shape, Circle):
            return self.PI * shape.radius * shape.radius
        else:
            raise NoSuchShapeException()
 ```

Pro: if you add a new function (e.g., `perimeter`), the shape classes (and any classes dependent on them) would be unaffected.
Con: if you add a new shape, you need to update all the functions in `Geometry` to handle it.

### Example of object-oriented code

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, top_left, side):
        self.top_left = top_left
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, top_left, height, width):
        self.top_left = top_left
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Circle(Shape):
    PI = 3.141592653589793

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return self.PI * self.radius * self.radius
```

Here the area() method is polymorphic. No Geometry class is necessary.

Pro: if you add a new shape, none of the existing functions would be affected.
Con: if you add a new function to the abstract class, all of the shapes would be affected.

## Error handling

- Use exceptions rather than return codes.
- Provide context with exceptions.
- Eliminate special cases by including them into the normal flow.

Example

```python
try:
    expenses: MealExpenses = expenseReportDAO.getMeals(employee.getID())
    m_total += expenses.getTotal()
except MealExpensesNotFound as e:
    m_total += getMealPerDiem()
```

In this scenario, we could include `getMealPerDiem()` as the default behavior and avoid raising the exception altogether. We can create a `PerDiemMealExpenses` that implements the `MealExpenses` interface and have `ExpenseReportDAO` always return a `MealExpenses`.

```python
from abc import ABC, abstractmethod

class MealExpenses(ABC):
    @abstractmethod
    def getTotal(self):
        pass

class PerDiemMealExpenses(MealExpenses):
    def __init__(self, per_diem_amount):
        self.per_diem_amount = per_diem_amount

    def getTotal(self):
        return self.per_diem_amount

# Usage example
expenses: MealExpenses = expenseReportDAO.getMeals(employee.getID())
m_total += expenses.getTotal()
```

- Don't return null. They're a pain for callers to handle. Does it have to return null? Or can it return, say, an empty list or container and then downstream callers can handle the empty result?
- Don't pass null into methods. It creates new vectors for exceptions that are annoying to handle.

## Boundaries

- When using third-party code, err on the side of wrapping it in an interface. Some exceptions are for commonly used and maintained code, but just note that this raises the possibility of breaking dependencies. Wrapping it in an interface also allows you to inject dependencies and mock it for testing. For example:

Bad:

```python
import boto3

s3 = boto3.client("s3")
res = []
s3.upload_file(res, "foo.json")
```

Err on the side of creating an interface for this.

Better:
```python
import boto3

class S3Client:
    def __init__(self):
        self.client = boto3.client("s3")
    
    def upload_file(self, file_obj, key):
        # can add business logic, etc.
        self.client.upload_file(file_obj, key)
```

## Classes

- Classes should be small. The name of a class should describe what responsibilities it fulfills.
- We should be able to write a brief description of the class in about 25 words, without using the words "if", "and", "or", or "but".
- If we cannot derive a concise name for a class, then it’s likely too large. The more ambiguous the class name, the more likely it has too many responsibilities.
- **Single Responsibility Principle (SRP)**: A class or module should have one, and only one, reason to change.

**Bad Example** (violates SRP by mixing multiple responsibilities):

```python
class UserSettingsManager:
    def __init__(self, user):
        self.user = user

    def load_settings(self):
        # Loads user settings from disk
        with open(f"{self.user}_settings.json") as f:
            data = f.read()
        return data

    def save_settings(self, data):
        # Saves user settings to disk
        with open(f"{self.user}_settings.json", "w") as f:
            f.write(data)

    def send_settings_email(self, email_address):
        # Sends settings data to an email address
        data = self.load_settings()
        # (Pretend send logic here)
        print(f"Sending settings to {email_address}: {data}")
```

**Why it's bad:**  
The `UserSettingsManager` class is responsible for three unrelated things: reading/writing settings (persistence), formatting/initiating email sending (communication), and user context management. If requirements for any of these features change (e.g., switch to cloud storage or change email delivery), you'd have to modify this class. This violates SRP and leads to tightly coupled, hard-to-maintain code.

**Good Example** (each class has a single responsibility):

```python
class UserSettingsStorage:
    def __init__(self, user):
        self.user = user

    def load(self):
        with open(f"{self.user}_settings.json") as f:
            return f.read()

    def save(self, data):
        with open(f"{self.user}_settings.json", "w") as f:
            f.write(data)

class SettingsEmailer:
    def send(self, email_address, data):
        # (Pretend send logic here)
        print(f"Sending settings to {email_address}: {data}")

# Usage:
storage = UserSettingsStorage(user="alice")
settings_data = storage.load()
emailer = SettingsEmailer()
emailer.send(email_address="alice@example.com", data=settings_data)
```

**Why it's good:**  
Now, each class has a single responsibility. `UserSettingsStorage` deals only with reading/writing settings, and `SettingsEmailer` deals only with sending emails. Changes in storage mechanism or email delivery will be restricted to the relevant class, making the code more modular, testable, and easier to maintain.

- **Cohesion**: Classes should have a small number of instance variables. Each of the methods of a class should manipulate one or more of those variables. In general the more variables a method manipulates the more cohesive that method is to its class. But find a balance! Too much cohesion leads to classes that are too small.
- **Dependency Inversion Principle**: High-level modules should not depend on low-level modules; both should depend on abstractions (e.g., interfaces or abstract classes). Abstractions should not depend on details; details should depend on abstractions. In other words, classes should depend on abstractions, not concrete details, to promote flexible and testable code.

**Bad Example** (depends on a concrete implementation):

```python
class FileLogger:
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")

class Processor:
    def __init__(self):
        self.logger = FileLogger()  # Direct dependency on concrete implementation

    def process(self):
        # ... do processing ...
        self.logger.log("Processing done.")

# It's hard to test Processor in isolation, or swap logging strategies,
# because the FileLogger is hard-coded.
```

**Why it's bad:**  
`Processor` is tightly coupled to `FileLogger`. You cannot easily replace the logging mechanism (e.g. log to console, or use a mock during tests) without modifying `Processor`. This makes the code less flexible and harder to test or extend.

**Good Example** (depends on an abstraction/interface):

```python
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")

class Processor:
    def __init__(self, logger: Logger):
        self.logger = logger  # Depends on abstraction

    def process(self):
        # ... do processing ...
        self.logger.log("Processing done.")

# Can now pass in any Logger implementation:
processor = Processor(FileLogger())
# Or for testing:
class MockLogger(Logger):
    def __init__(self):
        self.messages = []
    def log(self, message):
        self.messages.append(message)
mock_logger = MockLogger()
test_processor = Processor(mock_logger)
```

**Why it's good:**  
`Processor` now depends on a `Logger` abstraction rather than a concrete implementation. This allows different logging strategies to be substituted easily (such as mock loggers for testing). The code is now more flexible, testable, and maintainable, which is the essence of the Dependency Inversion Principle.

## Code smells

- It is inappropriate for a comment to hold information better held in a different kind of system such as your source code control system, your issue tracking system, or any other
record-keeping system.
- A comment that has gotten old, irrelevant, and incorrect is obsolete. Comments get old
quickly. It is best not to write a comment that will become obsolete.
- Avoid switch/case or if/else chain that appears again and again in various modules, always testing for the same set of conditions. These should be replaced with polymorphism.
- Well-defined modules have very small interfaces that allow you to do a lot with a little. Poorly defined modules have wide and deep interfaces that force you to use many different gestures to get simple things done. A well-defined interface does not offer very many functions to depend upon, so coupling is low. A poorly defined interface provides lots of functions that you must call, so coupling is high.
- The methods of a class should be interested in the variables and functions of the class they belong to, and not the variables and functions of other classes.
- Things that don’t depend upon each other should not be artificially coupled. For example, general enums should not be contained within more specific classes because this forces the whole application to know about these more specific classes. In general an artificial coupling is a coupling between two modules that serves no direct purpose. It is a result of putting a variable, constant, or function in a temporarily convenient, though inappropriate, location.
- Code should be placed where a reader would naturally expect it to be.
- **Be precise**. When you make a decision in your code, make sure you make it precisely. Know why you have made it and how you will deal with any exceptions. Don’t be lazy about the precision of your decisions. If you decide to call a function that might return null, make sure you check for null. If you query for what you think is the only record in the database, make sure your code checks to be sure there aren’t others. If you need to deal with currency, use integers and deal with rounding appropriately. If there is the possibility of concurrent update, make sure you implement some kind of locking mechanism.
- Avoid negative conditionals.
- Don't be arbitrary.  Have a reason for the way you structure your code, and make sure that reason is communicated by the structure of the code. If a structure appears arbitrary, others will feel empowered to change it. If a structure appears consistently throughout the system, others will use it and preserve the convention.
- Encapsulate boundary conditions. If you have boundary-related calculations (such as incrementing or decrementing by 1), it's best to isolate and encapsulate them in a variable with a meaningful name. This makes your code easier to read and reduces errors due to "magic numbers" or scattered arithmetic.

Avoid spreading `+1` or `-1` adjustments throughout your code. Instead, compute the boundary condition once, name it, and use it everywhere it's needed.

**Bad Example (repeating boundary logic):**

```python
if level + 1 < len(tags):
    parts = Parse(body, tags, level + 1, offset + end_tag)
    body = None
```

Here `level + 1` is repeated. If you change the meaning or computation of the boundary, you have to change it everywhere.

**Good Example (encapsulate boundary logic):**

```python
next_level = level + 1
if next_level < len(tags):
    parts = Parse(body, tags, next_level, offset + end_tag)
    body = None
```

Now, `next_level` clearly represents our intent, and if the boundary logic ever changes, it's updated in a single place.
