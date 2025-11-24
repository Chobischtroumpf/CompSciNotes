---
title: Notes
authors: Alessandro Dorigo
tags:
  -
---
# 1: Software Engineering
**Why software engineering?**
Problem Specification -> Final Program:
- It addresses key challenges in software development, such as ensuring the specification meets user needs, structuring programs effectively, verifying that the software meets its specifications, ensuring reliability, adapting to changing user requirements, and managing teamwork in multi-person projects.

**What is software engineering?**
The discipline of creating quality software within budget and time constraints while involving teamwork, continuous adaptation to change, and balancing stakeholder needs. Unlike traditional engineering, it's limited more by human and political factors than physical laws.
## Software Development Activities
![[c04040c310be97c249fbcc3f851fa487.png]]
**RADIT**M
## Software Process Models
*aka. Abstraction of a process*
### Waterfall Model:
![[2f7b301735fbc11ee2f5b9edc39ea13e.png]]
**Pros:**
+ Project documentation between phases
+ Well supported by planning tools / techniques

**Cons:**
- Unrealistic model:
	- Requirements must be frozen too early
	- Requirements are validated too late
### Iterative Development:
![[be037bc8fceccc0f89f6f56b38bbdfea.png]]
### Agile Development:
- Small iterations (2 - 3 weeks)
- People oriented
	- People are the key factor
- Adaptive rather than predictive (iterative is adaptive, waterfall is predictive)

It requires a lot of implication from both the developer team AND the client
**Constant redesigning / refactoring is necessary**
# 2: OOP: Introduction
## ADT (Abstract Data Types)
- Separate definition from implementation
	- Explicit interface on the outside
	- Implicit details kept inside

+ Allows changing data without impacting the clients
+ Raises level of abstraction

**Code that respects the ADT and uses it's interface is NOT affected by our change**
***ADT <=> OO Encapsulation***
## Basics of OOP
1. Objects
2. Methods
3. Polymorphism
4. Classes
5. Inheritance
### 1. Objects
- Encapsulate data (protection)
- Can refine another object
	- Enabling incremental reuse

- **React to messages** (interact via messages)
	- In a message there is a designated receiver that accepts the message
	- The interpretation of the message may be different, depending upon the receiver
- **Have an unique identity**
- **Protect their data**

![[a3f4fe42599e91bf8866bce39b6fe65c.png]]
### 2. Messages vs Methods
**Messages: What?** (specification-based)
- Specify what must be performed by objects

**Methods: How?** (implementation-based)
- Specify how to process received messages
#### 2.1. Method Lookup
**When sending message m to object o** -> find method with name m and invoke it
![[de8a48013004c38aa102bab0a654d605.png]]
## 3. Polymorphism
*Same message can be sent to different objects*
- Different objects can react in other ways

![[cd9ad449c4595ff514b058c4070f0e65.png]]
Makes it so that client code can send a message to an object without knowing its class, also decouples client code from the called object
## 4. Classes
*Sharing methods between objects*

Describe structure / behavior common for all the objects within the class
Also serve as units of reuse, by means of inheritance
*All objects know their class and are instances of classes*
![[5d351d25c0ee8ea80d2fc884c58247fa.png]]
## 5. Inheritance (also called Generalization for modeling)
***incremental reuse*** (for classes)

Mechanism that allows new subclasses to be derived which themselves inherit all the features of their parent(s) (superclasses) OR override the implementation of the same features
![[899d5b6c30476d1e3f5771ca075f7ee4.png]]
***Subclass = more specialized version of a superclass***
### Inheritance types:
#### Single (1 parent / superclass)
The method lookup also applies here, but this time when sending message m to object o, it tries to find method m in the class C of o, otherwise it recursively looks up message m in the superclass of C
#### Multiple (>1 parent / superclass)
Deprecated in new languages, as the method lookup does not work as intended (which parent is being prioritized?)
### Self / Super sends
**Methods use:**
- `self / this` when referring to the receiver object
- `super` when referring to the implementor's parent

![[1781372f03f454fb741c834ec5ae3e10.png]]
The method lookup starts from the class of the current receiver object for `self / this` and starts from the superclass of the class where the method doing the super-call is defined for `super`
## Visibility
![[c65986779477a672c378d534590de08f.png]]

