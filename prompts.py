PROMPTS = {
    "math_proofs": {
        "description": "Helpful prompt for helping me understand and break down math proofs.",
        "prompt": """

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
    }
}