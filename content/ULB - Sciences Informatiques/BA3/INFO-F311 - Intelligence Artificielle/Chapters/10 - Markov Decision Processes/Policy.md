---
title: Policy
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **Policy** is a mapping $\pi: S \to A$ that specifies which action to take in each state.

## Comparison to Search

> [!abstract]+ Policies vs Plans
> **Single-agent search problems:**
> - Want an optimal plan (sequence of actions from start to goal)
>
> **MDPs:**
> - Want an optimal policy $\pi^*: S \to A$
> - Policy gives an action for each state, not just a sequence
> - More robust to uncertainty

## Optimal Policy

> [!abstract]+ Properties
> **An optimal policy $\pi^*$:**
> - Maximizes expected utility if followed
> - Accounts for all possible state transitions
> - Defines behavior for every reachable state
>
> **Implementation:**
> - An explicit policy defines a [[Reflex Agent]]
> - Agent simply looks up action for current state

## Relation to Expectimax

> [!abstract]+ Computing vs Following Policies
> [[Expectimax Search]] computes the action for a single state only.
>
> **Key difference:**
> - Expectimax: Computes one action from root state
> - Policy: Specifies action for every possible state
> - Policy is complete contingency plan

> [!note]+ Related Concepts
> - **[[Markov Decision Process]]**: Framework using policies
> - **[[State]]**: Nodes where policy specifies actions
> - **[[Value Iteration]]**: Algorithm for computing optimal policies
> - **[[Policy Extraction]]**: Deriving policy from values
> - **[[Reflex Agent]]**: Implements explicit policy
> - **[[Expectimax Search]]**: Single-state decision making