![[9fb359ed3c0bace9c4e9d530397ab162.png]]
### Objects using other objects (also called composition)
One object can use other objects or be composed of other objects
*This consitutes a 'has-a' relationship*

**This is fundamentally different from inheritance (generalization)**
## C++ Polymorphism / Inheritance
Virtual methods allow polymorphism:
- A virtual method is a method that is overridden by a derived class and will always use the derived implementation

![[13fbb9a9827f459364987f64f6650602.png]]
# 3. Less Basic OOP
- `super` should only be used to access overridden methods, and an overridden method has the same signature than its parent
## Abstract Classes (runtime polymorphism)
- Contain one or more abstract methods (pure virtual), which lack implementation and cannot be instantiated
- Abstract methods should be overridden by concrete methods in subclasses

Useful for ensuring all subclasses have the behavior declared in the abstract class (runtime polymorphism)

**Pure virtual = `virtual void Method() = 0;`**
## Method Overriding
Subclasses can re-implement methods already present in the superclass with the **same signature**
- *Clients do not have to know this*
## Method Overloading
Allows methods of the same name but different signatures (compiler will decide which one to used based on expected result)
## White-box reuse
- Requires knowing the implementation to reuse a component
- **Disadvantages:** need to comprehend existing code / risk of subtle errors
## Black-box reuse (preferred for OOP)
- Reuse based only on knowing the component's interface
# 4. UML Overview
## General Goals of UML
- Model systems using OO concepts
- Establish an explicit coupling to conceptual / executable artifacts
- Create a modeling language usable by both humans and machines
- Model different types of systems (information systems, technical systems, embedded systems, real-time systems, distributed systems, system software, business systems, UML itself, ...)
## Views (5)
![[848c5aa81d7ce21ce3bce7f262d7fc28.png]]
### 1. Use Case View
*How the client interacts with the application / what the application does*
- Most abstract, describes the functionality of the system for the end-users
- Central view that drives the development of the others
### 2. Logical View
- Shows how the system functions by using class / object diagrams
### 3. Component View
- Shows how code components are organized with relationships / dependencies
### 4. Concurrency View
- Shows how different "threads" interact
### 5. Deployment View
- Shows how the system is deployed into physical architecture
## Diagrams (9)
### 1. Use Case Diagram
- Represents the system from the view of the user(s)

![[0e1921f4d846584a26b0b7790c196cbf.png]]
### 2. Class Diagram
- Represents classes and their **static** relationships

![[3f9e69ab1f733c5d23addc7e76cff30a.png]]
### 3. State Diagram
- Represents the state of the system

![[9a767c17f097ca0dc553d0eaf296ab89.png]]
### 4. Sequence Diagram
- Temporal relation between objects (object <- signal, sends it to another)

![[561560bb26fe6bdd480d5056b96f67f0.png]]
### 5. Collaboration Diagram
- Spatial relation between objects

![[4b4ac093b717191ddd19fa7f5afe6823.png]]
### 6. Object Diagram
- Represents the **dynamic** relations between objects

![[ffa80aacd8430c189630b7defd1a1866.png]]
### 7. Activity Diagram
- Represents the behavior of an operation (describe a method through sequence of actions)

![[f286dafbfb08e4fb5efe10b9daa46f0a.png]]
### 8. Component Diagram
- Represents the relations / dependencies between components (blocks of code)
### 9. Deployment Diagram
- Represents the deployment of a system onto hardware
# 5. UML Class Diagrams
## Class Diagrams
- Static model type - show the system in terms of classes and relationships
- Describe attributes and behavior of objects or type of objects

*All objects are instances of a certain class*
## Class in UML:
![[993e054fe1a9314d7ff027ee1d5dc452.png]]

