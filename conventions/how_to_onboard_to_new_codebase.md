# How to onboard to a new codebase

Whenever I onboard to a new codebase, I think about common principles and ways that I like to do it.

Below I diagram the way that I think about onboarding to a new codebase. As you will see I prefer to start outside of the code and to really understand what the purpose and motivation of the codebase is before I do a deeper dive into the code itself. This also applies recursively: I apply the same idea to an individual folder or microservice, where I look at what the code is intended to do, the journeys and the ways that it's supposed to be used, as well as any workflows that it supports, before I actually look at any code.

## Step 1: Get the key context for what problem the codebase solves

This could look like a variety of things. It could be a wiki, design docs, architectural documents, slide decks, or a homepage for the application. Basically I want the highest level of context for what it is that the application is trying to solve in the first place. I want to ideally be able to inspect that myself, try an application, look at a demo video, and so on and so forth.

## Step 2: Inspect key user journeys

How are people supposed to use this app? I want to try the app or software as a user, click around, and know what kinds of user journeys it's supposed to support. I want to know the ideal workflows where everything works correctly. I also want a sense of edge cases that may be tested or expected in the app. As I'm doing this it's giving me a sense for how different components likely fit together under the hood and where the bottlenecks are.

## Step 3: Architecture diagrams

Once I have a sense for the user journeys and the problems that the codebase is supposed to support, I then look at architecture diagrams. I want to see our architecture diagrams of multiple levels of abstraction. First I want to start at the highest possible level of abstraction. This would be an architecture diagram that shows the highest-level services and how they interact together. This could take the form of multiple architecture diagrams, each of which, for example, outlines key workflows in the app. For example in a rag-based application, the highest-level diagrams I would like to see are what happens during online retrieval and offline generation. I want these to be ideally clearly annotated with nice boxes and diagrams that are at the same level of abstraction. For example the retrieval diagram does not have to go into the details about the choice of database or the choice of chunking strategy. It should stay at the level of:
- a user request
- the database
- the types of retrieval that are done or the multiple databases that are referenced at a high level
- a fusion layer
- a serving layer to the end user

Once the highest-level architecture diagrams are done, I also want to see lower-level architecture diagrams of specific components that are particularly important to the operation of the app itself. For example a follow-up to a retrieval diagram would show what actually happens during retrieval. I want to do a deeper dive about:
- what databases are hit
- any sort of caching that's used
- perhaps a discussion on model endpoints that are referenced.

I would like these to be presented in a top-down manner that reads like a narrative, where the highest-level diagrams show the highest-level key interfaces and architecture workflows, and then subsequent diagrams do lower-level dives.

## Step 4: Key interfaces and contracts

Once I have an understanding of the architecture, I want to know the key interfaces and contracts. In particular I want to know which interfaces serve as boundaries between two microservices or two logical layers or units. In addition I want to also know what contracts are preserved across API boundaries or other boundaries, especially if those boundaries include third-party providers. Here I'd like to also know any sort of table schemas as well as how they interface with each other. Like in the previous section I want this presented first at the highest level and then as a deeper dive into specifics. I want reviews to ideally highlight the most critical interfaces and contracts first and then present additional interfaces and contracts as needed and as part of a clean narrative towards understanding the codebase.

## Step 5: Revisiting user journeys, with more detail

Once I've developed a better understanding of the architecture, key interfaces, and contracts, at this point I like to revisit the key user journeys. Given that I'll have better language for understanding it, this can go into more detail and more domain-specific language. In addition it can also do a deeper dive on edge cases and how those are handled. I want to be able to trace the user journeys from end to end as well as understand the points that may require deeper analysis, such as:
- caching layers
- key interfaces
- places that are potential bottlenecks for SLAs

## Step 6: Cross-cutting concerns

I want to understand any cross-cutting concerns that may not be owned by a single owner or microservice but rather are throughout the entire app. Some of these include the model for data consistency and who owns things like deduplication and postprocessing, authentication and who owns it at what layer, and how requests are transformed across service boundaries.

## Step 7: Latest work

Then I want to zoom out to get a state of where the codebase is at and what the team is working on. I want to get a sense for the last commits and PRs that were shipped and what they were delivering towards. Ideally if there are also any documents around architectural planning, design docs, or anything of the sort, I would like to see that as well.

