# AI-Driven Discovery of Fundamental Constants in Physical Phenomena

## Introduction
Understanding the emergence of fundamental constants, such as \(\pi\), in physics has been a cornerstone of scientific inquiry. This project explores whether AI can autonomously detect and hypothesize mathematical structures underlying physical laws by analyzing numerical simulations. Precisely, our AI model successfully rediscovered pi from a classical mechanics simulation involving elastic collisions, and has also completely discovered the underlying relation that was the cause of the emergence of pi.

## Background and Theoretical Motivation
Physical constants such as pi, e, and h emerge in diverse contexts, from statistical mechanics to quantum field theory. This project draws inspiration from classical mechanics, particularly the problem of counting collisions between blocks with different mass ratios, where the number of collisions follows a pattern related to pi. Using machine learning techniques, we allow AI to process numerical data and propose functional relationships autonomously.

## Methodology
### Data Generation
We simulate elastic collisions of two blocks with varying mass ratios and count the total number of collisions before they separate indefinitely. The classical solution predicts that the number of collisions scales as pi times sqrt{m_2/m_1} for large mass ratios. For the visualisation of this emergence of pi, we have forked the repository  https://github.com/prajwalsouza/Counting-Collisions. His HTML website https://prajwalsouza.github.io/Experiments/Colliding-Blocks.html truly captures how pi comes out of nowhere.

### AI-Driven Pattern Recognition
We utilize symbolic regression techniques to extract underlying equations from the generated numerical data. The AI:
- Analyzes the dataset to identify relationships between variables.
- Constructs mathematical expressions to approximate the observed behavior.
- Simplifies expressions to reveal fundamental mathematical structures.

### Results
The AI successfully derived a function of the form:
\[
N \approx 3.141 \times 10^{X_0}
\]
where \(X_0\) represents a transformed mass ratio variable. This approximation aligns with the expected presence of \(\pi\) in the theoretical solution.

## AI as a Theoretical Physicist or Mathematician
AI excels at recognizing patterns in large datasets, mirroring the process of human theoretical discovery. In this context, the AI acts as an automated theorist, autonomously deriving mathematical relationships from empirical observations. Unlike traditional numerical curve fitting, AI-driven symbolic regression enables the emergence of physically meaningful expressions.

A useful comparison is SANATA AI, which aims to derive new physical theories by searching for invariant structures within data. Unlike SANATA, which operates on more abstract theoretical principles, our approach focuses on direct symbolic extraction from simulated experiments, making it accessible for targeted applications in physics and mathematics.

## Future Directions
### Extending to Other Physical Phenomena
The success of this approach suggests broader applicability in uncovering hidden mathematical structures in nature. Future work may involve:
- Applying AI to discover constants in chaotic systems.
- Exploring quantum mechanics for emergent symmetries.
- Investigating connections between AI-derived hypotheses and deep theoretical frameworks such as Noether’s theorem.

### AI-Guided Hypothesis Generation
Beyond rediscovering known results, AI may play a role in formulating new conjectures in physics. By training on diverse datasets, AI could generate plausible mathematical structures that human researchers can refine and validate, potentially accelerating breakthroughs in fundamental physics.

## Conclusion
This project demonstrates the feasibility of AI in autonomously detecting fundamental constants within physical simulations. By treating AI as an analytical tool akin to a theoretical physicist, we open the possibility of AI-driven scientific discovery. Future research will further refine these techniques, expanding AI's role in hypothesizing physical laws beyond known mathematical structures.