| **Category**   | **Description** |
| -------------- | --------------- |
| **Name**       | Starts with an uppercase<br>Bold |
| **Attributes** | Start with a lowercase<br>Have types<br>Can have visibility (+ public, - private, # protected)<br>Default values are optional<br>Allowed values ({...})<br>Class scopes also optional (underlined) - static members / methods |
| **Operations** | Contain the signature of the operation<br>&nbsp;&nbsp;- Return type<br>&nbsp;&nbsp;- Name<br>&nbsp;&nbsp;- Zero or more parameters<br>Can also have visibility |

![[d6c91244eeb122f5cbcb20a1982a75b2.png]]
## Relationships
- **Association:** connection between classes - *"usage”*
- **Generalization:** relationship between a more general and a more specific element - *“inheritance”*
- **Refinement:** relationship between two descriptions of the same thing but at different levels of abstraction
- **Realization:** relationship between elements where one carries out what the other specifies
## Associations
- Specify structural relationships
- Classes are interconnected (through instance variables, method arguments)

![[67afa9ad259d4be510b4fccd024e5097.png]]
![[421a7eb50eaa407e49ee1f15a632ec64.png]]

| **Multiplicity** | **Notation**      |
| ---------------- | ----------------- |
| Optional         | `0..1`            |
| Zero or more     | `0..*` or `*`     |
| At least one     | `1..*`            |
| Exactly one      | `1` or `(blank)`  |
### Recursive Association
- Connecting a class to itself

![[fac9527127ebd4afbb92ae3310dc478c.png]]
### Qualified Association
- Specific `initials` (or set of `initials`) can only be associated to a specific `Employee` by `Company` once

![[8c6a13455cf4f25a97fc392076be9f2a.png]]
### "xor" Association
- A `contract` belongs to a `Person` or a `Company`

![[732c2fd499d2404eb7cbb3c692e453ce.png]]
### Other constraints
| **Constraint** | **Description**                                          |
| -------------- | -------------------------------------------------------- |
| `{ordered}`    | Implies an ordered sequence of links.                    |
| `{xor}`        | Denotes an exclusive ***or*** relationship.                    |
| `{implicit}`   | Indicates the relationship is only conceptual.           |
| `{changeable}` | Links between objects may be added, removed, and changed freely. |
| `{addonly}`    | New links may be added from an object on the opposite end of the association. |
| `{frozen}`     | Link on the opposite end of the association may not be modified or deleted. |
## Aggregation
- A whole-part association - *whole owns the part*

![[8fbd483142e0e381f4e9c1aa7bf42539.png]]
### Composition Aggregation
- Parts can only exist if the whole does - *they're destroyed with the whole*

![[e70b62c86ecc1df3c11e1d844300f269.png]]
### Shared Aggregation
- Parts belong to >= 1 wholes

![[8317b0f68d9fd447b43b517755658051.png]]
### Association or Aggregation?
- Depends on context:
	- **Aggregation:** inseparable part-whole relationships (car and its tires in service center)
	- **Association:** separable relationships (tires sold individually in the tire store)
## Generalization
- Inheritance - *is-a relationship*

![[4dee3c631185eb03a2358be3b998eda2.png]]
## Refinement
- Represents a fuller specification of something that has already been specified at less detail
	- A relation between the analysis version and the design version
	- A relation between a clean implementation and an optimized but potentially difficult variation
## Realization
- Interface - contract between the description and the implementor (contract assures that it provides the implementation)

![[28f3a6f934edd2cc6f2c9fec0c61fa33.png]]
## TL;DR
![[e3a0ec136820a0b2cd0011608a4a54e7.png]]
# 6. Requirements Engineering
- Process of analyzing what a system should do (not how)

**User Requirements:** High-level abstract requirements
**System Requirements:** Detailed descriptions of what the system should do
## Classifying Requirements
1. **Functional Requirements:** specify what the system should or shouldn't do
2. **Non-functional Requirements:** other aspects like performance or security, not specific system functions
3. **Domain Requirements:** requirements derived from the application's domain, from the standards present in the domain of the application
### Metrics for Non-functional Requirements
![[d4ab0b348feb3ec8671cf51fbdcc60d3.png]]
### Writing User Requirements
- Use simple language, diagrams
- Avoid software jargon / formal notations
## Software Requirements Document (SRD)
- Official statement of what the system developers should implement
	- Outlines functional, non-functional and domain-specific requirements

- Contains diagrams / short descriptions / enumerated lists

**Best practices:**
1. **Clarity:** Avoid ambiguity
2. **Format:** Use a clean, spaced layout w/ short sentences
3. **Language:** Minimize technical jargon
4. **Evolve:** Update over time
## Use Case Diagrams
- Can be used to discover requirements
### Parts
#### System
- Can be any system
- Define clear and precise boundaries
- Compile a catalog of central concepts or entities
#### Actors
- Who / what will use the system
- Communicate with the system by sending and receiving messages
- Are in control and initiate actions
#### Use Cases
- Set of sequences of actions a system performs
- Always initiated by an actor
- Delivers an observable result of value to an actor
- Is connected to an actor through associations
- Specifies behavior - not how
- Carries out some tangible amount of work

![[a9c331bc4df62a60b459c8120a4a8c4c.png]]
### Use Case Description
- How and when the use case starts and ends
- When it interacts with actors and what objects are exchanged
- The basic flow and alternative flows of the behaviour
## Use Case Specification Structure
1. Actors
2. Pre-conditions
3. Post-conditions
4. Basic Flow
5. Alternative Flows
6. Special Requirements
7. Use case relationships

![[e9a7a03a44a0d60d825afb3c06dbf292.png]]
## Relationships
- Between actors
	- Generalization
- Between use cases
	- Generalization
	- Inclusion
	- Extension
### Actor Generalization
![[f66298c3eee4f9e5c5990a09a60a7cee.png]]
### Use Case Generalization
- Still an *is-a* relationship

![[f42f44a9ab931202b5edcc476a6ab7a1.png]]
### Use Case Inclusion
- Pulling behavior from a supplier case - *base use case incorporates another use case*

![[68d3f19d322c4d58e5457ca7a505a0ab.png]]
### Use Case Extension
- Show different possible variants - *provides alternative or additional behavior that can be triggered under specific conditions*

![[38ac9d95cb51efab891c105c7c605975.png]]
# 7. Dynamic Modelling
- Describes the system's behavior during runtime
- How to do things described by static models

**Objects (dynamic) vs Classes (static)**
- How elements of static diagrams:
	- Cooperate
	- Communicate
	- Change their state
	- Provide functionality
## Types
![[e9220d7c6915617512911088bc97892e.png]]
### Interaction Diagrams
1) **Sequence Diagrams:** emphasize time
2) **Collaboration Diagrams:** emphasize structure
#### Forms
1) **Generic form:** documents all possible scenarios
2) **Instance form:** documents one possible interaction
### Message Types
![[db25899c2502533aea373972363e29fd.png]]
## Sequence Diagram Notation
![[3b380c25c7cb16fb721b6182f14d62c6.png]]
### Overlaid Activations
![[74c05e576d30c8a91841161a3437d730.png]]
### Iteration
![[02eba129c09571f0d5a32de36a1ed95d.png]]
### Labels and Constraints
![[fd6fbdefa73ecae478bb656930bda8b9.png]]
### Object creation / destruction
![[4b33da135dfde0058f3e7822574a381d.png]]
### Latency
![[aab115f8b3b882dedbeb35cf2d98d569.png]]
## Collaboration Diagrams
Focus on:
- Interaction / communication between objects
- Shows the static / dynamic relationships - context aspect
- Space aspect

