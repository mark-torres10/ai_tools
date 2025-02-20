PROMPTS = {
    "math_proofs": {
        "description": "Helpful prompt for helping me understand and break down math proofs.",
        "prompts": [
            """
            OK, start with a conceptual, geometric interpretation of what the
            problem actually is and the implications of the proof. Why do we care
            about proving this? Set the stage.

            Then, lay out what the implications would be for demonstrating the
            proof in question. What is an example of a practical application where
            this claim being true would matter?

            Then, lay out a multi-step outline of your proof.

            I want your answer in this format:

            **[conceptual, geometric interpretation of what the problem actually is and the implications of the proof]**

            **[Implications would be for demonstrating the proof in question. What is an example of a practical application where this claim being true would matter?]**

            **[Outline]**
            <Step 1>
            <Step 2>
            ...
            <Step n>

            **Start of Proof**

            1. [Claim 1]
            - What the first claim is
            - Why do we care to demonstrate that? How does that get us closer to our proof? What insights does it enable or what alternatives does it remove? How does this narrow the sample space for our solution?
            - Steps to the claim
            - Resolution of the claim
            - Geometric and conceptual interpretation of the claim. What is an example of a practical application where this claim being true would matter?
            - What is unanswered about this claim that we will answer in the next claim.
            2. [Claim 2]
            ...


            **[Conclusion]**
            <conclusion>
            <re-phrase the outline, and how we've demonstrated this proof>
            """
        ]
    },
    "brainstorming": {
        "source": "https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/",
        "description": "Good prompt for greenfield development of a project.",
        "prompts": [
            """
            Ask me one question at a time so we can develop a thorough,
            step-by-step spec for this idea. Each question should build on my
            previous answers, and our end goal is to have a detailed
            specification I can hand off to a developer. Let's do this
            iteratively and dig into every relevant detail. Remember,
            only one question at a time.

            Here's the idea:

            <IDEA>
            """,
            """
            Now that we've wrapped up the brainstorming process, can you
            compile our findings into a comprehensive, developer-ready
            specification? Include all relevant requirements, architecture
            choices, data handling details, error handling strategies, and a
            testing plan so a developer can immediately begin implementation.
            """
        ]
    },
    "tdd_planning": {
        "source": "https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/",
        "description": "Good prompt for TDD planning.",
        "prompts": [
            """
            Draft a detailed, step-by-step blueprint for building this project.
            Then, once you have a solid plan, break it down into small,
            iterative chunks that build on each other. Look at these chunks and
            then go another round to break it into small steps. Review the
            results and make sure that the steps are small enough to be
            implemented safely with strong testing, but big enough to move the
            project forward. Iterate until you feel that the steps are right
            sized for this project.

            From here you should have the foundation to provide a series of
            prompts for a code-generation LLM that will implement each step in
            a test-driven manner. Prioritize best practices, incremental
            progress, and early testing, ensuring no big jumps in complexity at
            any stage. Make sure that each prompt builds on the previous
            prompts, and ends with wiring things together. There should be no
            hanging or orphaned code that isn't integrated into a previous step.

            Make sure and separate each prompt section. Use markdown. Each
            prompt should be tagged as text using code tags. The goal is to
            output prompts, but context, etc is important as well.

            <SPEC>
            """
        ]
    }
}