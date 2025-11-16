# How to Do Mechanistic Interpretability (Research-Grounded Guide)

Purpose: This guide compiles deeply researched, practitioner-grounded methods, patterns, pitfalls, and tools for mechanistic interpretability (MI) of transformer language models. It follows the methodology in the research-grounded persona creation process, documenting sources one-by-one with extracted insights, examples, pitfalls, pro tips, and references for further work.

How to use this guide:
- Start with Phase-oriented methodology and checklists distilled from sources.
- Use the Research Log entries to trace claims back to original expert materials.
- When applying methods, prioritize validation via interventions (e.g., ablations, activation patching) over correlational evidence alone.

---

## Research Log

### Resource 1: A Mathematical Framework for Transformer Circuits (Anthropic)
- **Citation**: Elhage, N.; Nanda, N.; Olsson, C.; Henighan, T.; et al. “A Mathematical Framework for Transformer Circuits.” Anthropic (Dec 22, 2021). [Link](https://transformer-circuits.pub/2021/framework/index.html)
- **Why this is foundational**: Establishes the MI framing for transformers, formalizing residual stream composition, attention as key-value reading/writing, and circuits as composable mechanisms acting via directions in representation space.

**Key Insights:**
- Transformers can be reverse engineered by analyzing computations in the residual stream as linear combinations of interpretable directions (“features”), with attention and MLP blocks writing to and reading from this shared space.
- Mechanistic interpretability aims to identify circuits—minimal sets of components (heads/MLPs/features) whose interaction causally explains a behavior.
- Attention heads often implement specific algorithms (e.g., positional copying, previous token lookup), which can be studied via weight/activation analysis and validated by interventions.
- Decomposition matters: QK (which tokens to attend to) and OV (what content is written) often admit separate mechanistic hypotheses and tests.
- Linear probes/logit lens are useful for hypothesis generation but must be validated causally (e.g., by patching or ablations).

**Notable Quotes (paraphrased/near-quote for brevity):**
- “Reverse engineering transformers is possible by viewing them as programs over a residual stream; attention and MLPs act as read/write operations over directions in this space.”  
- “Mechanistic interpretability should produce falsifiable, causal explanations in terms of circuits rather than correlational descriptions.”

**Examples Captured:**
- ✅ GOOD: Formulate a hypothesis for a head’s function (e.g., previous-token copying), test via attention pattern inspection, then validate by OV intervention that disrupts only that content pathway.
- ✅ GOOD: Separate analysis of QK vs. OV matrices to disambiguate “who to look at” from “what to copy/write,” followed by causal tests.
- ❌ BAD: Using only correlation (e.g., attention pattern visuals) to claim a head’s function without intervention-based validation.
- ❌ BAD: Treating linear probe success as proof of mechanism rather than hypothesis requiring causal confirmation.

**Common Pitfalls:**
- Confusing correlational patterns (attention heatmaps, linear probes) with causal mechanisms; failing to intervene/patch to test hypotheses.
- Over-attributing behaviors to single components rather than circuit interactions spanning multiple layers/heads/MLPs.
- Skipping representation-space reasoning—focusing on weights alone rather than the geometry of the residual stream features.

**Pro Tips:**
- Start with smallest models/tasks exhibiting the behavior; scale up only after validating mechanisms end-to-end with interventions.
- Decompose hypotheses into distinct sub-questions: Which positions are selected (QK)? What information is written (OV/MLP output)? How is it represented in the residual stream?
- Prefer localized interventions (activation/weight patching) that minimally disturb unrelated computation to strengthen causal claims.

**Tools/Frameworks Mentioned/Aligned:**
- Conceptual basis for tools like TransformerLens and subsequent circuit-analysis workflows (e.g., attention head function hypotheses, activation patching).
- Complements feature-level analysis later enabled by sparse autoencoders (SAEs) and path/causal tracing work.

**Why it matters for practice:**
- Provides the core mental model (residual stream + read/write operations + circuits) that underpins most modern MI techniques for transformers.

---

### Resource 2: In-Context Learning and Induction Heads (Anthropic)
- **Citation**: Olsson, C.; Elhage, N.; Nanda, N.; et al. “In-Context Learning and Induction Heads.” Anthropic (Mar 8, 2022). [Link](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)
- **Why this is foundational**: Provides the clearest mechanistic account of a concrete, scalable behavior—induction—implemented by specific attention heads, and links this mechanism to the broader in-context learning phenomenon.

**Key Insights:**
- Induction heads implement an algorithm: when a token repeats, attend from its second occurrence back to the first occurrence, then copy the token following the first occurrence to predict the token following the second (“AB … AB → predict next token after second B equals next after first B”).
- Typical circuit: a pair of heads—a “previous token” (positional) head facilitates the model learning token alignment, and an “induction” head performs the content copy. These emerge reliably with scale.
- Scaling observation: as models scale, induction heads appear consistently and earlier, suggesting they are a favored solution learned by gradient descent for next-token prediction with repeated patterns.
- Mechanistic decomposition: QK focuses on locating the matching earlier token; OV implements copying of the subsequent token’s representation into the residual stream; validation requires interventions/ablations rather than attention maps alone.

**Notable Quotes (paraphrased/near-quote for brevity):**
- “Induction heads are a simple, repeatable algorithm learned by transformers that underpins a significant fraction of in-context learning.”
- “Understanding QK (where to look) vs. OV (what is written) clarifies the copying behavior and enables causal testing.”

**Examples Captured:**
- ✅ GOOD: Use synthetic prompts with repeated name pairs (“John - Paris … John - ?”) to test whether a specific head’s ablation reduces next-token accuracy consistent with induction failing.
- ✅ GOOD: Patch OV outputs of the suspected induction head between source and target prompts to causally transfer the behavior (activation patching).
- ❌ BAD: Claim a head is “doing induction” solely from attention heatmaps without showing causal impact on predictions.
- ❌ BAD: Evaluate only on single-seed prompts; robust MI requires diverse synthetic and natural prompts with controls.

**Common Pitfalls:**
- Confusing frequency-based copying (n-gram heuristics) with true induction circuitry; must validate by tracing position-to-position copying and testing head-specific ablations.
- Ignoring the role of supporting heads/MLP features that set up positional/identity information—induction is usually a circuit, not a single isolated head.

**Pro Tips:**
- Construct controlled minimal prompts (two occurrences of a token pair) and vary distances to stress-test positional generalization.
- Separate QK vs. OV hypotheses: edit/patch them independently to see which subcomponent is necessary/sufficient for the copying effect.
- Measure causal effect size via logit differences and accuracy deltas when ablating only the suspected head(s).

**Tools/Frameworks Mentioned/Aligned:**
- Well-suited to implementation in TransformerLens using hooks for head-specific ablations and activation patching; aligns with later path/causal tracing methods.

**Why it matters for practice:**
- Demonstrates a complete MI workflow from hypothesis → measurement → causal validation on a ubiquitous behavior, serving as a template for other circuits.

---

### Resource 3: Toy Models of Superposition (Anthropic)
- **Citation**: Elhage, N.; Hume, T.; Olsson, C.; et al. “Toy Models of Superposition.” Anthropic (Sept 14, 2022). [Link](https://transformer-circuits.pub/2022/toy_model/index.html) • arXiv: [2209.10652](https://arxiv.org/abs/2209.10652) • Code: [GitHub](https://github.com/anthropics/toy-models-of-superposition)
- **Why this is foundational**: Explains polysemanticity via superposition—models store more sparse features than neuron dimensions by representing features as directions that overlap, challenging neuron-level interpretability and motivating feature-level methods.

**Key Insights:**
- Polysemanticity arises when many sparse features are packed into a lower-dimensional representation; individual neurons combine multiple features rather than mapping 1:1.
- There are phase transitions in representational strategies as feature sparsity/dimensionality trade-offs change; geometry (uniform polytopes) helps explain when superposition emerges.
- Superposition has implications for adversarial examples and overfitting; interference between features can produce brittle behaviors.
- Neuron-level analyses can be systematically misleading in superposition regimes; feature-level/linear subspace analyses are more appropriate.

**Notable Quotes (paraphrased/near-quote for brevity):**
- “Neurons are often polysemantic; the correct unit of understanding is frequently a feature (direction), not a single neuron.”
- “Superposition offers a mechanistic explanation for why clean monosemantic neurons are rare in LLMs.”

**Examples Captured:**
- ✅ GOOD: Train toy sparse-feature ReLU networks and show that the number of represented features exceeds neuron count; visualize interference and phase changes.
- ✅ GOOD: Demonstrate that simple neuron-level feature interpretations break in superposition regimes, while direction-level analysis remains consistent.
- ❌ BAD: Claim global neuron semantics without checking for feature interference or sparsity assumptions.
- ❌ BAD: Use single-neuron ablations as definitive evidence of mechanism in known superposition settings.

**Common Pitfalls:**
- Assuming neuron-level monosemanticity in LLMs; failing to account for overlapping features in the residual stream.
- Overfitting analyses to linear probes on neurons; ignoring that features may live in subspaces/directions shared across many units.

**Pro Tips:**
- Prefer analyses that operate on directions/features (e.g., SAE features, dictionary learning) over single neurons when polysemanticity is suspected.
- Measure interference: quantify how manipulating one feature direction affects others; stress-test with adversarial or rare-feature inputs.
- Use toy models to validate hypotheses before applying to large LLMs; look for the same qualitative phase behavior.

**Tools/Frameworks Mentioned/Aligned:**
- Motivates sparse autoencoders and dictionary learning for feature discovery; complements later “Towards Monosemanticity” and “Scaling Monosemanticity” work.

**Why it matters for practice:**
- Shifts MI focus from neurons to features/directions; informs methodology choice (SAEs, feature viz) and cautions against neuron-level conclusions.

---

### Resource 4: Scaling Monosemanticity — Sparse Autoencoders on Claude 3 Sonnet (Anthropic)
- **Citation**: Templeton, A.; Conerly, T.; Marcus, J.; et al. “Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet.” Anthropic (May 21, 2024). [Link](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) • Overview: [Anthropic blog](https://www.anthropic.com/research/mapping-mind-large-language-model)
- **Why this is foundational**: Demonstrates that sparse autoencoders (SAEs) can extract millions of interpretable features at scale in a production LLM, with behavioral, multilingual, and multimodal evidence and causal validation.

**Key Insights:**
- SAEs recover features that correlate with high-level concepts (e.g., entities, countries, code type signatures) and these features are often causal: activating or ablating them predictably changes model behavior.
- Many features are multilingual and multimodal, suggesting shared abstraction beyond token identity or single-language semantics.
- Engineering stack is critical: high-throughput activation capture, distributed shuffle, and robust training/validation pipelines are necessary to scale feature discovery.
- Feature faithfulness requires validation: dictionary learning can produce artifacts—rigorous causal tests (e.g., targeted activation/ablation) are needed to confirm that features track mechanisms, not dataset biases.

**Notable Quotes (paraphrased/near-quote for brevity):**
- “We extract high-quality, behaviorally causal features at scale from a production model.”
- “Features generalize across languages/modalities, indicating abstraction not tied to surface forms.”

**Examples Captured:**
- ✅ GOOD: Identify a “famous person” feature and show that activating it increases probability of relevant continuations; ablating reduces it across prompts and languages.
- ✅ GOOD: Use controlled interventions to measure causal effect sizes on logits/accuracy; ensure non-target behaviors remain stable (specificity).
- ❌ BAD: Cherry-pick visually appealing features without reporting the distribution of feature quality or causal validation rates.
- ❌ BAD: Assume monosemanticity from sparsity alone; validate with interventions and out-of-distribution prompts.

**Common Pitfalls:**
- Treating SAE features as ground truth units without testing for merging/splitting artifacts or “transcoder” induced distortions.
- Overlooking dataset/activation sampling bias; features can reflect sampling quirks rather than robust mechanisms.

**Pro Tips:**
- Maintain a validation battery: (1) selectivity (feature fires only when intended), (2) causality (activation/ablation effect), (3) robustness (OOD prompts, multilingual), (4) non-target collateral damage.
- Track metrics like sparsity, mutual interference, and faithfulness; automate audits to avoid subjective cherry-picking.
- Build reproducible, distributed activation pipelines early; scaling feature discovery is an engineering problem as much as a science one.

**Tools/Frameworks Mentioned/Aligned:**
- Sparse autoencoders/dictionary learning over residual stream activations; large-scale data infrastructure for activation capture and training; complements feature browsers and causal editors.

**Why it matters for practice:**
- Establishes SAEs as a practical pathway to feature-level MI at modern LLM scale, with standards for causal validation and engineering requirements.

---

### Resource 5: Causal Scrubbing — Rigorous Testing of MI Hypotheses (Redwood Research)
- **Citation**: Chan, L.; Garriga-Alonso, A.; Goldowsky-Dill, N.; et al. “Causal Scrubbing: a method for rigorously testing interpretability hypotheses.” Alignment Forum (Dec 2022). [Main post](https://www.alignmentforum.org/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing) • Sequence: [LessWrong](https://www.lesswrong.com/s/h95ayYYwMebGEYN5y/p/JvZhhzycHu2Yd57RN) • Author page: [Chan 2022](https://chanlawrence.me/publication/chan-2022-causal-scrubbing) • Critique: [Practical Pitfalls](https://www.lesswrong.com/posts/DFarDnQjMnjsKvW8s/practical-pitfalls-of-causal-scrubbing)
- **Why this is foundational**: Provides a principled framework to translate mechanistic hypotheses into resampling distributions over internal activations and then test whether behavior is preserved—offering falsifiable validation beyond ablation heuristics.

**Key Insights:**
- An MI hypothesis implies a set of internal variables that can be resampled (from a reference distribution) without changing output behavior if the hypothesis is correct.
- Causal scrubbing converts hypotheses into behavior-preserving resampling schemes and empirically tests preservation; failure indicates missing/incorrect parts of the mechanism.
- Applied to both algorithmic tasks (paren-balance checker) and LLM induction, refining earlier mechanistic claims.
- Follow-up work documents strengths and limitations: causal scrubbing can validate many correct hypotheses and quantify wrongness, but cannot falsify all incorrect hypotheses (false positives possible).

**Notable Quotes (paraphrased/near-quote for brevity):**
- “Causal scrubbing evaluates hypotheses as claims about which activations can be resampled without changing behavior.”
- “It offers a rigorous, falsifiable interface between informal circuit diagrams and model behavior.”

**Examples Captured:**
- ✅ GOOD: For an induction-head hypothesis, resample non-hypothesized paths while preserving the hypothesized causal path; check if behavior remains unchanged.
- ✅ GOOD: On paren-balance models, design scrubbing interventions that preserve the stack-like mechanism while resampling irrelevant activations.
- ❌ BAD: Using arbitrary ablations (zeroing) as proof of mechanism; scrubbing requires behavior-preserving resampling matched to the hypothesis.
- ❌ BAD: Ignoring failure modes documented in “Practical Pitfalls” (e.g., non-falsifiability of some wrong hypotheses, inadequate reference distributions).

**Common Pitfalls:**
- Assuming scrubbing can falsify any wrong hypothesis; in practice, some incorrect hypotheses can pass tests depending on resampling design.
- Poorly chosen resampling distributions that inadvertently leak information or break preconditions, leading to misleading conclusions.

**Pro Tips:**
- Treat scrubbing as part of a toolkit: combine with activation/weight patching, path patching, and targeted ablations for convergent validation.
- Design multiple independent scrubbing tests per hypothesis; vary resampling schemes to reduce false positives.
- Always report controls and power: how often do scrubs break behavior for nearby counterfactual hypotheses?

**Tools/Frameworks Mentioned/Aligned:**
- General methodology; can be implemented atop frameworks like TransformerLens with hooks for controlled resampling and evaluation.

**Why it matters for practice:**
- Raises the bar for hypothesis testing in MI by requiring behavior-preserving causal tests, not just correlational evidence or blunt ablations.

---

### Resource 6: Causal Tracing & Rank-One Model Editing (ROME) — Localizing and Editing Knowledge (Meng et al.)
- **Citation**: Meng, K.; Bau, D.; Andonian, A.; Belinkov, Y. “Locating and Editing Factual Associations in GPT.” arXiv: [2202.05262](https://arxiv.org/abs/2202.05262) • Project: [rome.baulab.info](https://rome.baulab.info/) • Code: [GitHub](https://github.com/kmeng01/rome)
- **Why this is foundational**: Introduces causal tracing to localize decisive activations for factual predictions and shows that mid-layer MLPs often store editable factual associations; demonstrates direct editing via ROME.

**Key Insights:**
- Causal tracing identifies layers/positions where resampling activations flips or preserves factual predictions, localizing mechanisms involved in recall.
- Mid-layer feed-forward (MLP) modules, at subject token positions, play a decisive role in storing/recalling factual associations in GPT-family models.
- ROME performs targeted rank-one updates to MLP weights to change specific facts, aiming for specificity (edit target fact) and generalization (across phrasings).
- Provides a concrete intervention workflow complementary to MI analysis: localization (causal tracing) → hypothesis → targeted edit → evaluation for side effects.

**Examples Captured:**
- ✅ GOOD: Use subject-identifier prompts to run causal tracing and isolate decisive MLP layers; verify by ablation or activation patching that edits change only the target fact.
- ✅ GOOD: Evaluate edits on counterfactual datasets and paraphrases to ensure generalization and measure unintended side effects.
- ❌ BAD: Claim “knowledge neuron” from correlation without causal tracing; skip post-edit regressions on unrelated facts.
- ❌ BAD: Apply large edits across many layers; ROME is designed for minimal, targeted updates.

**Common Pitfalls:**
- Over-editing causes collateral changes; specificity requires careful localization and minimal updates.
- Evaluating only near-duplicate prompts overestimates success; need paraphrases, negations, and contrast sets.

**Pro Tips:**
- Combine with MI: after identifying a circuit or feature related to a fact, use causal tracing to pinpoint decisive sites, then perform minimal edits and measure global impact.
- Always run a safety battery post-edit: target accuracy, paraphrase generalization, unrelated fact preservation, and downstream task checks.

**Tools/Frameworks Mentioned/Aligned:**
- Public ROME repo with demo notebooks for causal tracing and editing; methodology integrates with hook-based libraries (e.g., TransformerLens) for activation interventions.

**Why it matters for practice:**
- Bridges MI and control: shows that localized, causally identified computations can be surgically modified, with measurable trade-offs in specificity vs. generalization.

---

### Resource 7: TransformerLens — Practical Library for Mechanistic Interpretability (Nanda et al.)
- **Citation**: TransformerLens (formerly EasyTransformer). Docs: [Documentation](https://transformerlensorg.github.io/TransformerLens/) • GitHub: [TransformerLensOrg/TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) • Tutorials: [Tutorials index](https://transformerlensorg.github.io/TransformerLens/tutorials.html) • Activation Patching Demo: [Colab](https://colab.research.google.com/github/TransformerLensOrg/TransformerLens/blob/main/demos/Activation_Patching_in_TL_Demo.ipynb)
- **Why this is foundational**: De facto standard toolkit for MI experiments on GPT-style models, providing hooks to cache/modify activations, head-level interventions, logit attribution utilities, and streamlined workflows for exploratory analysis.

**Key Insights:**
- Hook-based API enables easy capture and intervention at arbitrary points (e.g., `blocks.{layer}.attn.hook_result`, `hook_q`, `hook_k`, `hook_v`, `hook_mlp_out`).
- Built-in utilities for head ablations, activation patching, and component-level logit attributions reduce boilerplate and standardize MI workflows.
- Emphasizes rapid feedback loops and reproducibility (seed control, deterministic runs) to iterate on hypotheses quickly.

**Examples Captured:**
- ✅ GOOD: Implement head-specific OV patching between source and target prompts to test copying/induction hypotheses; report effect sizes on logits/accuracy.
- ✅ GOOD: Use per-layer/component logit attributions to form hypotheses about relevant sites before running causal tests.
- ❌ BAD: Ad-hoc monkey-patching without controlling seeds or caching; hard to reproduce and compare.
- ❌ BAD: Only reporting attention maps; the library supports causal interventions—use them.

**Common Pitfalls:**
- Misinterpreting logit lens/probes as causal evidence; use them for hypothesis generation only.
- Forgetting to neutralize layer norms/residual scaling when comparing patched vs. unpatched runs.

**Pro Tips:**
- Start with small open models (e.g., GPT-2 small) for fast iteration, then replicate on larger checkpoints.
- Create standardized experiment harnesses (prompt sets, metrics, seeds) to compare interventions apples-to-apples.
- Combine with SAE feature extraction libraries to move beyond neuron-level analyses.

**Tools/Frameworks Mentioned/Aligned:**
- Direct integration target for MI techniques (activation/weight patching, path patching, causal scrubbing); commonly paired with visualization and SAE tooling.

**Why it matters for practice:**
- Provides the practical scaffolding to execute MI experiments quickly, reproducibly, and with standard interventions and metrics.

---

### Resource 8: Neel Nanda — Mechanistic Interpretability Guides, Course Materials, and Quickstarts
- **Citation**: Quickstart Guide: [Alignment Jam](https://alignmentjam.com/post/quickstart-guide-for-mechanistic-interpretability) • Prereqs Guide: [Barebones Prerequisites](https://www.neelnanda.io/mechanistic-interpretability/barebones-prereqs) • Collection: [Mechanistic Interpretability — Neel Nanda](https://www.neelnanda.io/mechanistic-interpretability) • Career/learning: [How To Become A MI Researcher](https://www.alignmentforum.org/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher)
- **Why this is useful**: Practical, opinionated guidance on starting and executing MI projects with short feedback loops, including tool usage (TransformerLens), experiment patterns, and concrete project ideas.

**Key Insights:**
- Focus on fast loops: small open models, minimal setup, priority on activation patching and head-level experiments over theory-first deep dives.
- Skill stack: linear algebra/representation geometry, basic PyTorch, transformers internals; heavy emphasis on hands-on experimentation.
- Project-driven learning with curated problem lists; begin with replicable toy problems (modular addition, IOI) and induction circuits.

**Examples Captured:**
- ✅ GOOD: Use standardized demo notebooks (TransformerLens) and expand to hypothesis-driven interventions on known behaviors (induction, IOI).
- ✅ GOOD: Maintain a research log with hypotheses, interventions, metrics, and outcomes; prioritize falsifiable tests.
- ❌ BAD: Spending weeks on environment setup; use Colab/GPU quickstarts to get results quickly.
- ❌ BAD: Jumping to large closed models; start with small open checkpoints.

**Common Pitfalls:**
- Over-indexing on attention map visuals without causal tests.
- Vague goals; not defining success metrics or expected effect sizes before experiments.

**Pro Tips:**
- Replicate canonical MI case studies (induction, IOI) before novel work to calibrate techniques and expected effect sizes.
- Use attribution/activation patching at scale (see “Attribution Patching”) to prioritize promising components for deeper analysis.

**Tools/Frameworks Mentioned/Aligned:**
- TransformerLens; structured notebooks and tutorial ecosystem around MI.

**Why it matters for practice:**
- Provides a pragmatic roadmap and patterns for productive MI research, lowering activation energy for new projects and improving rigor.

---

### Resource 9: OpenAI Microscope — Feature/Neuron Visualization (Vision Models) and Circuits Collaboration
- **Citation**: OpenAI Microscope — About: [microscope.openai.com](https://microscope.openai.com/about) • Circuits collaboration overview: [Distill — Zoom In](https://distill.pub/2020/circuits/zoom-in/)
- **Why this is useful**: Offers a rich reference for feature visualization, neuron/unit-level inspection, and circuits thinking in vision models—methods and intuitions that transfer partially to transformers/LLMs (with caveats due to superposition).

**Key Insights:**
- Feature visualization and unit-level analysis can reveal building blocks in vision models; comparable analyses in LLMs require care due to polysemanticity and superposition.
- Provides a taxonomy of visualization techniques (activation maximization, dataset examples, etc.) and a navigable interface for locating interesting units/circuits in studied models.

**Examples Captured:**
- ✅ GOOD: Use Microscope as methodological inspiration for feature discovery and circuit tracing; translate ideas to LLMs via feature-level (direction/SAE) analyses rather than neurons.
- ❌ BAD: Assume neuron-level interpretability in LLMs as in CNNs; prefer direction/feature methods for language models.

**Common Pitfalls:**
- Over-generalizing from vision to language; representation geometry differs (superposition more severe in LLMs).

**Pro Tips:**
- Borrow visualization/reporting patterns (feature galleries, behavior exemplars, counter-examples) for documenting LLM features discovered via SAEs.

**Why it matters for practice:**
- A mature reference for interpretability visualization craft that can inform how to present and audit LLM features and circuits.

---

### Resource 10: Interpretability in the Wild — Circuit for Indirect Object Identification (Redwood Research)
- **Citation**: Wang, K.; Variengien, A.; Conmy, A.; Shlegeris, B.; Steinhardt, J. “Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small.” arXiv: [2211.00593](https://arxiv.org/abs/2211.00593) • ICLR 2023: [OpenReview PDF](https://openreview.net/pdf?id=NpsVSN6o4ul)
- **Why this is foundational**: One of the most comprehensive end-to-end circuit analyses for a nontrivial natural-language behavior in GPT-2 small, with quantitative evaluation of faithfulness, completeness, and minimality.

**Key Insights:**
- Identifies a circuit spanning ~26–28 attention heads grouped into functional classes (e.g., name movers, S-inhibitors), showing multi-head, multi-layer cooperation.
- Uses a combination of causal interventions and projection methods to propose and validate circuit components.
- Introduces quantitative criteria for explanations: faithfulness (causal), completeness (explains performance), and minimality (no redundant parts).

**Examples Captured:**
- ✅ GOOD: Head-level ablations and targeted interventions that degrade IOI performance consistent with hypothesized roles (e.g., name movers).
- ✅ GOOD: Structured evaluation against metrics (faithfulness, completeness, minimality) rather than qualitative narrative alone.
- ❌ BAD: Asserting a minimal circuit without testing removal of each component or class.
- ❌ BAD: Evaluating on narrow prompt distributions—risk of overfitting the explanation.

**Common Pitfalls:**
- Circuit sprawl: many heads appear relevant; distinguishing necessary vs. incidental components requires rigorous tests and minimality checks.
- Over-reliance on projections without causal validation can misattribute roles.

**Pro Tips:**
- Start with heuristic identification (logit attributions, attention patterns), then narrow with causal ablations and path/activation patching.
- Use quantitative criteria to track progress and prune components; iterate to a minimal, faithful circuit.

**Why it matters for practice:**
- Establishes a template for large-scale, rigorous circuit discovery on natural behaviors beyond toy tasks.

---

### Resource 11: Distributed Alignment Search (DAS) — Causal Abstraction Alignment at Scale
- **Citation**: Wu, Z.; Geiger, A.; Icard, T.; Potts, C.; Goodman, N. “Interpretability at Scale: Identifying Causal Mechanisms in Alpaca.” arXiv: [2305.08809](https://arxiv.org/abs/2305.08809) • NeurIPS 2023 poster: [OpenReview](https://openreview.net/forum?id=nRfClnMhVX)
- **Why this is important**: DAS frames interpretability as finding neural representations aligned to variables in an interpretable causal model; Boundless DAS scales this to larger LLMs (e.g., Alpaca 7B), discovering robust, low-dimensional causal structure for tasks.

**Key Insights:**
- Causal abstraction: define a high-level symbolic model of the task and search for neural variables that instantiate its nodes and edges.
- Boundless DAS learns alignment parameters (replacing brute force) to efficiently find distributed neural representations implementing the abstract causal model.
- Demonstrates robustness of discovered variables across inputs/instructions for a simple numerical reasoning task in Alpaca.

**Examples Captured:**
- ✅ GOOD: Specify a minimal causal graph for the task (e.g., two boolean variables), then use DAS to discover corresponding neural variables and validate via interventions.
- ❌ BAD: Post-hoc mapping from arbitrary probes to variables without showing causal correspondence or generalization.

**Common Pitfalls:**
- Overfitting the abstract model to idiosyncrasies of the dataset; test across instruction variants and input distributions.

**Pro Tips:**
- Combine MI circuit hypotheses with DAS by using features/circuit nodes as candidate variables in the causal abstraction, then verify with DAS alignment and interventions.

**Why it matters for practice:**
- Offers a principled route to “top-down” mechanistic explanations tied to explicit causal models, complementary to “bottom-up” circuit discovery.

---

### Resource 12: Softmax Linear Units (SoLU) — Increasing Neuron Interpretability (Anthropic)
- **Citation**: Elhage, N.; Hume, T.; Olsson, C.; Nanda, N.; et al. “Softmax Linear Units.” Anthropic (June 27, 2022). [Link](https://transformer-circuits.pub/2022/solu/index.html) • Overview: [Anthropic research page](https://www.anthropic.com/research/softmax-linear-units)
- **Why this is useful**: Introduces SoLU activations for MLPs, empirically increasing the fraction of neurons that appear interpretable while noting trade-offs with superposition.

**Key Insights:**
- Replacing standard activations with SoLU increases observed neuron-level interpretability (more neurons respond to articulable features) with minimal performance cost in tested settings.
- Even with SoLU, superposition persists: some features may become more interpretable while others become “hidden,” implying no free lunch.
- Architectural choices can materially affect interpretability; MI is not only post-hoc analysis but also about designing models to be more legible.

**Examples Captured:**
- ✅ GOOD: Train small transformers with and without SoLU, then run blinded neuron interpretability evaluations; compare fraction of interpretable units and performance metrics.
- ✅ GOOD: Use SoLU models to derive new mechanistic insights on MLP processing pathways; validate with interventions.
- ❌ BAD: Assume SoLU eliminates superposition; it shifts the landscape and requires renewed causal validation.
- ❌ BAD: Generalize findings to all model sizes/tasks without replication.

**Common Pitfalls:**
- Overstating neuron interpretability improvements as mechanism discovery; still need causal tests at feature/circuit level.
- Ignoring potential feature “hiding” effects—run SAE/feature analyses to check what became less legible.

**Pro Tips:**
- Consider SoLU when running MI case studies that rely on neuron-level inspection; pair with SAE feature discovery to cover hidden features.
- Benchmark interpretability changes alongside downstream performance to establish acceptable trade-offs.

**Why it matters for practice:**
- Highlights that small architectural tweaks can improve legibility; encourages co-design of architectures and MI workflows.

---

### Resource 13: Towards Monosemanticity — Dictionary Learning in a One-Layer Transformer (Anthropic)
- **Citation**: Bricken, T.; Templeton, A.; Batson, J.; et al. “Towards Monosemanticity: Decomposing Language Models With Dictionary Learning.” Anthropic (Oct 4, 2023). [Link](https://transformer-circuits.pub/2023/monosemantic-features/index.html) • Overview: [Anthropic blog](https://www.anthropic.com/research/towards-monosemanticity)
- **Why this is foundational**: Shows that sparse autoencoders/dictionary learning can decompose a small transformer layer into thousands of features corresponding to interpretable patterns, motivating feature-level analysis over neuron-level.

**Key Insights:**
- Features (directions) recovered by dictionary learning align with human-interpretable patterns (e.g., DNA sequences, legal language, HTTP requests), often invisible at the single-neuron level due to superposition.
- A single layer with hundreds of neurons can be decomposed into thousands of sparse features, supporting feature-based MI rather than neuron-based.
- Provides concrete methodology and visualization for browsing features and linking them to behaviors.

**Examples Captured:**
- ✅ GOOD: Train an SAE on residual activations of a one-layer transformer; qualitatively label features; test causal relevance via activation/ablation.
- ✅ GOOD: Compare neuron-level probes vs. feature-level analyses to show visibility gains under superposition.
- ❌ BAD: Treat SAE features as ground truth without causal tests; some features may be merged/split artifacts.
- ❌ BAD: Assume small-model results trivially scale without engineering/validation (addressed later by Scaling Monosemanticity).

**Common Pitfalls:**
- Confusing interpretability of discovered features with completeness of decomposition; maintain skepticism and validate causally.

**Pro Tips:**
- Use feature browsers and curated prompt sets to stress-test semantics; check multilingual/format robustness where applicable.
- Pair dictionary learning with causal interventions (patching) and selectivity metrics to assess faithfulness.

**Why it matters for practice:**
- Establishes the core feature-discovery paradigm that later scales to production LLMs; anchors many modern MI workflows around directions/features rather than neurons.

---

### Resource 14: The Engineering Challenges of Scaling Interpretability (Anthropic)
- **Citation**: Anthropic. “The engineering challenges of scaling interpretability.” (Jun 13, 2024). [Link](https://www.anthropic.com/research/engineering-challenges-of-scaling-interpretability)
- **Why this is important**: Details the practical systems and infra required to scale SAE training and interpretability workflows to production LLMs, highlighting engineering bottlenecks and solutions.

**Key Insights:**
- Interpretability-at-scale is as much an engineering problem as a scientific one: high-throughput activation capture, distributed shuffles, and efficient training loops are critical.
- Data pipelines matter: activation sampling bias, shuffling correctness, and storage/IO throughput directly impact feature quality and reproducibility.
- Robust validation infra (metric tracking, dashboards, automated audits) is needed to quantify feature faithfulness, sparsity, interference, and collateral effects.

**Examples Captured:**
- ✅ GOOD: Implement distributed activation capture and shuffle to avoid modality/language biases; verify via stratified stats and spot checks.
- ✅ GOOD: Build regression tests for feature faithfulness (activation/ablation effects) and stability across model updates.
- ❌ BAD: Training SAEs on convenience samples of activations; leads to brittle or spurious features.
- ❌ BAD: Manual, ad-hoc validation without metrics/dashboards; not scalable or trustworthy.

**Common Pitfalls:**
- Silent drift in activation sampling distributions over time; breaks comparability of features.
- Under-provisioned storage/IO stalls the pipeline; GPU utilization collapses.

**Pro Tips:**
- Treat interpretability as a data platform: version activations, SAEs, and validation suites; enforce schema and lineage.
- Automate power analyses for intervention tests (how big an effect can you detect?).
- Co-design with product constraints (cost, latency) to make large-scale feature discovery sustainable.

**Why it matters for practice:**
- Provides a playbook for making interpretability work on modern LLMs, turning promising science into reliable, repeatable systems.

---

### Resource 15: Circuit Tracing — Attribution Graphs via Cross-Layer Transcoders (Anthropic, 2025)
- **Citation**: Ameisen, E.; Lindsey, J.; Pearce, A.; Gurnee, W.; Turner, N. L.; Chen, B.; Citro, C.; et al. “Circuit Tracing: Revealing Computational Graphs in Language Models.” Anthropic (Mar 27, 2025). [Link](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
- **Why this is important**: Introduces cross-layer transcoders (CLTs) to build replacement models that approximate MLPs, enabling attribution graphs (“circuit tracing”) that visualize and validate computational pathways for behaviors in multi-layer LLMs.

**Key Insights:**
- Replacement-model approach: train a more interpretable component (CLT) to approximate hard-to-interpret MLPs, allowing step-by-step tracing of computation.
- Attribution graphs represent token-to-feature-to-output computation on specific prompts, offering a graph view of circuits rather than isolated heads/features.
- Provides validation tools and interventions to test whether proposed attribution paths are behaviorally causal.

**Examples Captured:**
- ✅ GOOD: Fit CLTs, generate attribution graphs for a simple behavior in an 18-layer model, then perform targeted interventions to confirm causal pathways.
- ✅ GOOD: Compare native vs. replacement model behavior on held-out prompts to quantify approximation fidelity before drawing conclusions.
- ❌ BAD: Interpreting attribution graphs without validating CLT fidelity; risks artifacts from approximation error.
- ❌ BAD: Treating single-prompt graphs as universal; behaviors can vary with context.

**Common Pitfalls:**
- Overconfidence in replacement-model explanations; always report approximation metrics and residuals.
- Missing alternative routes: graphs may omit parallel contributing paths; test for completeness.

**Pro Tips:**
- Use circuit tracing alongside SAE features and activation/weight patching to triangulate mechanisms.
- Document both graph topology and quantitative causal effects (logits/accuracy deltas) for each validated edge.

**Why it matters for practice:**
- Scales circuit explanations to deeper models by making MLP pathways tractable, turning qualitative circuits into concrete, validated computation graphs.

---

### Resource 16: Tracing Attention Computation Through Feature Interactions (Anthropic, 2025)
- **Citation**: Kamath, H.; Ameisen, E.; Lindsey, J.; et al. “Tracing Attention Computation Through Feature Interactions.” Anthropic (Jul 31, 2025). [Link](https://transformer-circuits.pub/2025/attention-qk/index.html)
- **Why this is important**: Connects attention patterns to underlying feature interactions, explaining QK selection via interpretable features and integrating these into attribution graphs.

**Key Insights:**
- Attention (QK) can be decomposed into interactions between discovered features (e.g., SAE features), clarifying why specific query tokens attend to specific keys.
- Mapping feature-to-feature interactions helps translate coarse attention heatmaps into mechanistic, feature-level explanations.
- Integration with attribution graphs offers end-to-end views from features → attention selection → downstream computation.

**Examples Captured:**
- ✅ GOOD: Identify salient features for queries and keys; show that manipulating these features changes the attention distribution as predicted.
- ✅ GOOD: Embed feature-interaction edges into an attribution graph and validate by localized interventions (feature activations/ablations) affecting attention.
- ❌ BAD: Infer causality from static attention maps without feature-level interventions.
- ❌ BAD: Assume a single feature explains an attention edge; multiple interacting features may contribute.

**Common Pitfalls:**
- Overlooking layernorm/residual scaling effects when comparing patched vs. unpatched attention.
- Ignoring alternative competing key candidates; must evaluate against distractors.

**Pro Tips:**
- Pair with SAE features to propose candidate Q/K feature sets; validate by selective feature patching before and after the attention op.
- Quantify changes via KL-divergence between attention distributions and logit impacts downstream.

**Why it matters for practice:**
- Bridges the gap between attention visualizations and concrete mechanisms by rooting attention choices in interpretable feature interactions.

---

### Resource 17: Emergent Linear Representations in Othello-GPT World Models (Nanda et al., 2023)
- **Citation**: Nanda, N.; Lee, A.; Wattenberg, M. “Emergent Linear Representations in World Models of Self-Supervised Sequence Models.” arXiv: [2309.00941](https://arxiv.org/abs/2309.00941) • BlackboxNLP 2023: [Proceedings PDF](https://aclanthology.org/2023.blackboxnlp-1.2.pdf)
- **Why this is important**: Demonstrates linear, controllable world-state representations in an Othello-trained transformer, enabling direct manipulation and interpretation of internal state via simple vector arithmetic.

**Key Insights:**
- The model encodes board state with approximately linear features, including “my colour” vs. “opponent’s colour,” enabling interpretable probes and interventions.
- Linear representations allow understanding and control of model behavior across prompts, supporting a mechanistic account of internal state tracking.

**Examples Captured:**
- ✅ GOOD: Use linear probes to read board state; verify by causal interventions that shifting state vectors alters predicted moves appropriately.
- ✅ GOOD: Show portability of representations across contexts/prompts; analyze how features are computed across layers.
- ❌ BAD: Treat probe accuracy as causal proof without interventions; probes can be correlational.
- ❌ BAD: Assume linearity for all tasks; this is a task-specific case study.

**Common Pitfalls:**
- Over-generalizing from Othello to complex LLM tasks; validate generality before extrapolating.

**Pro Tips:**
- Use Othello-GPT as a sandbox for MI techniques: fast iterations and clear ground truth states make it ideal for methodology development.

**Why it matters for practice:**
- Offers a concrete case where world-state is legible and controllable, illustrating how linear features can ground mechanistic explanations and interventions.

---

### Resource 18: Modular Addition & Grokking — Reverse-Engineered Circuits (Nanda et al., 2022–2023)
- **Citation**: Nanda, N.; Chan, L.; Lieberum, T.; Smith, J.; Steinhardt, J. “Progress Measures for Grokking via Mechanistic Interpretability.” arXiv: [2301.05217](https://arxiv.org/abs/2301.05217) • Walkthroughs: [Part 1–3](https://www.neelnanda.io/modular-addition-walkthrough)
- **Why this is important**: Fully reverse-engineers a transformer trained on modular addition, showing a trig/DFT-based algorithm and using interventions (including Fourier-space) to validate the mechanism; frames “grokking” in terms of circuit formation.

**Key Insights:**
- The learned algorithm converts addition to rotations on a circle via discrete Fourier transforms, realized by interpretable circuits in attention/MLP.
- Grokking emerges from gradual amplification of structured mechanisms and later removal of memorizing components—measurable via progress metrics.

**Examples Captured:**
- ✅ GOOD: Read out algorithm steps from weights and activations; confirm by ablations in Fourier space that disrupt specific algorithmic steps.
- ✅ GOOD: Track training dynamics using progress measures—memorization → circuit formation → cleanup—aligned with mechanistic findings.
- ❌ BAD: Treat end-line accuracy jump as “mysterious” without analyzing intermediate circuits.
- ❌ BAD: Skip DFT-based analysis; miss the core mechanism.

**Common Pitfalls:**
- Assuming conclusions transfer to unrelated tasks without verifying analogous structures.

**Pro Tips:**
- Use Fourier-domain tools to inspect/rescale components when tasks imply periodic structure.

**Why it matters for practice:**
- A canonical case study of complete circuit reverse-engineering, linking quantitative progress measures to concrete mechanisms.

---

### Resource 19: MEMIT — Mass Editing Memory in a Transformer (ICLR 2023)
- **Citation**: Meng, K.; Sen Sharma, A.; Andonian, A.; Belinkov, Y.; Bau, D. “Mass-Editing Memory in a Transformer.” ICLR 2023. Project: [memit.baulab.info](https://memit.baulab.info/) • Paper: [OpenReview PDF](https://openreview.net/pdf?id=MkbcAHIYgyS)
- **Why this is important**: Scales direct knowledge editing from single facts to thousands of edits, showing practical methods to update factual associations in LLMs with measured specificity and generalization.

**Key Insights:**
- Extends localized editing (e.g., ROME) to batch edit many facts; demonstrates feasibility on GPT-J and GPT-NeoX.
- Evaluates tradeoffs between specificity (target fact changes) and generalization (across phrasings) while minimizing collateral damage.

**Examples Captured:**
- ✅ GOOD: Run post-edit regression tests: target accuracy, paraphrase generalization, unrelated fact preservation, and downstream tasks.
- ✅ GOOD: Compare against alternative editors; quantify number of successful edits vs. side effects.
- ❌ BAD: Perform large-scale edits without safety metrics; risks widespread unintended behavior changes.

**Common Pitfalls:**
- Ignoring locality: insufficiently targeted edits may affect related concepts.

**Pro Tips:**
- Combine with causal tracing to localize decisive layers/positions first, then apply MEMIT; measure impact comprehensively.

**Why it matters for practice:**
- Demonstrates that knowledge can be systematically and scalably edited, bridging MI insights with practical control over model behavior.

---

### Resource 20: Superposition, Memorization, and Double Descent (Anthropic, 2023)
- **Citation**: Henighan, T.; Carter, S.; Hume, T.; Elhage, N.; et al. “Superposition, Memorization, and Double Descent.” Anthropic (Jan 5, 2023). [Link](https://transformer-circuits.pub/2023/toy-double-descent/index.html)
- **Why this is important**: Extends the superposition program to the overfitting regime, connecting memorization and double descent phenomena to representational superposition and interpretability challenges.

**Key Insights:**
- Overfitting and memorization interact with superposition; feature interference can explain brittle behaviors and generalization dips.
- Understanding transitions between under/overfitting regimes is critical for interpreting when neuron/feature analyses are reliable.

**Examples Captured:**
- ✅ GOOD: Track representational changes across training phases; relate feature interference metrics to validation/generalization behavior.
- ✅ GOOD: Use toy models to isolate mechanisms and generate hypotheses for LLM-scale experiments.
- ❌ BAD: Assume conclusions without measuring interference or testing generalization.

**Common Pitfalls:**
- Conflating correlation with mechanism; need interventions and robust measurements.

**Pro Tips:**
- Monitor interference and sparsity metrics alongside performance during training to detect shifts towards memorization.

**Why it matters for practice:**
- Offers a mechanistic lens on generalization pathologies and informs when feature-level approaches are likely to succeed.

---

### Resource 21: Zoom In — An Introduction to Circuits (Distill, 2020)
- **Citation**: Olah, C.; Cammarata, N.; Schubert, L.; Goh, G.; Petrov, M.; Carter, S. “Zoom In: An Introduction to Circuits.” Distill (Mar 10, 2020). [Link](https://distill.pub/2020/circuits/zoom-in/)
- **Why this is important**: Foundational overview of the Circuits agenda for mechanistically understanding neural networks by analyzing the connections between neurons and interpreting them as implementing human-comprehensible algorithms.

**Key Insights:**
- Proposes the notion of neural “circuits”: directed acyclic graphs over interpretable features implemented by weights and activations, enabling mechanistic explanations.
- Emphasizes dissecting early vision models (InceptionV1) to show how simple features compose into higher-level detectors, motivating analogous work in transformers.
- Advocates a research methodology: iterative hypothesis, visualization, intervention (e.g., ablation), and rigorous validation.

**Examples Captured:**
- ✅ GOOD: Decompose a convnet’s layer into interpretable units (e.g., curve detectors) and trace how they combine to form object detectors.
- ✅ GOOD: Use feature visualization and path-based analyses to propose circuit hypotheses and test via ablations.
- ❌ BAD: Treat attention or neuron activations as explanations without demonstrating causal roles in task performance.

**Common Pitfalls:**
- Conflating correlation with mechanism; failing to validate visualizations with interventions.
- Overfitting to cherry-picked visualizations without checking generalization across datasets.

**Pro Tips:**
- Use Distill’s interactive tools (feature visualization, activation atlases) to generate hypotheses; confirm with causal tests (ablation/patching).
- Translate these ideas to transformers by focusing on QK/OV decomposition and feature-level circuits (see Resources 2, 16).

**Why it matters for practice:**
- Establishes the core conceptual toolkit for mechanistic interpretability that later works (induction heads, SAEs, circuit tracing) build upon.

---

### Resource 22: Early Vision Circuits — InceptionV1 (Distill, 2020)
- **Citations**: Olah, C. et al. “An Overview of Early Vision in InceptionV1.” Distill (Apr 1, 2020). [Link](https://distill.pub/2020/circuits/early-vision/). See also companion deep-dives like [“Curve Detectors”](https://distill.pub/2020/circuits/curve-detectors/).
- **Why this is important**: Provides a rigorous template for identifying and validating interpretable features (edges, colors, curves) and their composition into higher-level detectors, establishing analysis patterns (feature visualization, path tracing, ablation) that generalize to transformer circuits.

**Key Insights:**
- Early convolutional layers learn Gabor-like edge detectors and color opponency; mid-level layers implement combinations (e.g., curves, corners) via weighted sums and nonlinearities.
- Path-tracing shows how features in lower layers causally contribute to activations in higher layers — a precursor to transformer path/attribution tracing (see Resource 16).

**Examples Captured:**
- ✅ GOOD: Use network dissection plus activation maximization to cluster neurons by feature semantics (edges, textures) and verify via ablation.
- ✅ GOOD: Trace specific feature synthesis (e.g., curves from oriented edges), demonstrating compositional circuits.
- ❌ BAD: Over-interpreting individual neuron images without corroborating causal tests (ablation/retargeted optimization).

**Common Pitfalls:**
- Confusing dataset biases (e.g., texture biases) with inherent architectural properties; control for confounds.

**Pro Tips:**
- Reproduce the Distill notebooks; adapt feature visualization to transformer MLP neurons and attention patterns to bootstrap hypotheses.

**Why it matters for practice:**
- These techniques underpin later transformer MI work by showing how to systematically extract, visualize, and validate building-block features and their compositions.

---

### Resource 23: Multimodal Neurons in Artificial Neural Networks (OpenAI/Distill, 2021)
- **Citation**: Goh, G.; Cammarata, N.; Voss, C.; et al. “Multimodal Neurons in Artificial Neural Networks.” Distill (Mar 4, 2021). [Link](https://distill.pub/2021/multimodal-neurons/) • OpenAI blog: [overview](https://openai.com/index/multimodal-neurons/)
- **Why this is important**: Reveals single neurons in CLIP that respond to high-level concepts across modalities (e.g., text “Halle Berry”, photos, sketches), illustrating how feature detectors can be multimodal and semantically rich — a caution and opportunity for LLM interpretability.

**Key Insights:**
- CLIP’s late-layer units often act as “multimodal neurons,” responding to semantic concepts rather than low-level stimuli, paralleling biological "grandmother"/"Halle Berry" neurons.
- Multimodality amplifies polysemanticity and introduces new failure modes (e.g., typographic attacks), underscoring the need for feature-level, causally grounded analysis.

**Examples Captured:**
- ✅ GOOD: Identifying person/region/emotion neurons that activate across images and text tokens; probing via feature visualizations and curated stimuli.
- ✅ GOOD: Demonstrating typographic attacks where text tokens hijack visual neurons; motivates robustness-aware interpretation.
- ❌ BAD: Treating a neuron’s top-activating images as full explanation; must test causal relevance and out-of-distribution behavior.

**Common Pitfalls:**
- Over-ascribing semantics to units without considering distributed codes and feature entanglement.

**Pro Tips:**
- Use feature-aligned analyses (e.g., SAEs) to separate genuinely semantic sub-features from entangled neuron responses in multimodal LMs.

**Why it matters for practice:**
- Anticipates and contextualizes multimodal feature detectors in LMMs, guiding both interpretability tooling and robustness evaluations.

---

### Resource 24: Transformer Feed‑Forward Layers Are Key‑Value Memories (EMNLP 2021)
- **Citation**: Geva, M.; Schuster, R.; Berant, J.; Levy, O. “Transformer Feed‑Forward Layers Are Key‑Value Memories.” EMNLP 2021. [ACL PDF](https://aclanthology.org/2021.emnlp-main.446.pdf) • [arXiv](https://arxiv.org/abs/2012.14913) • [Code](https://github.com/mega002/ff-layers)
- **Why this is important**: Establishes that transformer MLPs act as key–value memory systems with human-interpretable keys and value distributions, shaping next-token predictions — a key pillar for feature-level MI and model‑editing methods (cf. Resource 6, 19).

**Key Insights:**
- MLP “keys” match textual patterns in context; “values” encode distributions over next tokens; the MLP output is a learned mixture of value vectors.
- Lower layers capture local/syntactic patterns; higher layers encode more semantic abstractions, aligning with circuit‑level interpretations.

**Examples Captured:**
- ✅ GOOD: Identify specific MLP neurons whose keys fire on phrases (e.g., “such as”) and whose values amplify appropriate next tokens.
- ✅ GOOD: Demonstrate that suppressing key/value pairs changes predictions in interpretable, causal ways.
- ❌ BAD: Assuming attention alone explains predictions; MLP memories often dominate next‑token mass in later layers.

**Common Pitfalls:**
- Ignoring interactions: MLP memory composition is shaped by residual streams and attention; analyze full paths, not layers in isolation.

**Pro Tips:**
- Use key/value probing to generate hypotheses; validate via activation/value patching and editing (ROME/MEMIT) at specific MLP layers.

**Why it matters for practice:**
- Guides where and how to intervene in LMs (e.g., value vector editing), and motivates using SAEs to decompose MLP activations into interpretable features.

---

### Resource 25: A Comprehensive Mechanistic Interpretability Explainer & Glossary (Nanda, 2022)
- **Citation**: Nanda, N. “A Comprehensive Mechanistic Interpretability Explainer & Glossary.” (Dec 21, 2022). [Link](https://www.neelnanda.io/mechanistic-interpretability) • Full glossary: [Dynalist](https://neelnanda.io/glossary)
- **Why this is important**: A practitioner‑oriented reference that consolidates terminology, key results, workflows, and failure modes in transformer MI. Useful for onboarding teams and aligning vocabulary across research & engineering.

**Key Insights:**
- Defines core MI primitives (features, directions, circuits, attention heads, MLP key/value pairs, logit lens, activation/gradient methods) and how they relate.
- Emphasizes causal evaluation (ablation/patching) over purely correlational probes; discusses pitfalls (polysemanticity, gradient saturation, dataset confounds).
- Outlines practical workflows for reverse‑engineering circuits and building interpretable tooling (e.g., with TransformerLens; see Resource 7).

**Examples Captured:**
- ✅ GOOD: Walkthroughs of grokking analysis (Resource 18), Othello world‑model (Resource 17), and attribution patching (Resource 26).
- ✅ GOOD: Decision trees for when to use probes vs. SAEs vs. patching; framing MI as program synthesis over features.
- ❌ BAD: Treating saliency or linear probes as sufficient proof of mechanism without interventions.

**Pro Tips:**
- Start with small, synthetic tasks to practice end‑to‑end MI workflows; then transfer to larger LMs.
- Maintain a research log and a phase‑structured rubric (cf. this guide) to avoid cargo‑culting results.

**Why it matters for practice:**
- A living guide capturing community best practices; accelerates ramp‑up and helps avoid common errors in applied mechanistic analysis.

---

### Resource 26: Attribution Patching — Activation Patching at Scale (Nanda, 2023)
- **Citation**: Nanda, N. “Attribution Patching: Activation Patching At Industrial Scale.” (Mar 2023). [Article](https://www.neelnanda.io/mechanistic-interpretability/attribution-patching) • [AF/LW write‑up](https://www.alignmentforum.org/posts/gtLLBhzQTG6nKTeCZ/attribution-patching-activation-patching-at-industrial-scale) • Demo Colab: [link](https://neelnanda.io/attribution-patching-demo)
- **Why this is important**: Makes causal tracing (activation patching) scalable to larger LMs by approximating the effect of many localized interventions via gradient‑based attribution, enabling broad search over candidate sites.

**Key Insights:**
- Classic activation patching (swap activation from counterfactual run) is principled but expensive (O(#probes) forward passes). Attribution patching uses gradients to estimate effects in one backward pass.
- Attribution can triage promising hooks/positions for subsequent exact patching and more rigorous counterfactual validation (cf. Resource 16).

**Examples Captured:**
- ✅ GOOD: Use attribution scores to select top‑k attention heads/MLP neurons for exact path/activation patching; validate causal contribution to a behavior (e.g., IOI).
- ✅ GOOD: Compare attribution‑based ranking vs. brute‑force patching to quantify precision/recall.
- ❌ BAD: Rely solely on attribution scores as causal proof; treat them as hypotheses, not evidence.

**Common Pitfalls:**
- Gradient saturation or nonlinearity can mislead linear approximations; always confirm with true interventions.

**Pro Tips:**
- Combine with feature‑level hooks (e.g., SAE activations) to probe causality at the right abstraction level.

**Why it matters for practice:**
- Lowers the cost of exploratory MI, making it feasible to scan large models and iterate quickly toward high‑impact causal hypotheses.

---

### Resource 27: RAVEL — Evaluating Interpretability on LM Representations (ACL 2024)
- **Citation**: Huang, J.; Wu, Z.; Potts, C.; Geva, M.; Geiger, A. “RAVEL: Evaluating Interpretability Methods on Disentangling Language Model Representations.” ACL 2024. [Paper](https://aclanthology.org/2024.acl-long.470/) • [ArXiv](https://arxiv.org/html/2402.17700v2) • [Benchmark repo](https://github.com/explanare/ravel)
- **Why this is important**: Provides a controlled benchmark to assess whether MI methods (probes, SAEs, MDAS, etc.) can localize and causally validate disentangled features for LM‑encoded attributes (e.g., entity properties), pushing the field toward rigorous, comparable evaluation.

**Key Insights:**
- Introduces a suite of tasks with known ground truth factorization (attributes per entity), enabling objective measurement of feature localization and causal isolation.
- Proposes Multi‑task Distributed Alignment Search (MDAS) to find feature subspaces satisfying multiple causal criteria, outperforming neuron‑level baselines.

**Examples Captured:**
- ✅ GOOD: Using MDAS to identify feature subspaces for attributes like number, tense, or country across LLaMA‑2 layers; verifying causal control via interventions.
- ✅ GOOD: Comparing SAEs, probing, and MDAS on standardized metrics.
- ❌ BAD: Relying on single‑neuron explanations in contexts with heavy polysemanticity.

**Pro Tips:**
- Incorporate RAVEL tasks in your CI to regression‑test MI improvements and guard against overfitting or spurious features.

**Why it matters for practice:**
- Establishes shared yardsticks for MI methods in LLMs, enabling evidence‑based selection of techniques for production‑grade interpretability.

---

### Resource 28: Interchange Intervention Training for Typed Structure in LMs (ACL 2023)
- **Citation**: Huang, J.; Wu, Z.; Mahowald, K.; Potts, C. “Inducing Character‑level Structure in Subword‑based Language Models with Type‑level Interchange Intervention Training.” Findings of ACL 2023. [PDF](https://aclanthology.org/2023.findings-acl.770.pdf) • [ArXiv](https://arxiv.org/html/2212.09897v2) • [Code](https://github.com/explanare/char-iit)
- **Why this is important**: Demonstrates how to inject human‑interpretable, typed character‑level structure into subword LMs via explicit causal intervention training (IIT), improving robustness and interpretability on character‑manipulation tasks.

**Key Insights:**
- Treats characters as typed variables in a causal model; aligns LM internal representations with these variables using interchange interventions during training.
- Yields interpretable character features and boosts generalization on tasks like spelling correction and anagram solving where subword LMs struggle.

**Examples Captured:**
- ✅ GOOD: Enforcing that the representation of a character is consistent across contexts by swapping in type‑level features; measuring causal impact on downstream predictions.
- ✅ GOOD: Benchmarks showing gains over standard subword LMs and competitive performance with character‑level models on mixed semantic/form tasks.
- ❌ BAD: Assuming character‑level structure suffices for all linguistic phenomena without addressing compositional semantics.

**Why it matters for practice:**
- A concrete recipe to steer LM internals toward desired, human‑interpretable factorization, complementing post‑hoc MI and editing methods.

---

### Resource 29: Logit Lens — Layerwise Readout of Model Beliefs (nostalgebraist, 2020)
- **Citation**: nostalgebraist. “inter﻿preting GPT: the logit lens.” (Aug 31, 2020). [LessWrong](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens) • [Alignment Forum](https://www.alignmentforum.org/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)
- **Why this is important**: A simple but powerful diagnostic: apply the unembedding matrix to intermediate residual stream states to inspect token‑level predictions across layers. Useful for hypothesis generation and rapid debugging of circuits.

**Key Insights:**
- Many layers progressively refine distributions; some layers make “early guesses” that are later corrected — patterns that can hint at where mechanisms reside.
- Combined with logit attribution and path/activation patching, the logit lens helps localize influential layers/heads for a behavior.

**Examples Captured:**
- ✅ GOOD: Identify the layer where a factual association first becomes linearly decodable; target that region for causal tracing/editing (cf. ROME/MEMIT).
- ✅ GOOD: Compare lens outputs on base vs. counterfactual prompts to spot layers sensitive to the manipulated factor.
- ❌ BAD: Treat lens decodability as causal proof; it is a readout, not an intervention.

**Pro Tips:**
- Calibrate lens quality (e.g., with learned linear probes or logit prism variants) and corroborate with interventions.

**Why it matters for practice:**
- Fast, low‑overhead tool to guide deeper MI analysis, especially in larger models where exhaustive patching is expensive.

---

### Resource 30: Understanding RL Vision (Distill, 2020) — Lessons for MI
- **Citation**: Hilton, J.; Cammarata, N.; Carter, S.; Goh, G.; Olah, C. “Understanding RL Vision.” Distill (Nov 2020). [Link](https://distill.pub/2020/understanding-rl-vision/) • [Code](https://github.com/openai/understanding-rl-vision)
- **Why this is important**: Though focused on RL vision, this work exemplifies the circuits methodology: interactive inspection, targeted ablations, and distribution‑aware evaluation — patterns directly transferable to transformer MI.

**Key Insights:**
- Feature visualization and circuit editing can induce systematic behavioral changes (e.g., blinding to left‑moving enemies), providing strong causal evidence of mechanisms.
- Proposes the “diversity hypothesis” — richer, more diverse training distributions foster more interpretable features at matched abstraction levels.

**Examples Captured:**
- ✅ GOOD: Use procedurally generated datasets to avoid overfitting visualizations; validate hypotheses by forcing failures consistent with the proposed mechanism.
- ❌ BAD: Ignoring dataset shift when interpreting features; conclusions may not generalize without diverse inputs.

**Why it matters for practice:**
- Reinforces the value of hypothesis‑driven interventions and diverse evaluation in MI, especially when porting techniques to LLMs and multimodal models.