![[e2258c53c896f0923cb242d33436143e.png]]
## Message Descriptions
![[9cb2b39424dcbb3d2954013ee8dfe878.png]]
- Can have a guard condition
	- Condition has to be true
	- Expressed in (pseudo) code
### Predecessor
![[8c3bd0c94f573d9afa29f248928970e7.png]]
- Lists sequence numbers of other messages that need to be sent before this message can be sent (only specify if not implicitly available)
- Useful for expressing synchronization
- Example: message can only be sent when 1, 2.3 and 5 are finished: `1, 2.3 , 5 /`
### Sequence Expression
![[bb38001e9bd25278df855028ebace481.png]]
- Indicates that a message is a part of the actions undertaken in response to another message
- If messages are sent within an operation, they are given a new sub-sequence number separated by a dot
- Return value can be explicitly named
#### Numbering
![[c53d2d772b40c6bcdbee71aa51c41359.png]]
#### Recurrence
- Asterix (`*`) is used to specify recurrence
	- Optionally can be followed by an iteration-clause that gives more detail in (pseudo) code: `[x > 0] / [i := 1..n]`

![[713a1b7fd9e373a1d1479df28d5abcab.png]]
## Visibility Stereotypes
- Indicate how the objects know about each other

![[c39ba2125444b9726ee2eef494c8841b.png]]
![[ccb420d27ff025ab9e2aa23cd27bf3a3.png]]
## Existence Stereotypes
- Stereotypes or constraints can be used to indicate the objects’ existence during interaction

