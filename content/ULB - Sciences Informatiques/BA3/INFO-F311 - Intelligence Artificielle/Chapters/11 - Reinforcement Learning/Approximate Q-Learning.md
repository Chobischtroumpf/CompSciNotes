---
title: Approximate Q-Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Approximate Q-Learning** is an extension of [[Q-Learning]] that uses feature-based representations and linear value functions to generalize learning across similar states, significantly reducing memory requirements and enabling faster convergence in large state spaces.

## Motivation

> [!abstract]+ The Generalization Problem
> **Problem with exact Q-learning:**
> - Must learn Q-value for every $(s, a)$ pair individually
> - Cannot transfer knowledge between similar states
> - Infeasible for large or continuous state spaces

> [!example] Pacman
>
| ![[ed5c5bae3560694de6bbbff5d134ff58.png]] | ![[339cca10c5fad37f0810766dd7c71e50.png]] | ![[efdba3d25171c45a4e642dad2606fddf.png]] |
| :----------------------------------: | :----------------------------------: | :----------------------------------: |
>
> If Pacman learned that Figure 1 is unfavorable after running vanilla Q-learning, it would still have no idea that Figure 2 or even Figure 3 are unfavorable as well.
>
> **Solution:** Learn about general situations and extrapolate to similar states using feature-based representations.

## Feature-Based Representation

> [!abstract]+ Linear Value Functions
> **Feature vector:** Represent each state as a vector of features:
>
> $$\vec{f}(s) = [f_1(s) \quad f_2(s) \quad \ldots \quad f_n(s)]^T$$
> $$\vec{f}(s, a) = [f_1(s, a) \quad f_2(s, a) \quad \ldots \quad f_n(s, a)]^T$$
>
> **Example features (Pacman):**
> - Distance to closest ghost
> - Distance to closest food pellet
> - Number of ghosts
> - Is Pacman trapped? (0 or 1)
>
> **Linear value functions:**
>
> $$V(s) = w_1 \cdot f_1(s) + w_2 \cdot f_2(s) + \ldots + w_n \cdot f_n(s) = \vec{w} \cdot \vec{f}(s)$$
>
> $$Q(s, a) = w_1 \cdot f_1(s, a) + w_2 \cdot f_2(s, a) + \ldots + w_n \cdot f_n(s, a) = \vec{w} \cdot \vec{f}(s, a)$$
>
> where $\vec{w} = [w_1 \quad w_2 \quad \ldots \quad w_n]$ is the weight vector.

## Algorithm

> [!abstract]+ Approximate Q-Learning Update Rule
> **Define difference:**
>
> $$\text{difference} = [R(s, a, s') + \gamma \max_{a'} Q(s', a')] - Q(s, a)$$
>
> **Weight update rule:**
>
> $$w_i \leftarrow w_i + \alpha \cdot \text{difference} \cdot f_i(s, a)$$
>
> for each feature $i$.
>
> **Interpretation:**
> - Compute difference between sampled estimate and current Q-value
> - Adjust each weight proportionally to its feature's contribution
> - Magnitude of shift proportional to magnitude of difference

## Comparison with Exact Q-Learning

> [!abstract]+ Update Rule Equivalence
> **Exact Q-learning update:**
>
> $$Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \text{difference}$$
>
> **Approximate Q-learning update:**
>
> $$w_i \leftarrow w_i + \alpha \cdot \text{difference} \cdot f_i(s, a)$$
>
> **Key difference:**
> - Exact: Updates single Q-value in table
> - Approximate: Updates weight vector affecting many Q-values simultaneously

## Least Squares Approximation

> [!abstract]+ Mathematical Foundation
> **Objective:** Minimize squared error between estimated and target Q-values
>
> **Method:** Gradient descent on weights
> - Compute derivative: "How does changing weight $w_i$ affect error?"
> - Positive derivative -> decrease weight
> - Negative derivative -> increase weight
> - Iteratively minimize error through weight adjustments

## Policy Search

> [!abstract]+ Alternative Approach
> **Strategy:**
> 1. Find initial policy (e.g., via [[Q-learning]])
> 2. Iteratively nudge weights up and down
> 3. Test resulting policy performance:
>    - Better performance -> keep weights
>    - Worse performance -> discard weights
> 4. Repeat until convergence
>
> **Characteristics:**
> - Simpler to understand than [[Q-learning]]
> - Not sample-efficient (requires many episodes)
> - Direct policy optimization

## Properties

> [!success]+ Advantages
> - **Memory efficient:** Store only weight vector, not full Q-table
> - **Generalization:** Learn from one state applies to similar states
> - **Scalability:** Handles large and continuous state spaces
> - **Faster convergence:** Fewer parameters to learn than exact Q-learning

> [!fail]+ Disadvantages
> - **Feature engineering:** Requires manual design of good features
> - **Linear limitation:** Assumes linear relationship between features and values
> - **Approximation error:** May not represent true Q-function exactly

> [!note]+ Related Concepts
> - **[[Q-Learning]]**: Foundation algorithm
> - **[[Active Reinforcement Learning]]**: Framework for approximate Q-learning
> - **[[Model-Free Learning]]**: General approach category
> - **[[Reinforcement Learning]]**: Broader context
> - **[[Q-State]]**: What approximate Q-learning learns values for
> - **[[Policy]]**: Derived from learned Q-values