![[1670075178c1794531e5847e5d9d0bb2.png]]
![[0a429d7e47478de99852309967b2e4e2.png]]
# 8. UML Meta Model (not required for the exam)
- UML is based on a meta model - therefore each different diagram shares common elements with the other diagrams
- Each diagram is an instance of an UML meta model (each diagram shows a simplified view of the meta model)
- The meta model describes all possibilities
## Common UML: Elements
- Used within model elements and visual elements
	- **Model element**: represents system abstraction while modelling
	- **Visual element**: textual / graphical representation of a model element that allows the user to interact

![[7898876fc18eddc92d900a6b74207d0d.png]]
## Common UML: Mechanisms
- Stereotypes
- Tagged Values
- Notes
- Constraints
- Dependency Relationships
- (type, class) / (type, instance) dichotomies (?)

![[780510106bae14c1407e60856ca30f0c.png]]
## Common UML: Primitive Types
- **Boolean**: enumerated type {true, false}
- **Expression**: string with some semantics
- **List**: ordered sequence, possible indexed
- **Multiplicity**: Non-empty set of positive integers
- **Name**: string used to indicate element
- **Point**: tuple (x,y,z) that indicates point in space
- **String**: list of characters designated with a name
- **Time**: represents absolute or relative time
- **Non-interpreted**: blob
### Multiplicity
Syntax:
- **Multiplicity** ::= `[interval | number] { ‘ , ’ multiplicity}` - `1`
- **Interval** ::= `number ‘‘..’’ number` - `1, 3..4, 5..8`
- **Number** ::= `positive_number | name | ‘*’` - `0..*`
## Common UML: Packets
- Group model elements (all elements belong to a package)
	- Root package for the system
- Can contain other packets
- Enforce namespace
	- Two elements in different packages can have the same name

![[2d0e0fcf20328800f53d0bf4260bb10f.png]]
- Elements can be shared between packages
- The **import** relation between packages is modeled using a dependency relationship stereotyped with `<<import>>`

Elements contained in a package are not visible to the outside
- Except if declared **public** (stereotypes)
- Otherwise declared **implementation**
## Stereotypes
- Allow defining a new kind of model element based on an existing one
- Add extra semantics
- *There are predefined stereotypes*

![[cfe693484424fa7b44b28a11940982cd.png]]
### Tagged Values
- Pairs of information (name, value)
- Hold additional information about elements
### Notes
- Comment(s) attached to one or more elements
- Hold **no semantic** information
	- *Use stereotypes for semantic information*

![[7531d9abfb034d5bf45fc4c2052ea7ef.png]]
## Constraints
- Restrictions that limit the usage of an element or the semantics of an element
- Constraints expressed between `{...}`
- No syntax specified - Can be natural text, pseudo-code, mathematical expressions
## Dependency Relationships
- One-directional usage relationships between two model elements (called source and target)
- Notes or constraints are valid sources for dependency relationships

![[363f53370b43387509545a84be58dba7.png]]
# 9. Testing
## Invariants
A class invariant is any condition that expresses the valid states for objects of that class:
- Must be established when the instance is created.
- Every public method:
	- May assume it holds when the method starts.
	- Must be re-established when finished.

*They also make contracts explicit*
## Pre/Post-conditions
Pre-conditions **bind clients**:
- Define what the ADT requires for a call to the operation to be legitimate.
- May involve initial state and arguments.

Post-conditions, in return, **bind the supplier**:
- Define the conditions that the ADT ensures on return.
- May only involve the initial and final states, the arguments and the result.

![[80e097fb0e7db099f3f2748bf537c490.png]]
## Assertions
- An assertion is any boolean expression we expect to be true at some point.

Assertions have four main applications:
1. Help in writing correct software (formalizing invariants and pre/post-conditions)
2. Documentation aid (specifying contracts)
3. Debugging tool (testing assertions at run-time)
4. Support for software fault tolerance (detecting and handling failures at run-time)

To test assertions, either use the `assert()` provided by the language currently being used or code the assertion manually using a boolean argument (if it doesn't hold, throw an exception).
#### Testing Invariants
- Every class can implement it's own invariant (method returning a boolean).

```Cpp
private boolean Stack::invariant() {
	return (size_ >= 0) &&
	((size_ == 0 && this.top_ == null)
	|| (size_ > 0 && this.top_ != null));
}
```
### Checking pre-conditions
- Assert pre-conditions to inform clients when they violate a contract.
- Should always be checked and raise exceptions if they fail.

```Cpp
public Object top() {
	assert(!this.isEmpty());    // pre-condition
	return top_.item;
}
```
### Checking post-conditions
- Assert post-conditions and invariants to inform yourself when you violate the contract.
- Should be checked whenever the implementation is non-trivial.

```Cpp
public void Stack::push(Object item) {
	assert(item != null);       // pre-condition
	top_ = new Cell(item, top_);
	size_++;
	assert(!this.isEmpty());    // post-condition
	assert(this.top() == item); // post-condition
	assert(invariant());
}
```
## Unit Testing
**Tests represent your trust in the system**
- Should be built incrementally
	- No need to focus on everything
	- When a new bug shows up: write a test
- Act as your first client
- Helps finding proper interfaces

- Write unit tests that thoroughly test a single class
- Write tests as you develop (even before you implement)
- Write tests for every new piece of functionality

Unit Testing ensures that you get the specified behavior of the public interface of a class

- A **failure** is a **failed assertion** (an anticipated problem being tested for)
- An **error** is a **condition which was not checked** (an unexpected thrown exception)
### What are good/bad unit tests?
**Good unit tests**:
- Are repeatable (have to be deterministic to be useful)
- Require no human intervention (can be automated)
- Are “self-described” and tell a story (serve as documentation)
- Change less often than the system (encode stable functionality)

**Bad unit tests**:
- Require user intervention (cannot be repeated automatically)
- Test obvious things (no real point)
- Are not deterministic (sometimes pass, sometimes don't)
# 10. Implementation / Design Issues
**Good signs of OO thinking**:
- Short, clear methods
- No dense methods
- Objects should have clear responsibilities (state the purpose of the class in one sentence)
- No super-intelligent objects
- No manager objects
- Not too many instance variables
## Coding Standards
- Serve as a tool to improve communication
### Naming
- Should mean something
- Can introduce standard naming conventions
#### Naming Methods
- Specify *what* a method does, not *how*
- Consistent capitals (best use lowercase)

*If there is already a standard name for what is being implemented, it should be used*

| Category                                  | Naming Convention                                            | Examples                                |
| ----------------------------------------- | ------------------------------------------------------------ | --------------------------------------- |
| Methods that change state of the receiver | Verb phrase                                                  | `remove(Element e)`, `add(Element e)`, `transformWith(Model m)` |
| Methods that change state of the argument | Verb phrase ending with "on" or "to"                         | `displayOn(Canvas canvas)`, `printOn(Stream s)` |
| Methods that return a value from receiver | Noun phrase / adjective (description rather than command)    | `transformedBy():Model`, `size():int`, `topLeft():Point` |
| Accessing methods                         | Read / write into instance variables (such as "get" or "set")  | `getWinner()`, `setWinner(Player p)`    |
| Testing methods                           | Return boolean - prefixes like "be", "has", "is", "was", "will", "has" | `isNil()`, `hasBorder()`                |
| Converting methods                        | Prepend "as" to the name of the convertor method, followed by the type of return | `asSet() {...}`, `asFloat() {...}`, `asComposedText() {...}` |
#### Naming Classes
- Start class names with capitals
- Use simple names that convey meaning (one or two words - capitals between words)

| Category           | Naming Convention                                                   | Examples                                                                           |
| ------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Qualified Subclass | Prepend an adjective to the name of the most important superclass   | `OrderedCollection`, `CloneFigureCommand`, `CompositeCommand`, `ConnectionCommand` |
| Abstract Class     | Prefix abstract classes with "Abstract"                             | `AbstractCollection`, `AbstractVisualComponent`                                    |
| Design Pattern     | Use (part of) names of classes that play a role in a design pattern | `NodeVisitor`, `NodeSingleton`, `NodeFactory`                                      |
### Type vs Role
- Types are linked with classes
	- `Office`, `Campus`, `Secretary`, `CEO`, `Director`, `Manager`, `Developer`
- Roles are how objects are used
	- `location`, `employee`

When declaring a variable, we could use either the type or the role in the name:
- anOffice, aCampus <-> location
- aDirector, aManager <-> employee

- Types can be important for understanding, but are available through static types or comments
- Roles communicate intent and are typically harder to understand than types
### Naming Variables
- In most cases: name variables for the role they play
	- In class Point: `x`, `y`
	- In class Interval: `start`, `stop`, `step`
- Use plural when it is a collection:
	- In class PolyLine: `vertices`
- When you use a type: prefix with a or an:
	- `aPoint`, `aCampus`, `anArray`
### Formatting
Several standards exist but choice depends mostly on taste.
- If a standard is picked, it should be applied consistently.

Objects are strongly encapsulated:
- They have internal details
- and an external interface

Information hiding is useful because because it helps system evolution:
- Separation between clients and implementors
- Client code can evolve independently
- Implementation details can be changed without impacting clients
## Laws of Parnas
**Parnas’ Principles**:
- The developer of a software component must provide the intended user with all the information needed to make effective use of the services provided by the component, and should provide no other information.
- The user of a software component must be provided with all the information necessary to carry out the given responsibilities assigned to the component, and should be provided with no other information.

Leads to a ‘component’ with two faces:
- **Internal**: implementation details
- **External**: usage information

*Encapsulation is normally meant to separate private data from methods*
***Parnas’ principles are meant for all kinds of components***
## Coupling and Cohesion
*Code should preferably maintain a low coupling, high cohesion standard*

- **Cohesion** of a single module/component is the degree to which its responsibilities form a meaningful unit.
	- The higher the better
- **Coupling** between modules/components is their degree of mutual interdependence.
	- The weaker the better

**Good practices**:
- For two classes to either be not dependent on one another, or for one class to be only dependent on the interface of another class
- For a class to capture one and only one abstraction - unrelated information to be kept in separate classes
- To distribute the system intelligence as uniformly as possible

##### Kinds of Class Coupling
1. X inherits from Y
2. X has an attribute of class Y
3. X has a template attribute with a parameter of class Y
4. X has a method with an argument of class Y
5. X knows of a global variable of class Y
6. X is friend of Y *(in C++)*

The right balance between coupling and cohesion needs to be found:
- Making a subclass increases coupling (bad), but increases cohesion (good, when done right)
## Law of Demeter
The core of the problem:
![[6ac95034c561105185f19ff2470dfecd.png]]
- `Client` knows how `Provider` is implemented:
	- It knows that it uses an `IndirectProvider`
	- `Client` and `IndirectProvider` are strongly coupled

Therefore;
1. You are only allowed to send messages to:
	- An argument passed to you
	- An object you create
	- `Self`, `Super`
2. You must avoid global variables
3. You must avoid using objects returned from message sends other than `self`

![[012d5bfdd5b75026483c3bf29e482a32.png]]
## About Methods
- Methods take time to look up and call
- Flow of control can be difficult to follow when there are many methods

On the other hand:
- Reading is much improved
- Performance tuning is simpler
- Easier to maintain
- More re-usage possibilities (granularity is method)

- Methods should:
	- Perform only one identifiable task
	- Be short
	- Only contain comments when necessary (let the implementation be the comment)

Suppose we have a class with 2 big methods:
- Subclasses inherit these two methods
- They can only redefine 2 methods
- Very coarse-grain reuse

Suppose the same class has 20 small methods:
- Subclasses inherit 20 small methods
- They can redefine on a much finer level of granularity
### Responsibility
We need to make sure that each class has the right behavior:
- Implements good methods (short, with good names, readable, usable)
- Has the right responsibilities (not too many, not too few)

*Case (switch) statements in OO code are a sign of a bad design*
## Duplicated Code
- Makes the system harder to understand / maintain
- Errors get spread
- Evolution of code is not reflected everywhere (some places are forgotten and do not get updated)
- Code bloat: code gets much bigger
##### Where can duplicated code be found?
1. In the same class
	- Several methods that repeat a number of instructions
2. Between siblings
	- Two classes that share a common superclass
	- Methods in siblings that can repeat a number of instructions
3. Between unrelated classes
	- Classes not in a hierarchy can still repeat the same set of instructions

To get rid of duplicated code, we can extract duplicated statements into a method that gets used within all the places that duplicated the code.
# 11. Distribution & Synchronization in UML
## State Diagram
![[90aad316c38683b2c5d58da2cc806112.png]]
- Used to model the behavior of a system by describing the different states an object can be in, and how the state can change as a result of certain events.
- Used for a single object.

![[0953044294e9a19eb32e27a2f05417d3.png]]
### Transition Label Syntax
- Event / `[Guard]` / Action
	- All three parts are optional
- **Event**: transition will happen when event happens
- **Guard**: boolean condition that determine whether the transition can be taken or not
- **Action**: A quick, uninterruptable process

*When an event is omitted from the transition label, the transition will be taken as soon as the starting state is ready (has finished its activity)*

*When a transition is fired, the state of the object changes from the source state to the target state*
*When a transition fires, the (optional) action is executed*

A transition is fired when:
- the associated event occurs,
- (if there is one) the guard condition is true

#### Concurrency
Transitions are fired concurrently
- Guard conditions can be used to make them exclusive

Can model:
- A join from multiple concurrent states
- A fork to multiple concurrent states

![[d0aabe7b32b72402bf2f9a2ef2d2b952.png]]
#### Action / Activity
States can have an activity, transitions can have an action
- Activities take longer
- Actions have to be quick and uninterruptible (“Quick” depends on the system: different between information systems and real-time systems)
## Activity Diagram
***Strongly related to state diagrams***
- Corresponds to a state diagram where most (or all) of the states are activity states

![[25f94d1a3df84f86378d3bc976cefecb.png]]
*Guards can be used as in state charts*

![[b5fbc746201646d13c39860e0aa3a05d.png]]
### Subactivities
- Show either only the superstate
- Or the superstate with contained substates

![[4fa3307c7c5f4afc8b57f5e66138c54e.png]]
## Swimlanes
- They improve upon activity diagrams (when there's more than just one method's behavior being modeled / activity does not span across multiple classes)
- Arrange an activity diagram into vertical zones separated by lines, where each zone represents the responsibility of a class

![[336b8d39c3e8d4419ae12f121c4ca393.png]]
## Active Objects
- An object that owns a process / thread and can initiate control activity

*Threads* and *processes*:
- Use stereotypes `<<thread>>` or `<<process>>`
- Appear as sequences in interaction diagrams
### Active Class
![[826660dfa50294c688eef2cca6e6dbaa.png]]
- Class with thick lines
- Can contain an extra compartment for signals
### Communication
- Among passive objects: nothing special
- Among active objects: interprocess communication
	- Two possible styles:
		- **Synchronous**: rendez-vous semantics (blocking)
		- **Asynchronous**: mailbox-like semantics

- From passive to active: same as active to active
- From active to passive: Can be problematic when more than one active object pass their flow of control through a passive object
#### Active to Passive Communication
- Solution is to treat an object as a critical region, which can be done in 3 ways (alternatives):
	1. **Sequential**: callers have to coordinate to ensure integrity
	2. **Guarded**: only one operation execute at a time on an object
	3. **Concurrent**: these operations ensure integrity in case of concurrent execution

![[cc5cbccfc56d8728a9669e3888099b21.png]]
- Critical region in UML - constraints attached to operations
### Modeling multiple flows of control
- Use all the diagrams we have seen throughout the course
- Use active objects to represent the threads or processes as needed

![[32614c9549ad38c272b29862091ec8a6.png]]
### Modeling interprocess communication
- Threads typically communicate using signals or call events (that can be synchronous or asynchronous)
- Processes typically communicate using different mechanisms

- Model the multiple flows of control (consider which active objects are processes and which are threads)
- Model messaging using asynchronous communication
- Model remote procedure calls using synchronous communication
- Specify underlying mechanism for communication by notes (informally) or by collaborations (formally)

![[44bac3ea2a0a8e6418c5b6cd110b1bf1.png]]
## TL;DR
- Use ***asynchronous*** messages in sequence diagrams
- Use ***predecessors*** in collaboration diagrams
- Firing of transitions is concurrent in state diagrams
- Use ***fork*** and ***join*** in activity diagrams
