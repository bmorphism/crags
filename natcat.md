

# Categorical Tools for Natural Language Processing

Givanni de Felice

Wolfson College

University of Oxford

A thesis submitted for the degree of

_Doctor of Philosophy_

Michaelmas 2022

[MISSING_PAGE_POST]

 

###### Abstract

This thesis develops the translation between category theory and computational linguistics as a foundation for natural language processing. The three chapters deal with syntax, semantics and pragmatics. First, string diagrams provide a unified model of syntactic structures in formal grammars. Second, functors compute semantics by turning diagrams into logical, tensor, neural or quantum computation. Third, the resulting functorial models can be composed to form games where equilibria are the solutions of language processing tasks. This framework is implemented as part of DisCoPy, the Python library for computing with string diagrams. We describe the correspondence between categorical, linguistic and computational structures, and demonstrate their applications in compositional natural language processing.



[MISSING_PAGE_POST]

 

## Acknowledgements

I would like to thank my supervisor Bob Coecke for introducing me to the wonderland of string diagrams, for supporting me throughout my studies and always encouraging me to switch topics and pursue my ideas. This thesis is the fruit of a thousand discussions, board sessions, smokes and beers with Alexis Toumi. I am grateful to him for having the patience to teach Python to a mathematician, for his loyal friendship and the continual support he has given me in both personal matters and research. I want to thank my examiners Aleks Kissinger and Pawel Sobocinski for their detailed feedback on the first version of this thesis, and their suggestion to integrate the passage from categories to Python code. Thanks also to Andreas Petrossantis, Sebastiano Cultrera and Dimitri Kartsaklis for valuable comments on this manuscript, to Dan Marsden and Prakash Panangaden for providing guidance in my early research, and to Samson Abramsky for prompting me to search into the deeper history of applied category theory.

Among fellow collaborators who have shared their wisdom and passion, for many insightful discussions, I would like to thank Amar Hadzihasanovic, Rui Soares Barbosa, David Reutter, Antonin Delpeuch, Stefano Gogioso, Konstantinos Meichanetzidis, Mario Roman, Elena Di Lavore and Richie Yeung. Among my friends, who have been there for me in times of sadness and of joy, and made me feel at home in Oxford, Rome and Sicily, special thanks to Tommaso Salvatori, Pinar Kolancali, Tommaso Battistini, Emanuele Torlonia, Benedetta Magnano and Pietro Scammacca. Finally, a very special thanks to Nonna Miti for hosting me in her garden and to my mother and father for their loving support.



[MISSING_PAGE_POST]

 

###### Contents

* 1 Diagrams for Syntax
	* 1.1 Arrows
		* 1.1.1 Categories
		* 1.1.2 Regular grammars
		* 1.1.3 cat.Arrow
	* 1.2 Trees
		* 1.2.1 Operads
		* 1.2.2 Context-free grammars
		* 1.2.3 operad.Tree
	* 1.3 Diagrams
		* 1.3.1 Monoidal categories
		* 1.3.2 Monoidal grammars
		* 1.3.3 Functorial reductions
		* 1.3.4 monoidal.Diagram
	* 1.4 Categorial grammar
		* 1.4.1 Biclosed categories
		* 1.4.2 Ajdiuciewicz
		* 1.4.3 Lambek
		* 1.4.4 Combinatory
		* 1.4.5 biclosed.Diagram
	* 1.5 Pregroups and dependencies
		* 1.5.1 Pregroups and rigid categories
		* 1.5.2 Dependency grammars are pregroups
		* 1.5.3 rigid.Diagram
	* 1.6 Hypergraphs and coreference
		* 1.6.1 Hypergraph categories
		* 1.6.2 Pregroups with coreference
		* 1.6.3 hypergraph.Diagram
* 2 Functors for Semantics
	* 2.1 Concrete categories in Python
		* 2.1.1 Tensor
		* 2.1.2 Function
	* 2.2 Montague models
		* 2.2.1 Lambda calculus
		* 2.2.2 Typed first-order logic
		* 2.2.3 Montague semantics
		* 2.2.4 Montague in DisCoPy
	* 2.3 Neural network models
		* 2.3.1 Feed-forward networks
		* 2.3.2 Recurrent networks
		* 2.3.3 Recursive networks
		* 2.3.4 Attention is all you need?
		* 2.3.5 Neural networks in DisCoPy
	* 2.4 Relational models
		* 2.4.1 Databases and queries
		* 2.4.2 The category of relations
		* 2.4.3 Graphical conjunctive queries
		* 2.4.4 Relational models
		* 2.4.5 Entailment and question answering
	* 2.5 Tensor network models
		* 2.5.1 Tensor networks
		* 2.5.2 Tensor functors
		* 2.5.3 DisCoCat and bounded memory
		* 2.5.4 Bubbles
	* 2.6 Knowledge graph embeddings
		* 2.6.1 Embeddings
		* 2.6.2 Rescal
		* 2.6.3 DistMult
		* 2.6.4 ComplEx
	* 2.7 Quantum models
		* 2.7.1 Quantum circuits
		* 2.7.2 Quantum models
		* 2.7.3 Additive approximations
		* 2.7.4 Approximating quantum models
	* 2.8 DisCoPy in action
* 3 Games for Pragmatics
	* 3.1 Probabilistic models
		* 3.1.1 Categorical probability
		* 3.1.2 Discriminators
		* 3.1.3 Generators
	* 3.2 Bidirectional tools
		* 3.2.1 Lenses
 3.2.2 Utility functions 182 3.2.3 Markov rewards 183 3.3 Cybernetics 185 3.3.1 Parametrization 185 3.3.2 Open games 186 3.3.3 Markov decisions 189 3.3.4 Repeated games 191 3.4 Examples 194 3.4.1 Bayesian pragmatics 194 3.4.2 Adversarial question answering 196 3.4.3 Word sense disambiguation

 

[MISSING_PAGE_POST]

 

## Introduction

Since the very beginnings of human inquiry into language, people have investigated the natural processes by which we learn, understand and produce linguistic meaning. Only recently, however, the field of linguistics has become an autonomous scientific discipline. The origins of this modern science are closely interlinked with the birth of mathematical logic at the end of the nineteenth century. In the United States, Peirce founded "semiotics" -- the science of signs and their interpretation -- while developing graphical calculi for logical inference. At around the same time, in the United Kingdom, Frege and Russell developed formal languages for logic in the search for a Leibnizian "characteristic universalis" while discussing the sense and reference of linguistic phrases.

These mathematical origins initiated a formal and computational approach to linguistics, often referred to as the symbolic tradition, which aims at characterising language understanding in terms of structured logical processes and the automatic manipulation of symbols. On the one hand, it led to the development of mathematical theories of syntax, such as the categorial grammars stemming from the Polish school of logic [1, 2] and Chomsky's influential generative grammars [1]. On the other hand, it allowed for the development of formal approaches to semantics such as Tarski's theory of truth [14, 15], which motivated the work of Davidson [2] and Montague [30] in extracting the logical form of natural language sentences. From the technological perspective, these theories enabled the design of programming languages, the construction of large-scale databases for storing structured knowledge and linguistic data, as well as the implementation of expert computer systems driven by formal logical rules to reason about this accrued knowledge. Since the 1990s, the symbolic tradition has been challenged by a series of new advances motivated by the importance of context and ambiguity in language use [1]. With the growing amount of data and large-scale corpora available on the internet, statistical inference methods based on $n$-grams, Markov models or Bayesian classifiers allowed for experiments to tackle new problems such as speech recognition and machine translation [23]. The distributional representation of meaning in vector spaces [24] was found suitable for disambiguating words in context [25] and computing synonymity [17]. Furthermore, connectionist models based on neural networks have produced impressive results in the last couple of decades, outperforming previous models on a range of tasks such as language modelling [1, 26, 27], word sense disambiguation [28], sentiment analysis [29, 30], question answering [15, 16] and machine translation [1, 2].

Driven by large-scale industrial applications, the focus gradually shifted from theoretical enquiries into linguistic phenomena to the practical concern of building highly parallelizable connectionist code for beating state-of-the-art algorithms. Recently, a transformer neural network with billions of parameters (GPT-3) [14] wrote a Guardian article on why humans have nothing to fear from AI. The reasons for how and why GPT-3 "chose" to compose the text in the way that it did is a mystery and the structure of its mechanism remains a "black box". Connectionist models have shown the importance of the distributional aspect of language and the effectiveness of machine learning techniques in NLP. However, their task-specificity and the difficulty in analysing the underlying processes which concur in their output are limits which need to be addressed. Recent developments in machine learning have shown the importance of taking structure into account when tackling scientific questions in network science [23], chemistry [15], biology [24, 25]. NLP would also benefit from the same grounding in order to analyse and interpret the growing "library of Babel" of natural language data.

Category theory can help build models of language amenable to both linguistic reasoning and numerical computation. Its roots are the same as computational linguistics, as categories were used to link algebra, logic and computation [16, 17, 18]. Category theory has since followed a solid thread of applications, from the semantics of programming languages [22, 1] to the modelling of a wide range of computational systems, including knowledge-based [23], quantum [1, 1], dataflow [24], statistical [21] and differentiable [1] processes. In the Compositional Distributional models of Coecke et al. [1, 2, 3] (DisCoCat), categories are used to design models of language in which the meaning of sentences is derived by composition from the distributional embeddings of words. Generalising from this work, language can be viewed as a syntax for arranging symbols together with a functor for interpreting them. Specifically, syntactic structures form a free category of string diagrams, while meaning is computed in categories of numerical functions. Functorial models can then be learnt in data-driven tasks.

The aim of this thesis is to provide a unified framework of mathematical tools to be applied in three important areas of computational linguistics: syntax, semantics and pragmatics. We provide an implementation of this framework in object-oriented Python, by translating categorical concepts into classes and methods. This translation has lead to the development of DisCoPy [1], an open-source Python toolbox for computing with string diagrams and functors. We show the potential of this framework for reasoning about compositional models of language and building structured NLP pipelines. We show the correspondence between categorical and linguistic notions and we describe their implementation as methods and interfaces in DisCoPy. The library is available, with an extensive documentation and testing suite, at:

https://github.com/oxford-quantum-group/discopy

In Chapter 1, on syntax, we use the theory of free categories and string diagrams to formalise Chomsky's regular, context-free and unrestricted grammars [15]. With the same tools, the categorial grammars of Ajdiuciewicz [1], Lambek [16] and Steedman [14], as well as Lambek's pregroups [11] and Tesniere's dependency grammars [15, 2], are formalised. We lay out the architecture of the syntactic modules of DisCoPy, with interfaces for the corresponding formal models of grammar and functorial reductions between them. The second chapter deals with semantics. We use Lawvere's concept of functorial semantics [11] to define several NLP models, including logical, distributional and connectionist approaches. By varying the target semantic category, we recover knowledge-based, tensor-based and quantum models of language, as well as Montague's logical semantics [12] and connectionist models based on neural networks. The implementation of these models in Python is obtained by defining semantic classes that carry out concrete computation. We describe the implementation of the main semantic modules of DisCoPy and their interface with high-performance libraries for numerical computation. This framework is then applied to the study of the pragmatic aspects of language use in context and the design of NLP tasks in Chapter 3. To this end, we use the recent applications of category theory to statistics [10, 11], machine learning [17, 18] and game theory [2] to develop a formal language for modelling compositions of NLP models into games and pragmatic tasks.

The mathematical framework developed in this thesis provides a structural understanding of natural language processing, allowing for both interpreting existing NLP models and building new ones. The proposed software is expected to contribute to the design of language processing systems and their implementation using symbolic, statistical, connectionist and quantum computing.

 

## Contributions

The aim of this thesis is to provide a framework of mathematical tools for computational linguistics. The three chapters are related to syntax, semantics and pragmatics, respectively.

In Chapter 1, a unified theory of formal grammars is provided in terms of free categories and functorial reductions and implemented in object-oriented Python. This work started from discussions with Alexis Toumi, Bob Coecke, Mernoosh Sadrzadeh, Dan Marsden and Konstantinos Meichanetzidis about logical and distributional models of natural language [10, 11, 12]. It was a driving force in the development of DisCoPy [13]. The main contributions are as follows.

1. A unified treatment of _formal grammars_ is provided using the theory of string diagrams in free monoidal categories. We cover Chomsky's regular 1.1, context-free 1.2 and unrestricted grammar 1.3, corresponding to free categories, free operads and free monoidal categories respectively. This picture is obtained by aggregating the results of Walters and Lambek [14, 15, 16]. Using the same tools, we formalise categorial grammars 1.4, as well as pregroups and dependency grammars 1.5 in terms of biclosed and rigid categories. The links between pregroups and rigid categories are known since [10], those between categorial grammar and biclosed categories were previously discussed by Lambek [16] but not fully worked out, while the categorical formalisation of dependency grammar is novel. We also introduce the notion of pregroup with coreference for discourse representation in 1.6 [10] to offer an alternative to the DisCoCirc framework of Coecke [10] which can be implemented with readily available tools. To the best of our knowledge, this is the first time that models from the Chomskyan and categorial traditions appear in the same framework, and that the full correspondence between linguistic and categorical notions is spelled out.
2. _Functorial reductions_ between formal grammars are introduced as a convenient intermediate notion between weak and strong equivalences, and used to compute normal forms of context-free grammars in 1.3.3. We use this notion in the remainder of the chapter to capture the relationship between: i) CFGs and categorial grammar (Propositions 1.4.8 and ), ii) categorial grammar and biclosed categories (Propositions 1.4.7, 1.4.12 and 1.4.17), iii) categorial and pregroup grammars (Propositions 1.5.7 and 1.5.13) and iv) pregroups, dependency grammars and CFGs in 1.5.2. The latter yields a novel result showing that dependency grammars are the structural intersection of pregroups and CFGs (Theorem 1.5.23).
3. The previously introduced categorical definitions are implemented in _object-oriented Python_. The structure of this chapter follows the architecture of the syntactic modules of DisCoPy, as described at the end of this section. Free categories and syntactic structures are implemented by subclassing cat.Arrowor monoidal.Diagram, the core data structures of DisCoPy. Functorial reductions are implemented by calling the corresponding Functor class. We interface DisCoPy with linguistic tools for large-scale parsing.

In Chapter 2, functorial semantics is applied to the study of natural language processing models. Once casted in this algebraic framework, it becomes possible to prove complexity results and compare different NLP pipelines, while also implementing these models in DisCoPy. Section 2.4 is based on joint work with Alexis Toumi and Konstantinos Meichanetzidis on relational semantics [1]. Sections 2.5, 2.8 and 2.7 are based on the recent quantum models for NLP introduced with Bob Coecke, Alexis Toumi and Konstantinos Meichanetzidis [14, 15] and further developed in [13, 16]. We list the main contributions of this chapter.

1. _NLP models_ are given a unified theory, formalised as functors from free syntactic categories to concrete categories of numerical structures. These include i) knowledge-based relational models 2.4 casted as functors into the category of relations, ii) tensor network models 2.5 seen as functors into the category of matrices and including factorisation models for knowledge-graph embedding covered in 2.6 iii) quantum NLP models 2.7 casted as functors into the category of quantum circuits, iv) Montague semantics 2.2 given by functors into cartesian closed categories, and v) recurrent and recursive neural network models 2.3 which appear as functors from grammar to the category of functions on euclidean spaces.
2. We prove _complexity results_ on the evaluation of these functorial models and related NLP tasks. Expanding on [1], we use relational models to define NP-complete entailment and question-answering problems (Propositions 2.4.26, 2.4.31 and 2.4.33). We show that the evaluation of tensor network models is in general $\mathbb{P}$-complete (Proposition 2.5.18) but that it becomes tractable when the input structures come from a dependency grammar (Proposition 2.5.20). We show that the additive approximation of quantum NLP models is a BQP-complete problem (Proposition 2.7.18). We also prove results showing that Montague semantics is intractable in its general form (Propositions 2.2.14, 2.2.16).
3. _Montague semantics_ is given a detailed formalisation in terms of free cartesian closed categories. This corrects a common misconception in the DisCoCat literature, and in particular in [12, 13], where Montague semantics is seen as a functor from pregroup grammars to relations. These logical models are studied in 2.4, but they are distinct from Montague semantics where the lambda calculus and higher-order types play an important role 2.2.
4. We show how to implement _functorial semantics in DisCoPy_. More precisely, the implementation of the categories of tensors and Python functions is described in 2.1. We then give a concrete example of how to solve a knowledge-embedding task in DisCoPy by learning functors 2.8. We define currying and uncurrying of Python functions 2.2 and use it to give a proof-of-concept implementation of Montague semantics. We define sequential and parallel composition of Tensorflow/Keras models [11], allowing us to construct recursive neural networks with a DisCoPy functor 2.3.

In Chapter 3, we develop formal diagrammatic tools to model pragmatic scenarios and natural language processing tasks. This Chapter is based on our work with Mario Roman, Elena Di Lavore and Alexis Toumi [13], and provides a basis for the formalisation of monoidal streams in the stochastic setting [10]. The contribution for this section is still at a preliminary stage, but the diagrammatic notation succeeds in capturing and generalising a range of approaches found in the literature as follows.

1. _Categorical probability_[14] is applied to the study of discriminative and generative language models using notions from Bayesian statistics in 3.1. We investigate the category of _lenses_[15] over discrete probability distributions in 3.2 and use it to characterise notions of context, utility and reward for iterated stochastic processes [10] (see Propositions 3.2.4 and 3.2.6). Finally, we apply open games [1] the study of Markov decision processes and repeated games in 3.3, while giving examples relevant to NLP.
2. Three _NLP applications_ of the developed tools are provided in 3.4: i) we discuss reference games [12, 13, 14] and give a diagrammatic proof that Bayesian inversion yields a Nash equilibrium (Proposition 3.4.1), ii) we define a question answering game between a teacher and a student and compute the Nash equilibria when the student's strategies are given by relational models [13] +21] and iii) we give a compositional approach to word-sense disambiguation as a game between words where strategies are word-senses.

The DisCoPy implementation, carried out with Alexis Toumi [13], is described throughout the first two chapters of this thesis. We focused on i) the passage from categorical definitions to object-oriented Python and ii) the applications of DisCoPy to Natural Language Processing. Every section of Chapter 1 corresponds to a _syntactic module_ in DisCoPy, as we detail.

1. In 1.1, we view derivations of _regular_ grammars as arrows in the free category and show how these notions are implemented via the core DisCoPy class cat.Arrow.
2. In 1.2, we study _context-free_ grammars in terms of trees in the free operad and give an implementation of free operads and their algebras in DisCoPy. This is a new operad module which has been written for this thesis and features interfaces with NLTK [14] for CFG and SpaCy [15] for dependencies.
3. In 1.3, we formalise Chomsky's _unrestricted_ grammars in terms of monoidal signatures and string diagrams and describe the implementation of the key DisCoPy class monoidal.Diagram.

 4. In 1.4, we formalise _categorical_ grammar in terms of free biclosed categories. We give an implementation of biclosed.Diagram as a monoidal diagram with curry and uncurry methods and show its interface with state-of-the-art categorial grammar parsers, as provided by Lambeq [10].
5. In 1.5, we show that _pregroup_ and _dependency_ structures are diagrams in free rigid categories. We describe the data structure rigid.Diagram and its interface with SpaCy [14] for dependency parsing.
6. In 1.6, we introduce a notion of pregroup grammar with _coreference_ using hypergraphs to represent the syntax of text and discourse. We describe the hypergraph.Diagram data structure and show how to interface it with SpaCy's package for neural coreference.

The models studied in Chapter 2 can all be implemented using one of the four _semantic modules_ of DisCoPy which we detail.

1. The tensor module of DisCoPy implements the category of matrices, as described in 2.1 where we give its implementation in NumPy [11]. We use it in conjunction with Jax [1] in 2.8 to implement the models introduced in 2.4 and 2.5.
2. The quantum module of DisCoPy implements quantum circuits 2.7 and supports interfaces with PyZX [12] and TKET [13] for optimisation and compilation on quantum hardware. These features are described in our recent work [15].
3. The function module of DisCoPy implements the category of functions on Python types, as described in 2.1. We define currying and uncurrying of Python functions 2.2 and use it to give a proof-of-concept implementation of Montague semantics.
4. The neural module implements the category of neural networks on euclidean spaces. We describe it in 2.3 as an interface between DisCoPy and TensorFlow/Keras [12].

A schematic view of the modules in DisCoPy and their interfaces is summarized in Figure 1.

 Figure 1: DisCoPy: an interfaced compositional software for NLP



## Chapter 1 Diagrams for Syntax

The word "grammar" comes from the Greek $\gamma\rho\dot{\alpha}\mu\mu\alpha$ (gramma), itself from $\gamma\rho\dot{\alpha}\varphi\epsilon\iota\nu$ (graphein) meaning both "to write" and "to draw", and we will represent grammatical structure by drawing diagrams. A _formal grammar_ is usually defined by a set of _rewriting rules_ on strings. The rewriting process, also called _parsing_, yields a procedure for deciding whether a string of words is grammatical or not.

These structures were studied in mathematics since the 1910s by Thue and later by Post [11] and Markov Jr. [12]. Their investigation was greatly advanced by Chomsky [13], who used them to _generate_ grammatical sentences from some basic rewrite rules interpreted as _productions_. He showed that natural restrictions on the allowed production rules form a hierarchy, from unrestricted to regular grammars, which corresponds to models of computation of varying strengths, from Turing machines to deterministic finite state automata [13]. In parallel to Chomsky's seminal work, Lambek developed his syntactic calculus [14], refining and unifying the _categorial grammars_ originated in the Polish school of logic [1]. These are different in spirit from Chomsky's grammars, but they also have tight links with computation as captured by the Lambda calculus [15, 16].

In this chapter, we lay out the correspondence between free categorical structures and linguistic models of grammar. Every level in this hierarchy is implemented with a corresponding class in DisCoPy. In 1.1, we show that regular grammars can be seen as graphs with a labelling homomorphism and their derivations as arrows in the free category, implemented via the core DisCoPy class cat.Arrow. In 1.2, we show that context-free grammars are operadic signatures and their derivations trees in the free operad. We give an implementation of free operads as a class operad.Tree, interfaced with NLTK [10] for context-free parsing. In 1.3, we arrive at Chomsky's unrestricted grammars, captured by monoidal signatures and string diagrams. We discuss varying notions of reduction and normal form for these grammars, and show the implementation of the key DisCoPy class monoidal.Diagram. In 1.4, we show that categorial grammars such as the original grammars of Ajdiuciewicz and Bar-Hillel, the Lambek calculus and Combinatory Categorial Grammars (CCGs) can be seen as biclosed signatures and their grammatical reductions as morphisms in free biclosed categories. We give an implementation of biclosed.Diagram as a monoidal diagram with curry and uncurry methods and show its interface with state-of-theart categorial grammar parsers, as provided by Lambeq [17]. In 1.5, we show that pregroups and dependency grammars are both captured by rigid signatures, and their derivations by morphisms in the free rigid category. This leads to the data structure rigid.Diagram which we interface with SpaCy [18] for state-of-the-art dependency parsing. Finally, in 1.6, we introduce a notion of pregroup grammar with coreference using hypergraphs to represent the syntax of text and discourse, and give a proof-of-concept implementation in DisCoPy.

 

### 1.1 Arrows

In this section, we introduce three structures: categories, regular grammars and cat.Arrows. These cast light on a level-zero correspondence between algebra, linguistics and Python programming. We start by defining categories and their free construction from graphs. Following Walters [26], regular grammars are defined as graphs together with a labelling homomorphism and their grammatical sentences as labelled paths, i.e. arrows of the corresponding free category. This definition is very similar to the definition of a finite state automaton, and we discuss the equivalence between Walters' notion, Chomsky's original definition and finite automata. We end by introducing the cat module, an implementation of free categories and functors which forms the core of DisCoPy.

#### Categories

**Definition 1.1.1** (Simple signature / Directed graph).: _A simple signature, or directed graph, $G$ is a collection of vertices $G_{0}$ and edges $G_{1}$ such that each edge has a domain and a codomain vertex_

$$G_{0}\xleftarrow{\sf dom}\ G_{1}\xrightarrow{\sf cod}G_{0}$$

_. A graph homomorphism $\varphi:G\to\Gamma$ is a pair of functions $\varphi_{0}:G_{0}\to\Gamma_{0}$ and $\varphi_{1}:G_{1}\to\Gamma_{1}$ such that the following diagram commutes:_

_We denote by $G(a,b)$ the edges $f\in G_{1}$ such that ${\sf dom}(f)=a$ and ${\sf cod}(f)=b$. We also write $f:a\to b$ to denote an edge $f\in G(a,b)$._

A category is a directed graph with a composition operation, in this context vertices are called _objects_ and edges are called _arrows_ or _morphisms_.

**Definition 1.1.2** (Category).: _A category ${\bf C}$ is a graph ${\bf C}_{1}\rightrightarrows{\bf C}_{0}$, where ${\bf C}_{0}$ is a set of objects, and ${\bf C}_{1}$ a set of morphisms, equipped with a composition operation $\cdot:{\bf C}(a,b)\times{\bf C}(b,c)\to{\bf C}(a,c)$ defined for any $a,b,c\in{\bf C}_{0}$ such that:_

1. _for any_ $a\in{\bf C}_{0}$ _there is an identity morphism_ ${\tt id}_{a}\in{\bf C}(a,a)$ _(identities)._
2. _for any_ $f:a\to b$_,_ $f\cdot{\tt id}_{a}=f={\tt id}_{b}\cdot f$ _(unit law)._
3. _whenever_ $a\xrightarrow{f}b\xrightarrow{g}c\xrightarrow{h}d$_, we have_ $f\cdot(g\cdot h)=(f\cdot g)\cdot h$ _(associativity)._

_A functor $F:{\bf C}\to{\bf D}$ is a graph homomorphism which respects composition and identities, i.e. for any $a\in{\bf C}_{0}$$F({\tt id}_{a})={\tt id}_{F(a)}$ and whenever $a\xrightarrow{g}b\xrightarrow{f}c$ in ${\bf C}$ we have $F(f\cdot g)=F(f)\cdot F(g)$.__Given a pair of functors $F,G:\mathbf{C}\to\mathbf{D}$, a natural transformation $\alpha:F\to G$ is a family of maps $\alpha_{a}:F(a)\to G(a)$ such that the following diagram commutes:_

(1.1)

_for any $f:a\to b$ in $\mathbf{C}$._

**Remark 1.1.3**.: _The symbol $\to$ appeared remarkably late in the history of symbols with the earliest use registered in Bernard Forest de Belidor's 1737 L'architecture hydraulique, where it is used to denote the direction of a flow of water. Arguably, it conveys more structured information then its predecessor: the Medieval manicule symbol. Its current mathematical use as the type of a morphism $f:x\to y$ appeared only at the beginning of the 20th century, the first extensive use being registered in Hausdorff [14] to denote group homomorphisms._

**Example 1.1.4** (Basic).: _Sets and functions form a category $\mathbf{Set}$. Monoids and monoid homomorphisms for a category $\mathbf{Mon}$. Graphs and graph homomorphisms form a category $\mathbf{Graph}$. Categories and functors form a category $\mathbf{Cat}$._

An arrow $f$ in a graph $G$ is a sequence of edges $f\in G_{1}^{*}$ such that $\mathtt{cod}(f_{i})=\mathtt{dom}(f_{i+1})$, it can be represented graphically as a sequence of arrows:

$$a_{0}\xrightarrow{f}a_{n}=a_{0}\xrightarrow{f_{1}}a_{1}\ldots\xrightarrow{ f_{n}}a_{n}$$

Or as a sequence of vertices and edges:

Or as a sequence of boxes and wires:

Two arrows with matching endpoints can be composed by concatenation.

$$a\xrightarrow{f}b\xrightarrow{g}c=a\xrightarrow{f\cdot g}c$$

Paths on $G$ in fact form a category, denoted $\mathbf{C}(G)$. $\mathbf{C}(G)$ has the property of being the _free category_ generated by $G$[14].

The free category construction is the object part of functor $\mathbf{C}:\mathbf{Graph}\to\mathbf{Cat}$, which associates to any graph homomorphism $\varphi:G\to V$ a functor $\mathbf{C}(\varphi):\mathbf{C}(G)\to\mathbf{C}(V)$ which relabels the vertices and edges in an arrow. This free construction $\mathbf{C}$ is the _left adjoint_ of the functor $U:\mathbf{Cat}\to\mathbf{Graph}$ which forgets the composition operation on arrows. $\mathbf{C}$ is a left adjoint of $U$ in the sense that there is a natural isomorphism:

$$\mathbf{Graph}(G,U(\mathbf{S}))\simeq\mathbf{Cat}(\mathbf{C}(G),\mathbf{S})$$ which says that specifying a functor $F:\mathbf{C}(G)\to\mathbf{S}$ is the same as specifying an arrow in $\mathbf{S}$ for every generator in $G$. This will have important consequences in the context of semantics.

A preorder $P$ is a category with at most one morphism between any two objects. Given $a,b\in P_{0}$, the hom-set $P(a,b)$ is either the singleton or empty, we write $aPb$ for the corresponding boolean value. Identities and composition of the category, correspond to reflexivity and transitivity of the preorder. Following Lambek [1] and [13], we can interpret a preorder as a _logic_, by considering the underlying set as a set of _formulae_ and the relation $\leq$ as a _consequence_ relation, which is usually denoted $\vdash$ (entails). Reflexivity and transitivity of the consequence relation correspond to the following familiar rules of inference.

$$\infer{A\vdash A}{A\vdash B}{B\vdash C}$$ (1.2)

Given a graph $G$ we can build a preorder by taking the reflexive transitive closure of the relation $G\subseteq G_{0}\times G_{0}$ induced by the graph, $\leq=RTC(G)\subseteq G_{0}\times G_{0}$. We can think of the edges of the graph $G$ as a set of _axioms_, then the free preorder $RTC(G)$ captures the logical consequences of these axioms, and, in this simple setting, we have that $a\implies b$ if and only if there is an arrow from $a$ to $b$ in $G$.

This construction is analogous to the free category construction on a graph, and is in fact part of a commuting triangle of adjunctions relating topology, algebra and logic.

$U$$\mathbf{C}$$\mathbf{ From these considerations we deduce that $\mathtt{Path}\in\mathtt{FNL}$, since it is the _function problem_ corresponding to $\exists\mathtt{Path}$. These problems correspond to parsing problems for regular grammars.

#### Regular grammars

We now show how graphs and categories formalise the notion of regular grammar. Fix a finite set of words $V$, called the _vocabulary_, and let us use $V$ to label the edges in a graph $G$. The data for such a _labelling_ is a function $L:G_{1}\to V$ from edges to words, or equivalently a graph homomorphism $L:G\to V$ where $V$ is seen as a graph with one vertex and words as edges. Fix a starting vertex $s_{0}$ and a terminal vertex $s_{1}$. Given any arrow $f:s_{0}\to s_{1}\in\mathbf{C}(G)$, we can concatenate the labels for each generator to obtain a string $L^{*}(f)\in\mathbf{C}(V)=V^{*}$ where $L^{*}=\mathbf{C}(L)$ is the function $L$ applied point-wise to arrows. We say that a string $u\in V^{*}$ is _grammatical_ in $G$ whenever there is an arrow $f:s_{0}\to s_{1}$ in $G$ such that $L(f)=u$. We can think of the arrow $f$ as a witness of the grammaticality of $u$, called a _proof_ in logic and a _derivation_ in the context of formal grammars.

**Definition 1.1.7** (Regular grammar).: _A regular grammar is a finite graph $G$ equipped with a homomorphism $L:G\to V$, where $V$ is a set of words called the vocabulary, and two specified symbols $s_{0},s_{1}\in G_{0}$, the bottom (starting) and top (terminating) symbols. Explicitly it is given by three functions:_

_The language generated by $G$ is given by the image of the labelling functor:_

$$\mathcal{L}(G)=L^{*}(\mathbf{C}(G)(s_{0},s_{1}))\subseteq V^{*}\,.$$

_A morphism of regular grammars $\varphi:G\to H$ is a graph homomorphism such that the following triangle commutes:_

_and such that $\varphi(s_{1})=s_{1}^{\prime}$, $\varphi(s_{0})=s_{0}^{\prime}$. These form a category of regular grammars $\mathbf{Reg}$ which is the slice or $\mathrm{comma}$ category of the coslice over the points $\{\,s_{0},s_{1}\,\}$ of the category of signatures $\mathbf{Reg}=(2\backslash\mathbf{Graph})/V$._

**Definition 1.1.8** (Regular language).: _A regular language is a subset of $X\subseteq V^{*}$ such that there is a regular grammar $G$ with $\mathcal{L}(G)=X$._ 

**Example 1.1.9** (Svo).: _Consider the regular grammar generated by the following graph:_

_An example of sentence in the language $\mathcal{L}(G)$ is "A met B who met C."._

**Example 1.1.10** (Commuting diagrams).: _Commuting diagrams such as 1.1 can be understood using regular grammars. Indeed, a commuting diagram is a graph $G$ together with a labelling of each edge as a morphism in a category $\mathbf{C}$. Given a pair of vertices $x,y\in G_{0}$, we get a regular language $\mathcal{L}(G)$ given by arrows from $x$ to $y$ in $G$. Saying that the diagram $G$ commutes corresponds to the assertion that all strings in $\mathcal{L}(G)$ are equal as morphisms in $\mathbf{C}$._

We now translate from the original definition by Chomsky to the one above. Recall that a regular grammar is a tuple $G=(N,V,P,s)$ where $N$ is a set of non-terminal symbols with a specified start symbol $s\in N$, $V$ is a vocabulary and $P$ is a set of production rules of the form $A\to aB$ or $A\to a$ or $A\to\epsilon$ where $a\in V$, $A,B\in N$ and $\epsilon$ denotes the empty string. We can think of the sentences generated by $G$ as arrows in a free category as follows. Construct the graph $\Sigma=P\rightrightarrows(N+\left\{\,s_{1}\,\right\})$ where for any production rule in $P$ of the form $A\to aB$ there is an edge $A\xrightarrow{f}B$ with $L(f)=a$ and for any production rule $A\to a$ there is an edge $A\xrightarrow{w}s_{1}$ with $L(w)=a$. The language generated by $G$ is the image under $L$ of the set of labelled paths $s\to s_{1}$ in $\Sigma$, i.e. $\mathcal{L}(\Sigma)=L^{*}(\mathbf{C}(\Sigma)(s,s_{1}))$.

This translation is akin to the construction of a _finite state automaton_ from a regular grammar. In fact, the above definition of regular grammar directly is equivalent to the definition of _non-deterministic_ finite state automaton (NFA). Given a regular grammar $(G,L)$, we can construct the span

$$V\times G_{0}\xleftarrow{L\times\mathtt{dom}}G_{1}\xrightarrow{\mathit{cod}} G_{0}$$

which induces a relation $\mathtt{im}(G_{1})\subseteq V\times G_{0}\times G_{0}$, which is precisely the transition table of an NFA with states in $G_{0}$, alphabet symbols $V$ and transitions in $\mathtt{im}(G_{1})$. If we require that the relation $\mathtt{im}(G_{1})$ be a _function_ -- i.e. for any $(v,a)\in V\times G_{0}$ there is a unique $b\in G_{0}$ such that $(v,a,b)\in\mathtt{im}(G_{1})$ -- then this defines a _deterministic_ finite state automaton (DFA). From any NFA, one may build a DFA by blowing up the state space. Indeed relations $X\subseteq V\times G_{0}\times G_{0}$ are the same as functions $V\times G_{0}\to\mathcal{P}(G_{0})$ where $\mathcal{P}$ denotes the powerset construction. So any NFA $X\subseteq V\times G_{0}\times G_{0}$ can be represented as a DFA $V\times\mathcal{P}(G_{0})\to\mathcal{P}(G_{0})$.

Now that we have shown how to recover the original definition of regular grammars, consider the following folklore result from formal language theory.

**Proposition 1.1.11**.: _Regular languages are closed under intersection and union._Proof.: Suppose $G$ and $G^{\prime}$ are regular grammars, with starting states $q_{0},q^{\prime}_{0}$ and terminating states $q_{1},q^{\prime}_{1}$.

Taking the cartesian product of the underlying graphs $G\times G^{\prime}=G_{1}\times G^{\prime}_{1}\rightrightarrows G_{0}\times G^{ \prime}_{0}$ we can define a regular grammar $G\cap G^{\prime}\subseteq G\times G^{\prime}$ with starting state $(q_{0},q^{\prime}_{0})$, terminating state $(q_{1},q^{\prime}_{1})$ and such that there is an edge between $(a,a^{\prime})$ and $(b,b^{\prime})$ whenever there are edges $a\xrightarrow{f}b$ in $G$ and $a^{\prime}\xrightarrow{f^{\prime}}b^{\prime}$ in $G^{\prime}$ with the same label $L(f)=L^{\prime}(f^{\prime})$. Then an arrow from $(q_{0},q^{\prime}_{0})$ to $(q_{1},q^{\prime}_{1})$ in $G\cap G^{\prime}$ is the same as a pair of arrows $q_{0}\to q_{1}$ in $G$ and $q^{\prime}_{0}\to q^{\prime}_{1}$ in $G^{\prime}$. Therefore $\mathcal{L}(G\cap G^{\prime})=\mathcal{L}(G)\cap\mathcal{L}(G^{\prime})$. Proving the first part of the statement.

Moreover, the disjoint union of graphs $G+G^{\prime}$ yields a regular grammar $G\cup G^{\prime}$ by identifying $q_{0}$ with $q^{\prime}_{0}$ and $q_{1}$ with $q^{\prime}_{1}$. Then an arrow $q_{0}\to q_{1}$ in $G\cup G^{\prime}$ is either an arrow $q_{0}\to q_{1}$ in $G$ or an arrow $q^{\prime}_{0}\to q^{\prime}_{1}$ in $G^{\prime}$. Therefore $\mathcal{L}(G\cup G^{\prime})=\mathcal{L}(G)\cup\mathcal{L}(G^{\prime})$. 

The constructions used in this proof are canonical constructions in the category of regular grammars $\mathbf{Reg}$. Note that $\mathbf{Reg}=2\backslash\mathbf{Graph}/V$ is both a slice and a coslice category. Moreover, $\mathbf{Graph}$ has all limits and colimits. While coslice categories reflect limits and slice categories reflect colimits, we cannot compose these two statements to show that $\mathbf{Reg}$ has all limits and colimits. However, we can prove explicitly that the constructions defined above give rise to the categorical product and coproduct. We do not know whether $\mathbf{Reg}$ also has equalizers and coequalizers which would yield all finite limits and colimits.

**Proposition 1.1.12**.: _The intersection $\cap$ of NFAs is the categorical product in $\mathbf{Reg}$. The union $\cup$ of NFAs is the coproduct in $\mathbf{Reg}$._

Proof.: To show the first part. Suppose we have two morphisms of regular grammars $f:H\to G$ and $g:H\to G^{\prime}$. These must respect the starting and terminating symbols as well as the labelling homomorphism. We can construct a homomorphism of signatures $<f,g>:H\to G\cap G^{\prime}$ where $G\cap G^{\prime}=G\times_{V}G^{\prime}$ with starting point $(q_{0},q^{\prime}_{0})$ and endpoint $(q_{1},q^{\prime}_{1})$ as defined above. $<f,g>$ is given on vertices by $<f,g>_{0}(x)=(f_{0}(x),g_{0}(x))$ and on arrows by $<f,g>_{1}(h)=(f_{0}(h),g_{0}(h))$. Since $L(f(h))=L(h)=L(g(h))$, this defines a morphism of regular grammars $<f,g>:H\to G\cap G^{\prime}$. There are projections $G\cap G^{\prime}\to G,G^{\prime}$ induced by the projections $\pi_{0},\pi_{1}:G\times G^{\prime}\to G,G^{\prime}$, and it is easy to check that $\pi_{0}\circ<f,g>=f$ and $\pi_{1}\circ<f,g>=g$ where $\pi $h\in G\subseteq G\cup G^{\prime}$ and $k(h)=g$ otherwise, i.e. $k=[f,g]$. Therefore $G\cup G^{\prime}$ satisfies the universal property of the coproduct in $\mathbf{Reg}$. 

We now study the parsing problem for regular grammars. First, consider the _non-emptiness problem_, which takes as input a regular grammar $G$ and returns "no" if $\mathcal{L}(G)$ is empty and "yes" otherwise.

**Proposition 1.1.13**.: _The non-emptiness problem is equivalent to $\exists\mathtt{Path}$_

Proof.: $\mathcal{L}(G)$ is non-empty if and only if there is an arrow from $s_{0}$ to $s_{1}$ in $G$. 

Now, consider the problem of recognizing the language of a regular grammar $G$, also known as Parsing. We define the proof-relevant version which, of course, has a corresponding decision problem $\exists\mathtt{Parsing}$.

**Definition 1.1.14**.: Parsing__

_Input:_ $G$_,_ $u\in V^{*}$__

_Output:_ $f\in\mathbf{C}(G)(s_{0},s_{1})$ _such that_ $L^{*}(f)=u$_._

Given a string $u\in V^{*}$, we may build the regular grammar $G_{u}$ given by the path-graph with edges labelled according to $u$, so that $\mathcal{L}(G_{u})=\{\,u\,\}$. Then the problem of deciding whether there is a parse for $u$ in $G$ reduces to the non-emptiness problem for the intersection $G\cap G_{u}$. This has the following consequence.

**Proposition 1.1.15**.: $\exists\mathtt{Parsing}$ _is equivalent to $\exists\mathtt{Path}$ and is thus $\mathtt{NL}$-complete. Similarly, Parsing is $\mathtt{FNL}$-complete._

At the end of the section, we give a simple algorithm for parsing regular grammars based on the composition of arrows in a free category. In order to model the higher levels of Chomsky's hierarchy, we need to equip our categories with more structure.

#### cat.Arrow

We have introduced free categories and shown how they appear in formal language theory. These structures have moreover a natural implementation in object-oriented Python, which we now describe. In order to implement a free category in Python we need to define three classes: cat.Ob for objects, cat.Arrow for morphisms and cat.Box for generators. Objects are initialised by providing a name.

**Listing 1.1.16**.: Objects in a free category.__

``` classOb: def__init__(self, name): self.name=name ```

Arrows, i.e. morphisms of free categories, are given by lists of boxes with matching domains and codomains. In order to initialise a cat.Arrow, we provide a domain, a codomain and a list of boxes. The class comes with a method Arrow.then for composition and a static method Arrow.id for generating identity arrows.

 

**Listing 1.17**.: Arrows in a free category.

``` classArrow: def__init__(self,dom,cod,boxes,_scan=True): ifnotisinstance(dom,Ob)ornotisinstance(cod,Ob): raiseTypeError() if_scan: scan=dom fordepth,boxinenumerate(boxes): ifbox.dom!=scan: raiseAxiomError() scan=box.cod ifscan!=cod: raiseAxiomError() self.dom,self.cod,self.boxes=dom,cod,boxes defthen(self,*others): iflen(others)>1: returnself.then(others[0]).then(*others[1:]) other,=others ifself.cod!=other.dom: raiseAxiomError() returnArrow(self.dom,other.cod,self.boxes+other.boxes,_scan=False)) @staticmethod defid(dom): returnArrow(self,dom,dom,[],_scan=False) def__rshift__(self,other): returnself.then(other) def__lshift__(self,other): returnother.then(self) ```

_When_scan==False we do not check that the boxes in the arrow compose. This allows us to avoid checking composition multiple times for the same_Arrow_. The methods__rshift__ and__lshift__ allow to use the syntax_f >>g _and_g _<<f _for the composition of instances of the_Arrow _class._

Finally, generators of the free category are special instances of Arrow, initialised by a name, a domain and a codomain.

**Listing 1.18**.: Generators of a free category.

``` classBox(Arrow): def__init__(self,name,dom,cod): self.name,self.dom,self.cod=name,dom,cod Arrow.__init__(self,dom,cod,[self],_scan=False) ```

_The subclassing mechanism in Python allows for_Box _to inherit all the_Arrow _methods, so that there is essentially no difference between a box and an arrow with one box._

**Remark 1.1.19**.: _It is often useful to define dataclass methods such as __repr__, __str__ and __eq__ to represent, print and check equality of objects in a class. Similarly, other standard methods such as __hash__ may be overwritten and used as syntactic gadgets. We set self.name = name although, in DisCoPy, this parameter is immutable and e.g. Ob.name is implemented as a @property method. In order to remain concise, we will omit these methods when defining further classes._

We now have all the ingredients to compose arrows in free categories. We check that the axioms of categories hold for cat.Arrows on the nose.

**Listing 1.1.20**.: Axioms of free categories.

``` x,y,z=Ob('x'),Ob('y'),Ob('z') f,g,h=Box('f',x,y),Box('g',y,z),Box('h',z,x) assertf>>Arrow.id(y)==f==Arrow.id(x)>>f assert(f>>g)>>h==f>>g>>h==(f>>g)>>h ```

A signature is a pair of lists, for objects and generators. A homomorphism between signatures is a pair of Python dictionnaries. Functors between the corresponding free categories are initialised by a pair of mappings ob, from objects to objects, and ar from boxes to arrows. The call method of Functor allows to evaluate the image of composite arrows.

**Listing 1.1.21**.: Functors from a free category.

``` classFunctor: def__init__(self,ob,ar): self.ob,self.ar=ob,ar def__call__(self,arrow): ifisinstance(arrow,Ob): returnself.ob[arrow] ifisinstance(arrow,Box): returnself.ar[arrow] ifisinstance(arrow,Arrow): returnArrow.id(self(arrow.dom)).then(*map(self, arrow)) raiseTypeError() ```

_We check that the axioms hold._

``` x,y=Ob('x'),Ob('y') f,g=Box('f',x,y),Box('g',y,x) F=Functor(ob='{x:y,y:x},ar={f:g,g:f}) assertF(f>>g)==F(f)>>F(g) assertF(Arrow.id(x))==Arrow.id(F(x)) ```

As a linguistic example, we use the composition method of Arrow to write a simple parser for regular grammars.

**Listing 1.1.22**.: Regular grammar parsing.

from discovery.cat import Ob, Box, Arrow, AxiomError s0, x, s1 = Ob('s0'), Ob('x'), Ob('s1') A, B, C = Box('A', s0, x), Box('B', x, x), Box('A', x, s1) grammar = [A, B, C] def is_grammatical(string, grammar):  arrow = Arrow.id(s0)  bool = False  for x in string:  for box in grammar:  if box.name == x:  try:  arrow = arrow >> box  bool = True  break  except AxiomError:  bool = False  if not bool:  return False  return bool assert is_grammatical("ABBA", grammar) assert not is_grammatical("ABAB", grammar) ```

So far, we have only showed how to implement _free_ categories and functors in Python. However, the same procedure can be repeated. Implementing a category in Python amounts to defining a pair of classes for objects and arrows and a pair of methods for identity and composition. In the case of Arrow, and the syntactic structures of this chapter, we are able to check that the axioms hold in Python. In the next chapter, these arrows will be mapped to concrete Python functions, for which equality cannot be checked.

 

### 1.2 Trees

Context-free grammars (CFGs) emerged from the linguistic work of Chomsky [13] and are used in many areas of computer science. They are obtained from regular grammars by allowing production rules to have more than one output symbol, resulting in tree-shaped derivations. Following Walters [25] and Lambek [14], we formalise CFGs as operadic signatures and their derivations as trees in the corresponding free operad. Morphisms of free operads are trees with labelled nodes and edges. We give an implementation - the operad module of DisCoPy - which satisfies the axioms of operads on the nose and interfaces with the library NLTK [15].

#### Operads

**Definition 1.2.1** (Operadic signature).: _An operadic signature is a pair of functions:_

$$G_{0}^{*}\xleftarrow{\mathtt{dom}}G_{1}\xleftarrow{\mathtt{cod}}G_{0}$$

_where $G_{1}$ is the set of nodes and $G_{0}$ a set of objects. A morphism of operadic signatures $\varphi:G\to\Gamma$ is a pair of functions $\varphi_{0}:G_{0}\to\Gamma_{0}$, $\varphi_{1}:G_{1}\to\Gamma_{1}$ such that the following diagram commutes:_

_With these morphisms, operadic signatures form a category denoted $\mathbf{OpSig}$._

A node or box in an operadic signature is denoted $b_{0}\dots b_{n}\xrightarrow{f}a$. Nodes of the form $a\xrightarrow{w}\epsilon$ for the empty string $\epsilon$ are called _leaves_.

**Definition 1.2.2** (Operad).: _An operad $\mathbf{O}$ is an operadic signature equipped with a composition operation $\cdot:\prod_{b_{i}\in\vec{b}}\mathbf{Op}(\vec{c}_{i},b_{i})\times\mathbf{Op}( \vec{b},a)\to\mathbf{Op}(\vec{c},a)$ defined for any $a\in\mathbf{O}_{0}$, $\vec{b},\vec{c}\in\mathbf{O}_{0}^{*}$. Given $f:\vec{b}\to a$ and $g_{i}:\vec{c_{i}}\to b_{i}$, the composition of $\vec{g}$ with $f$ is denoted graphically as follows._

(1.3)

_We ask that they satisfy the following axioms:_1. _for any_ $a\in\mathbf{O}_{0}$ _there is an identity morphism_ $\mathtt{id}_{a}\in\mathbf{Op}(a,a)$ _(identities)._
2. _for any_ $f:\vec{b}\to a$_,_ $f\cdot\mathtt{id}_{a}=f=\mathtt{id}_{b_{i}}\cdot f$ _(unit law)._
3. (1.4)

_An algebra $F:\mathbf{O}\to\mathbf{N}$ is a morphism of operadic signature which respects composition, i.e. such that whenever $\vec{c}\stackrel{{ g}}{{\rightarrow}}\vec{b}\stackrel{{ f}}{{\rightarrow}}a$ in $\mathbf{O}$ we have $F(\vec{g}\cdot f)=\vec{F(g)}\cdot F(f)$. With algebras as morphisms, operads form a category $\mathbf{Operad}$._

**Remark 1.2.3**.: _The diagrammatic notation we are using is not formal yet, but it will be made rigorous in the following section where we will see that operads are instances of monoidal categories and thus admit a formal graphical language of string diagrams._

Given an operadic signature $G$, we may build the free operad over $G$, denoted $\mathbf{Op}(G)$. Morphism of $\mathbf{Op}(G)$ are labelled trees with nodes from $G$ and edges labelled by elements of the generating objects $B$. Two trees are equivalent (or congruent) if they can be deformed continuously into each other using the interchanger rules 1.4 repeatedly. The free operad construction is part of the following free-forgetful adjunction.

$$\mathbf{OpSig}\stackrel{{\mathbf{Op}}}{{\rightleftarrows}} \mathbf{Operad}$$

This means that for any operadic signature $G$ and operad $\mathbf{O}$, algebras $\mathbf{Op}(G)\to\mathbf{O}$ are in bijective correspondence with morphisms of operadic signatures $G\to U(\mathbf{O})$.

**Example 1.2.4** (Peirce's alpha).: _Morphisms in an operad can be depicted as trees, or equivalently as a nesting of bubbles:_

(1.5)

_Interestingly, the nesting perspective was adopted by Peirce in his graphical formulation of propositional logic: the alpha graphs [11]. We may present Peirce's alpha graphs as an operad $\alpha$ with a single object $x$, variables as leaves $a,b,c,d:1\to x$ a binary operation $\wedge:xx\to x$ and a unary operation $\neg:x\to x$, together with equations encoding the associativity of $\wedge$ and $\neg\neg=\mathtt{id}_{x}$. In order to encode Peirce's rules for "iteration" and "weakening", we would need to work in a preordered operad, but we omit these rules here, see [1] for a full axiomatisation. The main purpose here is to note that the nesting notation is sometimes more practical than its tree counterpart. Indeed, since $\wedge$ is associative and it is the only binary operation in $\alpha$, when two symbols are put side by side on the page, it is unambiguous that one should take the conjunction $\wedge$. Therefore the nested notation simplifies reasoning and we may draw the propositional formula_

$$\neg(a_{0}\wedge\,\neg(a_{1}\wedge a_{2})\,\wedge a_{3})$$

_as the following diagram:_

$$\tikzfig{height=1.5}$$ (1.6)

#### Context-free grammars

Given a finite operadic signature $G$, we can intepret the nodes in $G$ as _production rules_, the generating objects as _symbols_, and morphisms in the free operad $\mathbf{Op}(G)$ as _derivations_, obtaining the notion of a context-free grammar.

**Definition 1.2.5** (Context-free grammar).: _A CFG is a finite operadic signature of the following shape:_

$$(B+V)^{*}\gets G\to B$$

_where $B$ is a set of non-terminal symbols with a specified sentence symbol $s\in B$, $V$ is a vocabulary (a.k.a a set of terminal symbols) and $G$ is a set of production rules. The language generated by $G$ is given by:_

$$\mathcal{L}(G)=\{\,u\in V^{*}\,|\,\exists g:u\to s\in\mathbf{Op}(G)\,\}$$

_where $\mathbf{Op}(G)$ is the free operad of labelled trees with nodes from $G$._

**Remark 1.2.6**.: _Note that the direction of the arrows is the opposite of the usual direction used for CFGs, instead of seeing a derivation as a tree from the sentence symbol $s$ to the terminal symbols $u\in V^{*}$, we see it as a tree from $u$ to $s$. This, of course, does not change any of the theory._

**Definition 1.2.7** (Context-free language).: _A context-free language is a subset $X\subseteq V^{*}$ such that $X=\mathcal{L}(G)$ for some context-free grammar $G$._

**Example 1.2.8** (Backus Naur Form).: _BNF is a convenient syntax for defining context-free languages recursively. An example is the following expression:_

$$s\gets s\wedge s\,|\,\neg s\,|\,a$$ $$a\gets a_{0}\,|\,a_{1}\,|\,a_{2}\,|\,a_{3}$$

_which defines a CFG with seven production rules $\{s\gets s\wedge s\,,\,s\leftarrow\neg s\,,\,s\gets a\,a\gets a_{0} \,a\gets a_{1}\,a\gets a_{2}\,a\gets a_{3}\}$ and such that trees with root $s$ are well-formed propositional logic formulae with variables in $\{\,a_{0},a_{1},a_{2},a_{3}\,\}$. An example of a valid propositional formula is_

$$\neg(a_{0}\wedge a_{1})\,\wedge\,\neg(a_{2}\wedge a_{3})$$

_as witnessed by the following tree:_

_where we have omitted the types of intermediate wires for readability._

**Example 1.2.9**.: _As a linguistic example, let $B=\{\,n,d,v,vp,np,s\,\}$ for nouns, prepositions, verbs, verb phrases and prepositional phrases, and let $G$ be the CFG defined by the following lexical rules:_

$$\text{Caesar}\to n\quad\text{the}\to d\quad\text{Rubicon}\to n\quad\text{crossed }\to v$$

_together with the production rules $n\cdot v\to vp$, $n\cdot d\to vp$, $vp\cdot pp\to s$. Then the following is a grammatical derivation:_

_[scale=0.5]_

**Example 1.2.10** (Regular grammars revisited).: _Any regular grammar yields a CFG._ _The translation is given by turning paths into left-handed trees as follows:_

(1.7)

_Not all CFGs arise in this way. For example, the language of well-bracketed expressions, defined by the CFG with a single production rule $G=\{\,s\leftarrow(s)\,\}$, cannot be generated by a regular grammar. We can prove this using the pumping lemma. Indeed, suppose there is a regular grammar $G^{\prime}$ such that well-bracketed expressions are paths in $G^{\prime}$. Let $n$ be the number of vertices in $G^{\prime}$ and consider the grammatical expression $x=(\dots()\dots)$ with $n+1$ open and $n+1$ closed brackets. If $G^{\prime}$ parses $x$, then there must be a path $p_{0}$ in $G^{\prime}$ with labelling $(\dots($ and a path $p_{1}$ with labelling $(\dots)$ such that $p_{0}\cdot p_{1}:s_{0}\to s_{1}$ in $G^{\prime}$. By the pigeon hole principle, the path $p_{0}$ must have a cycle of length $k\geq 1$. Remove this cycle from $p_{0}$ to get a new path $p^{\prime}_{0}$. Then $p^{\prime}_{0}\cdot p_{1}$ yields a grammatical expression $x^{\prime}=(\dots()\dots)$ with $n+1-k$ open brackets and $n+1$ closed brackets. But then $x^{\prime}$ is not a well-bracketed expression. Therefore regular grammars cannot generate the language of well-bracketed expressions and we deduce that regular languages are strictly contained in context-free languages._

We briefly consider the problem of parsing context-free grammars.

**Definition 1.2.11**.: CfgParsing__

_Input:_ $G$_,_ $u\in V^{*}$__

_Output:_ $f\in\mathbf{Op}(G)(u,s)$__

This problem can be solved using a _pushdown automaton_, and in fact any language recognized by a pushdown automaton is context-free [10]. The following result was shown independently by several researchers at the end of the 1960s.

**Proposition 1.2.12**.: _[_11, 12_]_ _Context-free grammars can be parsed in cubic time._

#### operad.Tree

Tree data structures are ubiquitous in computer science. They can implemented via the inductive definition: a tree is a root together with a list of trees. Implementing operads as defined in this Section, presents some extra difficulties in handling types (domains and codomains) and identities. In fact, the concept of "identity tree" is not frequent in the computer science literature. Our implementation of free operads consists in the definition of classes operad.Tree, operad.Box, operad.Id and operad.Algebra, corresponding to morphisms (trees), generators (nodes), identities and algebras of free operads, respectively. A Tree is initialised by a root, instance of Node, together with a list of Trees called branches. Alternatively, it may be built from generating Boxs using the Tree.__call__ method, this allows for an intuitive syntax which we illustrate below.

**Listing 1.2.13**.: Tree in a free operad.

``` classTree: def__init__(self,root,branches,_scan=True): ifnotisinstance(root,Box): raiseTypeError() ifnotall([isinstance(branch,Tree)forbranchinbranches]): raiseTypeError() if__scanandnotroot.cod==[branch.domforbranchinbranches]: raiseAxiomError() self.dom,self.root,self.branches=root.dom,root,branches @property defcod(self): ifisinstance(self,Box): returnself._cod else: return[xforxinbranch.codforbranchinself.branches] def__repr__(self): return"Tree({},{})".format(self.root,self.branches) def__str__(self): ifisinstance(self,Box): returnself.name return"({})".format(self.root.name, ','.join(map(Tree.__str__,self.branches))) def__call__(self,*others): ifnotothersorall([isinstance(other,Id)forotherinothers]): returnself ifisinstance(self,Id): returnothers[0] ifisinstance(self,Box): returnTree(self,list(others)) ifisinstance(self,Tree): lengths=[len(branch.cod)forbranchinself.branches] ranges=[0]+[sum(lengths[:i+1])foriinrange(len(lengths))] branches=[self.branches[i](*others[ranges[i]:ranges[i+1]]) foriinrange(len(self.branches))] returnTree(self.root,branches,_scan=False) raiseNotImplementedError() ``` @staticmethod defid(dom): returnId(dom) def__eq__(self,other): returnself.root==other.rootandself.branches==other.branches ```

A Box is initialised by label name, a domain object dom and a list of objects cod for the codomain.

**Listing 2.14**.: Node in a free operad.

``` classBox(Tree): def__init__(self,name,dom,cod): ifnot(isinstance(dom,Ob)andisinstance(cod,list) andall([isinstance(x,Ob)forxincod])): returnTypeError self.name,self.dom,self..cod=name,dom,cod Tree...init__(self,self,[],_scan=False) def__repr__(self): return"Box('{'}',{},{})".format(self.name,self.dom,self..cod) def__hash__(self): returnhash(repr(self)) def__eq__(self,other): ifisinstance(other,Box): returnself.dom==other.domandself.cod==other.cod \ andself.name==other.name ifisinstance(other,Tree): returnother.root==selfandother.branches==[] ```

An Id is a special type of node, which cancels locally when composed with other trees. The cases in which identities must be removed are handled in the Tree.__call__ method. The Tree.__init__ method, as it stands, does not check the identity axioms. We will however always use the__call__ syntax to construct our trees.

**Listing 2.15**.: Identity in a free operad.

``` classId(Box): def__init__(self,dom): self.dom,self..cod=dom,[dom] Box.__init__(self,"Id({})".format(dom),dom,dom) def__repr__(self): return"Id({})".format(self.dom) ```

We can check that the axioms of operads hold for Tree.__call__.

**Listing 2.16**.: Axioms of free operads.

 x, y = Ob('x'), Ob('y') f, g, h = Box('f', x, [x, x]), Box('g', x, [x, y]), Box('h', x, [y, x]) assert Id(x)(f) == f == f(Id(x), Id(x)) left = f(Id(x), h)(g, Id(x), Id(x)) middle = f(g, h) right = f(g, Id(x))(Id(x), Id(x), h) assert left == middle == right == Tree(root=f, branches=[g, h]) ```

Listing 1.2.17: We construct the tree from Example 1.2.9.

``` n, d, v, vp, np, s = Ob('N'), Ob('D'), Ob('V'), Ob('VP'), Ob('SP') Caesar, crossed = Box('Caesar', n, []), Box('crossed', v, []), the, Rubicon = Box('the', d, []), Box('Rubicon', n, []) VP, NP, S = Box('VP', vp, [n, v]), Box('NP', np, [d, n]), Box('S', s, [vp, np]) sentence = S(VP(Caesar, crossed), NP(the, Rubicon)) ```

We define the Algebra class, which implements operad algebras as defined in 1.2.2 and is initialised by a pair of mappings: ob from objects to objects and ar from nodes to trees. These implement functorial reductions and functorial semantics of CFGs, as defined in the next section and chapter respectively.

``` classAlgebra: def__init__(self, ob, ar, cod=Tree): self.cod, self.ob, self.ar = cod, ob, ar def__call__(self, tree): if isinstance(tree, Id): return self.cod.id(self.ob[tree]) if isinstance(tree, Box): return self.ar[tree] return self.ar[tree.root](*[self(branch)forbranchintree.branches]) ```

_Note that we parametrised the class algebra over a codomain class, which by default is the free operad Tree. We may build any algebra from the free operad to an operad $A$ by providing a class cod=A with A.id and A.__call__ methods. We will see a first example of this when we interface Tree with Diagram in the next section. Further examples will be given in Chapter 2._

We end by interfacing the operad module with the library NLTK [LB02].

**Listing 1.2.19**.: Interface between nltk.Tree and operad.Tree.

``` deffrom_nltk(tree): branches, cod = [], [] forbranchintree: if isinstance(branch, str): returnBox(branch, Ob(tree.label()), []) else: branches += [from_nltk(branch)] cod += [Ob(branch.label())] root = Box(tree.label(), Ob(tree.label()), cod) return root(*branches) _This code assumes that the tree is generated from a lexicalised CFG. The operad module of DisCoPy contains the more general version. We can now define a grammar in NLTK, parse it, and extract an operad.Tree. We check that we recover the correct tree for "Caesar crossed the Rubicon"._

``` fromnltkimportCFG fromnltk.parseimportRecursiveDescentParser grammar=CFG.fromstring(""" S->VPNP NP->DN VP N N->'Caesar' V->'crossed' D->'the' N->'Rubicon""") rd=RecursiveDescentParser(grammar) forxinrd.parse('CaesarcrossedtheRubicon'.split()): tree=from_nltk(x) asserttree==sentence ``` 

### 1.3 Diagrams

String diagrams in monoidal categories are the key tool that we use to represent syntactic structures. In this section we introduce _monoidal grammars_, the equivalent of Chomsky's unrestricted type-0 grammars. Their derivations are string diagrams in a free monoidal category. We introduce _functorial reductions_ as a structured way of comparing monoidal grammars, and motivate them as a tool to reason about equivalence and normal forms for context-free grammar. String diagrams have a convenient _premonoidal encoding_ as lists of layers, which allows to implement the class monoidal.Diagram as a subclass of cat.Arrow. We give an overview of the monoidal module of DisCoPy and its interface with operad.

\begin{tabular}{|c|c|c|} \hline Monoidal category & Type-0 grammar & Python \\ \hline objects & strings & Ty \\ generators & production rules & Box \\ morphisms & derivations & Diagram \\ functors & reductions & Functor \\ \hline \end{tabular}

#### Monoidal categories

**Definition 1.3.1** (Monoidal signature).: _A monoidal signature $G$ is a signature of the following form:_

$$G_{0}^{*}\xleftarrow{\sf dom}\ G_{1}\xleftarrow{\sf cod}\ G_{0}^{*}$$

_. $G$ is a finite monoidal signature if $G_{1}$ is finite. A morphism of monoidal signatures $\varphi:G\to\Gamma$ is a pair of maps $\varphi_{0}:G_{0}\to\Gamma_{0}$ and $\varphi_{1}:G_{1}\to\Gamma_{1}$ such that the following diagram commutes:_

$$\begin{CD}G_{0}^{*}@<{\sf dom}<{}<G_{1}@>{\sf cod}<{}<G_{0}^{*}\\ @V{\varphi_{0}^{*}}V{\Gamma_{0}^{*}}V@V{\varphi_{1}}V{\Gamma_{0}^{*}}V\\ \end{CD}$$

_With these morphisms, monoidal signatures form a category_ ${\bf MonSig}$_._

Elements $f:\vec{a}\to\vec{b}$ of $G_{1}$ are called _boxes_ and are denoted by the following diagram, read from top to bottom, special cases are states and effects with no inputs and outputs respectively.

\begin{tabular}{|c|c|c|} \hline Box & $f$ & State & $w$ \\ \hline $b_{0}$ & $\cdots$ & $b_{n}$ & Effect & $m$ \\ \hline \end{tabular}

**Definition 1.3.2** (Monoidal category).: _A (strict) monoidal category is a category ${\bf C}$ equipped with a functor $\otimes:{\bf C}\times{\bf C}\to{\bf C}$ called the tensor and a specified object $1\in{\bf C}_{0}$ called the unit, satisfying the following axioms:_1. $1\otimes f=f=f\otimes 1$ _(unit law)_
2. $(f\otimes g)\otimes h=f\otimes(g\otimes h)$ _(associativity)_

_for any $f,g,h\in\mathbf{C}_{1}$. A (strict) monoidal functor is a functor that preserves the tensor product on the nose, i.e. such that $F(f\otimes g)=F(f)\otimes F(g)$. The category of monoidal categories and monoidal functors is denoted $\mathbf{MonCat}$._

**Remark 1.3.3**.: _The general (non-strict) definition of a monoidal category relaxes the equalities in the unit and associativity laws to the existence of natural isomorphisms, called unitors and associators. These are then required to satisfy some coherence conditions in the form of commuting diagrams, see MacLane [11]. In practice, these natural transformations are not used in calculations. MacLane's coherence theorem ensures that any monoidal category is equivalent to a strict one._

Given a monoidal signature $G$ we can generate the free monoidal category $\mathbf{MC}(G)$, i.e. there is a free-forgetful adjunction:

$$\mathbf{MonSig}\underset{U}{\overset{\mathbf{MC}}{\rightleftarrows}}\mathbf{ MonCat}$$

This means that for any monoidal signature $G$ and monoidal category $\mathbf{S}$, functors $\mathbf{MC}(G)\rightarrow\mathbf{S}$ are in bijective correspondence with morphisms of signatures $G\to U(\mathbf{S})$. The free monoidal category was first characterized by Joyal and Street [10] who showed that morphisms in $\mathbf{MC}(G)$ are topological objects called _string diagrams_. We follow the formalisation of Delpeuch and Vicary [13] who provided an equivalent combinatorial definition of string diagrams.

Given a monoidal signature $G$, we can construct the signature of _layers_:

$$G_{0}^{*}\underset{U}{\overset{\mathsf{dom}}{\rightleftarrows}}L(G)=G_{0}^{* }\times G_{1}\times G_{0}^{*}\overset{\mathsf{cod}}{\longrightarrow}G_{0}^{*}$$

where for every layer $l=(u,f:x\to y,v)\in L(G)$ we define $\mathsf{dom}(l)=uxv$ and $\mathsf{cod}(l)=uyv$. A layer $l\in L(G)$ is denoted as follows:

The set of _premonoidal diagrams_$\mathbf{PMC}(G)$ is the set of morphisms of the free category generated by the layers:

$$\mathbf{PMC}(G)=\mathbf{C}(L(G))$$

They are precisely morphisms of free premonoidal categories in the sense of [12]. Morphisms $d\in\mathbf{PMC}(G)$ are lists of layers $d=(d_{1},\dots,d_{n})$ such that $\mathsf{cod}(d_{i})=\mathsf{dom}(d_{i+1})$. The data for such a diagram may be presented in a more succint way as follows.

**Proposition 1.3.4** (Premonoidal encoding).: _[_13_]_ _A premonoidal diagram $d\in\mathbf{PMC}(G)$ is uniquely defined by the following data:_ 1. _a domain_ $\mathtt{dom}(d)\in\Sigma_{0}^{*}$_,_
2. _a codomain_ $\mathtt{cod}(d)\in\Sigma_{0}^{*}$_,_
3. _a list of boxes_ $\mathtt{boxes}(d)\in G_{1}^{n}$_,_
4. _a list of offsets_ $\mathtt{offsets}(d)\in\mathbb{N}^{n}$_._

_Where $n\in\mathbb{N}$ is the length of the diagram and the offsets indicate the number of boxes to the left of each wire. This data defines a valid premonoidal diagram if for $0<i\leq n$ we have:_

$$\mathtt{width}(d)_{i}\geq\mathtt{offsets}(d)_{i}+|\mathtt{dom}(b_{i})|$$

_where the widths are defined inductively by:_

$$\mathtt{width}(d)_{1}=\mathtt{size}(\mathtt{dom}(d))\quad\mathtt{width}(d)_ {i+1}=\mathtt{width}(d)_{i}+|\mathtt{cod}(b_{i})|-|\mathtt{dom}(b_{i})|$$

_and $b_{i}=\mathtt{boxes}(d)_{i}$._

As an example consider the following diagram:

It has the following combinatorial encoding:

$$(\mathtt{dom}=abc,\mathtt{cod}=auyv,\mathtt{boxes}=[f,g,h],\mathtt{offsets}=[2 ,1,2])$$

where $f:c\to xv$, $g:b\to u$ and $h:x\to y$ and $a,b,c,x,u,y,v\in\mathcal{G}_{0}$. This combinatorial encoding is the underlying data-structure of both the online proof assistant Globular [1] and the Python implementation of monoidal categories DisCoPy [13].

Premonoidal diagrams are a useful intermediate step to define the _free monoidal category_$\mathbf{MC}(G)$ over a monoidal signature $G$. Indeed, morphisms in $\mathbf{MC}(G)$ are equivalence classes of the quotient of $\mathbf{PMC}(G)$ by the _interchanger rules_, given by the following relation:

$$\left|\begin{array}{c}u\\ \hline\end{array}\right|\begin{array}{c}a\\ \hline\end{array}\right|\begin{array}{c}x\\ \hline\end{array}\right|\begin{array}{c}v\\ \hline\end{array}\sim\left|\begin{array}{c}u\\ \hline\end{array}\right|\begin{array}{c}a\\ \hline\end{array}\right|\begin{array}{c}x\\ \hline\end{array}$$ (1.8)

The following result was proved by Delpeuch and Vicary [14], who showed how to translate between the combinatorial definition of diagrams and the definition of Joyal and Street as planar progressive graphs up to planar isotopy [15].

 

**Proposition 1.3.5**.: _[_21_]___

$$\mathbf{MC}(G)\simeq\mathbf{PMC}(G)/\sim$$

Given two representatives $d,d^{\prime}:u\to v\in\mathbf{PMC}(G)$ we may check whether they are equal in $\mathbf{MC}(G)$ in cubic time [21]. Assuming $d$ and $d^{\prime}$ are boundary connected diagrams, this is done by turning $d$ and $d^{\prime}$ into their interchanger normal form, which is obtained by applying the interchanger rules 1.8 from left to right repeatedly. For disconnected diagrams the normalization requires more machinery but can still be performed efficiently, see [21] for details.

#### Monoidal grammars

Monoidal categories appear in linguistics as a result of the following change of terminology. Given a monoidal signature $G$, we may think of the objects in $G_{0}^{*}$ as _strings_ of symbols, the generating arrows in $G_{1}$ as _production rules_ and morphisms in $\mathbf{MC}(G)$ as _derivations_. We directly obtain a definition of Chomsky's generative grammars, or string rewriting system, using the notion of a monoidal signature.

**Definition 1.3.6** (Monoidal Grammar).: _A monoidal grammar is a finite monoidal signature $G$ of the following shape:_

$$(V+B)^{*}\xleftarrow{\mathtt{dom}}G\xrightarrow{\mathtt{cod}}(V+B)^{*}$$

_where $V$ is a set of words called the vocabulary, and $B$ is a set of symbols with $s\in B$ the sentence symbol. An utterance $u\in V^{*}$ is grammatical if there is a string diagram $g:u\to s$ in $\mathbf{MC}(G)$, i.e. the language generated by $G$ is given by:_

$$\mathcal{L}(G)=\{\,u\in V^{*}\,|\,\exists f\in\mathbf{MC}(G)(u,s)\,\}$$

_The free monoidal category $\mathbf{MC}(G)$ is called the category of derivations of $G$._

**Remark 1.3.7**.: _Any context-free grammar as defined in 1.2.5 yields directly a monoidal grammar._

**Proposition 1.3.8**.: _The languages generated by monoidal grammars are equivalent to the languages generated by Chomsky's unrestricted grammars._

Proof.: Unrestricted grammars are defined as finite relations $P\subseteq(V+B)^{*}\times(V+B)^{*}$ where $V$ is a set of terminal symbols, $B$ a set of non-terminals and $P$ is a set of prodution rules [10]. The only difference between this definition and monoidal grammars is that the latter allow more than one production rule between pairs of strings. However, a string $u$ is in the language if _there exists_ a derivation $g:u\to s$. Therefore the languages are equivalent. 

We define recursively enumerable languages as those generated by monoidal grammars, or equivalently by Chomsky's unrestricted grammars, or equivalently those recognized by Turing machines as discussed in the next paragraph.



**Definition 1.3.9** (Recursively enumerable language).: _A recursively enumerable language is a subset $X\subseteq V^{*}$ such that $X=\mathcal{L}(G)$ for some monoidal grammar $G$._

**Example 1.3.10** (Cooking recipes).: _As an example of a monoidal grammar, let $V=\{\text{aubergine},\text{tomato},\text{parmigiana}\}$ be a set of cooking ingredients, $B=\{\text{\,parmigiana}\}$ be a set of dishes and let $G$ be a set of cooking steps, e.g._

$$\mathtt{stack}:a\,p\to p\quad\mathtt{take}:t\to t\,t\quad\mathtt{spread}:t\,p \to p\quad\mathtt{eat}:t\to 1.$$

_Then the derivations $u\to\text{parmigiana}$ in $\mathbf{MC}(G)$ with $u\in V^{*}$ are cooking recipes to make parmigiana. For instance, the following is a valid cooking recipe:_

_aubergine parmigiana tomato_

_parmigiana_

_tomato_

_parmigiana_

Recall that a Turing machine is given by a tuple $(Q,\Gamma,\sharp,V,\delta,q_{0},s)$ where $Q$ is a finite set of _states_, $\Gamma$ is a finite set of _alphabet_ symbols, $\sharp\in\Gamma$ is the _blank_ symbol, $V\subseteq\Gamma\backslash\{\,\sharp\,\}$ is the set of _input_ symbols, $q_{0}\in Q$ is the _initial_ state, $s\in Q$ is the _accepting_ state and $\delta\subseteq((Q\backslash\{\,s\,\})\times\Gamma)\times(Q\times\Gamma) \times\{\,L,R\,\}$ is a _transition_ table, specifying the next state in $Q$ from a current state, the symbol in $\Gamma$ to overwrite the current symbol pointed by the head and the next head movement (left or right). At the start of the computation, the machine is in state $q_{0}$ and the tape contains a string of initial symbols $u\in V^{*}$ followed by the blank symbol $\sharp$ indicating the end of the tape. The computation is then performed by applying transitions according to $\delta$ until the accepting state $s$ is reached. We assume that the transition $\delta$ doesn't overwrite the blank symbol and that it leaves it at the end of the tape.

A Turing machine may be encoded in a monoidal grammar as follows. The set of non-terminal symbols is $B=(\Gamma\backslash V)+Q$, the set of terminal symbols is $V$ and the sentence type is $s\in B$. The production rules in $G$ are given by:

(1.9)

for all $a,a^{\prime},b,b^{\prime}\in\Gamma\backslash\{\,\sharp\,\},q,q^{\prime}\in Q$ such that $\delta((q,a),(q^{\prime},a^{\prime},R))=1$ and $\delta((q,b),(q^{\prime},b^{\prime},L))=1$ and $\delta((q,\sharp),(q^{\prime},\sharp,L))=1$. Note that the last rule ensures that the blank symbol $\sharp$ is always left at the end of the tape and never overwritten. Then we have that morphisms in $\mathbf{MC}(G)(q_{0}\,w\,\sharp,u\,s\,v)$ are terminating runs of the Turing machine. In order to express these runs as morphisms $w\to s$ we may erase the content of the tape once we reach the accepting state by adding a production rule $xsy\to s$ to $G$ for any $x,y\in B$. Using this encoding we can prove the following proposition.



**Proposition 1.3.11**.: _The parsing problem for monoidal grammars is undecidable._

Proof.: The encoding of Turing machines into monoidal grammars given above reduces the problem of parsing monoidal grammars to the Halting problem for Turing machines. Therefore it is an undecidable problem. 

#### 1.3.3 Functorial reductions

We now come to the question of reduction and equivalence for grammars. Several definitions are available in the literature and we introduce three alternative notions of varying strengths. The most established notion of equivalence between CFGs -- known as _weak equivalence_ -- judges a grammar from the language it generates.

**Definition 1.3.12** (Weak reduction).: _Let $G$ and $G^{\prime}$ be monoidal grammars over the same vocabulary $V$. We say that $G$ reduces weakly to $G^{\prime}$, denoted $G\leq G^{\prime}$, if $\mathcal{L}(G)\subseteq\mathcal{L}(G^{\prime})$. $G$ is weakly equivalent to $G^{\prime}$ if $\mathcal{L}(G)=\mathcal{L}(G^{\prime})$._

Even if two grammars are weakly equivalent, they may generate their sentences in completely different ways. This motivates the definition of a stronger notion of equivalence, which does not only ask for the generated languages to be equal, but also for the corresponding derivations to be the same. This notion has been studied in a line of work connecting context-free grammars (CFGs) and algebraic signatures [11, 12, 13], which we discuss below.

**Definition 1.3.13** (Strong reduction).: _Let $G$ and $G^{\prime}$ be monoidal grammars over the same vocabulary $V$. A strong reduction from $G$ to $G^{\prime}$ is a morphism of monoidal signatures $f:G\to G^{\prime}$ such that $f_{0}(v)=v$ for any $v\in V$ and $f_{0}(s)=s^{\prime}$. With strong reductions as morphisms, monoidal grammars over $V$ form a subcategory of $\mathbf{MonSig}$ denoted $\mathbf{Grammar}_{V}$. We say that $G$ and $G^{\prime}$ are strongly equivalent if they are isomorphic in $\mathbf{Grammar}_{V}$._

Note first that strong reduction subsumes its weak counterpart. Indeed given a morphism $f:G\to G^{\prime}$, we get a functor $\mathbf{MC}(f):\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$ mapping syntax trees of one grammar into syntax trees of the other. Since $f_{0}(v)=v$ for all $v\in V$ and $f_{0}(s)=s^{\prime}$, there is an induced function $\mathbf{MC}(f):\mathbf{MC}(G)(u,s)\to\mathbf{MC}(G^{\prime})(u,s^{\prime})$ for any $u\in V^{*}$, which implies that $\mathcal{L}(G)\subseteq\mathcal{L}(G^{\prime})$.

A strong reduction $f$ is a consistent relabelling of the nodes and types of the underlying operadic signature. This often results in too strict of a notion, since it relates very few grammars together. We introduce an intermediate notion of reduction between grammars, which we call _functorial reduction_.

**Definition 1.3.14** (Functorial reduction).: _Let $G$ and $G^{\prime}$ be monoidal grammars over the same vocabulary $V$. A functorial reduction from $G$ to $G^{\prime}$ is a functor $F:\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$ such that $F_{0}(v)=v$ for all $v\in V$ and $F_{0}(s)=s^{\prime}$. A functorial equivalence between $G$ and $G^{\prime}$ is a pair of functors $F:\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$ and $F^{\prime}:\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$. With functorial reductions as morphisms, monoidal grammars over $V$ form a category $\mathbf{Grammar}_{V}$._

**Remark 1.3.15**.: _The passage from strong to functorial reductions can be seen as as a Kleisli category construction. The free operad functor $\mathbf{MC}:\mathbf{MonSig}\to\mathbf{MonCat}$ induces a monad $U\circ\mathbf{MC}:\mathbf{MonSig}\to\mathbf{MonSig}$. We can construct the Kleisli category $\mathbf{KI}(U\circ\mathbf{MC})$ with objects given by operadic signatures and morphisms given by morphisms of signatures $f:G\to U\mathbf{MC}(G^{\prime})$. Equivalently, a morphism $G\to G^{\prime}$ in $\mathbf{KI}(U\circ\mathbf{MC})$ is a functor $\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$ since $\mathbf{MC}\dashv U$. $\mathbf{MC}$ to $\mathbf{Cfg}_{V}$ we still have an adjunction $\mathbf{MC}\dashv U$ and the following equivalence:_

$$\mathbf{Grammar}_{V}\simeq\mathbf{KI}(U\circ\mathbf{MC}).$$

Functorial reductions can be computed in logarithmic space. We give a proof, an alternative proof is given by the code for $\mathtt{Functor}\_\_$call$\_$.

**Proposition 1.3.16**.: _Funtorial reductions can be computed in log-space $\mathsf{L}$._

Proof.: Let $G$ and $G^{\prime}$ be monoidal grammars, a functorial reduction from $G$ to $G^{\prime}$ is a functor $F:\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$. By the universal property of the free monoidal category $\mathbf{MC}(G)$ the data for such a functor is a finite homomorphism of signatures $G\to U(\mathbf{MC}(G^{\prime}))$, i.e. a collection of morphisms $\left\{\,F(f)\,\right\}_{f\in G}$. Consider the problem which takes as input a diagram $g:x\to y\in\mathbf{MC}(G)$ and a functorial reduction $F:G\to U(\mathbf{MC}(G^{\prime}))$ and outputs $F(g)\in\mathbf{MC}(G^{\prime})$. We assume that we have premonoidal representations of $g$ and $F(f)$ for every production rule $f\in G$, i.e. they all come as a pair of lists for boxes and offsets. In order to compute $F(g)$ we run through the list of boxes and replace each box $f$ of $g$ by $F(f)$ adding the offset of $f$ to every offset in $F(f)$. This can be computed using a constant number of counters (one for the index of the box in the list, one for the offset and one for the pointer to $F(f)$) thus functorial reductions are in logspace. 

From the monoidal definition of weak, strong and functorial reduction we derive the corresponding notions for regular and CFGs using the following diagram.

We can now compare regular, context-free and unrestricted grammars via the notion of reduction.

**Proposition 1.3.17**.: _Any regular grammar strongly reduces to a CFG and any CFG to a monoidal grammar._

Proof.: This is done by proving that the injections in the diagram above exist and make the diagram commute. 

The functorial notion of reduction sits in-between the weak and strong notions. As shown above, any strong reduction $f:G\to G^{\prime}$ induces a functorial reduction $\mathbf{MC}(f):\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$ via the free construction $\mathbf{MC}:\mathbf{MonSig}\to\mathbf{MonCat}$ andthe existence of such a functor induces an inclusion of the corresponding languages. However, not all functorial reductions are strong. It is well-known that any CFG can be lexicalised without losing expressivity, the resulting grammar is functorially and not strongly equivalent to the original CFG.

**Definition 1.3.18** (Lexicalised CFG).: _A lexicalised CFG is an operadic signature of the following shape:_

$$B^{*}+V\gets G\to B$$

_In other words, all production rules involving terminal symbols in $V$ are of the form $w\to b$ for $w\in V$ and $b\in B$. These are called lexical rules._

**Proposition 1.3.19**.: _Any CFG is functorially (and not strongly) equivalent to a lexicalised CFG._

Proof.: For any CFG $(B+V)^{*}\gets G\to B$ we can build a lexicalised CFG $B^{\prime*}+V\gets G^{\prime}\to B^{\prime}$ where $B^{\prime}=B+V$ and $G^{\prime}=G+\left\{\,v\to v\,\right\}_{v\in V}$, where we distinguish between the two copies of $V$. There is a functor $F:\mathbf{MC}(G)\to\mathbf{MC}(G^{\prime})$ given on objects by $F_{0}(x)=x$ for $x\in B+V$ and on arrows $f:\vec{y}\to x$ by $F_{1}(f)=\vec{g}\cdot f$ where $g_{i}:y_{i}\to y_{i}$ is the identity if $y_{i}\in B$ and is a lexical rule $y_{i}\to y_{i}$ if $y_{i}\in V$. Similarly for the other direction, there is a functor $F^{\prime}:\mathbf{MC}(G^{\prime})\to\mathbf{MC}(G)$ given on objects by $F^{\prime}_{0}(x)=x$ for all $x\in B+V$ and on arrows by $F^{\prime}_{1}(f)=f$ for $f\in G$ and $F_{1}(v\to v)=\mathtt{id}_{v}$. Therefore $G$ and $G^{\prime}$ are functorially equivalent.

Note that even the $G^{\prime}$ is _not_ strongly equivalent to $G$. Indeed strong equivalence would imply that there is a bijection between the underlying sets of symbols, i.e. $|B+V|=|B+2V|$ which is only true for grammars over an empty vocabulary. 

We now study two useful normal forms for CFGs.

**Definition 1.3.20** (Chomsky normal form).: _A CFG $G$ is in Chomsky normal form if it has the following shape:_

$$B^{2}+V\gets G\to B$$

_i.e. all production rules are of the form $w\to a$ or $bc\to a$ for $w\in V$ and $a,b,c\in B$._

**Proposition 1.3.21**.: _Any CFG $G$ is weakly equivalent to a CFG $G^{\prime}$ in Chomsky normal form, such that the reduction from $G$ to $G^{\prime}$ is functorial._

Proof.: Fix any CFG $G$. Without loss of generality, we may assume that $G$ is lexicalised $B^{*}+V\gets G\to B$. In order to construct $G^{\prime}$, we start by setting $G^{\prime}\,=\,\left\{\,f:\vec{a}\to b\in G\,|\,\left|\vec{a}\right|\leq 2 \,\right\}$. Then, for any production rule $f:\vec{a}\to b$ in $G$ such that $k=\left|\vec{a}\right|>2$ we add $k-1$ new rules $f_{i}$ and $k-2$ new symbols $c_{i}$ to $G^{\prime}$ given by $\left\{\,f_{i}:c_{i}a_{i+1}\to c_{i+1}\,\right\}_{i=0}^{k-2}$ where $c_{0}=a_{0}$ and $c_{k-1}=b$. This yields a CFG $G^{\prime}$ in Chomsky normal form. There is a functorial reduction from $G$ to $G^{\prime}$ given by mapping production rules $f$ in $G$ to left-handed trees with $f_{i}$s as nodes, as in the following example:

(1.10)

This implies that $\mathcal{L}(G)\subseteq\mathcal{L}(G^{\prime})$. Now suppose $\vec{u}\in\mathcal{L}(G^{\prime})$, i.e. there is a tree $g:\vec{u}\to s$ in $\mathbf{Op}(G^{\prime})$. By construction, if some $f_{i}:c_{i}a_{i+1}\to c_{i+1}$ appears as an node in $g$ then all the $f_{i}$s must appear as a sequence of nodes in $g$, therefore $g$ is in the image of a tree in $\mathbf{Op}(G)(\vec{u},s)$ and $\vec{u}\in\mathcal{L}(G)$. Therefore $\mathcal{L}(G)=\mathcal{L}(G^{\prime})$. 

Since the reduction from a CFG to its Chomsky normal form is functorial, the translation can be performed in logspace. Indeed, we will show in the next section that the problem of applying a functor between free monoidal categories (of which operad algebras are an example) is in NL. We end with an even weaker example of equivalence between grammars.

**Definition 1.3.22** (Greibach normal form).: _A CFG $G$ is in Greibach normal form if it has the following shape:_

$$V\times B^{*}\gets G\to B$$

_i.e. every production rule is of the form $wb\to a$ for $a\in B$, $b\in B^{*}$ and $w\in V$._

**Proposition 1.3.23**.: _[_10_]_ _Any CFG is weakly equivalent to one in Greibach normal form and the conversion can be performed in poly-time._

We will use these normal forms in the next section, when we discuss functorial reductions between categorial grammars and their relationship with context-free grammars.

#### monoidal.Diagram

We now present monoidal, the key module of DisCoPy which allows to compute with diagrams in free monoidal categories. We have defined free monoidal categories via the concepts of layers and premonoidal diagrams. These have a natural implementation in object-oriented Python, consisting in the definition of classes monoidal.Ty, monoidal.Layer and monoidal.Diagram, for types, layers and diagrams in free premonoidal categories, respectively. Types are tuples of objects, equipped with a .tensor method for the monoidal product.

**Listing 1.3.24**.: Types of free monoidal categories.

 ```

``` fromdiscopyimportcat classTy(cat.Ob): def__init__(self,*objects): self.objects=tuple( xifisinstance(x,cat.Ob)elsecat.Ob(x)forxinobjects) super()__init__(self) deftensor(self,*others): forotherinothers: ifnotisinstance(other,Ty): raiseTypeError() objects=self.objects+[xfortinothersforxint.objects] returnTy(*objects) def__matmul__(self,other): returnself.tensor(other) ```

Layers are instances of cat.Box, initialised by triples $(u,f,v)$ for a pair of types $u,v$ and a box $f$.

**Listing 1.3.25**.: Layer in a free premonoidal category.

``` classLayer(cat.Box): def__init__(self,left,box,right): self.left,self.box,self.right=left,box,right dom,cod=left@box.dom@right,left@box.cod@right super()__init__("Layer",dom,cod) ```

DisCoPy diagrams are initialised by a domain, a codomain, a list of boxes and a list of offsets. It comes with methods Diagram.then, Diagram.tensor and Diagram.id for composing, tensoring and generating identity diagrams. As well as a method for normal_form which allows to check monoidal equality of two premonoidal diagrams.

**Listing 1.3.26**.: Diagram in a free premonoidal category.

``` classDiagram(cat.Arrow): def__init__(self,dom,cod,boxes,offsets,layers=None): iflayersisNone: layers=cat.Id(dom) forbox,offinzip(boxes,offsets): left=layers.cod[:off] iflayerselsedom[:off] right=layers.cod[off+len(box.dom):] iflayerselsedom[off+len(box.dom):] layers=layers>>Layer(left,box,right) layers=layers>>cat.Id(cod) self.boxes,self.layers,self.offsets=boxes,layers,tuple(offsets) super()__init__(dom,cod,layers,_scan=False) defthen(self,*others): iflen(others)>1: returnself.then(others[0]).then(*others[1:]) other, = others  return Diagram(self.dom, other.cod,  self.boxes + other.boxes,  self.offsets + other.offsets,  layers=self.layers >> other.layers)

 def tensor(self, other):  dom, cod = self.dom @ other.dom, self.cod @ other.cod  boxes = self.boxes + other.boxes  offsets = self.offsets + [n + len(self.cod) for n in other.offsets]  layers = cat.Id(dom)  for left, box, right in self.layers:  layers = layers >> Layer(left, box, right @ other.dom)  for left, box, right in other.layers:  layers = layers >> Layer(self.cod @ left, box, right)  return Diagram(dom, cod, boxes, offsets, layers=layers)

 @staticmethod  def id(dom):  return Diagram(dom, dom, [], [], layers=cat.Id(dom))  def interchange(self, i, j, left=False):  ...

 def normal_form(self, normalizer=None, **params):  ...

 def draw(self, **params):  ...

Diagrams always a carry a cat.Arrow called layers, which may be thought of as a witness that the diagram is well-typed. If no layers are provided, the Diagram.__init__method computes the layers and checks that they compose. A cat.AxiomError is returned when the layers do not compose. The Diagram.interchange method allows to change the order of layers in a diagram when they commute, and returns an InterchangerError when they don't. The Diagram.normal_form method implements the algorithm of [4], see the rewriting module of DisCoPy. The Diagram.draw method is implemented in the drawing module and allows to render a diagram via matplotlib [] as well as generating a TikZ [] output for academic papers._

Finally, a Box is initialised by a name together with domain and codomain types.

**Listing 1.3.27**.: Box in a free monoidal category.

``` classBox(cat.Box,Diagram): def__init__(self, name, dom, cod, **params): cat.Box__init__(self, name, dom, cod, **params) layer = Layer(dom[0:0], self, dom[0:0]) layers = cat.Arrow(dom, cod, [layer], _scan=False) Diagram.__init__(self, dom, cod, [self], [0], layers=layers) ```

We check that the axioms for monoidal categories hold up to interchanger.

 

**Listing 1.3.28**.: Axioms of free monoidal categories

x, y, z, w = Ty('x'), Ty('y'), Ty('z'), Ty('w') f0, f1, f2 = Box('f0', x, y), Box('f1', z, w), Box('f2', z, w) d = Id(x) @ f1 >> f0 @ Id(w) assert f0 @ (f1 @ f2) == (f0 @ f1) @ f2 assert f0 @ Diagram.id(Ty()) == f0 == Diagram.id(Ty()) @ f0 assert d == (f0 @ f1).interchange(0, 1) assert f0 @ f1 == d.interchange(0, 1)

Functorial reductions are implemented via the monoidal.Functor class, initialised by a pair of mappings: ob from objects to types and ar from boxes to diagrams. It comes with a __call__ method that scans through a diagram a replaces each box and identity wire with its image under the mapping.

**Listing 1.3.29**.: Monoidal functor.

``` classFunctor(cat.Functor): def__init__(self, ob, ar, cod=(Ty, Diagram)): super()__init__(ob, ar) def__call__(self, diagram): if isinstance(diagram, Ty): returnself.cod[0].tensor(*[self.ob[Ty(x)] forxindiagram]) if isinstance(diagram, Box): returnsuper()__call__(diagram) if isinstance(diagram, Diagram): scan, result = diagram.dom, self.cod[1].id(self(diagram.dom)) forbox, offinzip(diagram.boxes, diagram.offsets): id_1 = self.cod[1].id(self(scan[:off])) id_r = self.cod[1].id(self(scan[off + len(box.dom):])) result = result >> id_1 @ self(box) @ id_r scan = scan[:off] @ box.cod @ scan[off + len(box.dom):] returnresult raise TypeError() ```

_We check that the axioms hold._

``` x,y,z=Ty('x'),Ty('y'),Ty('z') f0,f1,f2=Box('f0', x, y),Box('f1', y, z),Box('f2', z, x) F = Functor(ob={x: y,y: z, z: x}, ar={f0: f1, f1: f2, f2: f0}) assert F(f0 >> f1) == F(f0) >> F(f1) assert F(f0 @ f1) == F(f0) @ F(f1) assert F(f0 @ f1 >> f1 @ f2) == F(f0) @ F(f1) >> F(f1) @ F(f2) ```

Any operad.Tree can be turned into an equivalent monoidal.Diagram. We show how this interface is built by overriding the __call__ method of operad.Algebra.

**Listing 1.3.30**.: Interface with operad.Tree.

``` fromdiscopyimportoperad classAlgebra(operad.Algebra): def__init__(self, ob, ar, cod=Diagram, contravariant=False):self.contravariant = contravariant  super()...init__(self, ob, ar, cod=cod)

 def__call__(self, tree):  if isinstance(tree, operad.Id):  return self.cod.id(self.ob[tree.dom])  if isinstance(tree, operad.Box):  return self.ar[tree]  box = self.ar[tree.root]  if isinstance(box, monoidal.Diagram):  if self.contravariant:  return box << monoidal.Diagram.tensor(  *[self(branch) for branch in tree.branches])  return box >> monoidal.Diagram.tensor(  *[self(branch) for branch in tree.branches])  return box(*[self(branch) for branch in tree.branches])

ob2ty = lambda ob: Ty(ob) node2box = lambda node: Box(node.name, Ty(node.dom), Ty(*node.cod)) t2d = Algebra(ob2ty, node2box, cod=Diagram) node2box_c = lambda node: Box(node.name, Ty(*node.cod), Ty(node.dom)) t2d_c = Algebra(ob2ty, node2box, cod=Diagram, contravariant=True)

def tree2diagram(tree, contravariant=False):  if contravariant:  return t2dc(tree)  return t2d(tree) 

### 1.4 Categorial grammar

The _categorial_ tradition of formal grammars originated in the works of Ajdukiewicz [1] and Bar-Hillel [1], their formalisms are now known as AB grammars [10]. They analyse language syntax by assigning to every word a _type_ generated from basic types using two operations: $\backslash$ (under) and / (over). Strings of types are then parsed according to the following basic reductions:

$$\alpha\left(\alpha\backslash\beta\right)\rightarrow\beta\qquad\left(\alpha/ \beta\right)\beta\rightarrow\alpha$$ (1.11)

The slash notation $\alpha/\beta$, replacing the earlier fraction $\frac{\alpha}{\beta}$, is due to Lambek who unified categorial grammars in an algebraic foundation known as the _Lambek calculus_, first presented in his seminal 1958 paper [11]. With the advent of Chomsky's theories of syntax in the 1960s, categorial grammars were disregarded for almost twenty years [11]. They were revived in the 1980s by several researchers such as Buszowski in Poland, van Benthem and Moortgat in the Netherlands, as witnessed in the 1988 books [12, 13].

One reason for this revival is the proximity between categorial grammars and logic. Indeed, the original rewrite rules (1.11) can be seen as versions of modus ponens in a Gentzen style proof system [11]. Another reason for this revival, is the proximity between categorial grammars, the typed Lambda calculus [10] and the semantic calculi of Curry [14] and Montague [15]. Indeed, one of the best intuitions for categorial grammars comes from interpreting the slash type $\alpha/\beta$ as the type of a _function_ with input of type $\beta$ and output of type $\alpha$, and the reduction rules (1.11) as function application. From this perspective, the syntactic process of recognizing a sentence has the same form as the semantic process of understanding it [13]. We will see the implications of this philosophy in 2.2.

Although he did not mention categories in his original paper [11], Lambek had in mind the connections between linguistics and category theory all along, as mentioned in [11]. Indeed the reductions in (1.11) and those introduced by Lambek, correspond to the morphisms of _free biclosed categories_, which admit a neat description as deductions in a Gentzen style proof system. This leads to a fruitful parallel between algebra, proof theory and categorial grammar, summarized in the following table.

\begin{tabular}{|c|c|c|c|} \hline Categories & Logic & Linguistics & Python \\ \hline Biclosed category & Proof system & Categorial grammar & DisCoPy \\ \hline objects & formulas & types & biclosed.Ty \\ generators & axioms & lexicon & biclosed.Box \\ morphisms & proof trees & reductions & biclosed.Diagram \\ \hline \end{tabular}

We start by defining biclosed categories and a general notion of biclosed grammar. Then the section will unfold as we unwrap the definition, meeting the three most prominent variants of categorial grammars: AB grammars [10], the Lambek calculus [11] and Combinatory Categorial Grammars [13]. We end by giving an implementation of free biclosed categories as a class biclosed.Diagram with methods for currying and uncurrying.



#### Biclosed categories

**Definition 1.4.1** (Biclosed signature).: _A biclosed signature $G$ is a collection of generators $G_{1}$ and basic types $G_{0}$ together with a pair of maps:_

$$T(G_{0})\xleftarrow{\text{\sf dom}}\ G_{1}\xrightarrow{\text{\sf cod}}T(G_{0})$$

_where $T(G_{0})$ is the set of biclosed types, given by the following inductive definition:_

$$T(B)\ni\alpha=a\in B\mid\alpha\otimes\alpha\mid\alpha\backslash\alpha\mid \alpha/\alpha$$ (1.12)

_A morphism of biclosed signatures $\varphi:G\to\Gamma$ is a pair of maps $\varphi_{1}:G_{1}\to\Gamma_{1}$ and $\varphi_{0}:G_{0}\to\Gamma_{0}$ such that the diagram with the signature morphisms commutes. The category of biclosed signatures is denoted $\mathbf{BcSig}$_

**Definition 1.4.2** (Biclosed category).: _A biclosed monoidal category $\mathbf{C}$ is a monoidal category equipped with two bifunctors $-\backslash-:\mathbf{C}^{op}\times\mathbf{C}\to\mathbf{C}$ and $-/-:\mathbf{C}\times\mathbf{C}^{op}\to\mathbf{C}$ such that for any object $a$, $a\otimes-\dashv a\backslash-$ and $-\otimes a\dashv-/a$. Explicitly, we have the following isomorphisms natural in $a,b,c\in\mathbf{C}_{0}$:_

$$\mathbf{C}(a,c/b)\simeq\mathbf{C}(a\otimes b,c)\simeq\mathbf{C}(b,a\backslash c)$$ (1.13)

_These isomorphisms are often called_ currying _(when $\otimes$ is replaced by $\backslash$ or $/$) and_ uncurrying_. With monoidal functors as morphisms, biclosed categories form a category denoted $\mathbf{BcCat}$._

Morphisms in free biclosed category can be described as the valid deductions in a proof system defined as follows. The axioms of monoidal categories may be expressed as the following rules of inference:

$$\xrightarrow{\text{\sf id}}\qquad\qquad\xrightarrow{\text{\sf a}\to b} \xrightarrow{\text{\sf b}\to c}\circ\qquad\xrightarrow{\text{\sf a}\to b} \xrightarrow{\text{\sf c}\to d}\otimes$$ (1.14)

Additionally, the defining adjunctions of biclosed categories may be expressed as follows:

$$a\otimes b\to c\quad\text{iff}\quad a\to c/b\quad\text{iff}\quad b\to a \backslash c$$ (1.15)

Given a biclosed signature $G$, the free biclosed category $\mathbf{Bc}(G)$ contains all the morphisms that can be derived using the inference rules 1.15 and 1.14 from the signature seen as a set of axioms for the deductive system. $\mathbf{Bc}$ is part of an adjunction relating biclosed signatures and biclosed categories:

$$\mathbf{BcSig}\xleftarrow{\text{\sf BC}}_{U}\mathbf{BcCat}$$

We can now define a general notion of biclosed grammar, the equivalent of monoidal grammars in a biclosed setting.



**Definition 1.4.3**.: _A biclosed grammar $G$ is a biclosed signature of the following shape:_

$$T(B+V)\xleftarrow{\sf don}G\xrightarrow{\sf cod}T(B+V)$$

_where $V$ is a vocabulary and $B$ is a set of basic types. The language generated by a G is given by:_

$$\mathcal{L}(G)=\{\,u\in V^{*}\,|\,\exists g:u\to s\in{\bf BC}(G)\,\}$$

_where ${\bf BC}(G)$ is the free biclosed category generated by $G$. We say that $G$ is lexicalised when it has the following shape:_

$$V\xleftarrow{\sf don}G\xrightarrow{\sf cod}T(B)$$

As we will see, AB grammars, Lambek grammars and Combinatory Categorial grammars all reduce functorially to biclosed grammars. However, biclosed grammars can have an infinite number of rules of inference, obtained by iterating over the isomorphism (1.15). Interestingly, these rules have been discovered progressively throughout the history of categorial grammars.

#### Ajdiuciewicz

We discuss the classical categorial grammars of Ajdiuciewicz and Bar-Hillel, known as AB grammars [10]. The types of the original AB grammars are given by the following inductive definition:

$$T_{AB}(B)\ni\alpha=a\in B\mid\alpha\backslash\alpha\mid\alpha/\alpha\;.$$

Given a vocabulary $V$, the _lexicon_ is usually defined as a relation $\Delta\subseteq V\times T_{AB}(B)$ assigning a set of candidate types $\Delta(w)$ to each word $w\in V$. Given an utterance $u=w_{0}\ldots w_{n}\in V^{*}$, one can prove that $u$ is a grammatical sentence by producing a reduction $t_{0}\ldots t_{n}\to s$ for some $t_{i}\in\Delta(w_{i})$, generated by the basic reductions in (1.11).

**Definition 1.4.4** (AB grammar).: _An AB grammar is a tuple $G=(V,B,\Delta,s)$ where $V$ is a vocabulary, $B$ is a finite set of basic types, and $\Delta\subseteq V\times T_{AB}(B)$ is a finite relation, called the lexicon. The rules of AB grammars are given by the following monoidal signature:_

$$R_{AB}=\left\{\begin{array}{ccc}a&a\backslash b&b/a&a\\ \cline{2-3}\cline{3-4}\cline{3-4}\cline{3-4}\cline{3-4}\cline{3-4}\cline{3-4} \cline{3-4}\cline

**Remark 1.4.5**.: _Sometimes, categorial grammarians use a different notation where $a\backslash b$ is used in place of $b\backslash a$. We find the notation used here more intuitive: we write $a\otimes a\backslash b\to b$ instead of $a\otimes b\backslash a\to b$. Ours is in fact the notation used in the original paper by Lambek [18]._

**Example 1.4.6** (Application).: _As an example take the vocabulary $V=\{\,\text{Caesar},\,\text{crossed},\,\text{the},\,\text{Rubicon}\}$ and basic types $B=\{s,n,d\}$ for sentence, noun and determinant types. We define the lexicon $\Delta$ by:_

$$\Delta(\text{Caesar})=\{\,n\,\}\quad\Delta(\text{crossed})=\{\,n\backslash(s /n)\,\}\quad\Delta(\text{the})=\{\,d\,\}\quad\Delta(\text{Rubicon})=\{\,d \backslash n\,\}$$

_Then the sentence "John wrote a dictionnary" is grammatical as witnessed by the following reduction:_

**Proposition 1.4.7**.: _AB grammars reduce functorially to biclosed grammars._

Proof.: It is sufficient to show that the rules $R_{AB}$ can be derived from the axioms of biclosed categories, i.e. that they are morphisms in any free biclosed category. Let $a,b$ be objects in a free biclosed category. We derive the forward application rule as follows.

$$\frac{\overline{a/b\to a/b}}{a/b\otimes b\to a}\,1.15$$

Similarly, one may derive backward application $\texttt{app}^{<}:b\otimes b\backslash a\to b$. 

AB grammars are weakly equivalent to context-free grammars [10] as shown by the following pair of propositions.

**Proposition 1.4.8**.: _For any AB grammar there is a functorially equivalent context-free grammar in Chomsky normal form._

Proof.: The only difficulty in this proof comes from the fact that $R_{AB}$ is an infinite set, whereas context-free grammars must be defined over a finite set of symbols and production rules. Given an AB grammar $G=(V,B,\Delta)$, define $X=\{x\in T_{AB}(B)|\exists(w,t)\in\Delta\text{such that}x\subseteq t\}$ where we write $x\subseteq t$ to say that $x$ is a sub-type of $t$. Note that $X$ is finite. Now let $P=\{r\in R_{AB}|\texttt{dom}(r)\in X\}$. Note that also $P$ is a finite set. Then $X\gets P+\Delta\rightarrow(X+V)^{*}$ forms a lexicalised context-free grammar where each production rule has at most arity 2, i.e. $P+\Delta$ is in Chomsky normal form. There is a functorial reduction $\mathbf{MC}(P+\Delta)\rightarrow\mathbf{MC}(R_{AB}+\Delta)$ induced by the injection $P\hookrightarrow R_{AB}$, also there is a functorial reduction $\mathbf{MC}(R_{AB}+\Delta)\rightarrow\mathbf{MC}(P+\Delta)$ which sends all the types in $T_{AB}(B)\backslash X$ to the unit and acts as the identity on the rest. Therefore $G$ is functorially equivalent to $P+\Delta$

**Proposition 1.4.9**.: _Any context-free grammar in Greibach normal form reduces functorially to an AB grammar._

Proof.: Recall that a CFG is in Greibach normal form when it has the shape:

$$B\gets G\to V\times B^{*}$$

We can rewrite this as a signature of the following shape:

$$V\gets G\to B\times B^{*}$$

This yields a relation $G\subseteq V\times(B\times B^{*})$. We define the lexicon $\Delta\subseteq V\times T(B)$ by $\Delta(w)=G(w)_{0}/\mathtt{inv}(G(w)_{1})$ where $\mathtt{inv}$ inverts the order of the basic types. Then there is a functorial reduction $\mathbf{MC}(G)\to\mathbf{MC}(\Delta+R_{AB})$ given on any production rule $wa_{0}\dots a_{k}\to b$ in $G$ by:

$$\begin{array}{c}\includegraphics[width=56.905512pt]{figs/m1.eps}\end{array} \quad\mapsto\quad\begin{array}{c}\includegraphics[width=56.905512pt]{figs/m1.



**Example 1.4.11** (Composition).: _We adapt an example from [12]. Consider the following lexicon:_

$$\Delta(\mathit{I})=\Delta(\mathit{Grandma})=\{\,n\,\}\quad\Delta(\mathit{the})=\{ \,d\,\}\quad\Delta(\mathit{parmigiana})=\{\,d\backslash n\,\}$$

$$\Delta(\mathit{will})=\Delta(\mathit{may})=\{\,(n\backslash s)/(n\backslash s) \,\}\quad\Delta(\mathit{eat})=\Delta(\mathit{cook})=\{\,n\backslash s/n\,\}$$

_The following is a grammatical sentence, parsed using the composition rule:_

_And the following sentence requires the use of type-raising:_

_where $x=s/n$ and we have omitted the composition of modalities (will, may) with their verbs (cook, eat)._

**Proposition 1.4.12**.: _Lambek grammars reduce functorially to biclosed grammars._

Proof.: It is sufficient to show that the rules of Lambek grammars $R_{\mathit{LG}}$ can be derived from the axioms of biclosed categories. We already derived forward and backward application in 1.4.7. The following proof tree shows that the forward composition rule follows from the axioms of biclosed categories.

$$\begin{array}{c}\cline{2-3}\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omitA similar argument derives the backward composition rule $\texttt{comp}^{<}:a/b\otimes a\backslash c\to c/b$. Forward type-raising is derived as follows.

$$\begin{array}{l}\hline\hline a\backslash b\to a\backslash b\quad\texttt{id}\\ \hline a\otimes a\backslash b\to b\\ \hline a\to b/(a\backslash b)\quad\texttt{1.15}\end{array}$$

And a similar argument derives backward type-raising $\texttt{tyr}^{<}:a\to(b/a)\backslash b$. 

It was conjectured by Chomsky that any Lambek grammar is weakly equivalent to a context-free grammar, i.e. that the language recognised by Lambek calculi is context-free. This conjecture was proved in 1993 by Pentus [11], calling for a more expressive version of categorial grammars.

#### Combinatory

In the 1980s, researchers interested in the syntax of natural language started recognizing that certain grammatical sentences naturally involve crossed dependencies between words, a phenomenon that cannot be captured by context-free grammars. These are somewhat rare in English, but they abound in Dutch for instance [10]. An English example is the sentence "I explained to John maths" which is often allowed to mean "I explained maths to John". Modeling cross-serial dependencies was one of the main motivations for the development the Tree-adjoining grammars of Joshi [12] and the Combinatory Categorial grammars (CCGs) of Steedman [13, 14]. These were later shown to be weakly equivalent to linear indexed grammars [15], making them all "mildly-context sensitive" according to the definition of Joshi [12].

CCGs extend the earlier categorial grammars by adding a _crossed composition_ rule which allows for controlled crossed dependencies within a sentence, and is given by the following pair of reductions:

$$\texttt{xcomp}^{>}:a/b\otimes c\backslash b\to c\backslash a\qquad \texttt{xcomp}^{<}:a/b\otimes a\backslash c\to c/b$$

We start by defining CCGs as monoidal grammars, and then discuss how they relate to biclosed categories.

**Definition 1.4.13** (Combinatory Categorial Grammar).: _A CCG is a tuple $G=(V,B,\Delta,s)$ where $V$ is a vocabulary, $B$ is a finite set of basic types and $\Delta\subseteq V\times T(B)$ is a lexicon. The rules of CCGs are given by the following monoidal signature:_

$$R_{CCG}=R_{LG}+\left\{\begin{array}{@{}c@{\quad\quad}c@{}}a/b\quad c \backslash b\quad\quad&a/b\quad a\backslash c\\ \quad\quad&\quad&\quad&\quad&\quad&\quad&\quad\\ \quad\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad\\ \quad\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad\\ \quad\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad\\ \quad\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad\\ \quad\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad \\ \quad\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad&\quad& \quad\end{array}\right\}\quad.$$

_Then the language generated by $G$ is given by:_

$$\mathcal{L}(G)=\{\,u\in V^{*}\,:\,\exists g\in\mathbf{MC}(\Delta+R_{CCG})(u,s )\,\}$$ 

**Example 1.4.14** (Crossed composition).: _Taking the grammar from Example and adding two lexical entries we may derive the following grammatical sentences:_

_Note that the first one can be parsed already in an AB grammar, whereas the second requires the crossed composition rule._

It was first shown by Moortgat [14] that the crossed composition rule cannot be derived from the axioms of the Lambek calculus. In our context, this implies that we cannot derive xcomp from the axioms of biclosed categories. Of course, CCGs may be seen as biclosed grammars by adding the crossed composition rules $R_{CCG}-R_{LG}$ as generators in the signature. However, it is interesting to note that these rules can be derived from _closed categories_, the _symmetric_ version of biclosed categories:.

**Definition 1.4.15** (Symmetric monoidal category).: _A symmetric monoidal category $\mathbf{C}$ is a monoidal category equipped with a natural transformation $\mathtt{swap}:a\otimes b\to b\otimes a$ satisfying:_

_for any $a,b,c\in\mathbf{C}_{0}$ and $f:a\to b\in\mathbf{C}_{1}$._

**Definition 1.4.16** (Closed category).: _A closed category is a symmetric biclosed category._

**Proposition 1.4.17**.: _The crossed composition rule follows from the axioms of closed categories._

Proof.: Let $a,b,c$ be objects in the free closed category with no generators. The following proof tree shows that the backward crossed composition rule follows from the axioms of closed categories.

$$\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline \begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\hline\begin{array}{c}\hline\hline\begin{array}{c}\hline\hline\begin{array}{c} \hline\begin class Ty(monoidal.Ty):  def __init__(self, *objects, left=None, right=None):  self.left, self.right = left, right  super()__init__(*objects)

 def __lshift__(self, other):  return Over(self, other)

 def __rshift__(self, other):  return Under(self, other)

 def __matmul__(self, other):  return Ty(*(self @ other))

 @staticmethod  def upgrade(old):  if len(old) == 1 and isinstance(old[0], (Over, Under)):  return old[0]  return Ty(*old.objects)

class Over(Ty):  def __init__(self, left=None, right=None):  Ty.__init__(self, self)

 def __repr__(self):  return "Over({}, {})".format(repr(self.left),repr(self.right))

 def __str__(self):  return "({} << {})".format(self.left, self.right)

 def __eq__(self, other):  if not isinstance(other, Over):  return False  return self.left == other.left and self.right == other.right

class Under(Ty):  def __init__(self, left=None, right=None):  Ty.__init__(self, self)

 def __repr__(self):  return "Under({}, {})".format(repr(self.left),repr(self.right))

 def __str__(self):  return "({} >> {})".format(self.left, self.right)

 def __eq__(self, other):  if not isinstance(other, Under):  return False  return self.left == other.left and self.right == other.right

_The_ Ty.upgrade _method allows for compatibility between the tensor methods__matmul__ of biclosed _and_ monoidal _types. The upgrading mechanism is further desribed in the documentation of monoidal.

We illustrate the syntax of biclosed types.

``` x=Ty('x') assertx>>x<<x==Over(Under(Ty('x'),Ty('x')),Ty('x')) assertx>>(x<<x)==Under(Ty('x'),Over(Ty('x'),Ty('x'))) x0,x1,y0,y1,m=Ty('x0'),Ty('x1'),Ty('y0'),Ty('y1'),Ty('m') lens=(x0>>m@y0)@(m@x1>>y1) assertlens==Ty(Under(Ty('x0'),Ty('m','y0')),Under(Ty('m','x1'),Ty('y1'))) ```

A biclosed.Diagram is a monoidal.Diagram with domain and codomain biclosed.Tys, together with a pair of static methods curry() and uncurry() implementing the defining isomorphism of biclosed categories (1.15). In fact, we can store the information of how a biclosed diagram is constructed by using two special subclasses of Box, which record every application of the currying morphisms. Thus a diagram in a biclosed category is a tree built from generating boxes using id, then, tensor, Curry and UnCurry.

**Listing 1.4.19**.: Diagrams in free biclosed categories

``` fromdiscopyimportmonoidal @monoidal.Diagram.subclass classDiagram(monoidal.Diagram): defcurry(self,n_wires=1,left=False): returnCurry(self,n_wires,left) defuncurry(self): returnUnCurry(self) classId(monoidal.Id,Diagram): classBox(monoidal.Box,Diagram): classCurry(Box): def__init__(self,diagram,n_wires=1,left=False): name="Curry({})".format(diagram) ifleft: dom=diagram.dom[n_wires:] cod=diagram.dom[:n_wires]>>diagram.cod else: dom=diagram.dom[:-n_wires] cod=diagram.cod<<diagram.dom[-n_wiresorlen(diagram.dom):] self.diagram,self.n_wires,self.left=diagram,n_wires,left super()__init__(name,dom,cod) classUnCurry(Box): def__init__(self,diagram): name="UnCurry({})".format(diagram) self.diagram = diagram  if isinstance(diagram.cod, Over):  dom = diagram.dom @ diagram.cod.right  cod = diagram.dom.left  super().__init__(name, dom, cod)  elif isinstance(diagram.cod, Under):  dom = diagram.dom.left @ diagram.dom  cod = diagram.dom.right  super().__init__(name, dom, cod)  else:  super().__init__(name, diagram.dom, diagram.cod) ```

_We give a simple implementation of free biclosed categories which does not impose the axioms of free biclosed categories,_UnCurry(Curry(f)) == f _and naturality. IT can be implemented on syntax by adding if statement in the inits, and upgrading_Curry _and_UnCurry _to subclasses of_ biclosed.Diagram..

Finally, a biclosed.Functor is a monoidal.Functor whose call method has a predefined mapping for all structural boxes in biclosed. It thus allows to map any biclosed.Diagram into a codomain class cod equipped with curry and uncurry methods.

**Listing 4.20**.: Functors from free biclosed categories

``` classFunctor(monoidal.Functor):  def__init__(self, ob, ar, cod=(Ty, Diagram)):  self.cod = cod  super().__init__(ob, ar, ob_factory=cod[0], ar_factory=cod[1]) def__call__(self, diagram):  if isinstance(diagram, Over):  return self(diagram.left) << self(diagram.right)  if isinstance(diagram, Under):  return self(diagram.left) >> self(diagram.right)  if isinstance(diagram, Ty) and len(diagram) > 1:  return self.cod[0].tensor(*[  self(diagram[i: i + 1]) for i in range(len(diagram))])  if isinstance(diagram, Id):  return self.cod[1].id(self(diagram.dom)) if isinstance(diagram, Curry):  n_wires = len(self(getattr(  diagram.cod, 'left' if diagram.left else 'right')))  return self.cod[1].curry(  self(diagram.diagram), n_wires, diagram.left) if isinstance(diagram, UnCurry):  return self.cod[1].uncurry(self(diagram.diagram)) return super().__call__(diagram) ```

We recover the rules of categorial grammars (in historical order) by constructing them from identities in the free biclosed category with no generators.

**Listing 4.21**.: Categorical grammars and the free biclosed category Adjiuicewicz FA = lambda a, b: UnCurry(Id(a >> b)) assert FA(x, y).dom == x @ (x >> y) and FA(x, y).cod == y BA = lambda a, b: UnCurry(Id(b << a)) assert BA(x, y).dom == (y << x) @ x and BA(x, y).cod == y

Lambek proofFC = FA(x, y) @ Id(y >> z) >> FA(y, z) FC = Curry(proofFC, left=True) assert FC.dom == (x >> y) @ (y >> z) and FC.cod == (x >> z) BC = Curry(Id(x << y) @ BA(z, y) >> BA(y, x)) assert BC.dom == (x << y) @ (y << z) and BC.cod == (x << z) YYR = Curry(UnCurry(Id(x >> y))) assert YR.dom == x and TYR.cod == (y << (x >> y))

Steedman Swap = lambda a, b: Box('Swap', a @ b, b @ a) proofBX = Id(x << y) @ (Swap(z >> y, z) >> FA(z, y)) >> BA(y, x) BX = Curry(proofBX) assert BX.dom == (x << y) @ (z >> y) and BX.cod == (x << z) proofFK = (Swap(x, y << x) >> BA(x, y)) @ Id(y >> z) >> FA(y, z) FX = Curry(proofFX, left=True) assert FX.dom == (y << x) @ (y >> z) and FX.cod == (x >> z)

The assertions above are alternative proofs of Propositions 1.4.7, 1.4.12 and 1.4.17. We draw the proofs for forward composition (proofFC) and backwards crossed composition (proofBX).

[FIGURE:Ch 

### 1.5 Pregroups and dependencies

In his 1897 paper "The logic of relatives" [11], Peirce makes an analogy between the sentence "John gives John to John" and the molecule of ammonia.

The intuition that words within a sentence are connected by "bonds", as atoms in a molecule, is the basis of Peirce's diagrammatic approach to logical reasoning, and of his analysis of the concept of _valency_ in grammar [1]. This intuition resurfaced in the work of Lucien Tesniere [10] who analysed the valency of a large number of lexical items, in an approach to syntax that became known as _dependency grammar_[1, 2]. These bear a striking resemblance to Lambek's pregroup grammars [11] and its developments in the DisCoCat framework of Coecke, Sadrzadeh et al. [12, 13, 14].

In this section, we formalise both Pregroup Grammar (PG) and Dependency Grammar (DG) in the language of _free rigid categories_. Once casted in this algebraic framework, the similarities between PG and DG become apparent. We show that dependency grammars are structurally equivalent to both pregroup grammar and context-free grammar, i.e. their derivations are tree-shaped rigid diagrams. We end by describing the implementation of the class rigid.Diagram and we interface it with SpaCy's dependency parser [15].

#### Pregroups and rigid categories

Pregroup grammars were introduced by Lambek in 1999 [11]. Arising from a non-commutative fragment of Girard's linear logic [10] they refine and simplify the earlier Lambek calculus discussed in Section 1.4.3. As shown by Buszowski, pregroup grammars are weakly equivalent to context-free grammars [1]. However, the syntactic structures generated by pregroup grammars differ from those of a CFG. Instead of trees, pregroups parse sentences by assigning to them a nested pattern of _cups_ or "links" as in the following example.

In the strict sense of the word, a pregroup is a preordered monoid where each object has a left and a right adjoint [11]. We formalise pregroup grammars in terms of _rigid categories_ which categorify the notion of pregroup by upgrading the preorder to a category. Going from inequalities in a preordered monoid to arrows in a monoidal category allows both to reason about syntactic ambiguity -- as discussed by Lambekand Preller [10] -- as well as to define pregroup semantics as a monoidal functor, an observation which lead to the development of the compositional distributional models of Coecke et al. [11] and which will form the basis of the next chapter on semantics.

Given a set of basic types $B$, the set of pregroup types $P(B)$ is defined as follows.

$$P(B)\ni t\,::=\,b\in B\,|\,t^{r}\,|\,t^{l}\,|\,t\otimes t.$$

we can use it to define the notion of a rigid signature.

**Definition 1.5.1** (Rigid signature).: _A rigid signature is a graph $\Sigma=\Sigma_{1}\rightrightarrows P(\Sigma_{0})$. A morphism of rigid signatures $\Sigma\to\Gamma$ is a pair of maps $\Sigma_{1}\to\Gamma_{1}$ and $\Sigma_{0}\to\Gamma_{0}$ satisfying the obvious commuting diagram. Rigid signatures and their morphisms form a category denoted $\mathbf{RgSi}$._

**Definition 1.5.2** (Rigid category).: _A rigid category $\mathbf{C}$ is a monoidal category such that each object $a$ has a left adjoint $a^{l}$ and a right adjoint $a^{r}$. In other words there are morphisms $a^{l}\otimes a\to 1$, $1\to a\otimes a^{l}$, $a\otimes a^{r}\to 1$ and $1\to a^{r}\otimes a^{l}$, denoted as cups and caps and satisfying the snake equations:_

(1.18)

_The category of rigid categories and monoidal functors is denoted $\mathbf{RigidCat}$._

**Proposition 1.5.3**.: _Rigid categories are biclosed, with $a\backslash b=a^{r}\otimes b$ and $b/a=b\otimes a^{l}$._

Given a rigid signature $\Sigma$ we can generate the _free rigid category_

$$\mathbf{RC}(\Sigma)=\mathbf{MC}(\Sigma+\{\,cupps,caps\,\})/\sim_{snake}$$

where $\sim_{snake}$ is the equivalence relation on diagrams induced by the snake equations (1.18). Rigid categories are called _compact 2-categories_ with one object by Lambek and Preller [10], who showed that $\mathbf{RC}$ defines an adjunction between rigid signatures and rigid categories.

$$\mathbf{RgSi}\underset{U}{\rightleftarrows\mathbf{RC}}\mathbf{RgCat}$$

We start by defining a general notion of _rigid grammar_, a subclass of biclosed grammars.

**Definition 1.5.4**.: _A rigid grammar $G$ is a rigid signature of the following shape:_

$$P(B+V)\underset{U}{\rightleftarrows\mathbf{don}}\,G\overset{\mathsf{cod}}{ \longrightarrow}P(B+V)$$

_where $V$ is a vocabulary and $B$ is a set of basic types. The language generated by $G$ is given by:_

$$\mathcal{L}(G)=\{\,u\in V^{*}\,|\,\exists g:u\to s\in\mathbf{RC}(G)\,\}$$

_where $\mathbf{RC}(G)$ is the free rigid category generated by $G$._ A pregroup grammar is a lexicalised rigid grammar defined as follows.

**Definition 1.5.5** (Pregroup grammar).: _A pregroup grammar is a tuple $G=(V,B,\Delta,I,s)$ where $V$ is a vocabulary, $B$ is a finite set of basic types, $G\subseteq V\times P(B)$ is a lexicon assigning a set of possible pregroup types to each word, and $I\subseteq B\times B$ is a finite set of induced steps. The language generated by $G$ is given by:_

$$\mathcal{L}(G)=\{\,u\in V^{*}\,:\,\exists g\in\mathbf{RC}(G)(u,s)\,\}$$

_where $\mathbf{RC}(G):=\mathbf{RC}(\Delta+I)$._

**Example 1.5.6**.: _Fix the basic types $B=\{\,s,n,n_{1},d,d_{1}\,\}$ for sentence, noun, plural noun, determinant and plural determinant and consider the following pregroup lexicon:_

$$\Delta(\text{pair})=\{\,d^{r}\,n\,\}\,,\;\Delta(\text{lives})=\{\,d^{r}_{1}\,n _{1}\,\}\,,\;\Delta(\text{lovers})=\{\,n_{1}\,\}\,,\;\Delta(\text{starcross})= \{\,n\,n^{l}\,\}\,,$$

_and one induced step $I=\{\,n_{1}\to n\,\}$. Then the following is a grammatical sentence:_

_where we omitted the types for readability, and we denoted the induced step using a black node._

The tight connections between categorial grammars and pregroups were discussed in [10], they are evermore apparent from a categorical perspective: since rigid categories are biclosed, there is a canonical way of mapping the reductions of a categorial grammar to pregroups.

**Proposition 1.5.7**.: _For any Lambek grammar $G$ there is a pregroup grammar $G^{\prime}$ with a functorial reduction $\mathbf{MC}(G)\to\mathbf{RC}(G^{\prime})$._

Proof.: The translation works as follows:

$$\begin{array}{c}\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par \par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par\par 

**Example 1.5.8**.: _Consider the categorial parsing of the sentence "Grandma will cook the parmigiana" from Example 1.4.14. The categorial type of "will" is given by $(n\backslash s)/(n\backslash s)$ which translates to the pregroup type $(n^{r}s)(n^{r}s)^{l}=n^{r}s\,s^{l}n$, the transitive verb type $(n\backslash s)/n$ for "cook" translates to $n^{r}\,s\,n^{l}$, and similarly for the other types. Translating the categorial reduction according to the mapping above, we obtain the following pregroup reduction:_

One advantage of pregroups over categorial grammars is that they can be parsed more efficiently. This is a consequence of the following lemma, proved by Lambek in [11].

**Proposition 1.5.9** (Switching lemma).: _For any pregroup grammar $G$ and any reduction $t\to s$ in $\mathbf{RC}(G)$, there is a type $t^{\prime}$ such that $t\to s=t\to t^{\prime}\to s$ and $t\to t^{\prime}$ doesn't use contractions (cups), $t^{\prime}\to s$ doesn't use expansions (caps)._

**Remark 1.5.10**.: _Note that the equivalent lemma for categorial grammars would state that all instances of the type-raising rule can appear after all instances of the composition and application rules. This is however not the case._

A direct corollary of this lemma, is that any sentence $u\in V^{*}$ may be parsed using only contractions (cups). This drastically reduces the search space for a reduction, with the consequence that pregroup grammars can be parsed efficiently.

**Proposition 1.5.11**.: _Pregroup grammars can be parsed in polynomial time [18, 19] and in linear-time in linguistically justified restricted cases [17]._

As discussed in Section 1.4.4, linguists have observed that certain grammatical sentences naturally involve crossed dependencies between words [25]. Although the planarity assumption is justified in several cases of interest [10], grammars with crossed dependencies allow for more flexibility when parsing natural languages. In order to model these phenomena with pregroup grammars, we need to step out of (planar) rigid categories and allow for (restricted) permutations. These can be represented in the symmetric version of rigid categories, known as _compact closed_ categories.

**Definition 1.5.12** (Compact-closed).: _A compact-closed category is a rigid category (1.18) that is also symmetric (1.16)._

Given a pregroup grammar $G$, we can generate the free compact-closed category defined by:

$$\mathbf{CC}(G)=\mathbf{RC}(G+\mathtt{swap})/\sim_{\mathtt{sym}}$$where $\sim_{\texttt{aym}}$ is the congruence induced by the axioms for the symmetry (1.16). Notice that in a compact-closed category $a^{r}\simeq a^{l}$ for any object $a$, see e.g. [11]. Pregroup reductions in the free rigid category $\mathbf{RC}(G)$ can of course be mapped in $\mathbf{CC}(G)$ via the canonical rigid functor which forgets the ${}^{r}$ and ${}^{l}$ adjoint structure.

We cannot use free compact-closed categories directly to parse sentences. If we only ask for a morphism $g:u\to s$ in $\mathbf{CC}(G)$ in order to show that the string $u$ is grammatical, then any permutation of the words in $u$ would also count as grammatical, and we would lose any notion of word order. In practice, the use of the swap must be restricted to only special cases. These were discussed in 1.4, where we saw that the crossed composition rule of combinatory grammars is suitable for modeling these restricted cases.

In recent work [13], Yeung and Kartsaklis introduced a translation from CCG grammars to pregroup grammars which allows to build a diagram in the free compact-closed category over a pregroup grammar from any derivation of a CCG. This is useful in practical applications since it allows to turn the output of state-of-the-art CCG parsers such as [10] into compact-closed diagrams. The translation is captured by the following proposition.

**Proposition 1.5.13**.: _For any combinatory grammar $G$ there is a pregroup grammar $G^{\prime}$ with a canonical functorial reduction $G\to\mathbf{CC}(G^{\prime})$._

Proof.: The translation is the same as 1.5.7, together with the following mapping for the crossed composition rules:

(1.19)

Representing the crossed composition rule in compact-closed categories, allows to reason diagrammatically about equivalent syntactic structures.

**Example 1.5.14**.: _As an example consider the pregroup grammar $G$ with basic types $B=\{\,n,s\,\}$ and lexicon given by:_

$$\Delta(\text{cooked})=\{\,n^{r}sn^{l}\,\}\quad\Delta(\text{me})=\Delta(\text{ Grandma})=\Delta(\text{parmigiana})=\{\,n\,\}\quad\Delta(\text{for})=\{\,s^{l}sn^{l}\,\}$$

_Then using the grammar from Example 1.4.14, we can map the two CCG parses to the following compact-closed diagrams in $\mathbf{CC}(G)$, even though the second is not grammatical in a planar pregroup grammar._

_Grandma cookedparmigiana for me_

_Grandma cooked for meparmigiana_

_If we interpret the wires for words as the unit of the tensor, then these two diagrams are equal in $\mathbf{CC}(G)$ but not when seen in a biclosed category._ 

#### Dependency grammars are pregroups

Dependency grammars arose from the work of Lucien Tesniere in the 1950s [111]. It was made formal in the 1960s by Hays [12] and Gaifman [13], who showed that they have the same expressive power as context-free grammars. Dependency grammars are very popular in NLP, supported by large-scale parsing tools such as those provided by Spacy [10]. We take the formalisation of Gaifman [13] as a starting point and show how the dependency relation may be seen as a diagram in a free rigid category.

Let us fix a vocabulary $V$ and a set of symbols $B$, called categories in [13], with $s\in B$ the sentence symbol.

**Definition 1.5.15** (Dependency grammar [13]).: _A dependency grammar $G$ consists in a set of rules $G\subseteq(B+V)\times B^{*}$ of the following shapes:_

1. $(x,y_{1}\ldots y_{l}\star y_{l+1}\ldots y_{n})$ _where_ $x,y_{i}\in B$_, indicating that the symbol_ $x$ _may depend on the symbols_ $y_{1}\ldots y_{l}$ _on the left and on the symbols_ $y_{l+1}\ldots y_{n}$ _on the right._
2. $(w,x)$ _for_ $w\in V$ _and_ $x\in B$_, indicating that the word_ $w$ _may have type_ $x$_._
3. $(x,s)$ _indicating that the symbol_ $x$ _may govern a sentence._

Following Gaifman [13], we define the language $\mathcal{L}(G)$ generated by a dependency grammar $G$ to be the set of strings $u=w_{1}w_{2}\ldots w_{n}\in V^{*}$ such that there are symbols $x_{1},x_{2}\ldots x_{n}\in B$ and a binary _dependency relation_$d\subseteq X\times X$ where $X=\{\,x_{1},\ldots,x_{n}\,\}$ satisfying the following conditions:

1. $(w_{i},x_{i})\in G$ for all $i\leq n$,
2. $(x_{i},x_{i})\notin RTC(d)$ where $RTC(d)$ is the reflexive transitive closure of $d$, i.e. the dependency relation is _acyclic_,
3. if $(x_{i},x_{j})\in d$ an $(x_{i},x_{k})\in d$ then $x_{j}=x_{k}$, i.e. every symbol depends on at most one head, i.e. the dependency relation is single-headed or _monogamous_,
4. if $i\leq j\leq k$ and $(x_{i},x_{k})\in RTC(d)$ then $(x_{i},x_{j})\in RTC(d)$, i.e. the dependency relation is _planar_,
5. there is exactly one $x_{h}$ such that $\forall j\,(x_{h},x_{j})\notin d$ and $(x_{h},s)\in G$, i.e. the relation is _connected_ and _rooted_ ($x_{h}$ is called the root and we say that $x_{h}$ governs the sentence).
6. for every $x_{i}$, let $y_{1},\ldots,y_{l}\in X$ be the (ordered list of) symbols which depend on $x_{i}$ from the left and $y_{l+1},\ldots,y_{n}\in X$ be the (ordered list of) symbols which depend on $x_{i}$ from the right, then $(x,y_{1}\ldots y_{l}\star y_{l+1}\ldots y_{n})\in G$, i.e. the dependency structure is allowed by the rules of $G$.



**Example 1.5.16**.: _Consider the dependency grammar with $V=\{\,\text{Moses},\,\text{crossed},\,\text{the},\,\text{Red},\,\text{Sea}\,\}$, $B=\{\,d,n,a,s,v\,\}$ and rules of type I:_

$$(v,n\star n),(a,\star n),(d,\star),(n,\star),(n,ad\star)\,,$$

_of type II:_

$$(\text{Moses},n),(\text{crossed},v),(\text{the},d),(\text{Red},a),(\text{Sea},n)$$

_and a single rule of type III $(v,s)$. Then the sentence "She tied a plastic bag" is grammatical as witnessed by the following dependency relation:_

$$\begin{array}{c}\text{Moses crossed}\quad\text{the}\quad\text{Red}\quad \text{Sea}\\ \end{array}$$

This combinatorial definition of a dependency relation has an algebraic counterpart as a morphism in a free rigid category. Given a dependency grammar $G$, let $\Delta(G)\subseteq V\times P(B)$ be the pregroup lexicon defined by:

$$(w,y_{1}^{r}\ldots y_{l}^{r}\,x\,y_{l+1}^{l}\ldots y_{n}^{l})\in\Delta(G)\iff (w,x)\in G\wedge(x,y_{1}\ldots y_{l}\,\star\,y_{l+1}\ldots y_{n})\in G$$ (1.20)

also, let $I(G)$ be rules in $G$ of the form $(x,s)$ where $x\in B$ and $s$ is the sentence symbol.

**Proposition 1.5.17**.: _For any dependency grammar $G$, if a string of words is grammatical $u\in\mathcal{L}(G)$ then there exists a morphism $u\to s$ in $\mathbf{RC}(\Delta(G)+I(G))$._

Proof.: Fix a dependency grammar $G$, and suppose $w_{1}\ldots w_{n}\in\mathcal{L}(G)$ then there is a list of symbols $X=\{x_{1},x_{2}\ldots x_{n}\}$ with $x_{i}\in B$ and a dependency relation $d\subseteq X\times X$ such that the conditions $(1),\ldots,(6)$ given above are satisfied. We need to show that $d$ defines a diagram $w_{1}\ldots w_{n}\to s$ in $\mathbf{RC}(\Delta(G)+I(G))$. Starting from the type $w_{1}w_{2}\ldots w_{n}$, conditions $(1)$ and $(6)$ of the dependency relation ensure that there is an assignment of a single lexical entry in $\Delta(G)$ to each $w_{i}$. Applying these lexical entries we get a morphism $w_{1}w_{2}\ldots w_{n}\to T$ in $\mathbf{RC}(\Delta(G))$ where:

$$T=\otimes_{i=1}^{n}(y_{i,1}^{r}\ldots y_{i,l_{i}}^{r}\,x_{i}\,y_{i,l_{i}+1}^{l }\ldots y_{i,n_{i}}).$$

For each pair $(x_{i},x_{j})\in d$ with $i\leq j$, $x_{i}$ must appear as some $y_{j,k}$ with $k\leq l_{j}$ by condition $(6)$. Therefore we can apply a cup connecting $x_{i}$ and $(y_{j,k})^{r}$ in $T$. Similarly for $(x_{i},x_{j})\in d$ with $j\leq i$, $x_{i}$ must appear as some $y_{j,k}$ with $k>l_{j}$ and we can apply a cup connecting $(y_{j,k})^{l}$ and $x_{i}$ in $T$. By monogamy $(3)$ and connectedness $(5)$ of the dependency relation, there is exactly one such pair for each $x_{i}$, except for the root $x_{h}$. Therefore we can keep applying cups until only $x_{h}$ is left. By planarity $(4)$ of the dependency relation, these cups don't have to cross, which means that the diagram obtained is a valid morphism $T\to x_{h}$ in $\mathbf{RC}(\Delta(G))$. Finally condition $(5)$ ensures that there exists an induced step $x_{h}\to s\in I(G)$. Overall

**Corollary 1.5.18**.: _For any dependency grammar $G$ there is a pregroup grammar $\tilde{G}=(V,B,\Delta(G),I(G),s)$ such that $\mathcal{L}(G)\subseteq\mathcal{L}(\tilde{G})$._

**Example 1.5.19**.: _An example of the translation defined above is the following:_

The proposition above gives a structural reduction from dependency grammars to pregroup grammars, where the dependency relation witnessing the grammaticality of a string $u$ is seen as a pregroup reduction $u\to s$. This leads to a first question: do all the pregroup reduction arise from a dependency relation? In [10], Preller gives a combinatorial description of pregroup reductions, which is strikingly similar to the definition of dependency relation. In particular it features the same conditions for monogamy (3), planarity (4) and connectedness (5). However, pregroup reductions are in general _not_ acyclic, as the following example shows:

(1.21)

Therefore we do not expect that any given pregroup grammar reduces to a dependency grammar. The question still remains for pregroup grammars with restricted types of lexicons. Indeed, the cyclic example above uses a lexicon which is not of the shape (1.20). We define operadic pregroups to be pregroup grammars with lexicon of the shape (1.20).

**Definition 1.5.20** (Operadic pregroup).: _An operadic pregroup is a pregroup grammar $G=(V,B,\Delta,s)$ such that for any lexical entry $(w,t)\in\Delta$ we have $t=y^{r}x\ z^{l}$ for some $x\in B$ and $y,z\in B^{*}$._

Using Delpeuch's autonomization of monoidal categories [1], we can show that reductions in an operadic pregroup always form a tree, justifying the name "operadic" for these structures.

**Proposition 1.5.21**.: _Every operadic pregroup is functorially equivalent to a CFG._

Proof.: It will be sufficient to show that the reductions of an operadic pregroup are trees. Fix an operadic pregroup $\tilde{G}=(V,B,\Delta,I,s)$. We now define a functor $F:\mathbf{RC}(\tilde{G})\to\mathcal{A}(\mathbf{MC}(G))$ where $\mathcal{A}$ is the free rigid (or autonomous) category construction on monoidal categories as defined by Delpeuch [1], and $G$ is a context-free grammar with basic symbols $B+V$ and production rules$x\in G$ whenever $(w,y_{1}^{r}\ldots y_{l}^{r}\,x\,y_{l+1}^{l}\ldots y_{n}^{l})\in\tilde{G}$. $F$ is given by the identity on objects $F(x)=x$, and on lexical entries it is defined by:

As shown by Delpeuch the embedding $\mathbf{MC}(G)\to\mathcal{A}(\mathbf{MC}(G))$ is full on the subcategory of morphisms $g:x\to y$ where $x,y\in(B+V)^{*}$. Given any pregroup reduction $g:u\to s$ in $\mathbf{RC}(\tilde{G})$ we may apply the functor $F$ to get a morphism $F(g):F(u)\to F(s)$. By definition of $F$, we have that $F(u)=u$ and $F(s)=s$ are both elements of $(B+V)^{*}$. By fullness of the embedding, all the cups and caps in $F(g)$ can be removed using the snake equation, i.e. $F(g)\in\mathbf{MC}(G)$. We give an example to illustrate this:

\begin{tabular}{c 

**Theorem 1.5.23**.: _Every dependency grammar is structurally equivalent to both a pregroup and a context-free grammar._

Proof.: Follows from Propositions 1.5.22 and 1.5.21. 

Overall, we have three equivalent ways of looking at the structures induced by dependency grammars a.k.a operadic pregroups. First, we may see them as _dependency relations_ as first defined by Gaifman [14] and reviewed above. Second, we may see them as _pregroup reductions_ (i.e. patterns of cups) as proven in Proposition 1.5.17. Third, we may see them as _trees_ as shown in Proposition 1.5.21.

On the one hand, this new algebraic perspective will allow us to give functorial semantics to dependency grammars. In 2.5 we interpret them in rigid categories using their characterization as pregroup grammars. In 3.4.3, we interpret them in a category of probabilistic processes (where cups and caps are not allowed) using the characterization of dependency relations as trees. On the other, it allows us to interface DisCoPy with established dependency parsers such as those provided by SpaCy [15].

#### rigid.Diagram

The rigid module of DisCoPy is often used as a suitable intermediate step between any grammar and tensor-based semantics. For example, the lambeq package [11] provides a method for generating instances of rigid.Diagram from strings parsed using a transformer-based CCG parser [1]. We describe the implementation of the rigid module and construct an interface with SpaCy's dependency parser [15]. A rigid.Ob, or basic type, is defined by a name and a winding number $\mathbf{z}$. It comes with property methods .1 and .r for taking left and right adjoints by acting on the winding integer $\mathbf{z}$.

**Listing 1.5.24**.: Basic types and their iterated adjoints.

``` classOb(cat.Ob): @property defz(self): """Windingnumber""" returnself._z @property defl(self): """Leftadjoint""" returnOb(self.name,self.z - 1) @property defr(self): """Rightadjoint""" returnOb(self.name,self.z + 1) def__init__(self,name,z=0): self._z = z super()__init__(name)Types in rigid categories also come with a monoidal product, We implement them by subclassing monoidal.Ty and providing the defining methods of rigid.Ob, note that taking adjoints reverses the order of objects.

**Listing 1.5.25**.: Pregroup types, i.e. types in free rigid categories.

``` classTy(monoidal.Ty,Ob):  @property  defl(self):  returnTy(*[x.l forxinself.objects[::-1]]) @property defr(self):  returnTy(*[x.r forxinself.objects[::-1]]) @property defz(self):  returnself[0].z def__init__(self,*t):  t = [x ifisinstance(x,Ob)  elseOb(x.name)ifisinstance(x,cat.Ob)  elseOb(x)forxint] monooidal.Ty__init__(self,*t)  Ob__init__(self,str(self)) ```

Rigid diagrams are monoidal diagrams with special morphisms called Cup and Cap, satisfying the snake equations (1.18). The requirement that the axioms are satisfied is relaxed to the availability of a polynomial time algorithm for checking equality of morphisms. This is implemented in DisCoPy, with the rigid.Diagram.normal_from method, following the algorithm of Dunn and Vicary [4, Definition 2.12]. Rigid diagrams are also biclosed, i.e. they can be curryed and uncurryed.

**Listing 1.5.26**.: Diagrams in free rigid categories.

``` @monoidal.Diagram.subclassclassDiagram(monoidal.Diagram):  @staticmethod  defcups(left, right):  returncups(left, right) @staticmethod  defcaps(left, right) @staticmethod  defcurry(self, n_wires=1,left=False):  returncurry(self, n_wires=n_wires,left=left) @staticmethod  defuncurry(self, n_wires=1,left=False):  returnuncurry(self, n_wires=n_wires,left=left) def normal_form(self, normalizer=None, **params):  ...

class Box(monoidal.Box, Diagram):  ...

class Id(monoidal.Id, Diagram):  ...

_Note that currying and uncurrying correspond to transposition of wires in the rigid setting. The class comes with its own_Box _instance which carry a winding number _z for their transpositions. The currying and uncurrying functions are defined as follows._

from discopy.rigid import Id, Ty, Box, Diagram

def curry(diagram, n_wires=1, left=False):  if not n_wires > 0:  return diagram  if left:  wires = diagram.dom[:n_wires]  return Diagram.caps(wires.r, wires) @ Id(diagram.dom[n_wires:])\  >> Id(wires.r) @ diagram  wires = diagram.dom[-n_wires:]  return Id(diagram.dom[:-n_wires]) @ Diagram.caps(wires, wires.l)\  >> diagram @ Id(wires.l)

def uncurry(diagram, n_wires=1, left=False):  if not n_wires > 0:  return diagram  if left:  wires = diagram.cod[:n_wires]  return Id(wires.l) @ diagram\  >> Diagram.cups(wires.l, wires) @ Id(diagram.cod[n_wires:])  wires = diagram.cod[-n_wires:]  return diagram @ Id(wires.r)\  >> Id(diagram.cod[:-n_wires]) @ Diagram.cups(wires, wires.r)

We only showed the main methods available with rigid diagrams. The DisCoPy implementation also comes with classes Cup and Cap for representing the structural morphisms. This allows to define rigid.Functor as a monoidal Functor with a predefined mapping on instances of Cup and Cap.

**Listing 1.5.27**.: Functors from free rigid categories.

class Functor(monoidal.Functor):  def __init__(self, ob, ar, cod=(Ty, Diagram)):  super().._init__(ob, ar, cod=cod)

def __call__(self, diagram):  if isinstance(diagram, Ty):  ...

 if isinstance(diagram, Cup):  returnself.cod[1].cups(  self(diagram.dom[:1]), self(diagram.dom[1:]))  if isinstance(diagram, Cap):  returnself.cod[1].caps(  self(diagram.cod[:1]), self(diagram.cod[1:]))  if isinstance(diagram, Box):  ...  if isinstance(diagram, monoidal.Diagram):  returnsuper()...call...(diagram)  raiseTypeError()

We build an interface with the dependency parser of SpaCy [Hon+20]. From a SpaCy dependency parse we may obtain both an operad.Tree and a rigid.Diagram.

**Listing 1.5.28**.: Interface between spacy and operad.Tree

``` fromdiscopyimportoperad deffind_root(doc):  forwordindoc:  ifword.dep.=='ROOT':  returnword defdoc2tree(word):  ifnotword.children:  returnoperad.Box(word.text, operad.Ob(word.dep_), [])  root=operad.Box(word.text, operad.Ob(word.dep_),  [operad.Ob(child.dep_) forchildinword.children])  returnroot(*[doc2tree(child)forchildinword.children]) deffrom_spacy(doc):  root=find_root(doc)  returndoc2tree(root) ```

``` importspacy nlp=spacy.load("em_core_web_sm") doc=nlp("MosescrossedtheRedSea") assertstr(from_spacy(doc))='crossed(Moses,Sea(the,Red))' ```

**Listing 1.5.29**.: Interface between spacy and rigid.Diagram

``` fromdiscopy.rigidimportTy,Id,Box,Diagram,Functor defdoc2rigid(word):  children=word.children  ifnotchildren:  returnBox(word.text,Ty(word.dep_),Ty())  left=Ty(*[child.dep_ forchildinword.lefts])  right=Ty(*[child.dep_ forchildinword.rights])  box=Box(word.text, left.l @Ty(word.dep_) @ right.r,Ty(),  data=[left,Ty(word.dep_), right])  top=curry(curry(box, n_wires=len(left), left=True), n_wires=len(right)) bot=Id(Ty()).tensor(*[doc2rigid(child)forchildinchildren]) returntop>>bot defdoc2pregroup(doc): root=find_root(doc) returndoc2rigid(root) ```

_We can now build pregroup reductions from dependency parses. We check that the outputs of the two interfaces are functorially equivalent._

``` defrewiring(box): ifnotbox.data: returnBox(box.name,box.dom,Ty()) left,middle,right=box.data[0],box.data[1],box.data[2] new_box=Box(box.name,middle,left@right) returnuncurry(uncurry(new_box,len(left),left=True),len(right)) F=Functor(ob=lambdaob:Ty(ob.name),ar=rewiring) assertrepr(F(doc2pregroup(doc)).normal_form())==\ repr(operad.tree2diagram(from_spacy(doc))) drawing.equation(dep2pregroup(doc).normal_form(left=True), operad.tree2diagram(from_spacy(doc)),symbol='->') ``` 

### 1.6 Hypergraphs and coreference

Coreference resolution is the task of finding all linguistic expressions, called mentions, which refer to the same entity in a piece of text. It has been a core research topic in NLP [10], including early syntax-based models of pronoun resolution [12], Bayesian and statistical approaches [13, 14] as well as neural-based models [14, 15]. This is still a very active area of research with new state-of-the-art models released every year, and several open-source tools available in the web [16, 17].

In the previous sections, we studied a range of formal grammars that capture the syntactic structure of sentences. The aim of this section is to cross the sentence boundary and move towards an analysis of text and discourse. Assuming that the resolution process has been completed, we want a suitable syntactic representation of text with coreference. We can obtain it using a piece of structure known as a commutative special Frobenius algebra, or more simply a "spider". These were introduced in linguistics by Sadrzadeh et al. [1, 2] as a model for relative pronouns, and have recently been used by Coecke [10] to model the interaction of sentences within text.

In this section, we introduce pregroup grammars with coreference, a syntactic model which allows to represent the grammatical and referential structure of text diagrammatically. This is similar in spirit to the work of Coecke [10], although our approach preserves the pregroup formalism and adds coreference as extra structure. This makes our model suited for implementation since one can first parse sentences with a pregroup grammar and then link the entities together using coreference resolution tools. We show a proof-of-concept implementation using the hypergraph module of DisCoPy.

#### Hypergraph categories

The term "hypergraph categories" was introduced in 2018 by Fong and Spivak [12], to refer to categories equipped with _Frobenius algebras_ on every object. These structures were studied at least since Carboni and Walters [13] and have been applied to such diverse fields as databases [1], control theory [1], quantum computing [14] and linguistics [15]. In a recent line of work [17, 18, 19, 20], Bonchi, Sobocinski et al. developed a rewrite theory for morphisms in these categories in terms of double-pushout hypergraph rewriting [19]. This makes apparent the combinatorial nature of hypergraph categories, making them particularly suited to implementation [16]. We will not be interested here in the rewrite theory for these categories, but rather in their power in representing the grammatical and coreferential structure of language. They will also provide us with an intermediate step between syntax and the semantics of Sections 2.4 and 2.5.

**Definition 1.6.1** (Hypergraph category).: _[_12_]_ _A hypergraph category is a symmetric monoidal category such that each object $a$ is equipped with a commutativespecial Frobenius algebra $\mathtt{Frob}_{a}=\{\Delta_{a},\epsilon_{a},\nabla_{a},\eta_{a}\}$ satisfying the following axioms:_

(1.22)

_where the unlabeled wire denotes object $a$._

**Proposition 1.6.2**.: _Hypergraph categories are self-dual compact-closed with cups and caps given by:_

(1.23)

The axioms of commutative special Frobenius algebras (1.22), may be expressed in a more intuitive way as fusion rules of _spiders_. Spiders are defined as follows:

(1.24)

They are the normal form of commutative special Frobenius algebras. More precisely, using the axioms (1.22), it can be shown that any connected diagram built using the Frobenius generators $\mathtt{Frob}_{a}$ can be rewritten into the right-hand side above. This was shown in the context of categorical quantum mechanics [11] where Frobenius algebras, corresponding to "observables", play a foundational role. The following result is also proved in [11], and used in the context of the ZX calculus [21], it provides a more concise and intuitive way of reasoning with commutative special Frobenius algebras.

**Proposition 1.6.3** (Spider fusion).: _[_11_]_ _The axioms of special commutative Frobe nius algebras (1.22), are equivalent to the spider fusion rules:_

(1.25)

Given a monoidal signature $\Sigma$, the free hypergraph category is defined by:

$$\mathbf{Hyp}(\Sigma)=\mathbf{MC}(\Sigma+\left\{\,\mathtt{Frob}_{a}\,\right\}_{a \in\Sigma_{0}})/\cong$$

where $\mathbf{MC}$ is the free monoidal category construction, defined in 1.3 and $\cong$ is the equivalence relation generated by the axioms of commutative special Frobenius algebras (1.22), or equivalently the spider fusion rules (1.25). Without loss of generality, we may assume that the monoidal signature $\Sigma$ has trivial $\mathtt{dom}$ function. Formally we have that for any monoidal signature $B^{*}\stackrel{{\mathsf{dom}}}{{\longleftarrow}}\Sigma\stackrel{{ \mathsf{cod}}}{{\longrightarrow}}B^{*}$ there is a monoidal signature of the form $\Sigma^{\prime}\stackrel{{\mathsf{cod}}}{{\longrightarrow}}B^{*}$ such that $\mathbf{Hyp}(\Sigma)\simeq\mathbf{Hyp}(\Sigma^{\prime})$. The signature $\Sigma^{\prime}$ is defined by taking the _name_ of every generator in $\Sigma$, i.e. turning all the inputs into outputs using caps as follows:

We define a hypergraph signature as a monoidal signature where the generators have only output types.

**Definition 1.6.4** (Hypergraph signature).: _A hypergraph signature $\Sigma$ over $B$ is a set of hyperedge symbols $\Sigma$ together with a map $\sigma:\Sigma\to B^{*}$._

Morphisms in $\mathbf{Hyp}(\Sigma)$ for a hypergraph signature $\Sigma$ have a normal form given as follows.

**Proposition 1.6.5** (Hypergraph normal form).: _Let $\Sigma\to B^{*}$ be a hypergraph signature and $x,y\in B^{*}$. Any morphism $d:x\to y\in\mathbf{Hyp}(\Sigma)$ is equal to a diagram of the following shape:_ _where $H(d)\in\mathbf{Hyp}(\varnothing)$ is a morphism built using only spiders, i.e. generated from $\cup_{b}\mathtt{Frob}_{b}$ for $b\in B$._

This normal form justifies the name "hypergraph" for these categories. Indeed we may think of the spiders of a diagram $d$ as _vertices_, and boxes with $n$ ports as _hyperedges_ with $n$ vertices. Then the morphism $H(d)$ defined above is the _incidence graph_ of $d$, indicating for each vertex (spider) the hyperedges (boxes) that contain it. Note however, that morphisms in $\mathbf{Hyp}(\Sigma)$ carry more data than a simple hypergraph. First, they carry labels for every hyperedge and every vertex. Second they are "open", i.e. they carry input-output information allowing to compose them. If we consider morphisms $d:1\to 1$ in $\mathbf{Hyp}(\Sigma)$, these are in one-to-one correspondence with hypergraphs labeled by $\Sigma$, as exemplified in the following picture:

(1.26)

#### Pregroups with coreference

Starting from a pregroup grammar $G=(V,B,\Delta,I,s)$, we can model coreference by adding memory or _reference types_ for each lexical entry, and rules that allow to swap, merge or discard these reference types. Formally, this is done by fixing a set of reference types $R$ and allowing the lexicon to assign reference types alongside pregroup types:

$$\Delta\subseteq V\times P(B)\times R^{*}$$

We can then represent the derivations for such a grammar with coreference in one category $\mathbf{Coref}(\Delta,I)$ defined by:

$$\mathbf{Coref}(\Delta,I)=\mathbf{RC}(\Delta+I+\left\{\,\mathtt{Frob}_{r}\, \right\}_{r\in R},\left\{\,\mathtt{swap}_{r,x}\,\right\}_{r\in R,\,x\in P(B)+ R})$$

where $\mathtt{Frob}_{r}$ contains the generators of Frobenius algebras for every reference type $r\in R$ (allowing to initialise, merge, copy and delete them), $\mathtt{swap}_{r,x}$ allows to swap any reference type $r\in R$ to the right of any other type $x\in P(B)+R$, i.e. reference types commute with any other object. Note that we are not quotienting $\mathbf{Coref}$ by any axioms since we use it only to represent the derivations.

**Definition 1.6.6** (Pregroup with coreference).: _A pregroup grammar with coreference is a tuple $G=(V,B,R,I,\Delta,s)$ where $V$ is a vocabulary, $B\ni s$ is a set of basic types, $R$ is a set of reference types, $I\subseteq B\times B$ is a set of induced steps, $\Delta\subseteq V\times P(B)\times R^{*}$ is a lexicon, assigning to every word $w\in V$ a set of types $\Delta(w)$ consisting of a pregroup type in $P(B)$ and a list of reference type in $R^{*}$. An utterance $u=w_{0}\ldots w_{n}\in V^{*}$ is $k$-grammatical in $G$ if there are types $(t_{i},r_{i})\in\Delta(w_{i})\subseteq P(B)\times R^{*}$ such that there is morphism $t_{0}\otimes r_{0}\otimes t_{1}\otimes r_{1}\ldots t_{n}\otimes r_{n}\to s^{k}$ in $\mathbf{Coref}(\Delta,I)=:\mathbf{Coref}(G)$ for some $k\in\mathbb{N}$._ 

**Example 1.6.7**.: _We denote reference types with red wires. The following is a valid reduction in a pregroup grammar with coreference, obtained from Example 1.5.6 by adding reference types for the words "A", "whose" and "their"._

We can now consider the problem of parsing a pregroup grammar with coreference.

**Definition 1.6.8**.: CoreParsing__

_Input:_ $G$_,_ $u\in V^{*}$_,_ $k\in\mathbb{N}$__

_Output:_ $f\in\mathbf{Coref}(G)(u,s^{k})$__

Note that, seen as a decision problem, CoreParsing is equivalent to the parsing problem for pregroups.

**Proposition 1.6.9**.: _The problem $\exists\mathtt{CorefParsing}$ is equivalent to the parsing problem for pregroup grammars._

Proof.: First note that for any pregroup grammar with coreference $G=(V,B,R,I,\Delta,s)$ there is aa corresponding pregroup grammar $\tilde{G}=(V,B,I,\tilde{\Delta},s^{k})$ where $\tilde{\Delta}$ is obtained from $\Delta$ by projecting out the $R^{*}$ component. Suppose there is a reduction $d:u\to s^{k}$ in $\mathbf{Coref}(G)$, since there are no boxes making pregroup and reference types interact, we can split the diagram $d$ into a pregroup reduction in $\mathbf{RC}(G)$ and a coreference resolution $R^{n}\to 1$ where $n$ is th number of reference types used. Therefore $u$ is also grammatical in $\tilde{G}$. Now, $\tilde{G}$ reduces functorially to $G$ since we can map the lexical entries in $\tilde{\Delta}$ to the corresponding entry in $\Delta$ followed by discarding the reference types with counit spiders. Therefore any parsing for $\tilde{G}$ induces a parsing for $\mathbf{Coref}(G)$, finishing the proof. 

Supposing we can parse pregroups efficiently, CoreParsing becomes only interesting as a function problem: which coreference resolution should we choose for a given input utterance $u$? There is no definite mathematical answer to this question. Depending on the context, the same utterance may be resolved in different ways. Prominent current approaches are neural-based such as the mention-ranking coreference models of Clark and Manning [10]. SpaCy offers a neuralcoref package implementing their model and we show how to interface it with the rigid.Diagramclass at the end of this section. Being able to represent the coreference resolution in the diagram for a piece of text is particularly useful in semantics, for example it allows to build arbitrary conjunctive queries as one-dimensional strings of words, see 2.4.

The image of the parsing function for pregroups with coreference may indeed be arbitrarily omplicated, in the sense that any hypergraph $d\in\mathbf{Hyp}(\Sigma)$ can be obtained as a $k$-grammatical reduction, where the hyperedges in $\Sigma$ are seen as _verbs_ and the vertices in $B$ as _nouns_.

**Proposition 1.6.10**.: _For any finite hypergraph signature $\Sigma\xrightarrow{\sigma}B^{*}$, there is a pregroup grammar with coreference $G=(V,B,R,\Delta(\sigma),s)$ and a full functor $J:\mathbf{Coref}(\Delta(\sigma))\to\mathbf{Hyp}(\Sigma)$ with $J(w)=J(s)=1$ for $w\in V$._

Proof.: We define the vocabulary $V=\Sigma+B$ where the elements of $\Sigma$ are seen as verbs and the elements of $B$ as nouns. We also set the basic types to be $B+\{\,s\,\}$ and the reference types to be $R=B$. The lexicon $\Delta(\sigma)\subseteq V\times P(B+\{\,s\,\})\times R^{*}$ is defined by:

$$\Delta(\sigma)=\{\,(w,s\,\sigma(w)^{l},\epsilon)\,\mid\,w\in\Sigma\subseteq V \,\}+\{\,(w,w,w)|w\in B\subseteq V\,\}$$

where $\epsilon$ denotes the empty list. The functor $J:\mathbf{Coref}(\Delta(\sigma))\to\mathbf{Hyp}(\Sigma)$ is given on objects by $J(w)=1$ for $w\in V$, $J(x)=x$ for $x\in B+R$ and $J(s)=1$ and on the lexical entries by $J(w)=w$ if $w\in\Sigma$ and $J(w)=\mathtt{cup}_{w}$ if $w\in B$.

In order to prove the proposition, we show that for any $d:1\to 1\in\mathbf{Hyp}(\Sigma)$ there is an utterance $u\in V^{*}$ with a $k$-grammatical reduction $g:u\to s^{k}$ in $\mathbf{Coref}(\Delta(\sigma))$ such that $J(g)=d$, where $k$ is the number of boxes in $d$. Fix any diagram $d:1\to 1\in\mathbf{Hyp}(\Sigma)$. By proposition 1.6.5, it can be put in normal form:

Where $f_{1}\dots f_{k}$ are the boxes in $d$ and $H(d)$ is a morphism built only from the Frobenius generators $\mathtt{Frob}_{b}$ for $b\in B$. Let $\sigma(f_{i})=b_{i0}\dots b_{in_{i}}$, then for every $i\in\{\,1,\dots k\,\}$, we may build a sentence as follows (leaving open the reference wires):

Tensoring these sentences together and connecting them with coreference $H(d)$ we get a morphism $g:u\to s^{k}$ in $\mathbf{Coref}(\Delta(\sigma))$ where $u=f_{1}\sigma(f_{1})\dots f_{k}\sigma(f_{k})$, and it is easy to check that $J(g)=d$ 

#### 1.6.3 hypergraph.Diagram

The hypergraph module of DisCoPy, still under development, is an implementation of diagrams in free hypergraph categories based on [11, 12, 13]. The main class hypergraph.Diagram is well documented and it comes with a method for composition implemented using pushouts. We give a high-level overview of the datastrutures of this module, with a proof-of-concept implementation of dependency grammars with coreference. Before introducing diagrams, recall that the types of free hypergraph categories are _self-dual_ rigid types.

``` classTy(rigid.Ty): @property defl(self): returnTy(*self.objects[::-1]) r=l ```

We store a hypergraph.Diagram via its incidence graph. This is given by a list of boxes and a list of integers wires of the same length as ports.

``` port_types=list(map(Ty,self.dom))+sum(
[list(map(Ty,box.dom @ box.cod))forboxinboxes],[])\ +list(map(Ty,self.cod)) ```

Note that port_types are the concatenation of the domain of the diagram, the pairs of domains and codomains of each box, and the codomain od the diagram. We see that wires defines a mapping from ports to spiders, which we store as a list of spider_types.

``` spider_types={} forspider,typinzip(wires,port_types): ifspiderinspider_types: ifspider_types[spider]!=typ: raiseAxiomError else: spider_types[spider]=typ spider_types=[spider_types[i]foriinsorted(spider_types)] ```

Thus a hypergraph.Diagram is initialised by a domain dom, a codomain cod, a list of boxes boxes and a list of wires wires as characterised above. The __init__ method automatically computes the spider_types, and in doing so checks that the diagram is well-typed.

**Listing 1.6.11**.: Diagrams in free hypergraph categories

``` classDiagram(cat.Arrow): def__init__(self,dom,cod,boxes,wires,spider_types=None): ... defthen(self,other): ... deftensor(self,other=None,*rest): ...

_matmul__= tensor

 @property  def is_monogamous(self):  ...

 @property  def is_objective(self):  ...

 @property  def is_progressive(self):  ...

 def downgrade(self):  ...

 @staticmethod  def upgrade(old):  return rigid.Functor(  ob=lambda typ: Ty(typ[0]),  ar=lambda box: Box(box.name, box.dom, box.cod),  ob_factory=Ty, ar_factory=Diagram)(old)

 def draw(self, seed=None, k=.25, path=None):  ...

_The current draw method is based on a random spring layout algorithm of the hypergraph. One may check whether a diagram is symmetric, compact-closed or traced, using methods is_progressive, is_objective and is_monogamous respectively. The downgrade method turns any hypergraph.Diagram into a rigid.Diagram. This is by no means an optimal algorithm. There are indeed many ways to tackle the problem of extraction of rigid diagrams from hypergraph diagrams._

The classes hypergraph.Box and hypergraph.Id are defined as usual, by subclassing the corresponding rigid classes and Diagram. Two special types of morphisms, Spider and Swap, can be defined directly as subclasses of Diagram.

**Listing 6.12**.: Swaps and spiders in free hypergraph categories

``` classSwap(Diagram):  """Swapdiagram.""" def__init__(self, left, right):  dom, cod=left@right, right@left  boxes, wires=[], list(range(len(dom)))\  +list(range(len(left), len(dom)))+list(range(len(left))) super()__init__(dom, cod, boxes, wires) classSpider(Diagram):  """Spiderdiagram.""" def__init__(self, n_legs_in, n_legs_out, typ): dom, cod = typ **n_legs_in, typ **n_legs_out boxes, spider_types = [], list(map(Ty, typ)) wires = (n_legs_in + n_legs_out) * list(range(len(typ))) super()__init__(dom, cod, boxes, wires, spider_types) ```

We now show how to build hypergraph diagrams from SpaCy's dependency parser and the coreference information provided by the package neuralcoref.

**Listing 13**.: Coreference and hypergraph diagrams

``` importspacy importneuralcoref nlp=spacy.load('en') neuralcoref.add_to_pipe(nlp) doc1 = nlp("A pair of starcross lovers take their life") doc2 = nlp("whose misadventured piteous overthrows doth with \ their death bury their parent's strife.") ```

_We use the interface with SpaCy from the operad module to extract dependency parses and a rigid.Functor with codomain_ hypergraph.Diagram _to turn the dependency trees into hypergraphs._

``` fromdiscopy.operadimportfrom_spacy,tree2diagram fromdiscopy.hypergraphimportTy,Id,Box,Diagram fromdiscopyimportrigid F=rigid.Functor(ob=lambdatyp:Ty(typ[0]), ar=lambdabox:Box(box.name, box.dom, box.cod), ob_factory=Ty, ar_factory=Diagram) text=F(tree2diagram(from_spacy(doc1, lexicalised=True)))\ @F(tree2diagram(from_spacy(doc2, lexicalised=True))) assert text.is_monogamous text.downgrade().draw(figsize=(10, 7)) ```

_We can now use composition in hypergraph to add coreference boxes that link leaves according to the coreference clusters._

``` fromdiscopy.rigidimportOb ref=lambdax,y:Box('Coref',Ty(x,y),Ty(x)) defcoref(diagram, word0,word1): pos0=diagram.cod.objects.index(word0) pos1=diagram.cod.objects.index(word1) swaps=Id(Ty(word0)) @\ Diagram.swap(diagram.cod[pos0 + 1 or pos1:pos1],Ty(word1)) coreference=swaps>> \ ref(word0, word1) @Id(diagram.cod[pos0 + 1 or pos1:pos1]) returndiagram>Id(diagram.cod[:pos0]) @coreference @\  Id(diagram.cod[pos1 + 1 or len(diagram.cod):]) defresolve(diagram, clusters): coref_diagram = diagram  for cluster in clusters:  main = str(cluster.main)[0]  for mention in cluster.mentions[1:]:  coref_diagram = coref(coref_diagram, Ob(main), Ob(str(mention)))  return coref_diagram

doc = nlp("A pair of starcross lovers take their life, whose misadventured \  piteous overthrows doth with their death bury their parent's strife.")  clusters = doc...coref_clusters  resolve(text, clusters).downgrade().draw(figsize=(11, 9), draw_type_labels=False)

Note that the only way we have so far of applying functors to a hypergraph.Diagram is by first downgrading it to a rigid.Diagram. An important direction of future work is the implementation of double pushout rewriting for hypergraph diagrams [1, 2, 3]. In particular, this would allow to compute free functors directly on the hypergraph representation as they are special instances of rewrites.

 

## Chapter 1 Introduction

Thesis of the thesis is divided into two parts. The first part of the thesis is devoted to the thesis of the thesis of the thesis.

### 1.1 Introduction

The

## Chapter 2 Functors for Semantics

The modern word "semantics" emerged from the linguistic turn of the end of the 19th century along with Peirce's "semiotics" and Saussure's "semiology". It was introduced as "semantique" by the French linguist Michel Breal, and has its root in the greek word $\sigma\eta\mu\breve{\alpha}\sigma\iota\bar{\alpha}$ (semasia) which translates to "meaning" or "signification". Semantics is the scientific study of language meaning. It thus presupposes a definition of language as a system of signs, a definition of meaning as a mental or computational process, and an understanding of how signs are mapped onto their meaning. The definition and analysis of these concepts is a problem which has motivated the work of linguists, logicians and computer scientists throughout the 20th century.

In his work on "The Semantic Conception" [10, 11], Alfred Tarski proposed to found the science of semantics on the concept of _truth_ relative to a _model_. As a mathematician, Tarski focused on the formal language of logic and identified the conditions under which a logical formula $\varphi$ is true in a model $K$. The philosophical intuition and mathematical tools developed by Tarski and his collaborators had a great impact on linguistics and computer science. They form the basis of Davidson's [12, 13] truth-conditional semantics, as well as Montague's "Universal Grammar" [14, 15, 16], which translates natural language sentences into logical formulae. They are also at the heart of the development of relational databases in the 1970s [17, 18, 19], where formulas are used as queries for a structured storage of data. These approaches adhere to the principle of _compositionality_, which we may sum up in Frege's words: "The possibility of our understanding sentences which we have never heard before rests evidently on this, that we can construct the sense of a sentence out of individual parts which correspond to words" [10]. In Tarski's approach, compositionality manifests itself in the notion of _satisfaction_ for a formula $\varphi$ in a model $K$, which is defined by induction over the formal grammar from which $\varphi$ is constructed.

Formulas

$$\xrightarrow{\text{Model}}$$

 Truth

In his 1963 thesis [10], Lawvere introduced the concept of _functorial semantics_ as a foundation for universal algebra. The idea is to represent syntax as a free category with products and semantics as a structure-preserving functor computingthe meaning of a compound algebraic expression from the semantics of its basic operations. The functorial approach to semantics is naturally compositional, but it generalises Tarski's set-theoretic approach by allowing the semantic category to represent processes in different models of computation. For example, taking semantics in the category of complex vector spaces and linear maps allows to build a structural understanding of quantum information protocols [1]. The same principles are used in applications of category theory to probability [14, 15], databases [20], chemistry [16] and network theory [17]. Of particular interest to us are the Categorical Compositional Distributional (DisCoCat) models of Coecke et al. [18, 19] where functors are used to compute the semantics of natural language sentences from the distributional embeddings of their constituent words. As we will see, functors are useful for both constructing new models of meaning and formalising already existing ones.

$$\text{Syntax}\xrightarrow{\text{Functor}}\text{Semantics}$$

In this chapter, we use functorial semantics to characterise the expressivity and complexity of a number of NLP models, including logical, tensor network, quantum and neural network models, while showing how they are implemented in DisCoPy. We start in 2.1 by showing how to implement semantic categories in Python, while introducing the two main concrete categories we are interested in, $\mathbf{Mat}_{\mathbb{S}}$ and $\mathbf{Set}$, implemented respectively with the Python classes Tensor and Function. In 2.2, we show that Montague semantics is captured by functors from a biclosed grammar to the category of sets and functions $\mathbf{Set}$, through a lambda calculus for manipulating first-order logic formulas. We then give an implementation of Montague semantics by defining currying and uncurrying methods for Function. In 2.3, we show that recurrent and recursive neural network models are functors from regular and monoidal grammars (respectively) to a category $\mathbf{NN}$ of neural network architectures. We illustrate this by building an interface between DisCoPy and Tensorflow/Keras [14]. In 2.4, we show that functors from pregroup grammars to the category of relations allow to translate natural language sentences into conjunctive queries for a relational database. In 2.5, we formalise the relationship between DisCoCat and tensor networks and use it to derive complexity results for DisCoCat models. In 2.7, we study the complexity of our recently proposed quantum models for NLP [14, 15]. We show how tensor-based models are implemented in just a few lines of DisCoPy code, and we use them to solve a knowledge embedding task 2.8.

 

### 2.1 Concrete categories in Python

We describe the implementation of the main semantic modules in DisCoPy: tensor and function. These consists in classes Tensor and Function whose methods carry out numerical computation. Diagram may then be evaluated using Functor. We may start by considering the _monoid_, a set with a unit and a product, or equivalently a category with one object. We can implement it as a subclass of cat.Box by overriding init, repr, then and id. In fact, it is sufficient to provide an additional tensor method and we can make Monoid a subclass of monoidal.Box. Both then and tensor are interpreted as multiplication, id as the unit.

**Listing 2.1.1**.: Delooping of a monoid as monoidal.Box.

``` fromdiscopyimportmonoidal fromdiscopy.monoidalimportTy fromnumpyimportprod classMonoid(monoidal.Box): def__init__(self,m): self.m=m super()__init__(m,Ty(),Ty()) def__repr__(self): return"Monoid({})".format(self.m) defthen(self,other): ifnotisinstance(other,Monoid): raiseValueError returnMonoid(self.m*other.m) deftensor(self,other): returnMonoid(self.m*other.m) def__call__(self,*others): returnMonoid(prod([self.m]+[other.mforotherinothers])) @staticmethod defid(x): ifx!=Ty(): raiseValueError returnMonoid(1) assertMonoid(2)@Monoid.id(Ty())>>Monoid(5)@Monoid(0.1)==Monoid(1.0) assertMonoid(2)(Monoid(1),Monoid(4))==Monoid(8) ```

**Remark 2.1.2**.: _We define semantic classes as subclasses of monoidal.Box in order for them to inherit the usual DisCoPy syntax. This can be avoided by explicitly providing the definitions __matmul__, right and left __shift__ as well as the dataclass methods._

A weighted context-free grammar (WCFG) is a CFG where every production rule is assigned a _weight_, scores are assigned to derivations by multiplying the weightsof each production rule appearing in the tree. This model is equally expressive as probabilistic CFGs and has been applied to range of parsing and tagging tasks [15]. WCFGs are simply functors from Tree into the Monoid class! Thus we can define weighted grammars as a subclass of monoidal.Functor.

**Listing 2.1.3**.: Weighted grammars as Functor.

``` fromdiscopy.monoidalimportFunctor,Box,Id classWeightGrammar(Functor): def__init__(self,ar): ob=lambdax:Ty() super()__init__(ob,ar,ar_factory=Monoid) weight=lambdabox:Monoid(0.5)  if(box.dom,box.cod)==(Ty('N'),Ty('A','N'))elseMonoid(1.0) WCFG=WeightedGrammar(weight) A=Box('A',Ty('N'),Ty('A','N')) tree=A>>Id(Ty('A'))@A assertWCFG(tree)==Monoid(0.25) ```

We can now generate trees with NLTK and evaluate them in a weighted CFG.

**Listing 2.1.4**.: Weighted context-free grammar.

``` fromdiscopy.operadimportfrom_nltk,tree2diagram fromnltkimportCFG fromnltk.parseimportRecursiveDescentParser grammar=CFG.fromstring(""" S->VPNPNP->DN VP N->ANN V->'crossed' D->'the' N->'Moses' A->'Red' N->'Sea'""") rd=RecursiveDescentParser(grammar) parse=next(rd.parse('MosescrossedtheRedSea'.split())) diagram=tree2diagram(from_nltk(parse)) parse2=next(rd.parse('MosescrossedtheRedRedSea'.split())) diagram2=tree2diagram(from_nltk(parse2)) assertWCFG(diagram).m>WCFG(diagram2).m ```

Functors into Monoid are degenerate examples of a larger class of models called Tensor models. An instance of Monoid is in fact a Tensor with domain and codomain of dimension 1. In Tensor models of language, words and production rules are upgraded from just carrying a weight to carrying a tensor. The tensors are multiplied according to the structure of the diagram.

 

#### Tensor

Tensors are multidimensional arrays of numbers that can be multiplied along their indices. The tensor module of DisCoPy comes with interfaces with numpy[15], tensornetwork[16] and pytorch[17] for efficient tensor contraction as well as simpy[18] and jax[19] for computing gradients symbolically and numerically. We describe the implementation of the semantic class Tensor. We give a more in-depth example in 2.8, after covering the relevant theory in 2.4 and 2.5.

A semiring is a set $\mathbb{S}$ equipped with two binary operations $+$ and $\cdot$ called addition and multiplication, and two specified elements $0,1$ such that $(\mathbb{S},+,0)$ is a commutative monoid, $(\mathbb{S},\cdot,1)$ is a monoid, the multiplication distributes over addition:

$$a\cdot(b+c)=a\cdot b+a\cdot c\qquad(a+b)\cdot c=a\cdot c+b\cdot c$$

and multiplication by $0$ annihilates: $a\cdot 0=0=0\cdot a$ for all $a,b,c\in\mathbb{S}$. We say that $\mathbb{S}$ is commutative when $a\cdot b=b\cdot a$ for all $a,b\in\mathbb{S}$. Popular examples of semirings are the booleans $\mathbb{B}$, natural numbers $\mathbb{N}$, positive reals $\mathbb{R}^{+}$, reals $\mathbb{R}$ and complex numbers $\mathbb{C}$.

The axioms of a semiring are the minimal requirements to define matrix multiplication and thus a category $\mathbf{Mat}_{\mathbb{S}}$ with objects natural numbers $n,m\in\mathbb{N}$ and arrows $n\to m$ given by $n\times m$ matrices with entries in $\mathbb{S}$. Composition is given by matrix multiplication and identities by the identity matrix. For any commutative semiring $\mathbb{S}$ the category $\mathbf{Mat}_{\mathbb{S}}$ is monoidal with tensor product $\otimes$ given by the kronecker product of matrices. Note that $\mathbb{S}$ must be _commutative_ in order for $\mathbf{Mat}_{\mathbb{S}}$ to be monoidal, since otherwise the interchanger law wouldn't hold. When $\mathbb{S}$ is non-commutative, $\mathbf{Mat}_{\mathbb{S}}$ is a premonoidal category [14].

**Example 2.1.5**.: _The category of finite sets and relations $\mathbf{FRel}$ is isomorphic to $\mathbf{Mat}_{\mathbb{B}}$. The category of finite dimensional real vector spaces and linear maps is isomorphic to $\mathbf{Mat}_{\mathbb{R}}$. The category of finite dimensional Hilbert spaces and linear maps is isomorphic to $\mathbf{Mat}_{\mathbb{C}}$._

Matrices $f:1\to n_{0}\otimes\cdots\otimes n_{k}$ for objects $n_{i}\in\mathbb{N}$ are usually called _tensors_ with $k$ indices of dimensions $n_{i}$. The word tensor emphasizes that this is a $k$ dimensional array of numbers, while matrices are usually thought of as $2$ dimensional. Thus $\mathbf{Mat}_{\mathbb{S}}$ can be thought of as a category of tensors with specified input and output dimensions. This gives rise to more categorical structure. $\mathbf{Mat}_{\mathbb{S}}$ forms a hypergraph category with Frobenius structure $(\mu,\nu,\delta,\epsilon)$ given by the "generalised Kronecker delta" tensors, defined in Einstein's notation by:

$$\mu_{i,j}^{k}=\delta_{i}^{j,k}=\begin{cases}1&\text{if }i=j=k\\ 0&\text{otherwise}\end{cases}\qquad\nu^{i}=\epsilon_{i}=1$$ (2.1)

In particular, $\mathbf{Mat}_{\mathbb{S}}$ is compact closed with cups and caps given by $\mu\epsilon$ and $\delta\nu$. The transpose $f^{*}$ of a matrix $f:n\to m$ is obtained by pre and post composing with cups and caps. When the semiring $\mathbb{S}$ is involutive, $\mathbf{Mat}_{\mathbb{S}}$ has moreover a dagger structure, i.e. an involutive identity on objects contravariant endofunctor (see the nlab). In thecase when $\mathbb{S}=\mathbb{C}$ this is given by taking the conjugate transpose, corresponding to the dagger of quantum mechanics.

The class Tensor implements the category of matrices in numpy [11], with matrix multiplication as then and kronecker product as tensor. The categorical structure of $\mathbf{Mat}_{\mathbb{S}}$ translates into methods of the class Tensor, as listed below. The types of the category of tensors are given by tuples of dimensions, each entry corresponding to a wire. We can implement them as a subclass of rigid.Ty by overriding __init__.

**Listing 2.1.6**.: Dimensions, i.e. types of Tensors.

``` classDim(Ty): @staticmethod defupgrade(old): returnDim(*[x.nameforxinold.objects]) def__init__(self,*dims): dims=map(lambdax:xifisinstance(x,monoidal.Ob)elseOb(x),dims) dims=list(filter(lambdax:x.name!=1,dims))#Dim(1)==Dim() fordimindims: ifnotisinstance(dim.name,int): raiseTypeError(messages.type_err(int,dim.name)) ifdim.name<1: raiseValueError super()__init__(*dims) def__repr__(self): return"Dim({})".format(','.join(map(repr,self))or'1') def__getitem__(self,key): ifisinstance(key,slice): returnsuper()__getitem__(key) returnsuper()__getitem__(key).name @property defl(self): returnDim(*self[::-1]) @property defr(self): returnDim(*self[::-1]) @property defr(self): returnDim(*self[::-1]) ```

A Tensor is initialised by domain and codomain Dim types and an array of shape dom @ cod. It comes with methods then, tensor for composing tensors in sequence and in parallel. These matrix operations can be performed using numpy, jax.numpy [11] or pytorch [12] as backend.

**Listing 2.1.7**.: The category of tensors with Dim as objects.

``` importnumpyasnp classTensor(rigid.Box):  def__init__(self, dom, cod, array):  self._array = Tensor.np.array(array).reshape(tuple(dom @ cod))  super()__init__("Tensor", dom, cod)

 @property  defarray(self):  returnself._array

 def then(self, *others):  if self.cod != other.dom:  raise AxiomError()  array = Tensor.np.tensordot(self.array, other.array, len(self.cod))\  if self.array.shape and other.array.shape\  else self.array * other.array  return Tensor(self.dom, other.cod, array)

 def tensor(self, others):  dom, cod = self.dom @ other.dom, self.cod @ other.cod  array = Tensor.np.tensordot(self.array, other.array, 0)\  if self.array.shape and other.array.shape\  else self.array * other.array  source = range(len(dom @ cod))  target = [  i if i ! < len(self.dom) or i >= len(self.dom @ self.cod @ other.dom)  else i - len(self.cod) if i >= len(self.dom @ self.cod)  else i + len(other.dom) for i in source]  return Tensor(dom, cod, Tensor.np.moveaxis(array, source, target))

 def map(self, func):  return Tensor(  self.dom, self.cod, list(map(func, self.array.flatten())))

 @staticmethod  def id(dom=Dim(1)):  from numpy import prod  return Tensor(dom, dom, Tensor.np.eye(int(prod(dom))))

 @staticmethod  def cups(left, right):  ...

 @staticmethod  def swap(left, right):  array = Tensor.id(left @ right).array  source = range(len(left @ right), 2 * len(left @ right))  target = [i + len(right) if i < len(left @ right @ left)  else i - len(left) for i in source]  return Tensor(left @ right, right @ left,  Tensor.np.moveaxis(array, source, target)) 

#### Tensor.np = np

The compact-closed structure of the category of matrices is implemented via static methods cups and caps and swap. We check the axioms of compact closed categories (1.5.12) on a Dim object.

**Listing 2.1.8**.: Axioms of compact closed categories.

``` fromdiscopyimportDim,Tensor importnumpyasnp x=Dim(3,2) cup_r,cap_r=Tensor.cups(x,x.r),Tensor.caps(x.r,x) cup_l,cap_l=Tensor.cups(x.l,x),Tensor.caps(x,x.l) snake_r=Tensor.id(x)@cap_r>>cup_r@Tensor.id(x) snake_l=cap_l@Tensor.id(x)>>Tensor.id(x)@cup_l assertnp.allclose(snake_l.array,Tensor.id(x).array,snake_r.array) swap=Tensor.swap(x,x) assertnp.allclose((swap>>swap).array,Tensor.id(x @x).array) assertnp.allclose((swap@Tensor.id(x)>>Tensor.id(x)@swap).array, Tensor.swap(x,x @x).array) ```

Functors into Tensor allow to evaluate any DisCoPy diagram as a tensor network. They are simply monoidal.Functors with codomain (Dim, Tensor), initialised by a mapping ob from Ty to Dim and a mapping ar from monoidal.Box to Tensor. We can use them to give an example of a DisCoCat model [10] in DisCoPy, these are studied in 2.4 and 2.5 and used for a concrete task in 2.8.

**Listing 2.1.9**.: DisCoCat model as Functor.

``` fromlambeqimportBobcatParser parser=BobcatParser() diagram=parser.sentence2diagram('MosescrossedtheRedSea') diagram.draw() ```

#### Function

Function is the semantic class that characterises the models studied in 2.2 and 2.3. It consists in an implementation of the category $\mathbf{Set}$ of sets and functions, or more precisely, the category of Python functions on tuples with $\mathtt{Ty}$ as objects. We describe the basic methods of Function, that arise from the cartesian structure of the category of functions. In 2.2, we also define curry and uncurry methods for Function, accounting for the biclosed structure of this category. Alexis Toumi [13] gives detailed implementation and examples for this class.

$\mathbf{Set}$ is a monoidal category with the cartesian product $\times:\mathbf{Set}\times\mathbf{Set}\rightarrow\mathbf{Set}$ as tensor. It is moreover symmetric, there is a natural transformation $\sigma_{A,B}:A\times B\to B\times A$ satisfying $\sigma_{B,A}\circ\sigma_{A,B}=\mathtt{id}_{A\times B}$ and the axioms 1.16. $\mathbf{Set}$ is a _cartesian_ category.

**Definition 2.1.10** (Cartesian category).: _A cartesian category $\mathbf{C}$ is a symmetric monoidal category such that the product $\times$ satisfies the following properties:_

1. _there are projections_ $A\xleftarrow{\pi_{1}}A\times B\xrightarrow{\pi_{2}}B$ _for any_ $A,B\in\mathbf{C}_{0}$_,_
2. _any pair of function_ $f:C\to A$ _and_ $g:C\to B$ _induces a unique function_ $<f,g>:C\to A\times B$ _with_ $\pi_{1}\circ<f,g>=f$ _and_ $\pi_{2}\circ<f,g>=g$_._

The structure of the category of functions is orthogonal to the structure of tensors. This may be stated formally as in the following proposition, shown in the context of the foundations of quantum mechanics.

**Proposition 2.1.11**.: _[_1_]_ _A compact-closed category that is also cartesian is trivial, i.e. there is at most one morphism between any two objects._

The main difference comes from the presence of the diagonal map copy in $\mathbf{Set}$. This is a useful piece of structure which exists in any cartesian category.



**Proposition 2.1.12** (Fox [11]).: _In any cartesian category $\mathbf{C}$ there is a natural transformation $\mathtt{copy}_{A}:A\to A\otimes A$ satisfying the following axioms:_

1. _Commutative comonoid axioms:_ (2.2)
2. _Naturality of copy:_ (2.3)

This proposition may be used to characterise the _free cartesian category_ $\mathbf{Cart}(\Sigma)$ from a generating monoidal signature $\Sigma$ as the free monoidal category with natural comonoids on every object. These were first studied by Lawvere [10] who used them to define algebraic theories as functors.

**Definition 2.1.13** (Lawvere theory).: _A Lawvere theory with signature $\Sigma$ is a product-preserving functor $F:\mathbf{Cart}(\Sigma)\to\mathbf{Set}$._

We now show how to implement these concepts in Python. A Function is initialised by a domain dom and a codomain cod together with a Python function inside which takes tuples of length len(dom) to tuples of length len(cod). The class comes with methods id, then and tensor for identities, sequential and parallel composition of functions, as well as a __call__ method which accesses inside.

**Listing 2.1.14**.: The category of Python functions on tuples.

``` classFunction(monoidal.Box): def__init__(self,inside,dom,cod): self.inside=inside name="Function({},{},{})".format(inside,dom,cod) super()__init__(name,dom,cod) defthen(self,other): inside=lambda*xs:other(*tuple(self(*xs))) returnFunction(inside,self.dom,other.cod) deftensor(self,other): definside(*xs): left,right=xs[:len(self.dom)],xs[len(self.dom):] result=tuple(self(*left))+tuple(other(*right)) return(result[0],)iflen(self.cod@other.cod)==1elseresult returnFunction(inside,self.dom@other.dom,self.cod@other.cod) def__call__(self,*xs):returnself.inside(*xs) @staticmethod defid(x): returnFunction(lambda*xs:xs,x,x)@staticmethod  def copy(x):  return Function(lambda *xs: (*xs, *xs), x, x @ x)

 @staticmethod  def delete(x):  return Function(lambda *xs: (), x, Ty())

 @staticmethod  def swap(x, y):  return Function(lambda x0, y0: (y0, x0), x @ y, y @ x)

We can check the properties of diagonal maps and projections.

**Listing 2.1.15**.: Axioms of cartesian categories.

X = Ty('X') copy = Function.copy(X) delete = Function.delete(X) I = Function.id(X) swap = Function.swap(X, X)

assert (copy >> copy @ I)(54) == (copy >> I @ copy)(54) assert (copy >> delete @ I)(46) == (copy >> I @ delete)(46) assert (copy >> swap)('was my number') == (copy)('was my number')

f = Function(lambda x: (46,) if x == 54 else (54,), X, X) assert (f >> copy)(54) == (copy >> f @ f)(54) assert (copy @ copy >> I @ swap @ I)(54, 46) == Function.copy(X @ X)(54, 46)

This is all we need in order to interpret diagrams as functions! Indeed, it is sufficient to use an instance of monoidal.Functor, with codomain cod = (Ty, Function). We generate a diagram using the interface with SpaCy and we evaluate its semantics with a Functor.

**Listing 2.1.16**.: Lawvere theory as a Functor

``` fromdiscopy.operadimportfrom_spacy,tree2diagram importspacy nlp=spacy.load("en_core_web_sm") doc=nlp("Fiftyfourwasmynumber") diagram=tree2diagram(from_spacy(doc),contravariant=True) diagram.draw() 

## Chapter 2 Functors for Semantics



### 2.2 Montague models

Montague's work appeared in three papers in the 1970s [10, 11, 12]. In the first, he characterises his endeavour in formulating a mathematically precise theory of natural language semantics: "The basic aim of semantics is to characterize the notion of a true sentence (under a given interpretation) and of entailment" [10].

On the syntactic side, Montague's grammar can be seen as an instance of the categorial grammars studied in 1.4, see e.g. [10]. On the semantic side, he used a blend of lambda calculus and modal logic allowing him to combine the logical meaning of individual words into the meaning of a sentence. This work had an immediate influence on philosophy and linguistics [11, 12, 13]. It motivated much of the work on combinatory categorial grammars (see 1.4.4) and has been used in the implementation of semantic parsers turning natural language into database queries [11, 1]. From the point of view of large-scale NLP, Montague models suffer from great complexity issues and making them practical comes at the cost of restricting the possibility of (exact) logical reasoning.

It was first proposed by Lambek [1, 1], that Montague semantics should be seen as a functor from categorial grammars to a cartesian closed category. In this section, we make this idea precise, focusing on the first-order logic aspects of Montague's translation and leaving the intensional and modal aspects for future work. We formulate Montague semantics as a pair of functors:

$$G\longrightarrow\mathbf{CCC}(\Gamma_{\Sigma})\longrightarrow\mathbf{Set}$$

where $G$ is a categorial grammar, $\mathbf{CCC}(\Gamma_{\Sigma})$ is a lambda calculus for typed first-order-logic and $\mathbf{Set}$ is the category of sets and functions. This factorization allows to distinguish between the syntactic translation from sentences to formulae $G\rightarrow\mathbf{CCC}(\Gamma_{\Sigma})$ and the evaluation of the resulting formulae in a concrete model $\mathbf{CCC}(\Gamma_{\Sigma})\rightarrow\mathbf{Set}$.

We start in 2.2.1 by introducing the lambda calculus and reviewing its relationship with cartesian closed categories. In 2.2.2, we define a typed lambda calculus $\mathbf{CCC}(\Gamma_{\Sigma})$ for manipulating first-order logic formulae, and in 2.2.3 we define Montague models and discuss their complexity. Finally, in 2.2.4 we show how to implement Montague semantics in DisCoPy, by defining curry and uncurry methods for the Function class introduced in 2.1.

#### Lambda calculus

The lambda calculus was introduced in the 1930s by Alonzo Church as part of his research into the foundations of mathematics [10, 11]. It is a model of computation which can be used to simulate any Turing machine [12]. Church also introduced a simply typed version in [10] which yields a weaker model of computation but allows to avoid the infinite recursions of the untyped calculus. There is a well known correspondence -- due to Curry and Howard -- between the typed lambda calculus and intuitionistic logic, where types are seen as formulae and termsas proofs. This correspondence was later extended by Lambek [10] who showed that the typed lambda calculus has a clear characterisation as the equational theory of _cartesian closed categories_, viewing programs (or proofs) as morphisms.

The rules of the lambda calculus emerge naturally from the structure of the category of sets and functions $\mathbf{Set}$. We have seen in 2.1 that $\mathbf{Set}$ is a monoidal category with the cartesian product $\times:\mathbf{Set}\times\mathbf{Set}\to\mathbf{Set}$. Moreover, for any pair of sets $A$ and $B$, the hom-set $\mathbf{Set}(A,B)$ is itself a set, denoted $B^{A}$ or $A\to B$. In fact, there is a functor $-^{B}:\mathbf{Set}\to\mathbf{Set}$ taking a set $A$ to $A^{B}$ and a function $f:A\to C$ to a function $f^{B}:A^{B}\to C^{B}$ given by $f^{B}(g)=f\circ g$ for any $g\in A^{B}$. This functor is the right adjoint of the cartesian product, i.e. there is a natural isomorphism:

$$\mathbf{Set}(A\times B,C)\simeq\mathbf{Set}(A,C^{B})$$

This is holds in any cartesian closed category.

**Definition 2.2.1** (Cartesian closed category).: _A cartesian closed category $\mathbf{C}$ is cartesian category equipped with a functor $-^{A}$ for any object $A\in\mathbf{C}_{0}$ which is the right adjoint of the cartesian product $A\times-\dash-^{A}$. Explicitly, there is a natural isomorphism:_

$$\mathbf{C}(A\times B,C)\simeq\mathbf{C}(A,C^{B})$$ (2.4)

**Proposition 2.2.2**.: _A cartesian closed category is a cartesian category (Definition 2.1.10) which is also biclosed (Definition 1.4.2)._

**Remark 2.2.3**.: _The categorial biclosed grammars studied in 1.4 map canonically into the lambda calculus, as we will see in 2.2.3._

A functional signature is a set $\Gamma$ together with a function $\mathtt{ty}:\Gamma\to TY(B)$ into the set of functional types defined inductively by:

$$TY(B)\ni T,U\,=\,b\in B\mid T\otimes U\mid T\to U\ .$$

we write $x:T$ whenever $\mathtt{ty}(x)=T$ for $x\in\Gamma$. Given a functional signature $\Gamma$, we can consider the free cartesian closed category $\mathbf{CCC}(\Gamma)$ generated by $\Gamma$. As first shown by Lambek [10], morphisms of the free cartesian closed category over $\Gamma$ can be characterised as the terms of the simply typed lambda calculus generated by $\Gamma$.

We define the lambda calculus generated by the basic types $B$ and a functional signature $\Gamma$. Its _types_ are given by $TY(B)$. We define the set of _terms_ by the following inductive definition:

$$TE\ni t,u\ =\ x\mid tu\mid\lambda x.t\mid\ <t,u>\ \mid\pi_{1}u\mid\pi_{2}u$$

A _typing context_ is just a set of pairs of the form $x:T$, i.e. a functional signature $\Gamma$. Then a _typing judgement_ is a triple:

$$\Gamma\vdash t:T$$ consisting in the assertion that term $t$ has type $T$ in context $\Gamma$. A _typed term_ is a term $t$ with a typing judgement $\Gamma\vdash t:T$ which is derivable from the following rules of inference:

$$\overline{\Gamma,x:T\vdash x:T}$$ (2.5)

$$\frac{\Gamma\vdash t:T\qquad\Gamma\vdash u:U}{\Gamma\vdash<t,u>:T\times U} \qquad\frac{\Gamma\vdash v:T\times U}{\Gamma+\pi_{1}v:T}\qquad\qquad\frac{ \Gamma\vdash v:T\times U}{\Gamma\vdash\pi_{2}v:U}$$ (2.6)

$$\frac{\Gamma,x:U\vdash t:T}{\Gamma\vdash\lambda x.t:U\to T}\quad\frac{\Gamma \vdash t:U\to T}{\Gamma\vdash tu:T}$$ (2.7)

We define the typed lambda terms generated by $\Gamma$, denoted $\Lambda(\Gamma)$ as the lambda terms that can be typed in context $\Gamma$. In order to define equivalence of typed lambda terms we start by defining $\beta$-reduction $\to_{\beta}$ which is the relation on terms generated by the following rules:

$$(\lambda x.t)u\to_{\beta}t[u/x]\qquad\pi_{1}<t,u>\to_{\beta}t\qquad\pi_{2}<t,u> \to_{\beta}u$$ (2.8)

where $t[u/x]$ is the term obtained by substituting $u$ in place of $x$ in $t$, see e.g. [1] for an inductive definition. We define $\beta$-conversion $\sim_{\beta}$ as the symmetric reflexive transitive closure of $\to_{\beta}$. Next, we define $\eta$-conversion $\sim_{\eta}$ as the symmetric reflexive transitive closure of the relation defined by:

$$t\sim_{\eta}\lambda x.tx\qquad v\sim_{\eta}<\pi_{1}v,\pi_{2}v>$$ (2.9)

Finally $\lambda$-conversion, denoted $\sim_{\lambda}$ is the transitive closure of the union $\sim_{\beta}\cup\sim_{\eta}$. One may show that for any typed term $\Gamma\vdash t:T$, if $t\to_{\beta}t^{\prime}$ then $\Gamma\vdash t^{\prime}:T$, and similarly for $\sim_{\eta}$, so that $\lambda$-equivalence is well defined on typed terms. Moreover, $\beta$-reduction admits _strong normalisation_, i.e. ever reduction sequence is terminating and leads to a normal form without redexes. For any lambda term $t$ we denote its normal form by $\mathtt{nm}(t)$, which of course satisfies $t\sim_{\lambda}\mathtt{nm}(t)$. However normalising lambda terms is a problem known to be _not elementary recursive_ in general [15]! We discuss the consequences of this result for Montague grammar at the end of the section.

We can now state the correspondence between cartesian closed categories and the lambda calculus [11]. For a proof, we refer to the lecture notes [1] where this equivalence is spelled out in detail alongside the correspondence with intuitionistic logic.

**Proposition 2.2.4**.: _[_1_, Section 1.6.5]_ _The free cartesian closed category over $\Gamma$ is equivalent to the lambda calculus generated by $\Gamma$._

$$\mathbf{CCC}(\Gamma)\simeq\Lambda(\Gamma)/\sim_{\lambda}$$

Note that a morphism $f:x\to y$ in $\mathbf{CCC}(\Gamma)$ may have several equivalent representations as a lambda term in $\Lambda(\Gamma)$. In the remainder of this section, by $f\in\mathbf{CCC}(\Gamma)$ we will mean any such representation, and we will write explicitly $\mathtt{nm}(f)$ when we want its normal form.

 

#### Typed first-order logic

Montague used a blend of lambda calculus and logic which allows to compose the logical meaning of individual words into the meaning of a sentence. For example to intepret the sentence "John walks", Montague would assign to "John" the lambda term $J=\lambda x.\mathrm{John}(x)$ and to "walks" the term $W=\lambda\varphi.\exists x\cdot\varphi(x)\wedge\mathrm{walks}(x)$ so that their composition results in the closed logic formula $\exists x\cdot\mathrm{John}(x)\wedge\mathrm{walks}(x)$. Note that $x$ and $\varphi$ above are symbols of different type, $x$ is a variable and $\varphi$ a proposition. The aim of this section is to define a typed lambda calculus for manipulating first-order logic formulae -- akin to [10] and [11] -- which will serve as codomain for Montague's mapping.

We start by recalling the basic notions of first-order logic (FOL). A _FOL signature_$\Sigma=\mathcal{C}+\mathcal{F}+\mathcal{R}$ consist in a set of constant symbol $a,b\in\mathcal{C}$, a set of function symbols $f,g\in\mathcal{F}$ and a set of relational symbols $R,S\in\mathcal{R}$ together with a function $\mathtt{ar}:\mathcal{F}+\mathcal{R}\rightarrow\mathbb{N}$ assigning an arity to functional and relational symbols. The terms of first-order logic over $\Sigma$ are generated by the following context-free grammar:

$$FT(\Sigma)\ni t\ \ ::=\ \ x\ \mid\ a\ \mid\ f(\vec{x})$$

where $x\in\mathcal{X}$ for some countable set of variables $\mathcal{X}$, $a\in\mathcal{C}$, $f\in\mathcal{F}$ and $\vec{x}\in(\mathcal{X}\cup\mathcal{C})^{\mathtt{ar}(f)}$. The set of first-order logic formulae over $\Sigma$ is defined by the following context-free grammar:

$$FOL(\Sigma)\ni\varphi\ \ ::=\ \top\ \mid\ t\ \mid\ x=x^{\prime}\ \mid\ R(\vec{x})\ \mid\ \varphi\wedge\varphi\ \mid\ \exists\ x\cdot\varphi\ \mid\ \neg\varphi$$ (2.10)

where $t,x,x^{\prime}\in FT(\Sigma)$, $R\in\mathcal{R}$, $\vec{x}\in FT(\Sigma)^{\mathtt{ar}(R)}$ and $\top$ is the truth symbol. Let us denote the variables of $\varphi$ by $\mathtt{var}(\varphi)\subseteq\mathcal{X}$ and its free variables by $\mathtt{fv}(\varphi)\subseteq\mathtt{var}(\varphi)$. For any formula $\varphi$ and $\vec{x}\in FT(\Sigma)^{*}$, we denote by $\varphi(\vec{x})$ the formula obtained by substituting the terms $x_{1}\ldots x_{n}$ in place of the free variables of $\varphi$ where $n=|\mathtt{fv}(\varphi)|$.

We can now build a typed lambda calculus over the set of FOL formulae.

**Definition 2.2.5** (Typed first-order logic).: _Given a FOL signature $\Sigma=\mathcal{C}+\mathcal{R}$, we define the typed first order logic over $\Sigma$ as the free cartesian closed category $\mathbf{CCC}(\Gamma_{\Sigma})$ where $\Gamma_{\Sigma}$ is the functional signature with basic types:_

$$B=\left\{\,X,P\,\right\}_{n\in\mathbb{N}}$$

_where $X$ is the type of terms and $P$ is the type of propositions, and entries given by:_

$$\Gamma_{\Sigma}=\left\{\,\varphi:P\ \mid\ \varphi\in FOL(\Sigma)-FT(\Sigma)\, \right\}+\left\{\,x:X\ \mid\ x\in FT(\Sigma)\,\right\}$$

In order to recover a FOL formula from a lambda term $f:T$ in $\mathbf{CCC}(\Gamma_{\Sigma})$, we need to normalise it.

**Proposition 2.2.6**.: _For any lambda term $f:P$ in $\mathbf{CCC}(\Gamma_{\Sigma})$, the normal form is a first order logic formula $\mathtt{nm}(f)\in FOL(\Sigma)$._

Proof.:Note that morphisms $\varphi:P$ in $\mathbf{CCC}(\Gamma_{\Sigma})$ are the same as first-order logic formulae $\varphi\in FOL(\Sigma)$, since we have adopted the convention that a morphism in $\mathbf{CCC}(\Gamma)$ is the normal form of its representation as a lambda term in $\Lambda(\Gamma)$.

**Example 2.2.7**.: _Take $\Sigma=\{\,\text{John},\text{Mary},\text{walks},\text{loves}\,\}$ with $\mathtt{ar}(\text{John})=\mathtt{ar}(\text{Mary})=\mathtt{ar}(\text{walks})=1$ and $\mathtt{ar}(\text{loves})=2$. Then the following are examples of well-typed lambda expressions in $\mathbf{CCC}(\Gamma_{\Sigma})$:_

$$\lambda\varphi.\exists x\cdot\varphi(x)\wedge\text{John}(x)\,:\,P\to P \qquad\lambda x\lambda y.\text{loves}(x,y)\,:\,X\times X\to P$$

A model for first-order logic formulae is defined as follows.

**Definition 2.2.8** (FOL model).: _A model $K$ over a FOL signature $\Sigma$, also called $\Sigma$-model, is given by a set $U$ called the universe and an interpretation $K(R)\subseteq U^{\mathtt{ar}(R)}$ for every relational symbol $R\in\mathcal{R}$ and $K(a)\in U$ for every constant symbol $c\in\mathcal{C}$. We denote by $\mathcal{M}_{\Sigma}$ the set of $\Sigma$-models._

Given a model $K\in\mathcal{M}_{\Sigma}$ with universe $U$, let

$$\mathtt{eval}(\varphi,K)=\{\,v\in U^{\mathtt{fv}(\varphi)}\,\mid\,(K,v)\vDash \varphi\,\}$$

where the satisfaction relation ($\vDash$) is defined by induction over (2.10) in the usual way.

**Proposition 2.2.9**.: _Any model $K\in\mathcal{M}_{\Sigma}$ induces a monoidal functor $F_{K}:\mathbf{CCC}(\Gamma_{\Sigma})\to\mathbf{Set}$ such that closed lambda terms $\varphi:F_{0}$ are mapped to their truth value in $K$._

Proof.: By the universal property of free cartesian closed categories, it is sufficient to define $F_{K}$ on generating objects and arrows. On objects we define:

$$F_{K}(X)=1\qquad F_{K}(P)=\coprod_{n=0}^{N}\mathcal{P}(U^{n})$$

where $N$ is the maximum arity of a symbol in $\Sigma$ and $\mathcal{P}(U^{n})$ is the powerset of $U^{n}$. On generating arrows $\varphi:P$ and $x:X$ in $\Gamma$, $F_{k}$ is defined by:

$$F_{K}(\varphi)=\mathtt{eval}(\varphi,K)\in F_{K}(P)\qquad F_{K}(x)=1$$

#### Montague semantics

We model Montague semantics as a pair of functors $G\to\mathbf{CCC}(\Gamma_{\Sigma})\to\mathbf{Set}$ for a grammar $G$. We have already seen that functors $\mathbf{CCC}(\Gamma_{\Sigma})\to\mathbf{Set}$ can be built from $\Sigma$-models or relational databases. It remains to study functors $G\to\mathbf{CCC}(\Gamma_{\Sigma})$, which we call _Montague models_.

 

**Definition 2.2.10** (Montague model).: _A Montague model is a monoidal functor $M:G\to\mathbf{CCC}(\Gamma_{\Sigma})$ for a biclosed grammar $G$ and a FOL signature $\Sigma$ such that $M(s)=P$ and $M(w)=1$ for any $w\in V\subseteq G_{0}$. The semantics of a grammatical sentence $g:u\to s$ in $\mathbf{BC}(G)$ is the first order logic formula $\mathtt{nm}(M(w))\in FOL(\Sigma)$ obtained by normalising the lambda term $M(w):P$ in $\mathbf{CCC}(\Gamma_{\Sigma})$._

**Remark 2.2.11**.: _Note that since $\mathbf{CCC}(\Gamma_{\Sigma})$ is biclosed, it is sufficient to define the image of the lexical entries in $G$ to obtain a Montague model. The structural morphisms $\mathtt{app}$, $\mathtt{comp}$ defined in 1.4.3 have a canonical intepretation in any cartesian closed category given by:_

$$\mathtt{app}_{A,B}\mapsto\lambda f.(\pi_{2}f)(\pi_{1}f):(A\times(A\to B))\to B$$

$$\mathtt{comp}_{A,B,C}\mapsto\lambda f\lambda a.(\pi_{2}f)(\pi_{1}f)a:((A\to B )\times(B\to C))\to(A\to C)$$

**Example 2.2.12**.: _Let us consider a Lambek grammar $G$ with basic types $B=\{\,n,n^{\prime},s\,\}$ and lexicon given by:_

$$\Delta(\mathit{All})=\{\,s/(n\backslash s)/n^{\prime}\,\}\quad\Delta(roads)= \{\,n^{\prime}\,\}\quad\Delta(\mathit{lead}\ to)=\{\,(n\backslash s)/n\,\} \quad\Delta(\mathit{Rome})=\{\,n\,\}$$

_The following is a grammatical sentence in $\mathcal{L}(G)$:_

_We fix a FOL signature $\Sigma=\mathcal{R}+\mathcal{C}$ with one constant symbol $\mathcal{C}=\{\,\mathit{Rome}\,\}$ and two relational symbols $\mathcal{R}=\{\,\mathit{road},\mathit{leads-to}\,\}$ with arity $1$ and $2$ respectively. We can now define a Montague model $M$ on objects by:_

$$M(n)=X\quad M(n^{\prime})=X\to P\quad M(s)=P$$

_and on arrows by:_

$$M(\mathit{All})=\lambda\varphi\lambda\psi.\forall x(\varphi(x)\implies\psi(x)) :(X\to P)\to((X\to P)\to P)$$

$$M(\mathit{roads})=\lambda x.\mathit{road}(x):X\to P\qquad M(\mathit{Rome})= \mathit{Rome}:X$$

$$M(\mathit{lead}\ to)=\lambda x\lambda y.\mathit{leads-to}(x,y):X\to(X\to P)$$

_Then the image of the sentence above normalises to the following lambda term:_

$$M(\mathit{All}\ to\ \mathit{Rome}\to s)=\forall x\cdot(\mathit{road}(x)\implies \mathit{leads-to}(x,\mathit{Rome}))$$We are interested in the problem of computing the Montague semantics of sentences generated by a biclosed grammar $G$.

**Definition 2.2.13**.: LogicalForm$(G)$__

_Input:_ $g:u\to s$_,_ $\Sigma$_,_ $M:G\rightarrow\mathbf{CCC}(\Gamma_{\Sigma})$__

_Output:_ $\mathtt{nm}(M(g))\in FOL(\Sigma)$__

We may split the above problem in two steps. First, given the sentence $g:u\to s$ we are asked to produce the corresponding lambda term $M(g)\in\Lambda(\Gamma_{\Sigma})$. Second, we are asked to normalise this lambda term in order to obtain the underlying first-order logic formula in $FOL(\Sigma)$. The first step is easy and may in fact be done in L since it is an example of a functorial reduction, see Proposition 1.3.16. The second step may however be exceptionally hard. Indeed, Statman showed that deciding $\beta$ equivalence between simply-typed lambda terms is not elementary recursive [10]. As a consequence, the normalisation of lambda terms is itself not elementary recursive. We may moreover show that any simply typed lambda term can be obtained in the image of some $M:G\rightarrow\mathbf{CCC}(\Gamma_{\Sigma})$, yielding the following result.

**Proposition 2.2.14**.: _There are biclosed grammars $G$ such that $\mathtt{LogicalForm}(G)$ is not elementary recursive._

Proof.: Let $G$ be a biclosed grammar with one generating object $a$ generating arrows $\mathtt{swap}:a\otimes a\to a\otimes a$, $\mathtt{copy}:a\to a\otimes a$ and $\mathtt{discard}:a\to 1$. These generators map canonically in any cartesian category. In fact, there is a full functor $F:\mathbf{BC}(G)\rightarrow\mathbf{CCC}$, since all the structural morphisms of cartesian closed categories can be represented in $\mathbf{BC}(G)$. Therefore for any morphism $h\in\mathbf{CCC}$ there is a morphism $f\in\mathbf{BC}(G)$ such that $F(f)=h$. Then for any typed lambda term $g\in\Lambda(\varnothing)$ there is a morphism $f\in\mathbf{BC}(G)$ such that $F(f)$ maps to $g$ under the translation 2.2.4. Therefore normalising $g$ is equivalent to computing $\mathtt{nm}(F(f))=\mathtt{LogicalForm}(G)$. Therefore the problem of normalising lambda terms reduces to LogicalForm. 

Of course, this proposition is about the worst case scenario, and definitely not about human language. In fact, small to medium scale semantic parsers exist which translate natural language sentences into their logical form using Montague's translation [15, 1]. It would be interesting to show that for restricted choices of grammar $G$ (e.g. Lambek or Combinatory grammars), and possibly assuming that the order of the lambda terms assigned to words is bounded (as in [11]), LogicalForm becomes tractable.

Even if we are able to extract a logical formula efficiently from natural language, we need to be able to evaluate it in a database in order to compute its truth value. Thus, in order to compute the full-blown montague semantics we need to solve the following problem.

**Definition 2.2.15**.: Montague$(G)$__

_Input:_ $g:u\to s$_,_ $\Sigma$_,_ $M:G\rightarrow\mathbf{CCC}(\Gamma_{\Sigma})$_,_ $K\in\mathcal{M}_{\Sigma}$__

_Output:_ $F_{K}(M(g))\subseteq U^{\mathtt{fv}(M(g))}$__ Note that solving this problem does not necessarily require to solve LogicalForm. However, since we are dealing with first-order logic, the problem for a general biclosed grammar is at least as hard as the evaluation of FOL formulae.

**Proposition 2.2.16**.: _There are biclosed grammars $G$ such that_ Montague _is_ PSPACE_-hard._

Proof.: It was shown by Vardi that the problem of evaluating $\mathtt{eval}(\varphi,K)$ for a first-order logic formula $\varphi$ and a model $K$ is PSPACE-hard [11]. Reducing this problem to Montague is easy. Take $G$ to be a categorial grammar with a single word $w$ of type $s$. Given any first-order logic formula $\varphi$ and model $K$, we define $M:G\rightarrow\mathbf{CCC}(\Gamma_{\Sigma})$ by $M(s)=P$ and $M(w)=\varphi$. Then we have that the desired output $F_{K}(M(w))=F_{K}(\varphi)=\mathtt{eval}(\varphi,K)$ is the evaluation of $\varphi$ in $K$. 

It would be interesting to look at restrictions of this problem, such as fixing the Montague model $M$, fixing the input sentence $g:u\to s$ and restricting the allowed grammars $G$. In general however, the proposition above shows that working with full-blown first-order logic is inpractical for large-scale industrial NLP applications. It also shows that models of this kind are the most general and applicable if we can find a compromise between tractability and logical expressivity.

#### Montague in DisCoPy

We implement Montague models as DisCoPy functors from biclosed.Diagram into the class Function, as introduced in 1.4 and 2.1 respectively. Before we can do this, we need to upgrade the Function class to account for its biclosed structure. The only additional methods we need are curry and uncurry.

**Listing 2.2.17**.: Curry and UnCurry methods for Function.

``` classFunction: ...  defcurry(self, n_vires=1, left=False):  ifnotleft:  dom=self.dom[:-n_vires]  cod=self.cod <<self.dom[-n_vires:]  inside=lambda*xl: (lambda *xr: self.inside(*(xl + xr)),)  returnFunction(inside, dom, cod) else:  dom=self.dom[n_vires:]  cod=self.dom[:n_vires] >>self.cod  inside=lambda*xl: (lambda *xr: self.inside(*(xl + xr)),)  returnFunction(inside, dom, cod)

def uncurry(self):  if isinstance(self.cod, Over):  left, right=self.cod.left, self.cod.right  cod=left  dom=self.dom @right  inside=lambda*xs: self.inside(*xs[:len(self.dom)])[0](*xs[len(self.dom):]) return Function(inside, dom, cod) elif isinstance(self.cod, Under): left, right = self.cod.left, self.cod.right cod = right dom = left @ self.dom inside = lambda *xs: self.inside(*xs[len(left):])[0](*xs[:len(left)]) return Function(inside, dom, cod) return self ```

We can now map biclosed diagrams into functions using biclosed.Functor. We start by initialising a sentence with its categorial grammar parse.

**Listing 2.2.18**.: Example parse from a categorial grammar

``` fromdiscopy.biclosedimportTy,Id,Box,Curry,UnCurry N,S=Ty('N'),Ty('S') two,three,five=Box('two',Ty(),N),Box('three',Ty(),N),Box('five',Ty(),N) plus,is_=Box('plus',Ty(),N>>(N<<N)),Box('is',Ty(),N>>S<<N) FA=lambdaa,b:UnCurry(Id(a>>b)) BA=lambdaa,b:UnCurry(Id(b<<a)) sentence=two @plus @three @is_ @five grammar=FA(N,N<<N) @Id(N) @ BA(N,N>>S)>>BA(N,N) @ Id(N>>S)>>FA(N,S) sentence=sentence>>grammar sentence.draw() ```

We can now evaluate this sentence in a Montague model defined as a biclosed functor.

**Listing 2.2.19**.: Evaluating a sentence in a Montague model.

``` fromdiscopy.biclosedimportFunctor number=lambday:Function(lambda:(y,),Ty(),N) add=Function(lambdax,y:(x+y,),N@N,N) equals=Function(lambdax,y:(x==y,),N@N,S) 
#### 2.2.3.1 The $\alpha$-function

The $\alpha$-function is a function of the form $\alpha=\alpha_{1}+\alpha_{2}$, where $\alpha_{1}$ is the $\alpha_{2}$-function. The function $\alpha_{1}$ is a function of the form $\alpha=\alpha_{1}+\alpha_{2}$.

 

### 2.3 Neural network models

In the last couple of decades, neural networks have become ubiquitous in natural language processing. They have been used successfully in a wide range of tasks including language modelling [15], machine translation [1, 20], parsing [14], question answering [16] and sentiment analysis [21, 1].

In this section we show that neural network models can be formalised as functors from a grammar $G$ to the category $\mathbf{Set}_{\mathbb{R}}$ of Euclidean spaces and functions via a category $\mathbf{NN}$ of neural network architectures. This includes feed-forward, recurrent and recursive neural networks and we discuss how the recent attention mechanisms could be formalised in this diagrammatic framework. At each step, we show how these neural architectures are used to solve concrete tasks such as sentence classification, language modelling, sentiment analysis and machine translation. We keep a level of informality in describing the learning process, an aspect which we will further explore in Chapter 3. We end the section by building an interface between DisCoPy and Tensorflow/Keras neural networks [1, 16, 17], by defining a class Network that allows for composing and tensoring Keras models.

#### Feed-forward networks

The great advantage of neural networks comes from their ability to simulate any function on Euclidean spaces, a series of results known as universal approximation theorems [18, 19]. We will thus give them semantics in the category $\mathbf{Set}_{\mathbb{R}}$ where morphisms are functions acting on Euclidean spaces. Note that $\mathbf{Set}_{\mathbb{R}}$ is monoidal with product $\oplus$ defined on objects as the direct sum of Euclidean spaces $\mathbb{R}^{n}\oplus\mathbb{R}^{m}=\mathbb{R}^{n+m}$ and on arrows as the cartesian product $f\oplus g(x,y)=(f(x),g(y))$. To our knowledge, $\mathbf{Set}_{\mathbb{R}}$ doesn't have much more structure than this. We will in fact not be able to interpret

In a typical supervised machine learning problem one wants to approximate an unknown function $f:\mathbb{R}^{n}\rightarrow\mathbb{R}^{m}$ given a dataset of pairs $D=\{(x,f(x))|x\in\mathbb{R}^{n},\,f(x)\in\mathbb{R}^{m}\}$. Neural networks are parametrized functions built from the following basic processing units:

1. sum $\texttt{sum}:n\to 1$ for $n\in\mathbb{N}$,
2. weights $\{w:1\to 1\}_{w\in W_{0}}$,
3. biases $\{r:0\to 1\}_{r\in W_{1}}$
4. and activation $\sigma:1\to 1$.

where $W=W_{0}+W_{1}$ is a set of variables. These generate a free cartesian category

$$\mathbf{NN}=\mathbf{Cart}(W+\{\texttt{sum},\sigma\})$$

where morphisms are the diagrams of neural network architectures. For example, a neuron with $n$ inputs, bias $w_{0}\in W$ and weights $\vec{w}\in W^{*}$ is given by the followingdiagram in $\mathbf{NN}$.

(2.11)

"Deep" networks are simply given by composing these neurons in parallel forming a _layer_ :

$n$$\cdots$$ of the network step-by-step while descending along the gradient of $l$, see [10] for a recent categorical treatment of differentiation.

Although neural networks are deterministic functions, it is often useful to think of them as probabilistic models. One can turn the output of a neural network into a probability distribution using the softmax function as follows. Given a neural network $K:m\to n$ and a choice of parameters $\theta:W\to\mathbb{R}$ we can compose $I_{\theta}(K):\mathbb{R}^{m}\to\mathbb{R}^{n}$ with a softmax layer, given by:

$$\texttt{softmax}_{n}(\vec{x})_{i}=\frac{e^{x_{i}}}{\sum_{i=1}^{n}e^{x_{i}}}$$

Then the output is a normalised vector of positive reals of length $n$, which yields a distribution over $[n]$ the set with $n$ elements, i.e. softmax has the following type:

$$\texttt{softmax}_{n}:\mathbb{R}^{n}\to\mathcal{D}([n])$$

where $\mathcal{D}(A)$ is the set of probability distributions over $A$, as defined in 3.1, where softmax is analysed in more detail. In order to simulate a probabilistic process, from a neural network $K:m\to n$, an element of $[n]$ is drawn at random from the induced distribution $\texttt{softmax}_{n}(I_{\theta}(K)(x))\in\mathcal{D}([n])$.

Feed-forward neural networks can be used for _sentence classification_: the general task of assigning labels to pieces of written text. Applications include spam detection, sentiment analysis and document classification. Let $D\subseteq V^{*}\times X$ be a dataset of pairs $(u,x)$ for $u$ an utterance and $x$ a label. The task is to find a function $f:V^{*}\to\mathcal{D}(X)$ minimizing a loss function $l(f,D)$ which computes the distance between the predicted labels and the expected ones given by $D$. For example one may take the mean squared error $l(f,D)=\sum_{(u,x)\in D}(f(u)-|x))^{2}$ or the cross entropy loss $-\frac{1}{|D|}\sum_{(u,x)\in D}|x)\cdot\texttt{log}(f(u))$, where $|x)$ is the one-hot encoding of $x\in X$ as a distribution $|x)\in\mathcal{D}(X)$ and $\cdot$ is the inner product. Assuming that every sentence $u\in V^{*}$ has length at most $m$ and that we have a word embedding $E:V\to\mathbb{R}^{k}$, we can parametrize the set of functions $\mathbb{R}^{mk}\to\mathbb{R}^{|X|}$ using a neural network $K:mk\to|X|$ and use softmax to get a probability distribution over classes:

$$f(x\,|\,u)=\texttt{softmax}_{k}(I_{\theta}(K)(E^{*}(u)))\in\mathcal{D}(X)$$

where $u=v_{1}v_{2}\ldots v_{m}\in V^{*}$ is an utterance and $E^{*}(u)$ is the feature vector for $u$, obtained by concatenating the word embeddings $E^{*}(u)=\texttt{concat}(E(v_{1}),E(v_{2}),\ldots,E(v_{n}))$. In this approach, $K$ plays the role of a black box which takes in a list of words and ouputs a class. For instance in a sentiment analysis task, we can set $X=\{\,\texttt{positive},\texttt{negative}\,\}$ and $m=3$ and expect that "not so good" is classified as "negative".

$$\begin{array}{c|c|c|c|}\text{Not}&\text{so}&\text{good}\\ k&k&k&k\\ \hline\end{array}$$
 A second task we will be interested in is _language modelling_, the task of predicting a word in a text given the previous words. It takes as input a corpus, i.e. a set of strings of words $C\subseteq V^{*}$, and outputs $f:V^{*}\rightarrow\mathcal{D}(V)$ a function which ouputs a distribution for next word $f(u)\in\mathcal{D}(V)$ given a sequence of previous words $u\in V^{*}$. Language modelling can be seen as an instance of the classification task, where the corpus $C$ is turned into a dataset of pairs $D$ such that $(u,x)\in D$ whenever $ux$ is a substring of $C$. Thus language modelling is a _self-supervised_ task, i.e. the supervision is not annotated by humans but directly generated from text. Neural networks were first used for language modelling by Bengio et al. [1], who trained a single (deep) neural network taking a fixed number of words as input and predicting the next, obtaining state of the art results at the time.

For both of these tasks, feed-forward neural networks perform poorly compared to the recurrent architectures which we are about to study. This is because feed-forward networks take no account of the sequential nature of the input.

#### Recurrent networks

The most popular architectures currently used modelling language are _recurrent neural networks_ (RNNs). They were introduced in NLP by Mikolov et al. in 2010 [10] and have since become widely used, see [1] for a survey.

RNNs were introduced by Ellman [1] to process sequence input data. They are defined by the following recursive equations:

$$h_{t}=\sigma(W_{h}x_{t}+U_{h}h_{t-1}+b_{h})\quad y_{t}=\sigma(W_{y}h_{t}+b_{y})$$ (2.12)

where $t\in\mathbb{N}$ is a time variable, $h_{t}$ denotes the encoder hidden vector, $x_{t}$ the input vector, $y_{t}$ the output, $W_{h}$ and $W_{y}$ are matrices of weights and $b_{h},b_{y}$ are bias vectors. We may draw these two components as diagrams in **NN**:

**Remark 2.3.1**.: _The diagrams in the remainder of this section should be read from left/top to bottom/right. One may obtain the corresponding string diagram by bending the left wires to the top and the right wires to the bottom. In the diagram above we have omitted the subscript $t$ since it is determined by the left-to-right reading of the diagram and we use the labels $h,x,y$ for dimensions, i.e. objects of_ **NN**_._ The networks above are usually called _simple_ recurrent networks since they have only one layer. More generally $X$ and $Y$ could be any neural networks of type $X:x\oplus h\to h$ and $Y:h\to y$, often called recurrent network and decoder respectively.

**Definition 2.3.2**.: _A recurrent neural network is a pair of neural networks $X:x\oplus h\to h$ and $Y:h\to y$ in $\mathbf{NN}$ for some dimensions $x,h,y\in\mathbb{N}$._

The data of RNNs defined above captures precisely the data of a functor from a regular grammar as we proceed to show. Fix a finite vocabulary $V$ and consider the regular grammar $RG$ with three symbols $s_{0},h,s_{1}$ and transitions $h\xrightarrow{w}h$ for each word $w\in V$.

Note that $RG$ parses any string of words, i.e. the language generated by $RG$ is $\mathcal{L}(RG)=V^{*}$. The derivations in $RG$ are sequences:

$$s_{0}\,\raisebox{-1.5pt}{\includegraphics[width=14.226378pt]{figs_0$0$1_1$2$2_3$4$5_6$7$8_9_1 $2$4_5$7$8_1$2$5_8$1$2_6$7$8_1$2$7_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_8$1$2_81$8$1_2$8$1_2_81$8$1_2_81$8$1_2_81$8$1_2_81$8$1_2_81$8$1_81$8$1_2_81$8$1_81$8$1_81$8$1_81_81$8$1_81 In order to classify sentences in a set of classes $X$, one may choose $y=|X|$, so that the implementation of the diagram above is a vector of size $|X|$ giving scores for the likelihood that $w_{0}w_{1}\ldots w_{k}$ belongs to class $c\in X$.

For language modelling, we may set $y=|V|$. Given a string of words $u\in V^{*}$ with derivation $g_{u}:s_{0}\to s_{1}\in\mathbf{C}(RG)$ and an implementation $I_{\theta}:\mathbf{NN}\rightarrow\mathbf{Set}_{\mathbb{R}}$, we can compute the distribution over the next words $\mathtt{softmax}(I_{\theta}(RN(g_{u})))\in\mathcal{D}\left|V\right|$.

Another task that recurrent neural networks allow to tackle is _machine translation_. This is done by composing a encoder recurrent network $X:|V|\oplus h\to h$ with a decoder recurrent network $K:h\to h\oplus|V|$, as in the following diagram.

$$\begin{array}{c|cccc}w_{0}&&w_{k}&&\\ |V|&\cdots&|V|&\\ \hline h&\begin{array}{c}X\\ \end{array}&\begin{array}{c}h\\ |V|\end{array}&\begin{array}{c}X\\ \end{array}&\ DAG $(N,E)$, the parents of a vertex $v$ are defined by $\mathtt{pa}(v)=\{\,v^{\prime}\in N\,|\,(v^{\prime},v)\in E\,\}$ and the children by $\mathtt{ch}(v)=\{\,v^{\prime}\in N\,|\,(v,v^{\prime})\in E\,\}$. A $\Sigma$-labelled DAG is a DAG $(N,E)$ with a labelling function $\varphi:N\to\Sigma$.

Suppose we have a set $X$ of $\Sigma$-labelled DAGs which we want to classify over $k$ classes, given a dataset of pairs $D\subseteq X\times[k]$. The naive way to do this is to encode every graph in $D$ as a vector of fixed dimension $n$ and learning the parameters of a neural network $K:n\to k$. Sperduti and Starita propose instead to assign a _recursive neuron_ to each vertex of the graph, and connecting them according to the topological structure of the graph. Given a labelled DAG $(N,E,\varphi)$ with an assignment $\theta:E+\Sigma\to\mathbb{R}$ of weights to every edge in $E$ and every label in $\Sigma$, the recursive neuron assigned to a vertex $v$ in a DAG $(N,E)$ is the function defined by the following recursive formula:

$$o(v)=\sigma(\theta(\varphi(v))+\sum_{v^{\prime}\in\mathtt{pa}(v)}\theta(v^{ \prime},v)o(v^{\prime}))$$ (2.15)

Note that this is a simplification of the formula given by Sperduti et al. where we assume that a single weight is assigned to every edge and label, see [10] for details. They further assume that the graph has a _sink_, i.e. a vertex which can be reached from any other vertex in the graph. This allows to consider the output of the neuron assigned to the supertarget as the score of the graph, which they use for classification.

We show that the recursive neuron (2.15) defines a functor from a monoidal grammar to the category of neural networks $\mathbf{NN}$. Given any set of $\Sigma$-labelled DAGs $X$, we may construct a monoidal signature $G=\Sigma+E^{*}\xleftarrow{\varphi+\mathtt{in}}N\xrightarrow{\mathtt{out}}E^{*}$ where $N$ is the set of all vertices appearing in a graph in $X$ and $E$ is the set of all edges appearing in a graph in $X$, with $\mathtt{in},\mathtt{out}:N\to E^{*}$ listing the input and output edges of vertex $v$ respectively and $\varphi:N\to\Sigma$ is the labelling function. Then the recursive neuron $o$ given above defines a functor $O:\mathbf{MC}(G+\mathtt{swap})\to\mathbf{Set}_{\mathbb{R}}$ from the free monoidal category generated by $G$ and swaps to $\mathbf{Set}_{\mathbb{R}}$. The image of a vertex $v:l\oplus\vec{e}\to\vec{e^{\prime}}$ is a function $O(v):\mathbb{R}^{|\vec{e}|+1}\to\mathbb{R}^{|\vec{e^{\prime}}|}$ given by: $O(v)(x)=\mathtt{copy}(o(v)(x))$ where $\mathtt{copy}:\mathbb{R}\to\mathbb{R}^{|\vec{e}|}$ is the diagonal map in $\mathbf{Set}_{\mathbb{R}}$. Note that any DAG $H\in X$ gives rise to a morphism in $\mathbf{MC}(G+\mathtt{swap})$ given by connecting the boxes (vertices) according to the topological structure of the graph, using swaps if necessary. Note that the functor $O$ factors through the category $\mathbf{NN}$ of neural networks since all the components of Equation 2.15 are generators of $\mathbf{NN}$, thus $O$ defines a mapping from DAGs in $X$ to neural networks. Generalising from this to the case where vertices in the graph can be assigned multiple neurons, we define recursive neural networks as follows.

**Definition 2.3.5**.: _A recursive network model is a monoidal functor $F:G\to\mathbf{NN}$ for a monoidal grammar $G$, such that $F(w)=1$ for $w\in V\subseteq G_{0}$. Given a choice of parameters $\theta:W\to\mathbb{R}$, the semantics of a parsed sentence $g:u\to s$ in $\mathbf{MC}(G)$ is given by $\textit{I}_{\theta}(F(g))\in\mathbb{R}^{F(s)}$._

**Remark 2.3.6**.: _Although it is in general useful to consider non-planar graphs as the input of a recursive neural network, in applications to linguistics one can usually assume that the graphs are planar. In order to recover non-planar graphs from the definition above it is sufficient to add a swap to the signature $G$._

With this definition at hand, we can look at the applications of RvNNs in linguistics. The recursive networks for sentiment analysis of [12] are functors from a context-free grammar to neural networks. In this case RvNNs are shown to capture correctly the role of negation in changing the sentiment of a review. This is because the tree structure induced by the context-free grammar captures the part of the phrase which is being negated, as in the following example.

$$\begin{array}{c}\includegraphics[width=142.26378pt]{figs/r- where $x_{i}$ is the $i$th input word in the domain language, $y_{i}$ is the $i$th output word in the target language, the $h_{i}$s and $s_{i}$s are the hidden states of the encoder and decoder RNN respectively:

$$h_{i}=f(x_{i},h_{i-1})\qquad s_{i}=g(s_{i-1},y_{i-1},c_{i})$$

and $c_{i}$ is the context vector calculated from the input $\vec{x}$, the hidden states $\vec{h}$ and the last decoder hidden state $s_{i-1}$ as follows:

$$c_{i}=\sum_{j=1}^{n}\alpha_{ij}h_{j}$$ (2.17)

where

$$\alpha_{ij}=(\texttt{softmax}_{n}(\vec{e_{i}}))_{j}\quad(\vec{e_{i}})_{j}=a(s _{i-1},h_{j})$$ (2.18)

where $n=|\vec{x}|$ and $a$ is a (learned) feed-forward neural network. The coefficients $\alpha_{ij}$ are called _attention weights_, they provide information as to how much input word $x_{j}$ is relevant for determining the output word $y_{i}$. In the picture above, we used a comb notation for Attention informally to represent the recursive relation between context vectors $c$ and hidden states $h$ and $s$, capturing the flow of information in the architecture of Bahdanau et al. This diagram should be read from top-left to bottom-right. At each time step $t$, the attention mechanism computes the context vector $c_{t}$ from the last decoder hidden state $s_{t-1}$ and all the encoder hidden states $\vec{h}$. Infinite comb diagrams such as the one above may be formalised as monoidal streams over the category of neural networks [10]. A similar notation is used in Chapter 3. Note that Bahdanau et al. model the encoder $f$ as a bidirectional RNN [14] which produces hidden states $h_{i}$ that depend both on the previous and the following words. For simplicity we have depicted $f$ as a standard RNN.

In 2017, Vaswani et al. published the paper "Attention is all you need" [21] which introduced _transformers_. They showed that the recurrent structure is not needed to obtain state-of-the-art results in machine translation. Instead, they proposed a model built up from three simple components: positional encoding, attention and feed-forward networks, composed as in the following diagram:

(2.19)

where 1. $W_{Q},W_{K},W_{V}$ are (learned) linear functions, and $D$ is a (learned) decoder neural network.
2. the positional encoding pos supplements the word vector $w_{i}$ of dimension $n$ with another $n$ dimensional vector $\texttt{pos}(i)\in\mathbb{R}^{n}$ where $\texttt{pos}:\mathbb{N}\rightarrow\mathbb{R}^{n}$ is given by: $$\texttt{pos}(i)_{j}=\begin{cases}\texttt{sin}(\frac{j}{m^{2k/n}})&\text{if $j=2k$}\\ \texttt{cos}(\frac{j}{m^{2k/n}})&\text{if $j=2k+1$}\end{cases}$$ where $m\in\mathbb{N}$ is a hyperparameter which determines the phase of the sinusoidal function (Vaswani et al. choose $m=1000$[23]),
3. and attention is defined by the following formula: $$\texttt{Attention}(Q,K,V)=\texttt{softmax}(\frac{QK^{T}}{\sqrt{d_{K}}})V$$ (2.20) where $Q$ and $K$ are vectors of the same dimension $d_{K}$ called _query_ and _keys_ respectively and $V$ is a vector called _values_.

Note that the positional encoding is needed since otherwise the network would have no information about the position of words in a sentence. Using these sinusoidal encodings turns absolute into relative position [23]. Comparing this definition 2.20 of attention with the one used by Bahdanau et al. [1], we note that in Equations 2.17 and 2.18 the hidden states $\vec{h}$ and $\vec{s}$ play the role of keys $K$ and queries $Q$ respectively, and the values $V$ are again taken to be encoder hidden states $\vec{h}$. The main difference is that instead of a deep neural network (denoted $a$ above) the queries and keys are pre-processed with _linear_ operations ($W_{K}$, $W_{Q}$ and $W_{V}$ above). This architecture is the basis of BERT [17] and its extensions such as GPT-3 which use billions of parameters to achieve state of the art results in a wide range of NLP tasks.

Reasoning about what happens inside these models and explaining their behaviour with linguistic analysis is hard. Indeed, the same architectures where sentences are replaced by images and words by parts of that image give surprisingly accurate results in the image recognition task [18], suggesting that linguistic principles are insufficient for analysing these algorithms. However, viewing deep neural networks as end-to-end black-box learners, it becomes interesting to open the box and analyse the output of the intermediate layers with the aim of understanding the different features that the network learns in the process. Along these lines, researchers have found that neural network models automatically encode linguistic features such as grammaticality [17] and dependency parsing [1]. One possible line of future research would be to study what happens in the linear world of keys, values and queries. One may take the latest forms of attention [23] as the realisation that accurate predictions can be obtained from a linear process $fracQK^{T}\sqrt{d_{K}}$ by using a single softmax activation. We will give a bayesian interpretation of this activation function in Chapter 3.

 

#### Neural networks in DisCoPy

We now show how to interface DisCoPy with Tensorflow/Keras neural networks [14, 15]. In order to do this, we need to define objects, identities, composition and tensor for Keras models.

The objects of our category of neural networks will be instances of PRO, a subclass of monoidal.Ty initialised by a dimension n. A morphism from PRO(n) to PRO(k) is a neural network with input shape (n, ) and output shape (k, ) (we only deal with flat shapes for simplicity). A neural.Network is initialised by providing domain and codomain dimensions together with a Keras model of that type. Composition is easily implemented using the call method of Keras models. For tensor, we first need to split the domain using keras.layers.Lambda, then we act on each subspace independently with self and other, and finally we concatenate the outputs. Identities are simply Keras models with outputs = inputs, and we include a static method for constructing dense layer models.

**Listing 2.3.7**.: The category of Keras models

``` fromdiscopyimportmonoidal,PRO importtensorflowastf fromtensorflowimportkeras classNetwork(monoidal.Box): def__init__(self,dom,cod,model): self.model=model super()__init__("Network",dom,cod) defthen(self,other): inputs=keras.Input(shape=(len(self.dom),)) output=self.model(inputs) output=other.model(output) composition=keras.Model(inputs=inputs,outputs=output) returnNetwork(self.dom,other.cod,composition) deftensor(self,other): dom=len(self.dom)+len(other.dom) cod=len(self.cod)+len(other.cod) inputs=keras.Input(shape=(dom,)) model1=keras.layers.Lambda( lambdax:x[:,len(self.dom)],)(inputs) model2=keras.layers.Lambda( lambdax:x[:,len(self.dom):],)(inputs) model1=self.model(model1) model2=other.model(model2) outputs=keras.layers.Concatenate()([model1,model2]) model=keras.Model(inputs=inputs,outputs=outputs) returnNetwork(PRO(dom),PRO(cod),model)

``` @staticmethod defid(dim): inputs=keras.Input(shape=(len(dim),)) returnNetwork(dim,dim,keras.Model(inputs=inputs,outputs=inputs))

## Chapter 2 Functors for Semantics

### 2.1 Introduction

The _Functors_ are the most important tools for the development of the theory. The _Functors_ are the most important tools for the development of the theory.



### 2.4 Relational models

The formal study of _relations_ was initiated by De Morgan in the mid 19th century [4]. It was greatly developed by Peirce who only published small fragments of his _calculus of relations_[12], although much of it was popularised in the influential work of Schroder [13]. In the first half of the twentieth century, this calculus was often disregarded in favour of Frege's and Russell's approach to logic [1], until it was revived by Tarski [14] who developed it into the rich field of model theory.

With the advent of computer science, the calculus of relations came to be recognized as a convenient framework for storing and accessing data, leading to the development of _relational databases_ in the 1970s [15]. SQL queries were introduced by Chamberlin and Boyce in 1976 [1] and they are still used for accessing databases today. _Conjunctive queries_ are an important subclass of SQL, corresponding to the Select-Where-From fragment. They were introduced by Chandra and Merlin [1] who showed that their evaluation in a relational database is an NP-complete problem, spawning a large field of studies in the complexity of constraint satisfaction problems [10]. The blend of algebra and logic offered by the theory of relations is particularly suited to a categorical formalisation and it has motivated the work of Carboni and Walters [11] as well as Brady and Trimble [2] and Bonchi et al. [12, 13] among others.

In this section, we start by reviewing the theory of relational databases and conjunctive queries from a categorical perspective. We then introduce relational models by transposing the definitions into a linguistic setting. This allows us to transfer results from database theory to linguistics and define $\mathtt{NP-complete}$_entailment_ and _question answering_ problems. The correspondence of terminology between databases, category theory and linguistics is summarized in the table below.

\begin{tabular}{|c|c|c|} \hline Databases & Algebra & Linguities \\ \hline Relational database & Cartesian bicategory & Relational model \\ \hline attributes & objects & basic types \\ schema & signature & lexicon \\ query & morphism & sentence \\ instance & functor & model \\ containment & preorder enrichment & entailment \\ \hline \end{tabular}

#### Databases and queries

We introduce the basic notions of relational databases, starting with an example.

\begin{tabular}{|c|c|c|} \hline _reader_ & _book_ & _writer_ \\ \hline _Spinoza_ & _De Causa_ & _Bruno_ \\ _Shakespeare_ & _World of Wordes_ & _Florio_ \\ _Florio_ & _De Causa_ & _Bruno_ \\ _Leibniz_ & _Tractatus_ & _Spinoza_ \\ \hline \end{tabular}

_Consider the structure of the table above, which we denote by $\rho$. There is a set of_ attributes $A=\{\,\text{reader},\text{book},\text{writer}\,\}$ _which name the columns of the table and a set of data values_ $D_{a}$ _for each attribute_ $a\in A$_,_

$$D_{r}=D_{w}=\{\text{Spinoza, Shakespeare, Leibniz, Bruno, Florio}\}$$

$$D_{b}=\{\text{De Causa},\text{World of Wordes},\text{Tractatus}\}$$

_A row of the table is a tuple $t\in\prod_{a\in A}D_{a}$, which assigns a particular value $t_{a}$ to each attribute $a\in A$, e.g. $($Leibniz, Tractatus, Spinoza$)$. The table then consists in a set of tuples, i.e. a relation $\rho\subseteq\prod_{a\in A}D_{a}$._

A relational database is a collection of tables (relations), organised by a _schema_. Given a set of attributes $A$, a schema $\Sigma$ is a set of relational symbols, together with a domain function $\texttt{dom}:\Sigma\to A^{*}$. The schema serves to specify the set of names $\Sigma$ for the tables in a database together with the type of their columns. For example we may have $\rho\in\Sigma$ for the table above with $\texttt{dom}(\rho)=(\text{reader},\text{book},\text{writer})$. We have already encountered this type of structure in 1.6.1, where we used the term _hypergraph signature_ instead of schema.

**Definition 2.4.2**.: _A relational database $K$ with schema $\Sigma$ is an assignment of each attribute $a\in A$ to a corresponding set of data values $D_{a}$, and an assignment of each symbol $R\in\Sigma$ to a relation $K(R)\subseteq\prod_{a\in\texttt{dom}(R)}D_{a}$._

Instead of working directly with relational databases, it is often convenient to work with a simpler notion known as a _relational structure_. The schema is replaced by a _relational signature_, which is a set of symbols $\Sigma$ equipped with an _arity_ function $\texttt{ar}:\Sigma\rightarrow\mathbb{N}$.

**Definition 2.4.3** (Relational structure).: _A relational structure $K$ over a signature $\Sigma$, also called a $\Sigma$-structure, is given by a set $U$ called the universe and an interpretation $K(R)\subseteq U^{\texttt{ar}(R)}$ for every symbol $R\in\Sigma$. We denote by $\mathcal{M}_{\Sigma}$ the set of $\Sigma$-structures with finite universe $U(K)$._

_Given two $\Sigma$-structures $K,K^{\prime}$, a homomorphism $f:K\to K^{\prime}$ is a function $f:U(K)\to U(K^{\prime})$ such that $\forall\ R\in\Sigma\ \ \forall\ \vec{x}\in U^{\texttt{ar}(R)}\ \cdot\ \vec{x}\in K(R)\implies f(\vec{x})\in K ^{\prime}(R)$._

**Remark 2.4.4**.: _Note that relational structures are the same as relational databases with only one attribute. Attributes $a\in A$ can be recovered by encoding them as predicates $a\in\Sigma$ of arity $1$ and one may take the universe to be the union of the sets of data values $U=\cup_{a\in A}D_{a}$._

We consider the problem of finding a homomorphism between relational structures.

**Definition 2.4.5**.: Homomorphism__

_Input:_ $K,K^{\prime}\in\mathcal{M}_{\Sigma}$__

_Output:_ $f:K\to K^{\prime}$__

**Proposition 2.4.6**.: _[_GJ90_]_Homomorphism _is $\texttt{NP}-\texttt{complete}$._ Proof.: Membership may be shown to follow from Fagin's theorem: homomorphisms are defined by an existential second-order logic formula. Hardness follows by reduction from graph homomorphism: take $\Sigma=\{\,\bullet\,\}$ and $\mathtt{ar}(\bullet)=2$ then a $\Sigma$-structure is a graph. 

The most prominent query language for relational databases is SQL [3]. _Conjunctive queries_ form a subset of SQL (corresponding to the Select-Where-From fragment) with a convenient mathematical formulation. We define conjunctive queries and the corresponding Evaluation and Containment problems. Let $\mathcal{X}$ be a (countable) set of variables, $\Sigma$ a relational signature and consider the logical formulae generated by the following context-free grammar:

$$\varphi\ \::=\ \top\ \mid\ x=x^{\prime}\ \mid\ \varphi\land\varphi\ \mid\ \exists\ x\cdot\varphi\ \mid\ R(\vec{x})$$

where $x,x^{\prime}\in\mathcal{X}$, $R\in\Sigma$ and $\vec{x}\in\mathcal{X}^{\mathtt{ar}(R)}$. Let us denote the variables of $\varphi$ by $\mathtt{var}(\varphi)\subseteq\mathcal{X}$, its free variables by $\mathtt{fv}(\varphi)\subseteq\mathtt{var}(\varphi)$ and its atomic formulae by $\mathtt{atoms}(\varphi)\subseteq\coprod_{R\in\Sigma}\mathtt{var}(\varphi)^{ \mathtt{ar}(R)}$, i.e. an atomic formula is given by $R(x_{1},\ldots,x_{\mathtt{ar}(R)})$ for some variables $x_{i}\in\mathcal{X}$.

This fragment is called _regular logic_ in the category-theory literature [11]. It yields conjunctive queries via the _prenex normal form_.

**Definition 2.4.7**.: _Conjunctive queries $\varphi\in\mathcal{Q}_{\Sigma}$ are the prenex normal form $\varphi=\exists\ x_{0}\cdots\exists\ x_{k}\cdot\varphi^{\prime}$ of regular logic formulae, for the bound variables $\{\,x_{0},\ldots,x_{k}\,\}=\mathtt{var}(\varphi)\setminus\mathtt{fv}(\varphi)$ and $\varphi^{\prime}=\bigwedge\mathtt{atoms}(\varphi)$. We denote by :_

$$\mathcal{Q}_{\Sigma}(k)=\{\varphi\in\mathcal{Q}_{\Sigma}\,|\,\mathtt{fv}( \varphi)=k\}$$

_the set of conjunctive queries with $k$ free variables._

Given a structure $K\in\mathcal{M}_{\Sigma}$, let $\mathtt{eval}(\varphi,K)=\{\,v\in U(K)^{\mathtt{fv}(\varphi)}\,\mid\,(K,v) \vDash\varphi\,\}$ where the satisfaction relation ($\vDash$) is defined in the usual way.

**Definition 2.4.8**.: Evaluation__

_Input:_ $\varphi\in\mathcal{Q}_{\Sigma},\quad K\in\mathcal{M}_{\Sigma}$__

_Output:_ $\mathtt{eval}(\varphi,K)\subseteq U(K)^{\mathtt{fv}(\varphi)}$__

**Definition 2.4.9**.: Containment__

_Input:_ $\varphi,\varphi^{\prime}\in\mathcal{Q}_{\Sigma}$__

_Output:_ $\varphi\subseteq\varphi^{\prime}\ \equiv\ \forall\ K\in\mathcal{M}_{\Sigma}\ \cdot\ \mathtt{eval}(\varphi,K)\subseteq\mathtt{eval}(\varphi^{\prime},K)$__

**Example 2.4.10**.: _Following from 2.4.1 let $U:=D_{w}\cup D_{b}$ and fix the schema $\Sigma=\{\text{read, wrote}\}\cup U$ with $\mathtt{ar}(w)=1$ for $w\in U$ and $\mathtt{ar}(\text{read})=\mathtt{ar}(\text{wrote})=2$. Consider the relational structure $K\in\mathcal{Q}_{\Sigma}$ with universe $U$ and $K(w)=\{\,w\,\}\subseteq U$ for $w\in\Sigma-\{\,\text{read, wrote}\,\}$ and $K(\text{read})\subseteq U\times U$ given by the first two columns of table $\rho$, $K(\text{wrote})\subseteq U\times U$ given by the second two columns of $\rho$. The following is a conjunctive query with no free variables:_

$$\varphi=\exists y,z\,\cdot\,\text{read}(x,y)\wedge\text{Bruno}(y)\wedge\text{ wrote}(x,z)$$ _Since $\varphi$ has one free variables, $\mathtt{eval}(\varphi,K)\subseteq U$. With $K$ as defined above there are three valuations $v:\mathtt{var}(\varphi)=\{\,x,y,z\,\}\to U$ such that $(v,K)\vDash\varphi$, yielding $\mathtt{eval}(\varphi,K)=\{\,\text{\it Spinoza},\,\text{\it Florio},\,\text{\it Galileo }\,\}\subseteq U$._

**Definition 2.4.11** (Canonical structure).: _Given a query $\varphi\in\mathcal{Q}_{\Sigma}$, the canonical structure $CM(\varphi)\in\mathcal{M}_{\Sigma}$ is given by $U(CM(\varphi))=\mathtt{var}(\varphi)$ and $CM(\varphi)(R)=\{\,\vec{x}\in\mathtt{var}(\varphi)^{\mathtt{ar}(R)}\,\mid\,R( \vec{x})\in\mathtt{atoms}\,\,\text{for}\,\,R\in\Sigma$._

This result was used by Chandra and Merlin to reduce from Homomorphism to both Evaluation and Containment.

**Theorem 2.4.12** (Chandra-Merlin [21]).: _The problems Evaluation and Containment are logspace equivalent to Homomorphism, hence $\mathtt{NP-complete}$._

Proof.: Given a query $\varphi\in\mathcal{Q}_{\Sigma}$ and a structure $K\in\mathcal{M}_{\Sigma}$, query evaluation $\mathtt{eval}(\varphi,K)$ is given by the set of homomorphisms $CM(\varphi)\to K$. Given $\varphi,\varphi^{\prime}\in\mathcal{M}_{\Sigma}$, we have $\varphi\subseteq\varphi^{\prime}$ iff there is a homomorphism $f:CM(\varphi)\to CM(\varphi^{\prime})$ such that $f(\mathtt{fv}(\varphi))=\mathtt{fv}(\varphi^{\prime})$. Given a structure $K\in\mathcal{M}_{\Sigma}$, we construct $\varphi\in\mathcal{Q}_{\Sigma}$ with $\mathtt{fv}(\varphi)=\varnothing$, $\mathtt{var}(\varphi)=U(K)$ and $\mathtt{atoms}(\varphi)=K$. 

#### The category of relations

Let us now consider the structure of the category of relations. A relation $R:A\to B$ is a subset $R\subseteq A\times B$ or equivalently a predicate $R:A\times B\to\mathbb{B}$, we write $aRb$ for the logical statement $R(a,b)=1$. Given $S:B\to C$, the composition $R;S:A\to C$ is defined as follows:

$$aR;Sc\iff\exists b\in B\cdot aRb\wedge bSc\,.$$

Under this composition relations form a category denoted $\mathbf{Rel}$.

We can also construct the category of relations by considering the powerset monad $\mathcal{P}:\mathbf{Set}\to\mathbf{Set}$ defined on objects by $\mathcal{P}(X)=\{\,S\subseteq X\,\}$ and on arrows by $f:X\to Y$ by $\mathcal{P}(f):\mathcal{P}(X)\to\mathcal{P}(Y):S\mapsto f(S)$. A relation $R:A\to B$ is the same as a function $R:A\to\mathcal{P}(B)$ and in fact $\mathbf{Rel}=\mathbf{Kl}(\mathcal{P})$ is the Kleisli category of the powerset monad.

Any function $f:A\to B$ induces a relation $I(f)=\{\,(x,f(x))\,\mid\,x\in A\,\}\subseteq A\times B$, sometimes called the graph of $f$. The tensor product of relations $R:A\to B$ and $T:C\to D$ is denoted $R\otimes T:A\times C\to B\times D$ and defined by:

$$(a,c)R\otimes T(b,d)\iff aRb\wedge cTd\,.$$

Equipped with this tensor product and unit the one-element set $1$, $\mathbf{Rel}$ forms a symmetric monoidal category, with symmetry lifted from $\mathbf{Set}$. We can thus use the graphical language of monoidal categories for reasoning with relations.

Note that each object $A\in\mathbf{Rel}$ is self-dual, as witnessed by the morphisms $\mathtt{cup}_{A}:A\times A\to 1$ and $\mathtt{cap}_{A}:1\to A\times A$, defined by:

$$(a,a^{\prime})\mathtt{cup}_{A}\iff(a=a^{\prime})\iff\mathtt{cap}_{A}(a,a^{ \prime})$$ These denoted graphically as cups and caps and satisfy the snake equations 1.18. Thus $\mathbf{Rel}$ is a compact-closed category. Moreover, every object $A\in\mathbf{Rel}$ comes equipped with morphisms $\Delta:A\to A\times A$ and $\nabla:A\times A\to A$ defined by:

$$a\Delta(a^{\prime},a^{\prime\prime})\ \iff\ (a=a^{\prime}=a^{\prime\prime})\ \iff\ (a,a^{\prime})\nabla a^{\prime\prime}\,.$$

Together with the unit $\eta:1\to A$ and the counit $\epsilon:A\to 1$, defined by $\eta=A=\epsilon$, the tuple $(\Delta,\epsilon,\nabla,\eta)$ satisfies the axioms of special commutative frobenius algebras, making $\mathbf{Rel}$ a hypergraph category in the sense of Fong and Spivak [14]. Note that $\mathtt{cup}=\nabla;\epsilon$ and $\mathtt{cap}=\eta;\Delta$, moreover it is easy to show that the snake equations follow from the axioms of special commutative Frobenius algebras. Finally, we can equip the hom-sets $\mathbf{Rel}(A,B)$ with a preorder structure given by:

$$R\leq S\iff\left(aRb\implies aSb\right).$$

In category theory, this situation is known as a _preorder enrichment_. Equipped with this preorder enrichment, $\mathbf{Rel}$ forms a _Cartesian bicategory_ in the sense of Carboni and Walters [13].

#### Graphical conjunctive queries

Bonchi, Seeber and Sobocinski [15] introduced graphical conjunctive queries (GCQ), a graphical calculus where query evaluation and containment are captured by the axioms of the _free Cartesian bicategory_$\mathbf{CB}(\Sigma)$ generated by a relational signature $\Sigma$. Cartesian bicategories were introduced by Carboni and Walters [13] as an axiomatisation of categories of relations, they are hypergraph categories where every hom-set has a partial order structure akin to subset inclusion between relations. We review the correspondence of Bonchi et al. [15], between conjunctive queries and morphisms of free cartesian bicategories. We refer to Appendix 2.4.1 for an introduction to relational datatabases with examples.

**Definition 2.4.13** (Cartesian bicategory).: _[_13_]_ _A cartesian bicategory $\mathbf{C}$ is a hypergraph category enriched in preorders and where the preorder structure interacts with the hypergraph structure as follows:_

(2.21)

_for all objects $a,b\in\mathbf{C}_{0}$ and morphisms $R:a\to b$. A morphism of Cartesian bicategories is a strong monoidal functor which preserves the partial order, the monoid and the comonoid structure._ We recall the basic notions of relational databases and conjunctive queries. A _relational signature_ is a set of symbols $\Sigma$ equipped with an _arity_ function $\mathtt{ar}:\Sigma\to\mathbb{N}$. This is used to define a relational structure as a mathematical abstraction of a databases.

**Definition 2.4.14** (Relational structure).: _A relational structure $K$ over a signature $\Sigma$, also called a $\Sigma$-structure, is given by a set $U$ called the universe and an interpretation $K(R)\subseteq U^{\mathtt{ar}(R)}$ for every symbol $R\in\Sigma$. We denote by $\mathcal{M}_{\Sigma}$ the set of $\Sigma$-structures with finite universe $U(K)$._

_Given two $\Sigma$-structures $K,K^{\prime}$, a homomorphism $f:K\to K^{\prime}$ is a function $f:U(K)\to U(K^{\prime})$ such that $\forall\ R\in\Sigma\ \ \forall\ \vec{x}\in U^{\mathtt{ar}(R)}\ \ .\ \ \vec{x}\in K(R)\implies f(\vec{x})\in K^{\prime}(R)$._

Let $\mathcal{X}$ be a (countable) set of variables, $\Sigma$ a relational signature and consider the logical formulae generated by the following context-free grammar:

$$\varphi\ \ ::=\ \top\ |\ \ x=x^{\prime}\ \ |\ \ \varphi\wedge\varphi\ \ |\ \exists\ x\cdot\varphi\ \ |\ R(\vec{x})$$

where $x,x^{\prime}\in\mathcal{X}$, $R\in\Sigma$ and $\vec{x}\in\mathcal{X}^{\mathtt{ar}(R)}$. Let us denote the variables of $\varphi$ by $\mathtt{var}(\varphi)\subseteq\mathcal{X}$, its free variables by $\mathtt{fv}(\varphi)\subseteq\mathtt{var}(\varphi)$ and its atomic formulae by $\mathtt{atoms}(\varphi)\subseteq\coprod_{R\in\Sigma}\mathtt{var}(\varphi)^{ \mathtt{ar}(R)}$, i.e. an atomic formula is given by $R(x_{1},\ldots,x_{\mathtt{ar}(R)})$ for some variables $x_{i}\in\mathcal{X}$. This fragment is called _regular logic_ in the category-theory literature [10]. It yields conjunctive queries via the _prenex normal form_.

**Definition 2.4.15**.: _Conjunctive queries $\varphi\in\mathcal{Q}_{\Sigma}$ are the prenex normal form $\varphi=\exists\ x_{0}\cdots\exists\ x_{k}\cdot\varphi^{\prime}$ of regular logic formulae, for the bound variables $\{\,x_{0},\ldots,x_{k}\,\}=\mathtt{var}(\varphi)\setminus\mathtt{fv}(\varphi)$ and $\varphi^{\prime}=\bigwedge\mathtt{atoms}(\varphi)$. We denote by :_

$$\mathcal{Q}_{\Sigma}(k)=\{\varphi\in\mathcal{Q}_{\Sigma}\,|\,\mathtt{fv}( \varphi)=k\}$$

_the set of conjunctive queries with $k$ free variables._

**Proposition 2.4.16**.: _There is a bijective correspondence between relational structures with signature $\sigma:\Sigma\to\mathbb{N}=\{\,x\,\}^{*}$ and monoidal functors $K:\Sigma\to\mathbf{Rel}$ such that $K(x)=U$._

Proof.: Given a schema $\mathtt{dom}:\Sigma\to A^{*}$, the data for a monoidal functor $K:\Sigma\to\mathbf{Rel}$ is an assignment of each $a\in A$ to a set of data-values $D_{a}=K(a)$ and of each symbol $R\in\Sigma$ to a relation $K(R)\subseteq\coprod_{a\in\mathtt{dom}(R)}D_{a}$. This is precisely the data of a relational database. Relational structures are a sub-example with $A=\{\,x\,\}$. 

Bonchi, Seeber and Sobocinski show that queries can be represented as diagrams in the free cartesian bicategory, and that this translation is semantics preserving. Let $\mathbf{CB}(\Sigma)$ be the free Cartesian bicategory generated by one object $x$ and arrows $\{\,R:1\to x^{\mathtt{ar}}(R)\,\}_{R\in\Sigma}$, see [11, def. 21].

**Proposition 2.4.17**.: _([11, prop. 9, 10]) There is a two-way translation between formulas and diagrams:_

$$\Theta:\mathcal{Q}_{\Sigma}\leftrightarrows\mathbf{CB}(\Sigma):\Lambda$$

_which Proof.: The translation is defined by induction from the syntax of regular logic formulae to that of GCQ diagrams and back. Note that given $\varphi\in\mathcal{Q}_{\Sigma}$ with $|\mathtt{fv}(\varphi)|=n$, we have $\Theta(\varphi)\in\mathbf{CB}(\Sigma)(0,n)$ and similarly we have $\mathtt{fv}(\Lambda(d))=m+n$ for $d\in\mathbf{CB}(\Sigma)(m,n)$, i.e. open wires correspond to free variables. 

**Example 2.4.18**.: _The translation works as follows. Given a morphism in $\mathbf{CB}(\Sigma)$, normalized according to 1.6.5, the spiders are interpreted as variables and the boxes as relational symbols. For example, assuming $A,B,C\in\Sigma$, the following morphism $f:x\to x\in\mathbf{CB}(\Sigma)$_

_is mapped to the query:_

$$\Lambda(f)=\exists x_{1},x_{2}\,\cdot\,A(x_{0},x_{1})\wedge B(x_{0},x_{1},x_{2 })\wedge C(x_{1},x_{3})$$

_The query from Example 2.4.10, is mapped by $\Theta$ to the diagram:_

**Proposition 2.4.19**.: _Let $[\mathbf{CB}(\Sigma),\mathbf{Rel}]$ denote the set of morphisms of Cartesian bicategories, there are bijective correspondences between closed diagrams in $\mathbf{CB}(\Sigma)$, formulas in $\mathcal{Q}_{\Sigma}$ with no free variables and models with signature $\Sigma$._

$$\mathbf{CB}(\Sigma)(0,0)\ \stackrel{{(1)}}{{\simeq}}\ \{\,\varphi\in \mathcal{Q}_{\Sigma}\ |\ \mathtt{fv}(\varphi)=\varnothing\,\}\ \stackrel{{(2)}}{{\simeq}}\ \mathcal{M}_{\Sigma}\ \stackrel{{(3)}}{{\simeq}}\ [\mathbf{CB}(\Sigma), \mathbf{Rel}]$$

Proof.: (1) follows from theorem 2.4.17, (2) from theorem 2.4.12 and (3) follows from proposition 2.4.16 since any monoidal functor $\Sigma\to\mathbf{Rel}$ induces a morphism of Cartesian bicategories $\mathbf{CB}(\Sigma)\to\mathbf{Rel}$. 

#### Relational models

We have seen that relational databases are functors $K:\Sigma\to\mathbf{Rel}$ from a relational signature $\Sigma$. It is natural to to generalise this notion by considering functors $G\to\mathbf{Rel}$ where $G$ is a formal grammar. Any of the formal grammars studied in Chapter 1 may be used to build a relational model. However, it is natural to pick a grammar $G$ that we can easily interpret in $\mathbf{Rel}$. In other words, we are interested in grammars which have common structure and properties with the category of relations. Recall that $\mathbf{Rel}$ is compact-closed with the diagonal and its transpose as cups and caps. This makes rigid grammars particularly suited for relational semantics, since we can interpret cups and caps using the compact closed structure of $\mathbf{Rel}$.

 

**Definition 2.4.20** (Relational model).: _A relational model is a rigid monoidal functor $F:G\to\mathbf{Rel}$ where $G$ is a rigid grammar._

We illustrate relational models with an example.

**Example 2.4.21** (Truth values).: _Let us fix the vocabulary $V=U+\{\,\text{read, wrote}\,\}$, where $U=D_{w}\cup D_{b}\cup D_{r}$ is the set of data values from Example 2.4.1. Consider the pregroup grammar defined by the following lexicon:_

$$\Delta(x)=\{\,n\,\}\ ,\quad\Delta(\text{read})=\Delta(\text{wrote})=\{\,n^{r}sn ^{l}\,\}$$

_for all $x\in U\subseteq V$. We build a functor $F:\Delta\to\mathbf{Rel}$, defined on objects by $F(n)=U$, and $F(w)=1=F(s)$ for all $w\in V$, on proper nouns by $F(x\to n)=\{\,x\,\}\subseteq U$ for $x\in U\subseteq V$ and on verbs as follows:_

_read_

_where $\rho:1\to U\otimes U\otimes U\in\mathbf{Rel}$ is the table (relation) from Example 2.4.1. Interpreting cups and caps in $\mathbf{RC}(\Delta)$ with their counterparts in $\mathbf{Rel}$, we can evaluate the semantics of the sentence $g:\text{Spinoza}$ read Bruno $\to s$:_

_spinoza_

_read_

_Bruno_

_spinoza_

_spinoza_
_Let $F(q)=U$ and $F(\mathit{Who}\to q\,s^{l}\,n)=\mathtt{cap}_{U}\subseteq U\otimes U$. Then evaluating the question above in $F$ yields $F(g_{q})=\{\,\mathit{\text{Spinoza, Florio}}\,\}\subseteq U$._

As shown by Sadrzadeh et al. [15], we may give semantics to the relative pronoun "that" using the Frobenius algebra in **Rel**.

**Example 2.4.23** (Relative pronouns).: _Add the following lexical entries:_

$$\Delta(\mathit{that})=\{\,n^{r}\,n\,s^{l}\,n^{l},n^{r}\,n\,s^{l}\,n\,\}\ ,\quad \Delta(\mathit{a})=\{\,d\,\}\ ,\quad\Delta(\mathit{book})=\{\,d^{r}n\,\}\ .$$

_. Then there is a grammatical question $g^{\prime}_{q}:$ Who read a book that Bruno wrote $\to$$q$ in $\mathbf{RC}(\Delta)$ given by the following diagram:_

_Let $F(d)=1$, $F(\mathit{a}\to d)=\top$, $F(\mathit{that}\to n^{r}\,n\,s^{l}\,n)=\nu\cdot\delta\cdot(\delta\otimes \mathtt{id}_{U}):1\to U^{3}$ (the spider with 3 outputs and 0 inputs) and $F(\mathit{book}\to d^{r}\,n)=D_{b}\subseteq U$. Then evaluating the question above in $F$ yields $F(g^{\prime}_{q})=\{\,\mathit{\text{Spinoza, Florio, Galileo}}\,\}\subseteq U$, as expected._

The first linguistic problem that we consider is the task of computing the semantics of a sentence $u\in\mathcal{L}(G)$ for a pregroup grammar $G$ in a given relational model $F:G\to\mathbf{Rel}$. Throughout this section and the next, we assume that $G$ is a rigid grammar.

**Definition 2.4.24**.: $\mathtt{RelSemantics}(G)$__

_Input:_ $g\in\mathbf{RC}(G)(u,s)$_,_ $F:G\to\mathbf{Rel}$__

_Output:_ $F(g)$__

Since $\mathbf{Rel}$ is a cartesian bicategory, any monoidal functor from $G$ to $\mathbf{Rel}$ must factor through a free cartesian bicategory.

**Lemma 2.4.25**.: _Let $G=(V,B,\Delta,s)$ be a pregroup grammar. Any relational model $F:\mathbf{RC}(G)\to\mathbf{Rel}$ factors through a free cartesian bicategory $\mathbf{RC}(G)\to\mathbf{CB}(\Sigma)\to\mathbf{Rel}$, where $\Sigma$ is obtained from $\Delta$ via the map $P(B)\to B^{*}$ which forgets the adjoint structure._

Proof.: This follows from the universal property of the free cartesian bicategory. 

This lemma allows to reduce the problem of computing the semantics of sentences in $\mathbf{Rel}$ to $\mathtt{Evaluation}$, thus proving its membership in $\mathtt{NP}$.

**Proposition 2.4.26**.: _There is a logspace reduction from $\mathtt{RelSemantics}(G)$ to conjunctive query $\mathtt{Evaluation}$, hence $\mathtt{RelSemantics}\in\mathtt{NP}$._ Proof.: The factorisation $K\circ L=F$ of lemma 2.4.25 and the translation $\Lambda$ of theorem 2.4.17 are in logspace, they give a query $\varphi=\Lambda(L(r))\in\mathcal{Q}_{\Delta}$ such that $\mathtt{eval}(\varphi,K)=F(r)$. 

The queries that arise from a pregroup grammar are a particular subclass of conjunctive queries. This leads to the question: what is the complexity of Evaluation for this class of conjunctive queries? We conjecture that these queries have bounded treewidth, i.e. that they satisfy the tractability condition for the CSP dichotomy theorem [10].

**Conjecture 2.4.27**.: _For any pregroup grammar $G$, $\mathtt{RelSemantics}(G)$ is poly-time computable in the size of $(u,s)\in List(V)\times P(B)$ and in the size of the functor $F$._

#### Entailment and question answering

We have seen that relational models induce functors $L:G\to\mathbf{CB}(\Sigma)$, turning sentences into conjunctive queries. Thus we can test whether a sentence $u\in\mathcal{L}(G)$ entails a second sentence $u^{\prime}\in\mathcal{L}(G)$ by checking containment of the corresponding queries. More generally, we may consider models in a _finitely presented_ cartesian bicategory $\mathbf{C}$, i.e. a cartesian bicategory equipped with a finite set of _existential rules_ of the form $\forall\ x_{0}\ \cdots\ \forall\ x_{k}\ \cdot\ \varphi\to\varphi^{\prime}$ for $\varphi,\varphi^{\prime}\in\mathbf{CB}(\Sigma)$ with $\mathtt{fv}(\varphi)=\mathtt{fv}(\varphi^{\prime})=\{\,x_{0},\ldots,x_{k}\,\}$. These are also called tuple-generating dependencies in database theory [14]. They will allow us to model more interesting forms of entailment in natural language.

**Definition 2.4.28** (CB model).: _A CB model for a rigid grammar $G$ is a monoidal functor $L:G\to\mathbf{C}$ where $\mathbf{C}$ is a finitely presented Cartesian bicategory._

**Example 2.4.29**.: _Take $\mathbf{C}$ to be the Cartesian bicategory generated by the signature $\Sigma=\{\,\text{Leib}$, Spi, infl, calc, phi, ...$\}$ as 1-arrows with codomain given by the function $\mathtt{ar}:\Sigma\to\mathbb{N}$ and the following set of 2-arrows:_

$$\begin{array}{|c _Starting from the pregroup grammar $G$ defined in 2.4.4, and adding the following lexical entries:_

$$\Delta(\text{influenced})=\Delta(\text{discovered})=\set{n^{r}sn^{l}},\Delta( \text{calculus})=\set{n},\Delta(\text{philosopher})=\set{d^{r}n}.$$

_We may construct a functor $L:G\to\mathbf{CB}(\Sigma)$ given on objects by $L(w)=L(s)=1$ and $L(n)=x$, and on arrows by sending every lexical entry to the corresponding symbol in $\Sigma$ except for the question word "who" which is interpreted as a cap and the functional word "that" which is interpreted as a spider with three outputs. Then one may check that the image of the sentence "Spinoza influenced a philosopher that discovered calculus" is grammatical in $G$ and that the corresponding pregroup reduction is mapped via $L$ to the last diagram in the derivation above._

**Definition 2.4.30**.: Entailment__

_Input:_ $r\in\mathbf{RC}(G)(u,s),\quad r^{\prime}\in\mathbf{RC}(G)(u^{\prime},s),\quad L :\mathbf{RC}(G)\to\mathbf{C}$__

_Output:_ $L(r)\leq L(r^{\prime})$__

**Proposition 2.4.31**.: Entailment _is undecidable for finitely presented Cartesian bicategories. When $\mathbf{C}$ is freely generated (i.e. it has no existential rules), the problem reduces to conjunctive query_ Containment_._

Proof.: Entailment of conjunctive queries under existential rules is undecidable, see [1]. When $\mathbf{C}=\mathbf{CB}(\Sigma)$ is freely generated by a relational signature $\Sigma$, i.e. with no existential rules, theorem 2.4.17 yields a logspace reduction to Containment: Entailment$\in\mathbf{NP}$. 

We now consider the following computational problem: given a natural language corpus and a question, does the corpus contain an answer? We show how to translate a corpus into a relational database so that question answering reduces to query evaluation.

In order to translate a corpus into a relational database, it is not sufficient to parse every sentence independently, since the resulting queries will have disjoint sets of variables. The extra data that we need is a _coreference resolution_, which allows to link the common entities mentioned in these sentences. In 1.6.2, we defined a notion of pregroup grammar with coreference $G$ which allows to represent a corpus of $k$ sentences as one big diagram $C\in\mathbf{Coref}(G)$, assuming that both the pregroup parsing and the coreference resolution have been performed. In order to interpret a pregroup grammar with coreference $G=(V,B,\Delta,I,R,s)$ in a cartesian bicategory $\mathbf{C}$, it is sufficient to fix a CB model from the pregroup grammar $(V,B,\Delta,I,s)$ into $\mathbf{C}$ and choose an image for the reference types in $R$. Then the coreference resolution is interpreted using the Frobenius algebra in $\mathbf{C}$.

Fix a pregroup grammar with coreference $G$ and a CB model $L:\mathbf{Coref}(G)\to\mathbf{CB}(\Sigma)$ with $L(s)=0$, i.e. grammatical sentences are mapped to closed formulae. We assume that $L(q)=L(a)$ for $q$ and $a$ the question and answer types respectively, i.e. both are mapped to queries with the same number of free variable. Lexical items such as "influence" and "Leibniz" are mapped to their own symbol in the relational signature $\Sigma$, whereas functional words such as relative pronouns are sent to the Frobenius algebra of $\mathbf{CB}(\Sigma)$, see 2.4.4 or [13].

We describe a procedure for answering a question given a corpus. Suppose we are given a corpus $u\in V^{*}$ with $k$ sentences. Parsing and resolving the coreference yields a morphism $C\in\mathbf{Coref}(G)(u,s^{k})$. Using $L$ we obtain a relational database from $C$ given by the canonical structure induced by the corresponding query $K(C)=CM(L(C))$, we denote by $E:=\mathtt{var}(L(C))$ the universe of this relational structure. Given a parsed question $g:v\to q\in\mathbf{Coref}(G)$, we can answer the question $g$ by evaluating it in the model $K(C)$.

**Definition 2.4.32**.: QuestionAnswering__

_Input:_ $C\in\mathbf{Coref}(G)(u,s^{k}),g\in\mathbf{Coref}(G)(v,q)$

_Output:_ $\mathtt{Evaluation}(K,L(g))\subseteq E^{\mathtt{tr}(L(g))}$ _where $K=CM(L(C))$__

**Proposition 2.4.33**.: QuestionAnswering _is $\mathtt{NP-complete}$._

Proof.: Membership follows immediately by reduction to Evaluation. Hardness follows by reduction from Evaluation. Indeed fix any relational structure $K$ and query $\varphi$, using Proposition 1.6.10, we may build a corpus $C\in\mathbf{Coref}(G)$ and a question $g\in\mathbf{Coref}(G)$ such that $L(C)=K$ and $L(g)=\varphi$. 

Note that this is an asymptotic result. In practice, the questions we may ask are small compared to the size of the corpus. This would make the problem tractable since Evaluation is only $\mathtt{NP}$-complete in the combined size of database and query, but it becomes polytime computable when the query is fixed [11].

 

### 2.5 Tensor network models

Tensors arose in the work of Ricci and Levi-Civita in the end of the 19th century [14]. They were adopted by Einstein [15], who used repeated indices to denote their compositions, and applied to quantum mechanics by Heisenberg [14] to describe the possible states of quantum systems.

In the 1970s, Penrose introduced a diagrammatic notation for manipulating tensor expressions [13]: wires represent vector spaces, nodes represent multi-linear maps between them. This work was one of the main motivations behind Joyal and Street's graphical calculus for monoidal categories [11], which was later adopted in the development of Categorical Quantum Mechanics (CQM) [1]. The same notation is widely used in the Tensor Networks (TN) community [10, 12, 13]. Until recently, CQM and TN remained separated fields because they were interested in different aspects of these graphical networks. On the one hand, rewriting and axiomatics. On the other, fast methods for tensor contraction and complexity theoretic guarantees. These two lines of research are now seeing a fruitful exchange of ideas as category theorists become more applied and vice-versa. For instance, rewriting strategies developed in the context of categorical quantum mechanics can be used to speed-up quantum computations [15], or solve satisfiability and counting problems [16, 17].

The tools and methods developed by these communities are finding many applications in artificial intelligence. Tensor networks are widely used in machine learning, supported by efficient contraction tools such as Google's TensorNetwork library [1], and are beginning to be applied to natural language processing [18, 19]. Distributional Compositional models of meaning [12, 13] (DiscCoCat) arise naturally from Categorical Quantum Mechanics [1, 1], In a nutshell, CQM provides us with graphical calculi to reason about tensor networks, and DisCoCat provides a way of mapping natural language to these calculi so that semantics is computed by tensor contraction.

In this section, we establish a formal connection between tensor networks and functorial models. This allows us to transfer complexity and tractability results from the TN literature to the DisCoCat models of meaning. In particular, we show that DisCoCat models based on dependency grammars can be computed in polynomial time. We end by discussing an extension of these tensor-based models where bubbles are used to represent non-linear operations on tensor networks.

#### Tensor networks

In this section, we review the basic notions of tensor networks. We take as a starting point the definition of tensor networks used in the complexity theory literature on TNs [1, 2].

Let us denote an undirected graph by $(V,E)$ where $V$ is a finite set of vertices and $E\subseteq\{\,\{\,u,v\,\}\,|\,u,v\in V\,\}$ is a set of undirected edges. The incidence set of a vertex $v$ is $I(v)=\{\,e\in E\,|\,v\in e\,\}$ and the degree of $v$ is the number of incident edges $\mathtt{deg}(v)=|I(v)|$. An order $n$ tensor $T$ of shape $(d_{1},\dots,d_{n})$ with $d_{i}\in\mathbb{N}$ is a function$T:[d_{1}]\otimes\cdots\otimes[d_{n}]\to\mathbb{S}$ where $[d_{i}]=\{\,1,\ldots,d_{i}\,\}$ is the ordered set with $d_{i}$ elements and $\mathbb{S}$ is a semiring of numbers (e.g. $\mathbb{B},\mathbb{N},\mathbb{R},\mathbb{C}$), see 2.1.

**Definition 2.5.1** (Tensor network).: _A tensor network $(V,E,T)$ over a semiring $\mathbb{S}$ is a undirected graph $(V,E)$ with edge weights $\mathtt{dim}:E\to\mathbb{N}$ and a set of tensors $T=\{\,T_{v}\,\}_{v\in V}$ such that $T_{v}$ is a tensor of order $\mathtt{deg}(v)$ and shape $(\mathtt{dim}(e_{0}),\ldots,\mathtt{dim}(e_{\mathtt{deg}(v)}))$ for $e_{i}\in I(v)\subseteq E$. Each edge $e\in E$ corresponds to an index $i\in[\mathtt{dim}(e)]$ along which the adjacent tensors are to be contracted._

The contration of two tensors $T_{0}:[m]\otimes[d]\to\mathbb{S}$ and $T_{1}:[d]\otimes[l]\to\mathbb{S}$ along their common dimension $[d]$ is a tensor $T_{0}\cdot T_{1}:[k]\otimes[l]\to\mathbb{S}$ with:

$$T_{0}\cdot T_{1}(i,j)=\sum_{k\in[d]}T_{0}(i,k)T_{1}(k,l)$$

If $T_{0}:[m]\to\mathbb{S}$ and $T_{1}:[l]\to\mathbb{S}$ do not have a shared dimension then we still denote by $T_{0}\cdot T_{1}:[m]\otimes[l]\to\mathbb{S}$, the outer (or tensor) product of $T_{0}$ and $T_{1}$ given by $T_{0}\cdot T_{1}(i,j)=T_{0}(i)T_{1}(j)$. Note that this is sufficient to define the product $T_{0}\cdot T_{1}$ for tensors of arbitary shape since $(d_{0},\ldots,d_{n})$ shaped tensors are in one-to-one correspondence with order $1$ tensors of shape $(d_{0}d_{1}\ldots d_{n})$.

We are interested in the _value_$\mathtt{contract}(V,E,T)$ of a tensor network which is the number in $\mathbb{S}$ obtained by contracting the tensors in $(V,E,T)$ along their shared edges. We may define this by first looking at the order of contractions, called bubbling in [1, 1].

**Definition 2.5.2** (Contraction order).: _[_11_]_ _A contraction order $\pi$ for $(V,E,T)$ is a total order of its vertices, i.e. a bijection $\pi:[n]\to V$ where $n=|V|$._

Given a contraction order $\pi$ for $(V,E,T)$ we get an algorithm for computing the value of $(V,E,T)$, given by $\mathtt{contract}(V,E,T)=A_{n}$ where:

$$A_{0}=1\in\mathbb{S}\qquad A_{i}=A_{i-1}\cdot T_{\pi(i)}$$

One may check that the value $A_{n}$ obtained is independent of the choice of contraction order $\pi$, although the time and space required to compute the value may very well depend on the order of contractions [11]. We can now define the general problem of contracting a tensor network.

**Definition 2.5.3**.: $\mathtt{Contraction}(\mathbb{S})$__

_Input:_ _A tensor network $(V,E,T)$ over $\mathbb{S}$__

_Output:_ $\mathtt{contract}(V,E,T)$__

**Proposition 2.5.4**.: $\mathtt{Contraction}(\mathbb{S})$ _is $\#\mathtt{P}$-complete for $\mathbb{S}=\mathbb{N},\mathbb{R}^{+},\mathbb{R},\mathbb{C}$, it is $\mathtt{NP}$-complete for $\mathbb{S}=\mathbb{B}$._

Proof.: $\#\mathtt{P}$-hardness was proved in [1] by reduction from $\#\mathtt{SAT}$. $\mathtt{NP}$-completeness when $\mathbb{S}=\mathbb{B}$ follows by equivalence with Even though contracting tensor networks is a hard problem in general, it becomes tractable, in several restricted cases of interest.

Let us look a bit more closely at the process of contraction. Recall that given two matrices $M_{0},M_{1}$ the time complexity of matrix multiplication is in general $n^{3}$. This is the simplest instance of a tensor contraction which can be depicted graphically as follows:

The standard way to compute this contraction is with two for loops over the outgoing wires for each basis vector in the middle wire, resulting in the cubic complexity. There are Strassen-like algorithms with a better asymptotic runtime, but we do not consider these here. Now suppose $M_{0}$ and $M_{1}$ are tensors with indices of dimension $n$ connected by one edge, with $k_{0}$ and $k_{1}$ outgoing edges respectively:

Then in order to contract the middle wire, we need $k_{0}+k_{1}$ for loops for each basis vector in the middle wire, resulting in the complexity $n^{k_{0}+k_{1}+1}$. In particular if we have $0$ edges connecting the tensors, i.e. we are taking the outer product, then the time complexity is $O(n^{k_{0}+k_{1}})$. Similarly, if we have $k_{2}$ parallel edges connecting the tensors, the time complexity is $O(n^{k_{0}+k_{1}+k_{2}})$. We can speed up the computation by _slicing_[1], i.e. by parallelizing the computation over $k_{2}\cdot n$ GPUs, where each computes the for loops for a basis vector of the middle wires, reducing the time complexity to $n^{k_{0}+k_{1}}$. This is for instance enabled by Google's Tensor Network library [1].

For a general tensor network $(V,E,T)$, we have seen that the contraction strategy can be represented by a contraction order $\pi:[|V|]\to V$, this may be viewed as a _bubbling_ on the graph $(V,E)$:

At each contraction step $i$, we are contracting the tensor $A_{i-1}$ enclosed by the bubble with $T_{\pi(i)}$. From the considerations above we know that the time complexity will depend on the number of edges crossing the bubble at each time step. For instance in the bubbling above, there are at most $3$ edges crossing a bubble at each time step, We can capture this complexity using the notion of _bubblewidth_[1], also known as the cutwidth [1], of a tensor network.

**Definition 2.5.5** (Bubblewidth).: _The bubblewidth of a contraction order $\pi:[n]\to V$ for a graph $(V,E)$ is given by:_

$$\mathtt{bubblewidth}(\pi)=\mathtt{max}_{j\in[n]}\,|\{\{\,\pi(j),\pi(k)\,\} \in E\,|\,i\leq j<k\}|)$$ _The bubblewidth of a tensor network $(V,E)$ is the minimum bubblewidth of a contraction order $\pi$ for $(V,E)$:_

$$BW(V,E)=\mathtt{min}_{\pi:[n]\to V}(\mathtt{bubblewidth}(\pi))$$

Interestingly, the bubblewidth of a graph can be used to bound from above the much better studied notions of treewidth and pathwidth. Let us denote by $PW(V,E)$ and $TW(V,E)$ the path width and tree width of a graph $(V,E)$.

**Proposition 2.5.6** (Aharonov et al. [1]).: $$TW(V,E)\leq PW(V,E)\leq 2BW(V,E)$$

The following proposition is a weaker statement then the results of O'Gorman [1], that we can prove using the simple considerations about contraction time given above.

**Proposition 2.5.7**.: _Any tensor network $(V,E,T)$ can be contracted in $O(n^{BW(d)+a})$ time where $n=\mathtt{max}_{e\in E}(\mathtt{dim}(e))$ is the maximum dimension of the edges, $BW(d)$ is the bubble width of $d$ and $a=\mathtt{max}_{v\in V}(\mathtt{deg}(v))$ is the maximum order of the tensors in $T$._

Proof.: At each contraction step $i$, we are contracting the tensor $A_{i-1}$ enclosed by the bubble with $T_{\pi(i)}$. From the considerations above we know that the time complexity of such a contraction is at most $O(n^{w_{i}+\mathtt{deg}(\pi(i))})$ where $w_{i}$ is the number of edges crossing the $i$-th bubble and $\mathtt{deg}(\pi(i))$ is the degree of the $i$-th vertex in the contraction order $\pi$. The overall time complexity is the sum of these terms, which is at most of the order $O(n^{BW(d)+a})$. 

Therefore tensor networks of bounded bubblewidth may be evaluated efficiently.

**Corollary 2.5.8**.: $\mathtt{Contraction}(\mathbb{S})$ _can be computed in poly-time if the input tensor networks have bounded bubblewidth and bounded vertex degree._

#### Tensor functors

We now show that tensor networks may be reformulated in categorical language as diagrams in a free compact-closed category equipped with a functor into the category of matrices over a commutative semiring $\mathbf{Mat}_{\mathbb{S}}$, defined in 2.1. From this perspective, the contraction order $\pi$ provides a way of turning the compact-closed diagram into a premonoidal one, where the order of contraction is the linear order of the diagram.

**Proposition 2.5.9**.: _There is a semantics-preserving translation between tensor networks $(V,E,T)$ over $\mathbb{S}$ and pairs $(F,d)$ of a diagram $d:1\to 1\in\mathbf{CC}(\Sigma)$ in a free compact closed category and a monoidal functor $F:\Sigma\rightarrow\mathbf{Mat}_{\mathbb{S}}$. This translation is semantics-preserving in the sense that $\mathtt{contract}(V,E,T)=F(d)$._ Proof.: Given a tensor network $(V,E,T)$ we build the signature $\Sigma=V\xrightarrow{\mathtt{cod}}E^{*}$ where $\mathtt{cod}(v)=I(v)$ is (any ordering of) the incidence set of vertex $v$, i.e. vertices correspond to boxes and edges to generating objects. The set of tensors $\{\,T_{v}\,\}_{v\in V}$ induces a monoidal functor $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$ given on objects $e\in E$ by $F(e)=\mathtt{dim}(e)$ and on boxes $v\in V$ by $F(v_{i})=T_{i}:1\to\mathtt{dim}(e_{0})\otimes\cdots\otimes\mathtt{dim}(e_{ \mathtt{deg}(v)})$ for $e_{i}\in\mathtt{cod}(v_{i})=I(v)$. We build a diagram $d:1\to 1\in\mathbf{CC}(\Sigma)$ by first tensoring all the boxes in $\Sigma$ and then composing it with a morphism made up only of cups and swaps, where there is a cap connecting an output port of box $v\in\Sigma$ with an output port of $v^{\prime}\in\Sigma$, whenever $\{\,v,v^{\prime}\,\}\in E$.

One can check that $F(d)=\mathtt{contract}(V,E,T)$ since composing $T_{0}\otimes T_{1}:1\to m\otimes n\otimes n\otimes l$ with $\mathtt{id}_{m}\otimes\mathtt{cup}_{n}\otimes\mathtt{id}_{l}$ in $\mathbf{Mat}_{\mathbb{S}}$ corresponds to contracting the tensors $T_{0}$ and $T_{1}$ along their common dimension $n$. For the other direction, it is easy to see that any closed diagram in $\mathbf{CC}(\Sigma)$ induces a graph with vertices $\Sigma$ and edges given by the struture of the diagram. Then a functor $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$ yields precisely the data of the tensors $\{\,T_{v}\,\}_{v\in\Sigma}$ where $T_{v}=F(v)$. 

It is often useful to allow a special type of vertex in the tensor network. These are called _COPY tensors_ in the tensor network literature [1, 1, 1], where they are used for optimizing tensor contraction. They also appear throughout categorical quantum mechanics [1] -- and most prominently in the ZX calculus [20] -- where they are called _spiders_. We have seen in 1.6.1 that diagrams with spiders are morphisms in a free hypergraph category $\mathbf{Hyp}(\Sigma)$. Since $\mathbf{Hyp}(\Sigma)\simeq\mathbf{CC}(\Sigma+\mathtt{Frob})/\cong$ (see 1.6.1), Proposition 2.5.9 can be used to show that there is a semantics-preserving translation between tensor networks with COPY tensors and pairs $(F,d)$ of a diagram $d\in\mathbf{Hyp}(\Sigma)$ and a functor $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$.

**Example 2.5.10** (Conjunctive queries as TNs).: _Conjunctive queries are tensor networks over $\mathbb{B}$. Tensor networks also subsume probabilistic graphical models by taking the underlying category to be $\mathbf{Prob}$ or $\mathbf{Mat}_{\mathbb{R}^{+}}$[1]._

We now consider the problem of evaluating closed diagrams $d:1\to 1\in\mathbf{CC}(\Sigma)$ using a tensor functor $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$

**Definition 2.5.11**.: $\mathtt{FunctorEval}(\mathbb{S})$__

_Input:_ $\Sigma$ _a monoidal signature,_ $d:1\to 1\in\mathbf{CC}(\Sigma)$_,_ $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$_,_

_Output:_ $F(d)$__

**Proposition 2.5.12**.: $\mathtt{FunctorEval}(\mathbb{S})$ _is equivalent to $\mathtt{Contraction}(\mathbb{S})$_

Proof.: This follows from Proposition 2.5.9.

 The notion of contraction order has an interesting categorical counterpart. It gives a way of turning a compact-closed diagram into a premonoidal one, such that the width of the diagram is the bubblewidth of the contraction order.

**Proposition 2.5.13**.: _There is a semantics-preserving translation between tensor networks $(V,E,T)$ over $\mathbb{S}$ with a contraction order $\pi:[[V]]\to V$ and pairs $(F,d)$ of a diagram $d:1\to 1\in\mathbf{PMC}(\Sigma+\mathtt{swap})$ in a free premonoidal category with swaps and a monoidal functor $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$. This translation is semantics-preserving in the sense that $\mathtt{contract}(V,E,T)=F(d)$. Moreover, we have that_

$$\mathtt{bubblewidth}(\pi)=\mathtt{width}(d)$$

_with $\mathtt{width}(d)$ as defined in 1.3.4._

Proof.: We can use Proposition 2.5.9 to turn $(V,E,T)$ into a compact closed diagram $d:1\to 1\in\mathbf{CC}(\Sigma)$ over a signature $\Sigma$ with only output types for each box. Given a contraction order $\pi:[n]\to V$, we modify the signature $\Sigma$ by transposing a output port $e=\{\,v,v^{\prime}\,\}\in E$ of $v\in V$ into an input whenever $\pi^{-1}(v)>\pi^{-1}(v^{\prime})$ forming a signature $\Sigma_{\pi}$ Then we can construct a premonoidal diagram

$$\pi(d)=\circ_{i=1}^{k}(\mathtt{perm}_{i}\otimes b_{i})\in\mathbf{PMC}(\Sigma_ {\pi}+\mathtt{swap})$$

where $\mathtt{perm}_{i}\in\mathbf{PMC}(\mathtt{swap})$ is a morphism containing only swaps and identities. This is done by ordering the boxes according to $\pi$ and pushing all the wires to the left, as in the following example:

(2.22)

Note that no cups or caps need to be added since the input/output types of the boxes in the signature have been changed accordingly. The bubblewidth of $\pi$ is then precisely the width of the resulting premonoidal diagram. 

We may define the bubblewidth of a diagram $d\in\mathbf{CC}(\Sigma)$ as the bubblewidth of the corresponding graph via Proposition 2.5.9. Also we define the dimension of a functor $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$ as follows:

$$\mathtt{dim}(F)=\mathtt{max}_{x\in\Sigma_{0}}(F(x))$$

We may now derive the consequences of Proposition 2.5.8 in this categorical context.

**Proposition 2.5.14**.: $\mathtt{FunctorEval}(\mathbb{S})$ _can be computed in polynomial time if the input diagrams $d$ have bounded bubblewidth and the input functors $F$ have bounded dimension._

Proof.: This follows from the conjunction of Proposition 2.5.8 and the reduction from $\mathtt{FunctorEval}$ to $\mathtt{Contraction}$ of Proposition 2.5.12.

 

#### DisCoCat and bounded memory

DisCoCat models were introduced by Coecke et al. in 2008 [10, 11]. In the original formalism, the authors considered functors from a pregroup grammar to the category of finite dimensional real vector spaces and linear maps (i.e. $\mathbf{Mat}_{\mathbb{R}}$). In this work, we follow [10, 1] in treating DisCoCat models as functors into categories of matrices over any semiring. These in particular subsume the relational models studied in 2.4 by taking $\mathbb{S}=\mathbb{B}$. As shown in Section 2.1, $\mathbf{Mat}_{\mathbb{S}}$ is a compact-closed category for any commutative semiring. Therefore, the most suitable choice of syntax for this semantics are _rigid grammars_, for which we have a canonical way of interpreting the cups and caps. Thus, in this section, the grammars we consider are either pregroup grammars 1.5.1, or dependency grammars 1.5.2, or pregroup grammar with crossed dependencies 1.5.1 or with coreference 1.6.2.

**Definition 2.5.15**.: _A DisCoCat model is a monoidal functor $F:G\to\mathbf{Mat}_{\mathbb{S}}$ for a rigid grammar $G$ and a commutative semiring $\mathbb{S}$. The semantics of a sentence $g:u\to s\in\mathbf{RC}(G)$ is given by its image $F(g)$. We assume that $F(w)=1$ for $w\in V$ so that_

Distributional models $F:G\to\mathbf{Mat}_{\mathbb{R}}$ can be constructed by counting co-occurences of words in a corpus [11]. The image of the noun type $n\in B$ is a vector space where the inner product computes noun-phrase similarity [10]. When applied to question answering tasks, distributional models can be used to compute the distance between a question and its answer [10].

**Example 2.5.16**.: _As an example we may take the pregroup lexicon:_

$$\Delta(\text{Socrate})=\Delta(\text{spettu})=\{\,n\,\}\quad\Delta(j\acute{e})= \{\,n^{r}sn^{l},n^{r}n^{r}s\,\}$$

_And we may define a DisCoCat model $F:\Delta\to\mathbf{Mat}_{\mathbb{R}}$ with $F(n)=2$, $F(s)=1$ and $F(\text{Socrate},n)=(1,0):1\to 2$, $F(\text{spettu},n)=(-1,0)$ and $F(j\acute{e},n^{r}sn^{l})=F(j\acute{e},n^{r}n^{r}s)=\text{cap}_{2}:1\to 2 \otimes 2$ in $\mathbf{Mat}_{\mathbb{R}}$. Then the following grammatical sentences:_

_evaluate to a scalar in $\mathbb{R}$ given by the matrix multiplication:_

$$F(\text{``Socrate j\acute{e}\text{ spettu''}})=\begin{bmatrix}1&0\end{bmatrix} \begin{bmatrix}1&0\\ 0&1\end{bmatrix}\begin{bmatrix}-1\\ 0\end{bmatrix}=-1=F(\text{``Socrate spettu j\acute{e}''})$$

We are interested in the complexity of the following semantics problem.

**Definition 2.5.17**.: $\mathtt{TensorSemantics}(G,\mathbb{S})$__

_Input:_ $g\in\mathbf{RC}(G)(u,s)$_,_ $F:G\to\mathbf{Mat}_{\mathbb{S}}$__

_Output:_ $F(g)$__Given a sentence diagram $g\in\mathcal{L}(G)$, the pair $(g,F)$ forms a tensor network. Computing the semantics of $g$ in $F$ amounts to contracting this tensor network. Therefore $\mathtt{TensorSemantics}(G,\mathbb{S})\in\#\mathtt{P}$. For a general rigid grammar, this problem is $\#\mathtt{P}$-hard, since it subsumes the $\mathtt{FunctorEval}(\mathbb{S})(\Sigma)$ problem. When $G$ is a pregroup grammar with coreference, we can construct any tensor network as a list of sentences connected by the coreference, making the $\mathtt{TensorSemantics}(G,\mathbb{S})$ problem $\#\mathtt{P}-\mathtt{complete}$.

**Proposition 2.5.18**.: $\mathtt{TensorSemantics}(G,\mathbb{S})$ _where $G$ is a pregroup grammar with coreference is equivalent to $\mathtt{Contraction}(\mathbb{S})$._

Proof.: One direction follows by reduction to $\mathtt{FunctorEval}(\mathbb{S})$ since any model $F:G\to\mathbf{Mat}_{\mathbb{S}}$ factors through a free compact-closed category. For the other direction, fix any pair $(F,d)$ of a diagram $d:x\to y\in\mathbf{CC}(\Sigma)$ and a functor $F:\Sigma\to\mathbf{Mat}_{\mathbb{S}}$. Using Proposition 1.6.10 we can build a corpus $C:u\to s^{k}\in\mathbf{Coref}(G)$, where the connectivity of the tensor network is encoded a coreference resolution, so that the canonical functor $\mathbf{Coref}(G)\to\mathbf{CC}(\Sigma)$ maps $C$ to $d$. 

From a linguistic perspective, a contraction order for a grammatical sentence $g:u\to s$ gives a reading order for the sentence and the bubblewidth is the maximum number of tokens (or basic types) that the reader should hold in memory in order to parse the sentence. Of course, in natural language there is a natural reading order from left to right which induces a "canonical" bubbling of $g$. In light of the famous psychology experiments of Miller [18], we expect that the short-term memory required to parse a sentence is bounded, and more precisely that $BW(g)=7\pm 2$. For pregroup diagrams generated by a dependency grammar, it is easy to show that the bubblewidth is bounded.

**Proposition 2.5.19**.: _The diagrams in $\mathbf{RC}(G)$ generated by a dependency grammar $G$ have bubblewidth bounded by the maximum arity of a rule in $G$._

Proof.: Dependency relations are acyclic, and the bubblewidth for an acyclic graph is smaller than the maximum vertex degree of the graph, which is equal to the maximum arity of a rule in $G$, i.e. the maximum number of dependents for a symbol plus one. 

Together with Proposition 2.5.14, we deduce that the problem of computing the tensor semantics of sentences generated by a dependency grammar is tractable.

**Corollary 2.5.20**.: _If $G$ is a dependency grammar then $\mathtt{TensorSemantics}(G)$ can be computed in polynomial time._

For a general pregroup grammar we also expect the generated diagrams to have bounded bubblewidth, even though they are not acyclic. For instance, the cyclic pregroup reductions given in 1.21 have constant bubblewidth 4, which is obtained by chosing a contraction order from the middle to the sides, even though the naive contraction order of 1.21 from left to right has unbounded bubblewidth. We end with a cojecture, since we were unable to show pregroup reductions have bounded bubblewidth in general.

**Conjecture 2.5.21**.: _Diagrams generated by a pregroup grammar $G$ have bounded bubble width and thus $\mathtt{TensorSemantics}(G,\mathbb{S})$ can be computed in polynomial time._ 

#### Bubbles

We end this section by noting that a simple extension of tensor network models allows to recover the full expressive power of neural networks. We have seen that contraction strategies for tensor networks can be represented by a pattern of bubbles on the diagram. These bubbles did not have any semantic interpretation and they were just used as brackets, specifying the order of contraction. We could however give them semantics, by interpreting bubbles as operators on tensors. As an example, consider the following diagram, where each box $W_{i}$ is interpreted as a matrix:

Suppose that each bubble acts on the tensor it encloses by applying a non-linearity $\sigma$ to every entry. Then we see that this diagram specifies a neural network of depth $k$ and width $n$ where $n$ is the maximum dimension of the wires. With this representation of neural networks, we have more control over the structure of the network.

Suppose we have a pregroup grammar $G_{0}$ and context-free grammar $G_{1}$ over the same vocabulary $V$ and let $u\in\mathcal{L}(G_{0})\cap\mathcal{L}(G_{1})$ with two parses $g_{0}:u\to s$ in $\mathbf{RC}(G_{0})$ and $g_{1}:u\to s$ in $\mathbf{O}(G_{1})$. Take the skeleton of the context-free parse $g_{1}$, i.e. the tree without labels. This induces a pattern of bubbles, as described in Example 1.2.4 on Peirce's alpha. Fix a tensor network model $G_{0}\to\mathbf{Mat}_{\mathbb{S}}$ for the pregroup grammar with $F(w)=1$ for $w\in V$ and choose an activation function $\sigma:\mathbb{S}\to\mathbb{S}$. Then $\sigma$ defines a unary operator on homsets $\mathcal{S}_{\sigma}:\prod_{x,y\in\mathbb{N}}\mathbf{Mat}_{\mathbb{S}}(x,y) \to\prod_{x,y\in\mathbb{N}}\mathbf{Mat}_{\mathbb{S}}(x,y)$ called a _bubble_, see [10] or [11] for formal definitions. We can combine the pregroup reduction with the pattern of bubbles as in the example above. We maythen compute the semantics of $u$ as follows. Starting from the inner-most bubble, we contract the tensor network enclosed by it and apply the activation $\sigma$ to every entry in the resulting tensor. This gives a new bubbled network where the inner-most bubble has been contracted into a box. And we repeat this process. The procedure described above gives a way of controlling the non-linearities applied to tensor networks from the grammatical structure of the sentence. While this idea is not formalised yet, it points to a higher diagrammatic formalism in which diagrams with bubbles are used to control tensor computations. This diagrammatic notation can be traced back to Peirce and was recently used in [10] to model negation in first-order logic and in [14] to model differentiation of quantum circuits. We will also use it in the next section to represent the non-linearity of knowledge-graph embeddings and in Chapter 3 to represent the softmax activation function.

 

### 2.6 Knowledge graph embeddings

Recent years have seen the rapid growth of web-scale knowledge bases such as Freebase [1], DBpedia [14] and Google's Knowledge Vault [15]. These resources of structured knowledge enable a wide range of applications in NLP, including semantic parsing [11], entity linking [12] and question answering [13]. Knowledge base _embeddings_ have received a lot of attention in the statistical relational learning literature [16]. They approximate a knowledge base continuously given only partial access to it, simplifying the querying process and allowing to predict missing entries and relations -- a task known as _knowledge base completion_.

Knowledge graph embedding are of particular interest to us since they provide a link between the Boolean world of relations and the continuous world of tensors. They will thus provide us with a connection between the relational models of Section 2.4 and the tensor network models of Section 2.5. We start by defining the basic notions of knowledge graph embeddings. Then we review three factorization models for KG embedding, focusing on their expressivity and their time and space complexity. This will lead us progressively from the category of relations to the category of matrices over the complex numbers with its convenient factorization properties.

#### Embeddings

Most large-scale knowledge bases encode information according to the Resource Description Framework (RDF), where data is stored as triples $\operatorname{(head,relation,tail)}$ (e.g. $\operatorname{(Obama,BornIn,US)}$). Thus a _knowledge graph_ is just a set of triples $K\subseteq\mathcal{E}\times\mathcal{R}\times\mathcal{E}$ where $\mathcal{E}$ is a set of entities and $\mathcal{R}$ a set of relations. This form of knowledge representation can be seen as an instance of relational databases where all the relations are _binary_.

**Proposition 2.6.1**.: _Knowledge graphs are in one-to-one correspondence with functors $\Sigma\to\operatorname{\mathbf{Rel}}$ where $\Sigma=\mathcal{R}$ is a relational signature containing only symbols of arity two._

Proof.: This is easy to see, given a knowledge graph $K\subseteq\mathcal{E}\times\mathcal{R}\times\mathcal{E}$, we can build a functor $F:\mathcal{R}\to\operatorname{\mathbf{Rel}}$ defined on objects by $F(1)=\mathcal{E}$ and on arrows by $F(r)=\{\,(e_{0},e_{1})|(e_{0},r,e_{1})\in K\,\}\subseteq\mathcal{E}\times \mathcal{E}$. Similarly any functor $F:\Sigma\to\operatorname{\mathbf{Rel}}$ defines a knowledge graph $K=\{\,(\pi_{1}F(r),r,\pi_{2}F(r))\,|\,r\in\Sigma\,\}\subseteq F(1)\times\Sigma \times F(1)$. 

Higher-arity relations can be encoded into the graph through a process known as _reification_. To reify a $k$-ary relation $R$, we form $k$ new binary relations $R_{i}$ and a new entity $e_{R}$ so that $R(e_{1},\ldots,e_{k})$ is true iff $\forall i$ we have $R_{i}(e_{R},e_{i})$. Most of the literature on embeddings focuses on knowledge graphs, and the results which we present in this section follow this assumption. However, some problems with reification have been pointed out in the literature, and current research is aiming at extending the methods to knowledge _hypergraphs_[18], a direction which we envisage also for the present work.

Embedding a knowledge graph consists in the following learning problem. Starting from a knowledge graph $K:\mathcal{E}\times\mathcal{R}\times\mathcal{E}\rightarrow\mathbb{B}$, the idea is to approximate $K$ by a scoring function $X:\mathcal{E}\times\mathcal{R}\times\mathcal{E}\rightarrow\mathbb{R}$ such that $\|\sigma(X)-K\|$ is minimized where $\sigma:\mathbb{R}\rightarrow\mathbb{B}$ is any _activation_ function.

The most popular activation functions for knowledge graph embeddings are approximations of the sign function which takes a real number to its sign $\pm 1$, where $-1$ is interpreted as the Boolean $0$ (false) and $1$ is interpreted as the Boolean $1$ (true). In machine learning applications, one needs a differentiable version of sign such as tanh or the sigmoid function. In this section, we are mostly interested in the expressive power of knowledge graph embeddings, and thus we define "exact" embeddings as follows.

**Definition 2.6.2** (Embedding).: _An exact embedding for a knowledge graph $K\subseteq\mathcal{E}\times\mathcal{R}\times\mathcal{E}$, is a tensor $X:\mathcal{E}\times\mathcal{R}\times\mathcal{E}\rightarrow\mathbb{R}$ such that $\texttt{sign}(X)=K$._

Even though sign is not a homomorphism of semirings between $\mathbb{R}$ and $\mathbb{B}$, it allows to define a notion of sign rank which has interesting links to measures of learnability such as the VC-dimension [1].

**Definition 2.6.3** (Sign rank).: _Given $R\in\mathbf{Mat}_{\mathbb{B}}$ the sign rank of $R$, denoted $\texttt{rank}_{\pm}(R)$ is given by:_

$$\texttt{rank}_{\pm}(R)=\texttt{min}\{\texttt{rank}(X)\,|\,\texttt{sign}(X)=R \,,\,X\in\mathbf{Mat}_{\mathbb{R}}\}$$

The sign rank of a relation $R$ is often much lower than its rank. In fact, we don't know any relation $R:n\to n$ with $\texttt{rank}_{\pm}(R)>\sqrt{n}$. The identity Boolean matrix $n\to n$ has sign rank $3$ for any $n$[1]. Therefore any permutation of the rows and columns of an identity matrix has sign rank $3$, an example is the relation "is married to". For the factorization models studied in this section, this means that the dimension of the embedding is potentially much smaller than then the number of entities in the knowledge graph.

Several ways have been proposed for modeling the scoring function $X$, e.g. using translations [13] or neural networks [14]. We are mostly interested in _factorization_ models where $X:\mathcal{E}\times\mathcal{R}\times\mathcal{E}\rightarrow\mathbb{R}$ is treated as a tensor with three outputs, i.e. a state in $\mathbf{Mat}_{\mathbb{R}}$. Assuming that $X$ admits a factorization into smaller matrices allows to reduce the search space for the embedding while decreasing the time required to predict missing entries. The space complexity of the embedding is the amount of memory required to store $X$. The time complexity of an embedding is the time required to compute $\sigma(X\,|s,v,o)$ given a triple. These measures are particularly relevant when it comes to embedding integrated large-scale knowledge graphs. The problem then boils down to finding a good _ansatz_ for such a factorization, i.e. an assumed factorization shape that reduces the time and space complexity of the embedding.

#### Rescal

The first factorization model for knowledge graph embedding -- known as Rescal -- was proposed by Nickel et al. in 2011 [12]. It models the real tensor $X$ with the following ansatz:

(2.23)

where $E:|\mathcal{E}|\to n$ is the embedding for entities, $W:n\otimes|\mathcal{R}|\otimes n\to 1$ is a real tensor, and $n$ is a hyper-parameter determining the dimension of the embedding.

The well-known notion of rank can be used to get bounds on the dimension of an embedding model. It is formalised diagrammatically as follows.

**Definition 2.6.4** (Rank).: _The rank of a tensor $X:1\to\otimes_{i=1}^{n}d_{i}$ in $\mathbf{Mat}_{\mathbb{S}}$ is the smallest dimension $k$ such that $X$ factors as $X=\Delta_{k}^{n};\otimes_{i=1}^{n}E_{i}$ where $E_{i}:k\to d_{i}$ and $\Delta_{k}^{n}$ is the spider with no inputs and $n$ outputs of dimension $k$._

The lowest the rank, the lowest the search space for a factorization. In fact if $X$ is factorized as in 2.23 then $\mathtt{rank}(X)=\mathtt{rank}(W)\leq|\mathcal{R}|\,n^{2}$. The time and space complexity of the embedding are thus both quadratic in the dimension of the embedding $n$.

Since any three-legged real tensor $X$ can be factorized as in 2.23 for some $n$, Rescal is a very expressive model and performs well. However, the quadratic complexity is a limitation which can be avoided by looking for different ansatze.

#### DistMult

The idea of DistMult [15] is to factorize the tensor $X$ via _joint orthogonal diagonalization_, i.e. the entities are embedded in a vector space of dimension $n$ and relations are mapped to diagonal matrices on $\mathbb{R}^{n}$. Note that the data required to specify a diagonal matrix $n\to n$ is just a vector $v:1\to n$ which induces a diagonal matrix $\Delta(v)$ by composition with the frobenius algebra $\Delta:n\to n\otimes n$ in $\mathbf{Mat}_{\mathbb{R}}$. DistMult starts from the assumption -- or ansatz -- that $X$ can is factorized as follows:

(2.24) where $E:|\mathcal{E}|\to n$ and $W:|\mathcal{R}|\to n$ and $\Delta:n\otimes n\otimes n\to 1$ is the spider with three legs. Note that $\mathtt{rank}_{\pm}(K)\leq\mathtt{rank}(X)=\mathtt{rank}(\Delta)=n$, so that both the time and space complexity of DistMult are linear $O(n)$. DistMult obtained the state of the art on Embedding when it was released. It performs especially well at modeling _symmetric_ relations such as the transitive verb "met" which satisfies "x met y" iff "y met x". It is not a coincidence that DistMult is good in these cases since a standard linear algebra result says that a matrix $Y:n\to n$ can be orthogonally diagonalized if and only if $Y$ is a symmetric matrix. For tensors of order three we have the following genralization, with the consequence that DistMult models _only_ symmetric relations.

**Proposition 2.6.5**.: $X:1\to|\mathcal{E}|\times|\mathcal{R}|\times|\mathcal{E}|$ _is jointly orthogonally diagonalizable if and only if it is a family of symmetric matrices indexed by $R$._

Proof.:

This called for a more expressive factorization method, allowing to represent _asymmetric_ relations such as "love" for which we cannot assume that "x loves y" implies "y loves x".

#### ComplEx

Trouillon et al. [17] provide a factorization of any real tensor $X$ into complex-valued matrices, that allows to model symmetric and asymmetric relations equally well. Their model, called Complex allows to embed any knowledge graph $K$ in a low-dimensional complex vector space. We give a diagrammatic treatment of their results, working in the category $\mathbf{Mat}_{\mathbb{C}}$, allowing us to improve their results. The difference between working with real-valued and complex-valued matrices is that the latter have additional structure on morphisms given by conjugation. This is pictured, at the diagrammatic level, by an asymmetry on the boxes which allows to represent the operations of adjoint, transpose and conjugation as rotations or reflexions of the diagram. This graphical gadget was introduced by Coecke and Kissinger in the context of quantum mechanics [10], we summarize it in the following picture:

(2.25)

The key thing that Trouillon et al. note is that any real square matrix is the real-part of a diagonalizable complex matrix, a consequence of Von Neumann's _spectral theorem_.

**Definition 2.6.6**.: $Y:n\to n$ _in $\mathbf{Mat}_{\mathbb{C}}$ is unitarily diagonalizable if it factorizes as:_

(2.26)

_where $w:1\to n$ is a state and $E:n\to n$ is a unitary._

**Definition 2.6.7**.: $Y$ _is normal if it commutes with its adjoint: $YY^{\dagger}=Y^{\dagger}Y$._

**Theorem 2.6.8** (Von Neumann [20]).: $Y$ _is diagonalizable if and only if $Y$ is normal._

**Proposition 2.6.9** (Trouillon [17]).: _Suppose $Y:n\to n$ in $\mathbf{Mat}_{\mathbb{R}}$ is a real square matrix, then $Z=Y+iY^{T}$ is a normal matrix and $Re(Z)=Y$. Therefore there is a unitary $E$ and a diagonal complex matrix $W$ such that $Y=Re(EWE^{\dagger})$._ _Graphically we have:_

(2.27)

_where the red bubble indicates the real-part operator._

Note that $\mathtt{rank}(A+B)\leq\mathtt{rank}(A)+\mathtt{rank}(B)$ which implies that $\mathtt{rank}(Z)=\mathtt{rank}(Y+iY^{T})\leq 2\mathtt{rank}(Y)$.

**Corollary 2.6.10**.: _Suppose $Y:n\to n$ in $\mathbf{Mat}_{\mathbb{R}}$ and $\mathtt{rank}(X)=k$, then there is $E:n\to 2k$ and $W:2k\to 2k$ diagonal in $\mathbf{Mat}_{\mathbb{C}}$ such that $Y=Re(EWE^{\dagger})$_

Given a binary relation $R:|\mathcal{E}|\to|\mathcal{E}|$, the sign-rank gives a bound on the dimension of the embedding.

**Corollary 2.6.11**.: _Suppose $R:|\mathcal{E}|\to|\mathcal{E}|$ in $\mathbf{Mat}_{\mathbb{B}}$ and $\mathtt{rank}_{\pm}(R)=k$, then there is $E:|\mathcal{E}|\to 2k$ and $W:2k\to 2k$ diagonal in $\mathbf{Mat}_{\mathbb{C}}$ such that $R=\mathtt{sign}(Re(EWE^{\dagger}))$_

The above reasoning works for a single binary relation $R$. However, given knowledge graph $K\subseteq\mathcal{E}\times\mathcal{R}\times\mathcal{E}$ and applying the reasoning above we will get $|\mathcal{R}|$ different embeddings $E_{r}:|\mathcal{E}|\to n_{r}$, one for each relation $r\in\mathcal{R}$, thus obtaining only the following factorization: $K=\mathtt{sign}(\sum_{r\in\mathcal{R}}\Delta\circ(E_{r}\otimes W(r)\otimes E_ {r})$. Which means that the overall complexity of the embedding is $O(|\mathcal{R}|\,n)$ where $n=\mathtt{max}_{r\in\mathcal{R}}(n_{r})$. The problem becomes: can we find a single embedding $E:|\mathcal{E}|\to n$ such that all relations are mapped to diagonal matrices over the same $n$? In their paper, Trouillon et al. sketch a direction for this simplification but end up conjecturing that such a factorization does _not_ exist. We answer their conjecture negatively, by proving that for any real tensor $X$ of order $3$, the complex tensor $Z=X+iX^{T}$ is jointly unitarily diagonalizable.

**Definition 2.6.12**.: $X:n\,\otimes\,m\to n$ _in $\mathbf{Mat}_{\mathbb{C}}$ is simultaneously unitarily diagonalizable if there is a unitary $E:n\to n$ and $W:m\to n$ such that:_

(2.28) 

**Definition 2.6.13**.: $X:n\,\otimes\,m\to n$ _is a commuting family of normal matrices if:_

$$\tikzfig{x}\quad=\quad\tikzfig{x}\quad=\quad\tikzfig{x}\quad$$ (2.29)

The following is an extension of Von Neumann's theorem to the multi-relational setting.

**Theorem 2.6.14**.: _[_10_]__$X:n\,\otimes\,m\to n$ in $\mathbf{Mat}_{\mathbb{C}}$ is a commuting family of normal matrices if and only if it is simultaneously unitarily diagonalizable._

Our contribution is the following result.

**Proposition 2.6.15**.: _For any real tensor $X:n\,\otimes\,m\to n$ the complex tensor $Z$ defined by:_

$$\tikzfig{x}\quad=\quad\tikzfig{x}\quad-i\quad\tikzfig{x}\quad\tikzfig{x}$$

_is a commuting family of normal matrices._

Proof.: This follows by checking that the two expressions below are equal, using only the snake equation:

$$\tikzfig{x}\quad=\quad\tikzfig{x}\quad+\quad\tikzfig{x}\quad-i\quad\tikzfig{x }\quad+i\quad\tikzfig{x}\quad+i\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig{x}$$

$$\tikzfig{x}\quad=\quad\tikzfig{x}\quad+\quad\tikzfig{x}\quad+i\quad\tikzfig{x }\quad+i\quad\tikzfig{x}\quad+i\quad\tikzfig{x}\quad-i\quad\tikzfig{x}\quad\tikzfig{x }\quad\tikzfig{x}$$

**Corollary 2.6.16**.: _For any real tensor $X:1\to n\,\otimes\,m\otimes\,n$ there is a unitary $E:n\to n$ and $W:n\to m$ in $\mathbf{Mat}_{\mathbb{C}}$ such that:_

$$\tikzfig{x}\quad=\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig {x}\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig{x }\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig{x}\quad\tikzfig{x}\_where the bubble denotes the real-part operator._

**Proposition 2.6.17**.: _For any knowledge graph $K\subseteq\mathcal{E}\times\mathcal{R}\times\mathcal{E}$ of sign rank $k=\mathtt{rank}_{\pm}(K)$, there is $E:|\mathcal{E}|\to 2k$ and $W:|\mathcal{R}|\to 2k$ in $\mathbf{Mat}_{\mathbb{C}}$ such that_

$$K=\mathtt{sign}(\text{Re}(\Delta\circ(E\otimes W\otimes E^{*}))).$$

This results in an improvement of the bound on the size of the factorization by a factor of $|\mathcal{R}|$. Although this improvement is only incremental, the diagrammatic tools used here open the path for a generalisation of the factorization result to higher-order tensors which would allow to model higher-arity relations. This may require to move into quaternion valued vector spaces where (at least) ternary symmetries can be encoded.

Moreover, as we will show in Section 2.7, quantum computers allow to speed up the multiplication of complex valued tensors. An implementation of ComplEx on a quantum computer was proposed by [10]. The extent to which quantum computers can be used to speed up knowledge graph embeddings is an interesting direction of future work.

 

### 2.7 Quantum models

Quantum computing is an emerging model of computation which promises speed-up on certain tasks as compared to classical computers. With the steady growth of quantum hardware, we are approaching a time when quantum computers perform tasks that cannot be done on classical hardware with reasonable resources. Quantum Natural Language Processing (QNLP) is a recently proposed model which aims to meet the data-intensive requirements of NLP algorithms with the computational power of quantum hardware [11, 12, 13]. These models arise naturally from the categorical approaches to linguistics [10] and quantum mechanics [1]. They can in fact be seen as instances of the tensor network models studied in 2.5. We have tested them on noisy intermediate-scale quantum computers [13, 14], obtaining promising results on small-scale datasets of around 100 sentences. However, the crucial use of post-selection in these models, is a limit to their scalability as the number of sentences grows.

In this section, we study the complexity of the quantum models based on a mapping from sentences to pure quantum circuits [13, 14]. Building on the work of Arad and Landau [1] on the complexity of tensor network contraction, we show that the _additive_ approximation (with scale $\Delta=1$) of quantum models is a complete problem for BQP, the class of problems which can be solved in polynomial time by a quantum computer with a bounded probability of error. Note that this approximation scheme has severe limits when the amplitude we want to approximate is small compared to the scale $\Delta$. Thus the results may be seen as a negative statement about the first generation of QNLP models. However, specific types of linguistic structure (such as trees) may allow to reduce the post-selection and thus the approximation scale. Moreover, this puts QNLP on par with well-known BQP-complete problems such as approximate counting [14] and the evaluation of topological invariants [15, 16] to set a standard for the next generations of QNLP models.

The development of DisCoPy was driven and motivated by the implementation of these QNLP models. The quantum module of DisCoPy is described in [14], it features interfaces with the tensor module for classical simulation, with PyZX [17] for optimization and with tket [20] for compilation and evaluation on quantum hardware. In order to run quantum machine learning routines, we also developed diagrammatic tools for automatic differentiation [13]. The pipeline for performing QNLP experiments with DisCoPy has been packaged in Lambeq [15] which provides state-of-the-art categorial parsers and optimised classes for training QNLP models.

#### Quantum circuits

In this section, we give a brief introduction to the basic ingredients of quantum computing, and define the categories **QCirc** and **PostQCirc** of quantum circuits and their post-selected counterparts. A proper introduction to the field is beyond the scope of this thesis and we point the reader to [10] and [21] for diagrammatic treatments.

The basic unit of information in a quantum computer is the _qubit_, whose _state space_ is the Bloch sphere, i.e. the set of vectors $\psi=\alpha\left|0\right\rangle+\beta\left|1\right\rangle\in\mathbb{C}^{2}$ with norm $\left\|\psi\right\|=\left|\alpha\right|^{2}+\left|\beta\right|^{2}=1$. Quantum computing is inherently probabilistic, we never observe the coefficients $\alpha$ and $\beta$ directly, we only observe the probabilities that outcomes $0$ or $1$ occur. These probabilities are given by the _Born rule_:

$$P(i)=\left|\left\langle i|\psi\right\rangle\right|^{2}$$

with $i\in\{\,0,1\,\}$ and where $\left\langle i|\psi\right\rangle$ is the inner product of $\left|i\right\rangle$ and $\left|\psi\right\rangle$ in $\mathbb{C}^{2}$, also called _amplitude_. Note that the requirement that $\psi$ be of norm $1$ ensures that these probabilities sum to $1$. The _joint state_ of $n$ qubits is given by the tensor product $\psi_{1}\otimes\cdots\otimes\psi_{n}$ and thus lives in $\mathbb{C}^{2n}$, a Hilbert space of dimension $2^{n}$. The evolution of a quantum system composed of $n$ qubits is described by a _unitary_ linear map $U$ acting on the space $\mathbb{C}^{2n}$, i.e. a linear map satisfying $UU^{\dagger}=\mathtt{id}=U^{\dagger}U$. Where $\dagger$ (dagger) denotes the conjugate transpose. Note that the requirement that $U$ be unitary ensures that $\left\|U\psi\right\|=\left\|\psi\right\|$ and so $U$ sends quantum states to quantum states.

The unitary map $U$ is usually built up as a _circuit_ from some set of basic _gates_. Depending on the generating set of gates, only certain unitaries can be built. We say that the set of gates is _universal_, when any unitary can be obtained using a finite sequence of gates from this set. The following is an example of a universal gate-set:

$$\mathtt{Gates}=\{\,CX,\,H,\,Rz(\alpha),\,\mathtt{swap}\,\}_{\alpha\in[0,2 \pi]}$$ (2.31)

where $CX$ is the controlled $X$ gate acting on $2$ qubits and defined on the basis of $\mathbf{C}^{4}$ by:

$$CX(\left|00\right\rangle)=\left|00\right\rangle\quad CX(\left|01\right\rangle )=\left|01\right\rangle\quad CX(\left|10\right\rangle)=\left|11\right\rangle \quad CX(\left|11\right\rangle)=\left|10\right\rangle$$

$Rz(\alpha)$ is the $Z$ phase, acting on $1$ qubit as follows:

$$Rz(\alpha)(\left|0\right\rangle)=\left|0\right\rangle\quad\quad Rz(\alpha)( \left|1\right\rangle)=e^{i\alpha}\left|1\right\rangle\,.$$

$H$ is the Hadamard gate, acting on $1$ qubit as follows:

$$H(\left|0\right\rangle)=\frac{1}{\sqrt{2}}(\left|0\right\rangle+\left|1 \right\rangle)\quad\quad H(\left|1\right\rangle)=\frac{1}{\sqrt{2}}(\left|0 \right\rangle-\left|1\right\rangle)\,.$$

and the swap gate acts on $2$ qubits and is defined as usual.

We define the category of quantum circuits $\mathbf{QCirc}=\mathbf{MC}(\mathtt{Gates})$ as a free monoidal category with objects natural numbers $n$ and arrows generated by the gates in (2.31).

**Definition 2.7.1** (Quantum circuit).: _A quantum circuit is a diagram $c:n\to n\in\mathbf{MC}(\mathtt{Gates})=\mathbf{QCirc}$ where $n$ is the number of qubits, it maps to a corresponding unitary $U_{c}:(\mathbb{C}^{2})^{\otimes n}\rightarrow(\mathbb{C}^{2})^{\otimes n}\in \mathbf{Mat}_{\mathbb{C}}$._ 

**Example 2.7.2**.: _An example of quantum circuit is the following:_

(2.32)

_where we denote the $Rz(\alpha)$ gate using the symbol $\alpha$ and the Hadamard gate using a small white box. Note that different quantum circuits $c$ and $c^{\prime}$ may correspond to the same unitary, we write $c\sim c^{\prime}$ when this is the case. For instance the swap gate is equivalent to the following composition:_

(2.33)

_When performing a quantum computation on $n$ qubits, the quantum system is usually prepared in an all-zeros states $\ket{\mathbf{0}}=\ket{0}^{\otimes n}$, then a quantum circuit $c$ is applied to it and measurements are performed on the resulting state $U_{c}\ket{\mathbf{0}}$, yielding a probability distribution over bitstrings of length $n$. We can then post-select on certain outcomes, or predicates over the resulting bitstring, by throwing away the measurements that do not satisfy this predicate. Diagrammatically, state preparations and post-selections are drawn using the generalised Dirac notation [10] as in the following post-selected circuit:_

(2.34)

_The category of post-selected quantum circuits is obtained from_ **QCirc** _by allowing state preparations $\ket{0},\ket{1}$, and post-selections $\bra{0},\bra{1}$._

_Note that we also allow arbitrary scalars $a\in\mathbb{R}$, seen as boxes $0\to 0$ in_ **PostQCirc** _to rescale the results of measurements, this is needed in order to interpret pregroup grammars in_ **PostQCirc**_, see 2.7.2. Post-selected quantum circuits map functorially into linear maps:_

$$I:\mathbf{PostQCirc}\rightarrow\mathbf{Mat}_{\mathbb{C}}$$by sending each gate in **Gates** to the corresponding unitary, state preparations and post-selections to the corresponding states and effects in $\mathbf{Mat}_{\mathbb{C}}$. This makes post-selected quantum circuits instances of tensor networks over $\mathbb{C}$.

**Proposition 2.7.3**.: _For any morphism $d:1\to 1$ in_ **PostQCirc**_, there exists a quantum circuit $c\in\mathbf{QCirc}$ such that $I(d)=a\cdot\left\langle\mathbf{0}\right|U_{c}\left|\mathbf{0}\right\rangle$ where $a=\prod_{i}U(a_{i})$ is the product of the scalars appearing in $d$._

Proof.: We start by removing the scalars $a_{i}$ from the diagram $d$ and multiplying them into $a=\prod_{i}U(a_{i})$. Then we pull all the kets to the top of the diagram and all the bras to the bottom, using swap if necessary. 

#### Quantum models

Quantum models are functors from a syntactic category to the category of post-selected quantum circuits **PostQCirc**. These were introduced in recent papers [16, 17], and experiments were performed on IBM quantum computers [16, 18].

**Definition 2.7.4** (Quantum model).: _A quantum (circuit) model is a functor $F:G\rightarrow\mathbf{PostQCirc}$ for a grammar $G$, the semantics of a sentence $g\in\mathcal{L}(G)$ is given by a distribution over bitstrings $b\in\left\{\,0,1\,\right\}^{F(s)}$ obtained as follows:_

$$P(b)=\left|\left\langle\mathbf{b}\right|F(g)\left|\mathbf{0}\right\rangle \right|^{2}$$

Quantum models define the following computational problem:

**Definition 2.7.5**.: QSemanctics__

_Input:_ $G$ _a grammar,_ $g:u\to s\in\mathbf{MC}(G)$_,_ $F:G\rightarrow\mathbf{PostQCirc}$_,_ $b\in\left\{\,0,1\,\right\}^{F(s)}$__

_Output:_ $\left|\left\langle\mathbf{b}\right|I(F(g))\left|\mathbf{0}\right\rangle \right|^{2}$__

**Remark 2.7.6**.: _Note that quantum language models do not assume that the semantics of words be a unitary matrix. Indeed a word may be interpreted as a unitary with some outputs post-selected. However, mapping words to unitaries is justified in many cases of interest in linguistics. For instance, this implies that there is no loss of information about "ball" when an adjective such as "big" is applied to it._

Any of the grammars studied in Chapter 1 may be intepreted with a quantum model. For monoidal grammars (including regular and context-free grammars), this is simply done by interpreting every box as a post-selected quantum circuit. For rigid grammars, we need to choose an interpretation for the cups and caps. Since the underlying category $\mathbf{Mat}_{\mathbb{C}}$ is compact-closed, there is a canonical way of interpreting them using a $CX$ gate and postselection, and re-scaling the result by a factor of $\sqrt{2}$ (2.34)

In order to interpret cross dependencies we can use the swap gate, see Example 2.7.2. Finally, in order to interpret the Frobenius algebras in a pregroup grammar with coreference, we use the following mapping:

One can check the the image under $I$ of the circuit above maps to the Frobenius algebra in $\mathbf{Mat}_{\mathbb{C}}$.

In practice, quantum models are learned from data by choosing a parametrized quantum circuit in $\mathbf{PostQCirc}$ for each production rule and then tuning the parameters (i.e. the phases $\alpha$ in $Rz(\alpha)$) appearing in this circuit, see [18, 19] for details on ansatze and training.

#### Additive approximations

Since quantum computers are inherently probabilistic, there is no deterministic way of computing a function $F:\{0,1\}^{*}\to\mathbb{C}$ encoded in the amplitudes of a quantum state. Rather what we obtain is an _approximation_ of $F$. In many cases, the best we can hope for is an _additive_ approximation, which garantees to generate a value within the range $[F(x)-\Delta(x)\epsilon,F(x)+\Delta(x)\epsilon]$ where $\Delta:\left\{\,0,1\,\right\}^{*}\to\mathbb{R}^{+}$ is an approximation scale. This approximation scheme has been found suitable to describe the performance of quantum algorithms for contracting tensor network [1], counting approximately [19], and computing topological invariants [10] including the Jones polynomial [13].

**Definition 2.7.7** (Additive approximation).: _[_1_]_ _A function $F:\left\{\,0,1\,\right\}^{*}\to\mathbb{C}$ has an additive approximation $V$ with an approximation scale $\Delta:\left\{\,0,1\,\right\}^{*}\to\mathbb{R}^{+}$ if there exists a probabilistic algorithm that given any instance $x\in\left\{\,0,1\,\right\}^{*}$ and $\epsilon>0$, produces a complex number $V(x)$ such that_

$$P(|V(x)-F(x)|\geq\epsilon\Delta(x))\leq\frac{1}{4}$$ (2.35)

_in a running time that is polynomial in $|x|$ and $\epsilon^{-1}$._ 

**Remark 2.7.8**.: _The error signal $\epsilon$ is usually inversely proportional to a polynomial in the run-time $t$ of the algorithm, i.e. we have $\epsilon=\frac{1}{\texttt{poly}(t)}$._

An algorithm $V$ satisfying the definiton above is a solution of the following problem defined for any function $F:\left\{\,0,1\,\right\}^{*}\rightarrow\mathbb{C}$ and approximation scale $\Delta:\left\{\,0,1\,\right\}^{*}\rightarrow\mathbb{R}^{+}$.

**Definition 2.7.9**.: $\texttt{Approx}(F,\Delta)$__

_Input:_ $x\in\left\{\,0,1\,\right\}^{*}$ _,_ $\epsilon>0$__

_Output:_ $v\in\mathbb{C}$ _such that_ $P(|v-F(x)|\geq\epsilon\Delta(x))\leq\frac{1}{4}$__

Compare this to the definition of a multiplicative approximation, also known as a fully polynomial randomised approximation scheme [13].

**Definition 2.7.10** (Multiplicative approximation).: _A function $F:\left\{\,0,1\,\right\}^{*}\rightarrow\mathbb{C}$ has a multiplicative approximation $V$ if there exists a probabilistic algorithm that given any instance $x\in\left\{\,0,1\,\right\}^{*}$ and $\epsilon>0$, produces a complex number $V(x)$ such that_

$$P(|V(x)-F(x)|\geq\epsilon\,|F(x)|)\leq\frac{1}{4}$$ (2.36)

_in a running time that is polynomial in $|x|$ and $\epsilon^{-1}$._

**Remark 2.7.11**.: _This approximation is called multiplicative because $V(x)$ is guaranteed to be within a multiplicative factor $(1\pm\epsilon)$ of the optimal value $F(x)$. For instance the inequality in (2.36) implies that $|F(x)|\,(1-\epsilon)\leq|V(x)|\leq|F(x)|\,(1+\epsilon))$ with probability bigger than $\frac{3}{4}$._

Note that any multiplicative approximation is also additive with approximation scale $\Delta(x)=|F(x)|$. However, the converse does not hold. An additive approximation scheme allows for the approximation scale $\Delta(x)$ to be exponentially larger than the size of the output $|F(x)|$, making the approximation (2.35) quite loose since the error parameter $\epsilon$ may be bigger than the output signal $V(x)$.

#### Approximating quantum models

In this section, we show that the problem of additively approximating the evaluation of sentences in a quantum model is in BQP and that it is BQP-complete in special cases of interest. The argument is based on Arad and Landau's work [1] on the quantum approximation of tensor networks. We start by reviewing their results and end by demonstrating the consequences for quantum language models.

Consider the problem of approximating the contraction of tensor networks $T(V,E)$ using a quantum computer. Arad and Landau [1] show that this problem can be solved in polynomial time, up to an additive accuracy with a scale $\Delta$ that is related to the norms of the swallowing operators.

**Proposition 2.7.12** (Arad and Landau [1]).: _Let $T(V,E)$ be a tensor network over $\mathbb{C}$ of dimension $q$ and maximal node degree $a$, let $\pi:[|V|]\to V$ be a contraction order for $T$ and let $\left\{\,A_{i}\,\right\}_{i\in\left\{\,1,\ldots,k\,\right\}}$ be the corresponding set of swallowing operators.__Then for any $\epsilon>0$ there exists a quantum algorithm that runs in $k\cdot\epsilon^{-2}\cdot\mathsf{poly}(q^{a})$ time and outputs a complex number $r$ such that:_

$$P(\left|\mathsf{value}(T)-r\right|\geq\epsilon\Delta)\leq\frac{1}{4}$$

_with_

$$\Delta(T)=\prod_{i=1}^{k}\left\|A_{i}\right\|$$

Proof.: Given a tensor network with a contration order $\pi$, the swallowing operators $A_{i}$ are linear maps. For each of them, we can construct a unitary $U_{i}$ acting on a larger space such that post-selecting on some of its outputs yields $A_{i}$. Composing these we obtain a unitary $U_{c}=U_{1}\cdot U_{2}\ldots U_{\left|V\right|}$ represented by a poly-size quantum circuit $c\in\mathbf{QCirc}$ such that $\mathsf{value}(T)=\left\langle\mathbf{0}\right|U_{c}\left|\mathbf{0}\right\rangle$. In order to compute an approximation of this quantity we can use an $H$-test, defined by the following circuit:

(2.37)

where the white boxes are hadamard gates and the subdiagram in the middle denotes the controlled unitary $U$. It can be shown that the probability $r$ of measuring $0$ on the ancillary qubit is equal to $Re(\left\langle\mathbf{0}\right|U_{c}\left|\mathbf{0}\right\rangle)$. A slightly modified version of the $H$-test computes $Im(\left\langle\mathbf{0}\right|U_{c}\left|\mathbf{0}\right\rangle)$. Arad and Landau [1] show that this process can be done in polynomial time and that the result of measuring the ancillary qubit gives an additive approximation of $\mathsf{value}(T)$ with approximation scale $\Delta(T)=\prod_{i=1}^{k}\left\|F(d_{i})\right\|$. 

**Corollary 2.7.13**.: _The problem $\mathsf{Approx}(\mathsf{Contraction}(\mathbb{C}),\Delta)$ with $\Delta$ as defined above is in $\mathtt{BQP}$._

**Remark 2.7.14**.: _From the Cauchy-Schwartz inequality we have that:_

$$\left|T\right|\leq\prod_{i=1}^{k}\left\|A_{i}\right\|=\Delta(T)\,.$$

_In fact we have no guarantee that the approximation scale $\Delta(T)$ is not exponentially larger than $\left|F(d)\right|$. This is a severe limitation, since the approximations we get from the procedure defined above can have an error larger than the value we are trying to approximate._

We now consider the problem of approximating the amplitude of a post-selected quantum circuit $\left|\left\langle\mathbf{0}\right|U_{c}\left|\mathbf{0}\right\rangle\right|^ {2}$. Note that this is an instance of the problem studied in the previous paragraph, since post-selected quantum circuits are instances of tensor networks, so that this problem belong to the class $\mathtt{BQP}$. For this subclass of tensor networks the approximation scale $\Delta(c)$ can be shown to be constant and equal to $1$, with the consequence -- shown by Arad and Landau [10] -- that the additive approximation of post-selected quantum circuits is $\mathtt{BQP}-\mathtt{hard}$.

In order to show $\mathtt{BQP}$-hardness of a problem $F$, it is sufficient to show that an oracle which computes $F$ can be used to perform universal quantum computation with bounded error. More precisely, for any quantum circuit $u\in\mathbf{QCirc}$ denote by $p_{0}$ the probability of obtaining outcome $0$ when measuring the last qubit of $c$. To perform universal quantum computation, it is sufficient to distinguish between the cases where $p_{0}<\frac{1}{3}$ and $p_{0}>\frac{2}{3}$ for any quantum circuit $c$. Thus a problem $F$ is $\mathtt{BQP}$-hard if for any circuit $c$, there is a poly-time algorithm $V$ using $F$ as an oracle that returns $YES$ when $p_{0}<\frac{1}{3}$ with probability bigger than $\frac{3}{4}$ and $NO$ when $p_{0}>\frac{2}{3}$ with probability bigger than $\frac{3}{4}$. .

**Proposition 2.7.15**.: _[_10_]_ _The problem of finding an additive approximation of with scale $\Delta=1$ where $U_{c}$ is the unitary induced by a quantum circuit $c\in\mathbf{QCirc}$ is $\mathtt{BQP}$-complete._

Proof.: Membership follows by reduction to $\mathtt{Approx}(\mathtt{Contraction}(\mathbb{S}),\Delta)$, since post-selected quantum circuits are instances of tensor networks. To show hardenss, fix any quantum circuit $c$ on $n$ qubits and denote by $p_{0}$ the probability of obtaining outcome $0$ on the last qubit of $c$. We can construct the quantum circuit:

(2.38)

it is easy to check that $\left\langle\mathbf{0}\right|U_{q}\left|\mathbf{0}\right\rangle=p_{0}$. Since $q$ is a circuit, there is a natural contraction order given by the order of the gates, moreover the corresponding swallowing operators $U_{q_{i}}$ are unitary and thus $\left\|U_{q_{i}}\right\|=1$, also $\left\|U(\left|\mathbf{0}\right\rangle)\right\|=\left\|U(\left\langle\mathbf{0 }\right|)\right\|=1$ and therefore the approximation scale is constant $\Delta(q)=1$. Suppose we have an oracle $V$ that computes an approximation of $\left\langle\mathbf{0}\right|U_{q}\left|\mathbf{0}\right\rangle$ with constant scale $\Delta(q)=1$. Then for any circuit $c\in\mathbf{QCirc}$, we construct the circuit $q$ and apply $V$ to get a complex number $V(q)$ such that:

$$P(\left|V(q)-p_{0}\right|\geq\epsilon)\leq\frac{1}{4}\implies P(p_{0}- \epsilon\leq\left|V(q)\right|\leq p_{0}+\epsilon)\geq\frac{3}{4}$$

Setting $\epsilon<\frac{1}{6}$, we see that if $\left|V(q)\right|<\frac{1}{6}$ then $p_{0}<\frac{1}{3}$ with probability $\geq\frac{3}{4}$ and similarly $\left|V(q)\right|>\frac{5}{6}$ implies $p_{0}>\frac{1}{3}$ with probability $\geq\frac{3}{4}$. Note that this would not be possible if we didn't know that the approximation scale $\Delta(q)$ is bounded. Thus $V$ can be used to distinguish between the cases where $p_{0}<\frac{1}{3}$ and $p_{0}>\frac{2}{3}$ with probability of success greater than $\frac{3}{4}$. Therefore the oracle $V$ can be used to perform universal quantum computation with bounded error. And thus $V$ is $\mathtt{BQP}$-hard.

 

**Corollary 2.7.16**.: $\mathtt{Approx}(\mathtt{FunctorEval}(\mathbb{C})(I),\Delta=1)$ _where $I:\mathbf{PostQCirc}\rightarrow\mathbf{Mat}_{\mathbb{C}}$ is the functor defined in paragraph 2.7.1 is a $\mathtt{BQP}$-complete problem._

Proof.: Membership follows by reduction to $\mathtt{Approx}(\mathtt{Contraction}(\mathbb{C}),\Delta)$ since post-selected quantum circuits are instances of tensor networks. Since $\mathtt{QCirc}\hookrightarrow\mathbf{PostQCirc}$ the problem of Proposition 2.7.15 reduces to $\mathtt{Approx}(\mathtt{FunctorEval}(I),\Delta=1)$, thus showing hardness. 

Note that the value $v=|\langle\mathbf{0}|\,U_{c}\,|\mathbf{0}\rangle|$ may be exponentially small in the size of the circuit $c$, so that the approximation scale $\Delta=1$ is still not optimal. In this case we would need exponentially many samples from the quantum computer approximate $v$ up to multiplicative accuracy.

We end by showing $\mathtt{BQP}$-completeness for the problem of approximating the semantics of sentences in a quantum model with approximation scale $\Delta=1$.

**Definition 2.7.17**.: $\mathtt{QASemantics}=\mathtt{Approx}(\mathtt{QSemantics},\Delta=1)$__

_Input:_ $G$ _a monoidal grammar,_ $g:u\to s\in\mathbf{MC}(G)$_,_ $F:G\rightarrow\mathbf{PostQCirc}$_,_ $b\in\{\,0,1\,\}^{F(s)}$_,_ $\epsilon>0$__

_Output:_ $v\in\mathbb{C}$ _such that_ $P(|v-\langle\mathbf{b}|\,I(F(g))\,|\mathbf{0}\rangle|\geq\epsilon)\leq\frac{1} {4}$__

**Proposition 2.7.18**.: _There are pregroup grammars $G$, such that the problem $\mathtt{QASemantics}(G)$ is $\mathtt{BQP}$-complete._

Proof.: Membership follows by reduction to the problem of Proposition 2.7.15, since the semantics of a grammatical reduction $g:u\to s$ in $\mathbf{RC}(G)$ is given by the evaluation of $|\langle\mathbf{b}|\,I(F(g))\,|\mathbf{0}\rangle|^{2}$ which corresponds to evaluating $|\langle\mathbf{0}|\,U_{c}\,|\mathbf{0}\rangle|^{2}$ where $c$ is defined by Proposition 2.7.3. To show hardness, let $G$ have only one word $w$ of type $s$, fix any unitary $U$, and define $F:G\rightarrow\mathbf{PostQCirc}$ by $F(s)=0$ and $F(w)=\langle\mathbf{0}|\,U\,|\mathbf{0}\rangle$, then evaluating the semantics of $w$ reduces to the problem of Proposition 2.7.15 and is thus $\mathtt{BQP}-\mathtt{hard}$. 

Note that we were able to show completeness using the fact that the functor $F$ is in the input of the problem. It is an open problem to show that $\mathbf{QASemantics}(G)(F)$ is $\mathtt{BQP}$-complete for fixed choices of grammar $G$ and functors $F$. In order to show this, one may need to assume that $G$ is a pregroup grammar with coreference and show that there is a functor $F$ such that any post-selected quantum circuit can be built up using fixed size circuits (corresponding to words) connected by $\mathrm{GHZ}$ states (corresponding to the spiders encoding the coreference), adapting the argument from Proposition 2.5.12.

Moreover, as discussed above, this approximation scheme is limited by the fact that the approximation scale $\Delta$ may be too big when the output $\langle\mathbf{b}|\,I(F(g))\,|\mathbf{0}\rangle$ is exponentially small. This is particularly significant at the beginning of training, when $F$ is initialised as a random mapping to circuits, see [11]. This seems to be an inherent problem caused by the use of post-selection in the model, although methods to reduce the post-selection have been proposed, e.g. the snake removal scheme from [11].

One avenue to overcome this limitation, is to consider a different type of models, defined as functors $G\rightarrow\mathbf{CPM}(\mathbf{QCirc})$ where $\mathbf{CPM}(\mathbf{QCirc})$ is the category of completely positive maps induced by quantum circuits as defined in [10]. In this category, post-selection is not allowed since every map is causal. The problem with these models however is that we cannot interpret the cups and caps of rigid grammars. We may still be able to interpret monoidal grammars, as well as acyclic pregroup reductions such as those induced by a dependency grammar. Exploring the complexity of these models, and testing them on quantum hardware, is left for future work.

 

### 2.8 DisCoPy in action

We now give an example of how DisCoPy can be used to solve a concrete task. We define a relational model (2.4) and then learn a smaller representation of the data as a tensor model (2.5). Since the sentences we will deal with are all of the form subject-verb-object, this means we will perform a knowledge ambedding task in the sense of 2.6. We start by defining a simple pregroup grammar with 3 nouns and 2 verbs.

**Listing 2.8.1**.: Subject-verb-object language.

``` fromdiscopy.rigidimportTy,Id,Box,Diagram n,s=Ty('n'),Ty('s') make_word=lambdaname,ty:Box(name,Ty(),ty) nouns=[make_word(name,n)fornamein['Bruno','Florio','Shakespeare']] verbs=[make_word(name,n.l@s@n.r)fornamein['met','read']] grammar=Diagram.cups(n,n.l)@Id(s)@Diagram.cups(n.r,n) sentences=[a@b@c@>grammarforainnounsforbin verbsforcinnouns] sentences[2].draw() ```

We can now build a relational model for this language as a tensor.Functor.

**Listing 2.8.2**.: Relational model in DisCoPy.

``` fromdiscopy.tensorimportDim,Tensor,Functor,Spider importjax.numpyasnp Tensor.np=np ob={n:Dim(3),s:Dim(1)} defmapping(box): ifbox.name=='Bruno': returnnp.array([1,0,0]) ifbox.name=='Florio': returnnp.array([0,1,0]) ifbox.name=='Shakespeare': returnnp.array([0,0,1]) ifbox.name=='met': returnnp.array([[1,0,1],[0,1,1],[1,1,1]]) ifbox.name=='read': returnnp.array([[1,0,0],[0,1,1],[0,1,1]]) ifbox.name=='who':return Spider(0, 3, Dim(3)).array T = Functor(ob, mapping) assert T(sentences[2]).array == [0.] ```

_We use float numbers for simplicity, but one may use dtype=bool instead. Note the special intepretation of "who" as a Frobenius spider, see 2.4.4._

Relational models can be used to evaluate any conjunctive query over words. We can generate a new pregroup reduction using lambeq [Kar+21] and evaluate it in T.

``` from lambeqimportBobcatParser parser=BobcatParser() diagram=parser.sentence2diagram('BrunometFloriowhoreadShakespeare.') diagram.draw() assertT(diagram)=[1.0] ```

We now show how to embed the three-dimensional data defined by T as a two-dimensional tensor.Functor with float entries. We start by parametrising two-dimensional tensor functors.

``` importnumpy defp_mapping(box,params):  ifbox.name=='Bruno':  returnnp.array(params[0])  ifbox.name=='Florio':  returnnp.array(params[1])  ifbox.name=='Shakespeare':  returnnp.array(params[2])  ifbox.name=='met':  returnnp.array([params[3],params[4]])  ifbox.name=='read':  returnnp.array([params[5],params[6]])  ifbox.name=='who':  returnSpider(0, 3, Dim(2)).array ob={n:Dim(2), s:Dim(1)} F=lambdaparams:Functor(ob,lambdabox:p_mapping(box,params)) params0=numpy.random.rand(6, 2) assertF(params0)(sentences[2]).array !=[0.] ``` We obtain a prediction by evaluating F(params) on a sentence and taking sigmoid to get a number between 0 and 1. We can then define the loss of a functor as the mean squared difference between its predictions and the true labels given by T. Of course, other activation and loss functions may be used.

**Listing 2.8.5**.: Defining the loss function for a knowledge embedding task.

``` defsigmoid(x): sig=1/(1+np.exp(-x)) returnsig evaluate=lambdaF,sentence:sigmoid(F(sentence).array) defmean_squared(y_true,y_pred): returnnp.mean((np.array(y_true)-np.array(y_pred))**2) loss=lambdaparams:mean_squared(*zip() *[(T(sentence).array,evaluate(F(params),sentence))forsentenceinsentences])) ```

The Jax package [1] supports automatic differentiation grad and just-in-time compilation jit for jax compatible numpy code. Since the code for Tensor is compatible, we can directly use Jax to compile a simple update function for the functor's parameters. We run the loop and report the results obtained.

**Listing 2.8.6**.: Learning functors with Jax.

``` fromjaximportgrad,jit fromtimeimporttime step_size=0.1 @jit defupdate(params): returnparams-step_size*grad(loss)(params) epochs,iterations=7,30 params=numpy.random.rand(6,2) forepochinrange(epochs): start=time() foriinrange(iterations): params=update(params) print("Epoch{(:.3f) milliseconds)".format(epoch,1e3*(time()-start))) print("Testingloss:(.5f)".format(loss(params))) y_true=[T(sentence).arrayforsentenceinsentences] y_pred=[0ifevaluate(F(final_params),sentence)<0.5else1 forsentenceinsentences] print(classification_report(y_true,y_pred)) 
The 2D tensor representation of the data of a 3D relational model is given by

$$\begin{split}\text{dec}&=\text{dec}(\text{dec}(\text{dec}( \text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}( \text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}( \text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}( \text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec }(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec }(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec }(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}( \text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec }(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec}( \text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}( \text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec }(\text{dec}(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec }(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec }(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec }(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec }(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec }(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec }(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec)}( \text{dec}(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\text{dec }(\text{dec}(\text{dec)}(\text{dec}(\text{dec}(\text{dec)}(\ 

## Chapter 3 Games for Pragmatics

The threefold distinction between syntax, semantics and pragmatics may be traced back to the semiotics of Peirce an his trilogy between sign, object and interpretant. According to Peirce [14], these three aspects would induce three different approaches to semiotics, renewing the medieval _trivium_: formal grammar, logic and formal rhetoric. In his studies [15], Stalnaker gives a finer demarcation between pragmatics and semantics through the concept of _context_: "It is a semantic problem to specify the rules for matching up sentences of a natural language with the propositions that they express. In most cases, however, the rules will not match sentences directly with propositions, but will match sentences with propositions relative to features of the context in which the sentence is used. Those contextual features are part of the subject matter of pragmatics."

In his _Philosophical Investigations_[13], Wittgenstein introduces the concept of _language-game_ (_Sprachspiel_) as a basis for his theory of meaning. He never gives a general definition, and instead proceeds by enumeration of examples: "asking, thanking, cursing, greeting, praying". Thus, depending on the language-game in which it is played, the same utterance "Water!" can be interpreted as the answer to a question, a request to a waiter or the chorus of a song. From the point of view of pragmatics, language-games provide a way of capturing the notion of _context_, isolating a particular meaning/use of language within an environment defined by the game.

Since Lewis' work on conventions [10], formal _game theory_ has been used to model the variability of the meaning of sentences and their dependence on context [11, 12, 13]. These theoretical enquiries have also been supported by psycholinguistic experiments such as those of Frank and Goodman [10], where a Bayesian game-theoretic model is used to predict the behaviour of listeners and speakers in matching words with their referents.

In parallel to its use in pragmatics, game theory has been proven significant in designing machine learning tasks. It is at the heart of multi-agent reinforcement learning [14], where decision-makers interact in a stochastic environment. It is also used to improve the performance of neural network models, following the seminal work of Goodfellow et al. [12], and is beginning to be applied to natural language processing tasks such as dialogue generation [11, 12, 13], knowledge graph embedding [15, 16] and word-sense disambiguation [14].

The aim of this chapter is to develop formal and diagrammatic tools to model language games and NLP tasks. More precisely, we will employ the theory of _lenses_, which have been developed as a model for the dynamics of data-accessing programs [13] and form the basis of the recent applications of category theory to both game theory [10, 11] and machine learning [14, 15]. The results are still at a preliminary stage, but the diagrammatic representation succeeds in capturing a wide range of pragmatic scenarios.

In Section 3.1, we argue that probabilistic models are best suited for analysing pragmatics and NLP tasks and show how the deterministic models studied in Chapter 2 may be turned into probabilistic ones. In Section 3.2, we introduce lenses and show how they capture the dynamics of probabilistic systems and stochastic environments. In Section 3.3, we show how parametrization may be used to capture agency in these environments and discuss the notions of optimum, best response and equilibrium for multi-agent systems. Throughout, we give examples illustrating how these concepts may be used in both pragmatics and NLP and in Section 3.4, we give a more in-depth analysis of three examples, building on recent proposals for modelling language games with category theory [12, 11].

 

### 3.1 Probabilistic models

Understanding language requires resolving large amounts of vagueness and ambiguity as well as inferring interlocutor's intents and beliefs. Uncertainty is a central feature of pragmatic interactions which has led linguists to devise probabilistic models of language use, see [10] for an overview.

Probabilistic modelling is also used throughout machine learning and NLP in particular. For example, the language modelling task is usually formulated as the task of learning the conditional probability $p(x_{k}\,|\,x_{k-1},\ldots,x_{1})$ to hear the word $x_{k}$ given that words $x_{1},\ldots,x_{k-1}$ have been heard. We have seen in Section 2.3 how neural networks induce probabilistic models using the softmax function. The language of probability theory is particularly suited to formulating NLP tasks, and reasoning about them at a high level of abstraction.

Categorical approaches to probability theory and Bayesian reasoning have made much progress in recent years. In their seminal paper [11], Cho and Jacobs identified the essential features of probabilistic resoning using string diagrams, including marginalisation, conditionals, disintegration and Bayesian inversion. Some of their insights derived from Fong's thesis [14], where Bayesian networks are formalised as functors into categories of Markov kernels. Building on Cho and Jacobs, Fritz [15] introduced _Markov categories_ as a synthetic framework for probability theory, generalising several results from the dominant measure-theoretic approach to probability into this high-level diagrammatic setting. These algebraic tools are powering interesting developments in applied category theory, including diagrammatic approaches to causal inference [17] and Bayesian game theory [1].

In this section, we review the basic notions of probability theory from a categorical perspective and show how they can be used to reason about discriminative and generative NLP models.

#### Categorical probability

We introduce the basic notions of categorical probability theory, following [11] and [16]. For simplicity, we work in the setting of _discrete_ probabilities, although most of the results we use are formulated diagrammatically and are likely to generalise to any Markov category.

Let $\mathcal{D}:\mathbf{Set}\to\mathbf{Set}$ be the discrete distribution monad defined on objects by:

$$\mathcal{D}(X)=\{\,p:X\to\mathbb{R}^{+}\,|\,d\text{has finite support and }\sum_{x\in X}p(x)=1\,\}$$

and on arrows $f:X\to Y$ by:

$$\mathcal{D}(f):\mathcal{D}(X)\to\mathcal{D}(Y):(p:X\to\mathbb{R}^{+})\mapsto(y \in Y\mapsto\sum_{x\in f^{-1}(y)}p(x)\in\mathbb{R}^{+})$$

We can construct the Kleisli category for the distribution monad $\mathbf{Prob}=\mathbf{Kl}(\mathcal{D})$ with objects sets and arrows discrete conditional distributions $f:X\to\mathcal{D}(Y)$ wedenote by $f(y|x)\in\mathbb{R}^{+}$ the probability $f(x)(y)$. Composition of $f:X\to\mathcal{D}(Y)$ and $g:Y\to\mathcal{D}(Z)$ is given by:

$$X\xrightarrow{f}\mathcal{D}(Y)\xrightarrow{\mathcal{D}(g)}\mathcal{D}\mathcal{D }(Z)\xrightarrow{\mu_{Z}}\mathcal{D}(Z)$$

where $\mu_{Z}:\mathcal{D}\mathcal{D}(Z)\to\mathcal{D}(Z)$ flattens a distribution of distributions by taking sums. Explicitly we have:

$$f\cdot g(z|x)=\sum_{y}g(z|y)f(y|x)\in\mathbb{R}^{+}$$

We may think of the objects of **Prob** as _random variables_ and the arrows as _conditional distributions_.

The category **Prob** has interesting structure. First of all, it is a symmetric monoidal category with $\times$ as monoidal product. This is not a cartesian product since $\mathcal{D}(X\times Y)\neq\mathcal{D}(X)\times\mathcal{D}(Y)$. The unit of the monoidal product $\times$ is the singleton set $1$ which is _terminal_ in **Prob**, i.e. for any set $X$ there is only one map $\mathtt{del}_{X}:X\to\mathcal{D}(1)\simeq 1$ called _discard_. Terminality of the monoidal unit means that if we discard the output of a morphism we might as well have discarded the input, a property often interpreted as _causality_[13].

There is a commutative comonoid structure $\mathtt{copy}_{X}:X\to X\times X$ on each object $X$ with counit $!_{X}$. Also there is a embedding of **Set** into **Prob** which gives the deterministic maps. These are characterized by the following property

$$\mathtt{copy}_{Y}\circ f=(f\times f)\circ\mathtt{copy}_{X}\iff f:X\to Y\text{ is deterministic}$$

Morphisms $p:1\to X$ in **Prob** are simply distributions $p\in\mathcal{D}(X)$. Given a joint distribution $p:1\to X\times Y$ we can take _marginals_ of $p$ by composing with the discard map:

In **Prob** the disintegration theorem holds.

**Proposition 3.1.1** (Disintegration).: _[_11_]_ _For any joint distribution $p\in\mathcal{D}(X\times Y)$, there are channels $c:X\to\mathcal{D}(Y)$ and $c^{!}:Y\to\mathcal{D}(X)$ satisfying:_

(3.1) Proof.: The proof is given in [10] in the case of the full subcategory of $\mathbf{Prob}$ with objects finite sets, i.e. for the category $\mathbf{Stoch}$ of stochastic matrices. Extending this proof to the infinite discrete case is simple because for any distribution $p\in\mathcal{D}(X\times Y)$ we may construct a stochastic vector over the support of $p$, which is finite by definition of $\mathcal{D}$. So we can disintegrate $p$ in $\mathbf{Stoch}$ and then extend it to $\mathbf{Prob}$ by assigning probability $0$ to elements outside of the support. 

**Example 3.1.2**.: _Taking $X=\{\,1,2\,\}$ and $Y=\{\,A,B\,\}$ an example of disintegration is the following:_

$$\left(\begin{array}{c|c}\hline I&1/8\\ \hline 2&7/8\end{array}\right)\!,\quad\boxed{$\begin{array}{c|c|c}\hline A&B\\ \hline I&1&0\\ \hline 2&3/7&4/7\end{array}$}\right)\leftarrow\boxed{$\begin{array}{c|c|c} \hline A&B\\ \hline I&1/8&0\\ \hline 2&3/8&1/2\end{array}$}\rightarrow\left(\begin{array}{c|c|c}\hline A&B\\ \hline I&1/4&0\\ \hline 2&3/4&1\end{array}\right)\!,\quad\boxed{$\begin{array}{c|c|c}\hline A&B\\ \hline I/2&1/2\end{array}$}\right)$$

Given a _prior_$p\in\mathcal{D}(X)$ and a channel $c:X\rightarrow\mathcal{D}(Y)$, we can integrate them to get a joint distribution over $X$ and $Y$ and then disintegrate over $Y$ to get the channel $c^{\dagger}:Y\rightarrow\mathcal{D}(X)$. This process is known as _Bayesian inversion_ and $c^{\dagger}$ is called a Bayesian inverse of $c$ along $p$. These satisfy the following equation, which can be derived from 3.1.

(3.2)

Interpreting this diagrammatic equation in $\mathbf{Prob}$ we get that:

$$c(y|x)p(x)=c^{\dagger}(x|y)\sum_{x}(c(y|x)p(x))$$

known as Bayes law.

The category $\mathbf{Prob}$ satisfies a slightly stronger notion of disintegration which doesn't only apply to states or joint distributions but to channels directly.

**Proposition 3.1.3** (Conditionals).: _[_11_]_ _The category $\mathbf{Prob}$ has conditionals, i.e. for any morphism $f:A\rightarrow\mathcal{D}(X\times Y)$ in $\mathbf{Prob}$ there is a morphism $f|_{X}:A\times X\rightarrow\mathcal{D}(Y)$ such that:_

$$\begin{array}{c}\includegraphics[width=142.364pt]{figs/142.eps}\end{array}$$

Proof.: As for Proposition 3.1.1, this was proved in the case of $\mathbf{Stoch}$ by Fritz [11] and it is simple to extend the proof to $\mathbf{Prob}$.

 

#### Discriminators

The first kind of probabilistic systems that we consider are _discriminators_. We define them in general as probabilistic channels that take sentences in a language $\mathcal{L}(G)$ and produce distributions over a set of features $Y$. These can be seen as solutions to the general classification task of assigning sentences in $\mathcal{L}(G)$ to classes in $Y$.

**Definition 3.1.4** (Discriminator).: _A discriminator for a grammar $G$ in a set of features $Y$ is a probabilistic channel:_

$$c:\mathcal{L}(G)\to\mathcal{D}(Y)$$

**Remark 3.1.5**.: _Throughout this chapter we assume that parsing for the chosen grammar $G$ can be done efficiently. WFor simplicity, we assume that we are given a function:_

$$\mathsf{parsing}:\mathcal{L}(G)\to\coprod_{u\in V^{*}}\mathbf{G}(u,s)$$

_where $\mathbf{G}$ is the category of derivations for the grammar $G$. This could also be made a probabilistic channel with minor modifications to the results of this section._

In the previous chapters, we defined NLP models as functors $F:G\to\mathbf{S}$ where $G$ is a grammar and $\mathbf{S}$ a semantic category. The aim for this section is to show that, in most instances, we can turn these models into probabilistic discriminators. We will do this in two steps. Assuming that parsing can be performed efficiently, it is easy to show that functorial models $F:G\to\mathbf{S}$ induce _encoders_, i.e. deterministic functions $\mathcal{L}(G)\to S$ which assign to every sentence in the language $\mathcal{L}(G)\subseteq V^{*}$ a compressed semantic representation in the sentence space $S=F(s)$. In order to build a discriminator $c$ from an encoder $f:\mathcal{L}(G)\to S$ the only missing piece of structure is an _activation_ function $\sigma:S\to\mathcal{D}(Y)$, mapping semantic states to distributions over classes.

_Softmax_ is a useful activation function which allows to turn real valued vectors and tensors into probability distributions.

$$\mathtt{softmax}_{X}:\mathbb{R}^{X}\to\mathcal{D}(X)$$

$$\mathtt{softmax}(\vec{x})_{i}=\frac{e^{x_{i}}}{\sum_{i=1}^{n}e^{x_{i}}}$$

Thus, when the sentence space is $S=\mathbb{R}^{Y}$, $\mathtt{softmax}$ allows to turn encoders $f:X\to\mathbb{R}^{Y}$ into discriminators $c=\mathtt{softmax}\circ f:X\to\mathcal{D}(Y)$. In fact all discriminators arise from encoders by post-composition with $\mathtt{softmax}$ as the following proposition shows.

**Proposition 3.1.6**.: _Given a channel $c:X\to\mathcal{D}(Y)$ and a prior distribution $p\in\mathcal{D}(Y)$ there is a function $f:X\to\mathbb{R}^{Y}$ such that_

$$X\xrightarrow{f}\mathbb{R}^{Y}\xrightarrow{\mathtt{softmax}}\mathcal{D}(Y)\, =\,X\xrightarrow{c}\mathcal{D}(Y)$$Proof.: In order to prove the existence of $f$, we construct the log likelihood function. Given $c:X\to\mathcal{D}(Y)$ there is a Bayesian inverse $c^{\dagger}:Y\to\mathcal{D}(X)$, then we can define the _likelihood_$l:X\times Y\to\mathbb{R}^{+}$ by:

$$l(x,y)=c^{\dagger}(x|y)p(y)$$

and the _log likelihood_ is given by

$$f(x)=\texttt{log}_{Y}(l(x,y))\in\mathbb{R}^{Y}$$

where $\texttt{log}_{Y}:(\mathbb{R}^{+})^{Y}\to\mathbb{R}^{Y}$ is the logarithm applied to each entry. Then one can prove using Bayes law that:

$$\texttt{softmax}(f)=\texttt{softmax}(\texttt{log}(l(x,y)))=\frac{l(x,y)}{ \sum_{y^{\prime}}l(x,y^{\prime})}=\frac{c^{\dagger}(x|y)p(y)}{\sum_{y^{\prime} }c^{\dagger}(x|y^{\prime})}=c(y|x)$$ (3.3)

Note that many functions $f$ may induce the same channel $c$ in this way. The encoder $f:X\to(\mathbb{R}^{+})^{Y}$ given in the proof is the log of the likelihood function $l:X\times Y\to\mathbb{R}^{+}$. In these instances, the encoder is well behaved probabilistically, since it satisfies the version 3.3 of Bayes equation. However, in most gradient-based applications of stochastic methods, encoders $X\to(\mathbb{R})^{Y}$ such as those built from a neural network tend to achieve a better performance.

We already saw in Section 2.3, that softmax can be used to turn neural networks into probabilistic models. We rephrase this in the following definition.

**Definition 3.1.7**.: _Given any recursive neural network $F:G\to\mathbf{NN}(W)$ for a monoidal grammar $G$ with $F(s)=$and $F(v)=0$ for $v\in V\subseteq G_{0}$, and parameters $\theta:W\to\mathbb{R}$, we can build a discriminator $\tilde{F}:\mathcal{L}(G)\to\mathcal{D}([n])$ as the following composition:_

$$\tilde{F}=\mathcal{L}(G)\xrightarrow{\texttt{parsing}}\coprod_{u\in V^{*}} \mathbf{MC}(G)(u,s)\xrightarrow{F}\mathbf{NN}(W)(0,n)\xrightarrow{I_{\theta} }\mathbb{R}^{n}\xrightarrow{\texttt{softmax}}\mathcal{D}([n])$$

_where $I_{\theta}:\mathbf{NN}(W)\to\mathbf{Set}_{\mathbb{R}}$ is the functor defined in2.3._

Softmax induces a _function_$\mathcal{S}:\mathbf{Mat}_{\mathbb{R}}\to\mathbf{Prob}$ defined on objects by $n\mapsto[n]$ for $n\in\mathbb{N}$ and on arrows by:

$$n\xrightarrow{M}m\quad\mapsto\quad[n]\xrightarrow{\mathcal{S}(M)}\mathcal{D}([ m])=[n]\xrightarrow{|\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \! 

**Example 3.1.9** (Student).: _Consider a student who is faced with a question in $\mathcal{L}(G,q)$, and has to guess the answer. This can be seen as a probabilistic channel $\mathcal{L}(G,q)\to\mathcal{D}(A)$ where $A$ is a set of possible answers. We can build this channel using a tensor network model $F:G\to\mathbf{Mat}_{\mathbb{R}}$ with $F(q)=\mathbb{R}^{A}$ which induces a discriminator $\tilde{F}:\mathcal{L}(G,q)\to\mathcal{D}(A)$, as defined above. The image under $\tilde{F}$ of the grammatical question "Who was the emperor of France" in $\mathcal{L}(G,q)$ is given by the following diagram, representing a distribution in $\mathcal{D}(A)$:_

_where the bubble represents the unary operator on hom-sets $\mathcal{S}$._

**Definition 3.1.10**.: _Given any relational model $F:G\to\mathbf{Rel}$ for a rigid grammar $G$ with $F(s)=Y$ and $F(w)=1$ for $w\in V\subseteq G_{0}$ we can build a discriminator $\tilde{F}:\mathcal{L}(G)\to\mathcal{D}(Y)$ as follows: $\tilde{F}=\mathcal{L}(G)\xrightarrow{\mathtt{parsing}}\coprod_{u\in V^{*}} \mathbf{RC}(G)(u,s)\xrightarrow{F}\mathbf{Rel}(1,Y)\simeq\mathcal{P}(Y) \xrightarrow{\mathtt{uniform}}\mathcal{D}(Y)$ where $\mathtt{uniform}$ takes a subset of $Y$ to the uniform distribution over that subset._

**Example 3.1.11** (Literal listener).: _Consider a listener who hears a word in $W$ and needs to choose which object in $R$ the word refers to. This example is based on Bergen et al. [1]. Suppose we have a relation (called lexicon in [1]) $\varphi:W\times R\to\mathbb{B}$, where $\varphi(w,r)=1$ if $w$ could refer to $r$ and $0$ otherwise. We can treat $\varphi$ as a likelihood$\varphi:W\times R\to\mathbb{R}^{+}$. and model a literal listener as a classifier $l:W\to\mathcal{D}(R)$ defined by:_

$$l(w|r)\propto\varphi(w,r)$$

_This is the same as taking $l(r)\in\mathcal{D}(W)$ to be the uniform distribution over the words that could refer to $r$ according to $\varphi$. Thus the literal listener does not take the context into account. We can extend this model by allowing noun phrases to be uttered, instead of single words, i.e. $W=\mathcal{L}(G,n)$ for some rigid grammar $G$ with noun type $n\in G_{0}$. Then we can replace the relation $\varphi:W\times R\to\mathbb{B}$ by a relational model$F:G\to\mathbf{Rel}$ with $F(n)=R$, so that any grammatical noun phrase $g:u\to n$ in $\mathbf{RC}(G)$ is mapped to a subset $F(g)\subseteq R$ of the objects it could refer to. Then the listener is modeled by:_

$$l(g|r)\propto\langle F(g)|r\rangle$$

_where $\langle F(g)|r\rangle=1$ if $r\in F(g)$ and is zero otherwise. This corresponds to taking $l=\tilde{F}$ as defined in the proposition above. As we will see in Example 3.1.13 and Section 3.4.1, we can use a literal listener to define a pragmatic speaker which reasons about the literal interpretation of its words._

#### Generators

In order to solve NLP tasks, we need _generators_ along-side discriminators. These are probabilistic channels which produce a sentence in the language given some semantic information in $S$. They are used throughout NLP, and most notably in neural language modelling [1] and machine translation [1].

**Definition 3.1.12** (Generator).: _A generator for $S$ in $G$ is a probabilistic channel:_

$$c:S\to\mathcal{DL}(G)$$

Bayesian probability theory allows to exploit the symmetry between encoders and decoders. Recall that Bayes law relates a conditional distribution $c:X\to\mathcal{D}(Y)$ with its Bayesian inverse $c^{\dagger}:Y\to\mathcal{D}(X)$ given a prior $p:1\to\mathcal{D}(X)$:

$$c^{\dagger}(x|y)=\frac{c(y|x)p(x)}{\sum_{x^{\prime}}c(y|x^{\prime})p(x^{ \prime})}$$

Thus Bayesian inversion $\dagger$ can be used to build a decoder $c^{\dagger}:Y\to\mathcal{DL}(G)$ from an encoder $c:\mathcal{L}(G)\to\mathcal{D}(Y)$ given a prior over the language $p\in\mathcal{DL}(G)$, and viceversa.

**Example 3.1.13** (Speaker).: _Consider a speaker who is given an object in $R$ (e.g. a black chess piece), and needs to produce a word in $W$ to refer to it (e.g. "bishop"). We can model it as a generator $s:R\to\mathcal{D}(W)$. Following from Example 3.1.11, assume the speaker has access to a relation $\varphi:R\times W\to\mathbb{B}$. Then she knows what the literal interpretation of her words is, i.e. she can build a channel $l:W\to\mathcal{D}(R)$ corresponding to a literal speaker. In order to perform her task $s=R\to\mathcal{D}(W)$, she can take the Bayesian inverse of the literal listener $s=l^{\dagger}$. We will see in Section 3.4.1, that this strategy for the teacher yields a Nash equilibrium in a collaborative game with a listener._

In practice, it is often very expensive to compute the Bayesian inverse of a channel. Especially when one does not have a finite table of probabilities $X\times Y\to\mathbb{R}^{+}$ but rather a log-likelihood function $X\to\mathbb{R}^{Y}$ represented e.g. as a neural network. Thus, in most cases, we must resort to other tools to build generators. Recurrent neural networks are the simplest such tool. Indeed, given a recurrent network $g:n\to n\oplus|V|$ in $\mathbf{NN}$ we can build a generator $\mathbb{R}^{n}\to\mathcal{D}(V^{*})$, by picking an initial encoder state $x\in\mathbb{R}^{n}$ and simply iterate the recurrent network by composing it along the encoder space $n$, see Section 2.3 for examples.

**Example 3.1.14** (Translator/Chatbot).: _The sequence-to-sequence (Seq2Seq) model of Bahdanau et al. [1], surveyed at the end of Section 2.3 is composed of recurrent encoder and decoder networks connected by an attention mechanism, see (2.16). It was originally used to build a translator $V^{*}\to\mathcal{D}(V^{\prime*})$ for two vocabularies $V$ and $V^{\prime}$. Taking $V^{\prime}=V$ we can use Seq2Seq to build a chatbot $V^{*}\to\mathcal{D}(V^{*})$. We will use these in 3.3.15._From a categorical perspective, we do not understand generators as well as discriminators. If generators arise from functors, discriminators should arise from a dual notion, i.e. a concept of cofunctor, but we were unable to work out what these should be. Recently, Toumi and Koziell-Pipe [14] introduced a notion of functorial language model which allows to generate missing words in a grammatical sentence using DisCoCat models. Indeed, if we assume that the grammatical structure is given, then we may generate sentences with that structure using an activation function. We give an example in the case of relational models.

**Example 3.1.15** (Teacher).: _Consider a teacher who knows an answer (e.g. "Napoleon"), and needs to produce a question with that answer (e.g. "Who was emperor of France?"). Suppose that the teacher has access to a relational model $F:G\to\mathbf{Rel}$ for a grammar $G$ with a question type $q$ and a noun type $n$ with $F(q)=F(n)$ (i.e. answers are nouns). Following [10, 14, 14], we may repackage the functor $F$ via an embedding $E:N\to F(n)$ in $\mathbf{Rel}$ where $N=\{\,w\in V\,|\,(w,n)\in G\,\}$ is the set of nouns, so that $F(w\to n)=E\,|w\rangle$. Fixing a grammatical structure $g:u\to q$, the teacher can generate questions with that structure, by evaluating the structure in her model $F$ and then uniformly choosing which nouns to use in the question. This process is shown in the following diagram:_

_where the bubble indicates the_ uniform _operator on hom-sets of_ $\mathbf{Rel}$_. Read from bottom to top, the diagram above represents a channel $N\to\mathcal{D}(N\times N)$ which induces a channel $N\to\mathcal{D}(\mathcal{L}(G,q))$. However, taking the_ uniform _function is not a pragmatic choice for the teacher. Indeed, given "Napoleon" as input, the channel above is equally likely to choose the question "Who was emperor of France?" as "Who was citizen of France?". We will see in Section 3.4.2, that the pragmatics of posing questions may be captured by an adversarial scenario in which the teacher aims to ask hard questions to a student who tries to answer them._ 

### 3.2 Bidirectional tools

The concept of _reward_ is central in both game theory and machine learning. In the first, it is formalised in terms of a _utility function_ and allows to define the optimal strategies and Nash equilibria of games. In the second, where it is captured (pessimistically) using a _loss function_, it defines an objective that the learning system must minimise. Reward is also a central concept in reinforcement learning where one considers probabilistic processes which run through a state-space while collecting rewards [11, 12]. In this section we show that the information flow of rewards in a dynamic probabilistic system can be captured in a suitable category of _lenses_. The bidirectionality of lenses allows to represent the action-reaction structure of game-theoretic and machine learning systems.

#### Lenses

Lenses are bidirectional data accessors which were introduced in the context of the view-update problem in database theory [1, 2], although they have antecedents in Godel's "Dialectica interpretation". They are widely used in functional programming [13] and have recently received a lot of attention in the applied category theory community, due to their applications to machine learning [14, 15] and game theory [16]. There are several variants on the definition of lenses available in the literature. These were largely unified by Riley who introduced _optics_ as generalisation of lenses from **Set** to any symmetric monoidal category [17]. We use the term lens instead of optics for this general notion.

**Definition 3.2.1** (Lens).: _[_17_]_ _Let $X,Y,O,S$ be objects in a symmetric monoidal category $\mathbf{C}$. A lens or optic $[f,v]:(X,S)\rightarrow(Y,O)$ in $\mathbf{C}$ is given by the following data:_

* _an object_ $M\in\mathbf{C}$_,_
* _a forward part_ $f:X\to M\otimes Y$ _called "get",_
* _a backward part_ $v:M\otimes O\to S$ _called "put"._

Stripped out of its set-theoretic semantics, a lens is simply seen as a pair of morphisms arranged as in the following two equivalent diagrams.

(3.4)

Two lenses $[f,v],[f^{\prime},v^{\prime}]:(X,S)\rightarrow(Y,R)$ are said to be _equivalent_, written $[f,v]\cong$$[f^{\prime},v^{\prime}]$, if there is a morphisms $h:M\to M^{\prime}$ satisfying

(3.5)

The quotient of the set of lenses by the equivalence relation $\cong$ can be expressed as a coend formula [111]. Here we omit the coend notation for simplicity. This quotient is needed in order to show that composition of lenses is associative and unital. Indeed, as shown by Riley [111], equivalence classes of lenses under $\cong$ form a symmetric monoidal category denoted $\mathbf{Lens}(\mathbf{C})$. Sequential composition for $[f,u]:(X,S)\to(Y,O)$ and $[g,v]:(Y,O)\to(Z,Q)$ is given by $[g,v]\circ[f,u]=[(\mathtt{id}_{M_{f}}\otimes g)\circ f,v\circ(\mathtt{id}_{M _{f}}\otimes u)]$ with $M_{g\circ f}=M_{f}\times M_{g}$, diagrammatically we have:

(3.6)

and tensor product $[f,v]\otimes[g,u]$ is given by:

(3.7)

Moreover, there are cups allowing to turn a covariant wire in the contravariant direction.

(3.8)

**Remark 3.2.2**.: _This diagrammatic notation is formalised in [10], where categories endowed with this structure are called teleological. Note that $\mathbf{Lens}_{\mathbf{C}}$ is not compact-closed, i.e. we can only turn wires from the covariant to the contravariant direction. When we draw a vertical wire as in 3.5, we actually mean a cup as in 3.8, this makes the notation more compact._ We interpret lenses along the lines of compositional game theory [11]. A lens is a process which makes _observations_ in $X$, produces _actions_ or moves in $Y$, then it gets some _reward_ or utility in $R$ and gives back information as to its degree of _satisfaction_ or coutility in $S$. Of course, this interpretation in no way exhausts the possible points of vue on lenses. For instance in [10] and [12], one interprets lenses as smooth functions turning inputs in $X$ into outputs in $Y$, and then backpropagating the _error_ in $R=\Delta Y$ to an error in the input $S=\Delta X$.

We are particularly interested in lenses over the category $\mathbf{Prob}$ of conditional probability distributions, which we call _stochastic lenses_. These have been characterised in the context of causal inference [13], where they are called _combs_, as morphisms of $\mathbf{Prob}$ satisfying a causality condition.

**Definition 3.2.3** (Comb).: _[_13_]_ _A comb is a stochastic map $c:X\otimes R\to Y\otimes S$ satisfying for some $c^{\prime}:X\to Y$, the following equation:_

(3.9)

Combs have an intuitive diagrammatic representation from which they take their name.

(3.10)

With this diagram in mind, the condition 3.9 reads: "the contribution from input $R$ is only visible via output $S$ "[13].

**Proposition 3.2.4**.: _In $\mathbf{Prob}$, combs $X\otimes R\to Y\otimes S$ are in one-to-one correspondence with lenses $(X,S)\to(Y,R)$._

Proof.: The translation works as follows:

(3.11)

where $c^{\prime}$ is the morphism defined in 3.2.3 and $c|_{X\otimes Y}$ is the conditional defined by Proposition 3.1.3. Note that $c|_{X\otimes Y}$ is not unique in general. However any such choice yields equivalent lenses since the category $\mathbf{Prob}$ is _productive_, see [14, Theorem 7.2] for a slightly more general result. Indeed, this proposition is the base case for the inductive proof of [14, Theorem 7.2]. 

Why should we use lenses $(X,S)\to(Y,R)$ instead of combs? The difference between them is in the composition. Indeed, composing lenses corresponds to nesting combs as in the following diagram:

As we will see, the composition of lenses allows to define a notion of feedback for probabilistic systems which correctly captures their dynamics.

#### Utility functions

We analyse a special type of composition in $\mathbf{Lens}(\mathbf{Prob})$: between a lens and its environment, also called _context_ in the open games literature [1]. This is a comb in $\mathbf{Lens}(\mathbf{C})$ that first produces an initial state in $X$, then receives a move in $Y$ and produces a _utility_ or reward in $R$.

**Definition 3.2.5** (Context).: _The context for lenses of type $(X,S)\to(Y,R)$ over $\mathbf{C}$ is a comb $c$ in $\mathbf{Lens}(\mathbf{C})$ of the following shape:_

(3.12)

**Proposition 3.2.6**.: _Contexts $C$ for lenses of type $(X,S)\to(Y,R)$ in $\mathbf{Prob}$ are in one-to-one correspondence with pairs $[p,k]$ where $p\in\mathcal{D}(X)$ is a distribution over observations called prior and $k:X\times Y\to\mathcal{D}(R)$ is a channel called utility function._

Proof.: Since the unit of the tensor is terminal in $\mathbf{Prob}$, a context $C$ of the type above is given by a pair of morphisms, $[p^{\prime},k^{\prime}]$ as in the following diagram:

(3.13) Moreover, by the disintegration theorem, the joint distribution $p^{\prime}$ above may be factored into a prior distribution $p$ over $X$ and a channel $c:X\to\mathcal{D}(M)$. Therefore the context above is equivalent to to a context induced by a distribution over starting state $p\in\mathcal{D}(X)$ and a utility function $k:X\times Y\to R$ as in the following diagram:

(3.14)

As we will see in Section 3.3.2, this notion of utility captures the notion from game theory where utility functions assign a reward in $R$ given the move of the player in $Y$ and the moves of the other players, see also [1].

#### Markov rewards

Another interesting form of composition in $\mathbf{Lens}(\mathbf{Prob})$ arises when considering the notion of a Markov reward process (MRP) [13]. MRPs are dynamic probabilistic systems which transit through a state space $X$ while collecting rewards in $\mathbb{R}$.

**Definition 3.2.7** (Mrp).: _A Markov reward process with state space $X$ is given by the following data:_

1. _a transition function_ $T:X\to\mathcal{D}(X)$_,_
2. _a payoff function_ $R:X\to\mathbb{R}$_,_
3. _and a discount factor_ $\gamma\in[0,1)$_._

This data defines lens $[T,R_{\gamma}]:(X,\mathbb{R})\to(X,\mathbb{R})$ in $\mathbf{Prob}$ drawn as follows:

(3.15)

where $R_{\gamma}:X\times\mathbb{R}\to\mathcal{D}(\mathbb{R})$ is given by the one-step discounted payoff:

$$R_{\gamma}(x,r)=R(x)+\gamma r$$

Intuitively, the MRP observes the state $x\in X$ which it is in and collects a reward $R(x)$, then uses the transition $T$ to move to the next state. Given an expected future reward $r$, the MRP computes the current value given by summing the current reward with the expected future reward discounted by $\gamma$. This process is called _Markov_, because the state at time step $t+1$ only depends on the state a time step $t$, i.e. $x_{t+1}$ is sampled from the distribution $T(x_{t})$.

Thus an MRP is an endomorphism $[T,R_{\gamma}]:(X,\mathbb{R})\to(X,\mathbb{R})$ in the category of stochastic lenses. We can compose $[T,R_{\gamma}]$ with itself $n$ times to get a new lens $[T,R_{\gamma}]^{n}$ where the forward part is given by iteration of the transition function and the backward part is given by the $n$-step discounted payoff:

$$R_{\gamma}^{n-}(x,r)=\sum_{i=1}^{n-1}\gamma^{i}R(T^{i}(x))+\gamma^{n}r$$

Since $0\leq\gamma<1$, this expression converges in the limit as $n\to\infty$ if $R$ and $T$ are deterministic. When $R$ and $T$ are stochastic, one can show that the expectation $\mathbb{E}(R_{\gamma}^{n-})$ converges to the _value_ of the MRP which yields a measure of the total reward expected from this process.

$$\mathtt{value}([T,R_{\gamma}])(x)=\mathbb{E}(\sum_{i=1}^{\infty}\gamma^{i}R( T^{i}(x)))=\lim_{n\to\infty}\mathbb{E}(\sum_{i=1}^{n}\gamma^{i}R(T^{i}(x)))$$ (3.16)

We can represent this as an effect $v=\mathtt{value}([T,R_{\gamma}]):(X,\mathbb{R})\to(1,1)$ in $\mathbf{Lens}(\mathbf{Prob})$, which simply consists in a probabilistic channel $v:X\to\mathbb{R}$. This effect $v$ satifies the following Bellman fixed point equation in $\mathbf{Lens}(\mathbf{Prob})$, characterising it as the iteration of $[T,R_{\gamma}]$, see [10].

$$v(x)=\mathbb{E}(R(x)+\gamma v(T(x)))$$

which we may express diagrammatically as:

(3.17)

where $\mathbb{E}$ denotes the conditional expectation operator, given for any channel $f:X\to\mathcal{D}(\mathbb{R})$ by the function $\mathbb{E}(f):X\to\mathbb{R}$ defined by $\mathbb{E}(f)(x)=\sum_{y\in\mathbb{R}}yf(y|x)$ (note that there only finitely many non-zero terms in this discrete setting). The value $v$ of the reward process is often estimated by running Monte Carlo methods which iterate the transition function while collecting rewards. Note that _not_ all stochastic lenses $(X,\mathbb{R})\to(X,\mathbb{R})$ have an effect $(X,\mathbb{R})\to(1,1)$ with which they satisfy Equation 3.17. In fact it is sufficient to set $T=\mathtt{id}_{X}$, $R(x)=1$ for all $x\in X$ and $\gamma>1$ in order to get a counter-example. It would be interesting to characterise the stochastic lenses satisfying 3.17 algebraically, e.g. are they closed under composition? This would in fact be true if the conditional expectation operator $\mathbb{E}$ was functorial. Given the results of [12] and [1], we expect that conditional expectation can be made a functor by restriciting the objects of $\mathbf{Prob}$.

 

### 3.3 Cybernetics

Parametrization is the process of representing functions $X\to Y$ via a parameter space $\Pi$ with a map $\Pi\to(X\to Y)$. It is a fundamental tool in both machine learning and game theory, since it allows to define a notion of _agency_, through the choice of parameters. For example, players in a formal game are parametrized over a set of _strategies_: there is a function $X\to Y$, turning observations into moves, for any strategy in $\Pi$. In reinforcement learning, the agent is parametrized by a set of _policies_, describing how to turn states into actions. We show that parametrized lenses are suitable for representing these systems and give examples relevant for NLP.

#### Parametrization

Categories allow to distinguish between two types of parametrization. Let $\mathbf{S}$ be a semantic category with a forgetful functor $\mathbf{S}\hookrightarrow\mathbf{Set}$

**Definition 3.3.1** (External parametrization).: _An external parametrization $(f,\Pi)$ of morphisms $X\to Y$ in a category $\mathbf{S}$, also called a family of morphisms indexed by $\Pi$, is a function $f:\Pi\to\mathbf{S}(X,Y)$. These form a category $\mathbf{Fam}(\mathbf{S})$ with composition defined for $f:\Pi_{0}\to\mathbf{S}(X,Y)$ and $g:\Pi_{1}\to\mathbf{S}(Y,Z)$ by $g\circ f:\Pi_{0}\times\Pi_{1}\to\mathbf{S}(X,Z)$ with $g\circ f(\pi_{0},\pi_{1})=f(\pi_{0})\circ g(\pi_{1})$._

**Definition 3.3.2** (Internal parametrization).: _An internal parametrization $(f,\Pi)$ of morphisms $X\to Y$ in a monoidal category $\mathbf{S}$ is a morphism $f:\Pi\otimes X\to Y$ in $\mathbf{S}$. These form a category $\mathbf{Para}(\mathbf{S})$ with composition defined for $f:\Pi_{0}\otimes X\to Y$ and $g:\Pi_{1}\otimes Y\to Z$ by $g\circ f:\Pi_{0}\otimes\Pi_{1}\otimes X\to Z$ with $g\circ f=f(\pi_{0})\circ g(\pi_{1})$._

Which parametrization should we prefer, $\mathbf{Fam}$ or $\mathbf{Para}$? It depends on context. Internal parametrization is usually a stricter notion, because it imposes that the parametrization be a morphism of $\mathbf{S}$ and not simply a function. For example, $\mathbf{Para}(\mathbf{Smooth})$ embeds in $\mathbf{Fam}(\mathbf{Smooth})$ but the embedding is not full, i.e. there are external parametrizations defined by non-differentiable functions. In fact, the $\mathbf{Para}$ construction was introduced in the context of gradient-based learning [15], where it is very desirable that the parametrization be differentiable. External parametrizations are mostly used in the compositional game theory literature [11], since they are more flexible and allow to define a notion of _best response_ (see 3.3.6). However they are also inextricably linked to $\mathbf{Set}$, making them less desirable from a categorical perspective, since it is harder to prove results about $\mathbf{Fam}(\mathbf{S})$ given knowledge of $\mathbf{S}$.

Note that the two notions coincide for the category of sets and functions. Indeed, since $\mathbf{Set}$ is cartesian closed, we have that:

$$\Pi\to\mathbf{Set}(X,Y)\iff\Pi\to(X\to Y)\iff\Pi\times X\to Y$$

and therefore $\mathbf{Para}(\mathbf{Set})\simeq\mathbf{Fam}(\mathbf{Set})$. Even though $\mathbf{Prob}$ is not cartesian closed, these notions again coincide.



**Proposition 3.3.3**.: _Internal and external parametrizations coincide in $\mathbf{Prob}$, i.e. $\mathbf{Fam}(\mathbf{Prob})\simeq\mathbf{Para}(\mathbf{Prob})$._

Proof.: This follows by the following derivation in $\mathbf{Set}$.

$$\Pi\to\mathbf{Prob}(X,Y)\iff\Pi\to(X\to\mathcal{D}(Y))\iff\Pi\times X\to \mathcal{D}(Y)$$

In fact, the derivation above holds in any Kleisli category for a commutative strong monad.

**Proposition 3.3.4**.: _For any commutative strong monad $M:\mathbf{Set}\to\mathbf{Set}$, the Kleisli category $\mathbf{Kl}(M)$ is monoidal and we have:_

$$\mathbf{Fam}(\mathbf{Kl}(M))\simeq\mathbf{Para}(\mathbf{Kl}(M))$$

_i.e. the notions of internal and external parametrization for Kleisli categories coincide._

#### Open games

We now review the theory of open games [10, 1]. Starting from the definition of lenses, open games are obtained in two steps. First an open game is a family of lenses parametrized by a set of _strategies_: for each strategy the forward part of the lens says how the agent turns observations into moves and the backward part says how it computes a payoff given the outcome of its actions. Second, this family of lenses is equipped with a _best response_ function indicating the optimal strategies for the agent in a given context.

**Definition 3.3.5** (Family of lenses).: _A family of lenses over a symmetric monoidal category $\mathbf{C}$ is a morphism in $\mathbf{Fam}(\mathbf{Lens}(\mathbf{C}))$. Explicitly, a family of lenses $P:(X,S)\to(Y,R)$ is given by a function $P:\Pi\to\mathbf{Lens}(\mathbf{C})((X,S),(Y,R))$ for some set of parameters $\Pi$._

Recall the definition of _context_ for lenses given in 3.2.5. Let us use the notation $\mathbb{C}((X,S),(Y,R))$ for the set of contexts of lenses $(X,S)\to(Y,R)$.

**Definition 3.3.6** (Best response).: _A best response function for a family of lenses $P:(X,S)\to(Y,R)$ is a function of the following type:_

$$B:\mathbb{C}((X,S),(Y,R))\to\mathcal{P}(P)$$

_Thus $B$ takes as input a context and outputs a predicate on the set of parameters (or strategies)._

**Definition 3.3.7** (Open game).: _[_1_]_ _An open game $\mathcal{G}:(X,R)\to(Y,O)$ over a symmetric monoidal category $\mathbf{C}$ is a family of lenses $\left\{\left.\left[\pi,v_{\pi}\right]\right.\right\}_{\pi\in P_{\mathcal{G}}}$ in $\mathbf{C}$ equipped with a best response function $B_{\mathcal{G}}$._

**Proposition 3.3.8**.: _[_21_]_ _Open games over $\mathbf{C}$ form a symmetric monoidal category denoted $\mathbf{Game}(\mathbf{C})$._

Proof.: See [21] for details on the proof and the composition of best responses in this general case. 

The category $\mathbf{Game}(\mathbf{C})$ admits a graphical calculus developed in [1] which is the same as the one for lenses described in Section 3.2.1.. Each morphism is represented as a box with covariant wires for observations in $X$ and moves in $Y$, and contravariant wires for rewards in $R$ (called utilities in [19]) and satisfaction in $S$ (called coutilities in [19]).

(3.18)

These boxes can be composed in parallel, indicating that the players make a move simultaneously, or in sequence, indicating that the second player can observe the first player's move.

(3.19)

Of particular interest to us is the category of open games over $\mathbf{Prob}$. Since we focus on this category for the rest of the chapter we will use the notation $\mathbf{Game}:=\mathbf{Game}(\mathbf{Prob})$. In this category the best response function is easier to specify, since contexts factor as in Proposition 3.2.6.

**Proposition 3.3.9**.: _A context for an open game in $\mathbf{Game}(\mathbf{Prob})$$(X,S)\rightarrow(Y,R)$ is given by a stochastic lens $[p,k]:(1,X)\rightarrow(Y,R)$ or explicitly by a pair of channels $p:1\rightarrow\mathcal{D}(M\times X)$ and $k:M\times Y\rightarrow\mathcal{D}(R)$._

Proof.: This follows from Proposition 3.2.6. 

With this simpler notation for contexts as pairs $[p,k]$ we can define the composition of best responses for open games.

**Definition 3.3.10**.: _[_21_, Definition 3.18]_ _Given open games $(X,S)\xrightarrow{\mathcal{G}}(Y,R)\xrightarrow{\mathcal{H}}(Z,O)$ the composition of their best responses is given by the cartesian product:_

$$B_{\mathcal{G}\cdot\mathcal{H}}([p,k])=B_{\mathcal{G}}([p,\mathcal{H}\cdot k]) \times B_{\mathcal{H}}([p\cdot\mathcal{G},k])\subseteq\Pi_{\mathcal{G}}\times \Pi_{\mathcal{H}}$$

_where $\Pi_{\mathcal{G}}$ and $\Pi_{\mathcal{H}}$ are the corresponding sets of strategies._

We can now define a notion of utility-maximising agent

**Definition 3.3.11** (Utility-maximising agent).: _An (expected) utility maximising agent is a morphism $c:(X,1)\rightarrow(Y,\mathbb{R})$ in $\mathbf{Game}$ given by the following data:_1. $\pi\in\Pi=X\to\mathcal{D}(Y)$ _is the set of strategies._
2. $f_{\pi}^{+}:X\to\mathcal{D}(A):x\mapsto\pi(x)$__
3. $f_{\pi}^{-}:\mathbb{R}\to 1$ _is the discard map._
4. $B:([p:1\to M\times X,\,k:M\times Y\to\mathbb{R}])=\mathtt{argmax}_{\pi\in P}( \mathbb{E}(p;\mathtt{id}_{M}\otimes f_{\pi};k))$__

_where $\mathtt{argmax}:\mathbb{R}^{\Pi}\to\mathcal{P}(\Pi)$._

Note that it is sufficient to specify the input type $X$ and output type $Y$ in order to define a utility-maximising agent $(X,1)\to(Y,\mathbb{R})$ in $\mathbf{Game}$.

**Example 3.3.12** (Classifier utility).: _We model a classifier $X\to\mathcal{D}(Y)$ as a utility-maximising agent $c:(X,1)\to(Y,\mathbb{R})$. Assume that $Y$ has a metric $d:Y\times Y\to\mathbb{R}$. Given a dataset of pairs, i.e. a distribution $K\in\mathcal{D}(X\times Y)$, we can define a context $[K,k]$ for $c$ by setting $k=-d$, as shown in the following pair of equivalent diagrams:_

_where $(p,K|_{X})$ is the disintegration of $K$ along $X$. This yields a distribution over the real numbers $\mathbb{R}$ corresponding to the utility that classifier $c$ gets in its approximation of $K|_{X}$. The best response function for $c$ in this context is given by:_

$$B([K,k])=\mathtt{argmax}_{c}\mathbb{E}(-K;\mathtt{id}_{Y}\otimes c;d)$$

_Maximising this expectation corresponds to minimising the average distance between the true label $y\in Y$ and the predicted label $c(x)$ for $(x,y)$ distributed as in the dataset $K\in\mathcal{D}(X\times Y)$._

**Example 3.3.13** (Generator/Discriminator).: _Fix a grammar $G$, a feature set $Y$ with a distance function $d:Y\times Y\to\mathbb{R}$ and a disribution $p\in\mathcal{D}(Y)$. We model a generator $G:Y\to\mathcal{D}\mathcal{L}(G)$ and a discriminator $D:\mathcal{L}(G)\to\mathcal{D}(Y)$ as utility-maximising agents and compose them as in the following diagram:_

_Where $-:\mathbb{R}\to\mathbb{R}$ is multiplication by $-1$. This yields an adversarial (or zero-sum) game between the generator and the discriminator. Assuming $G$ and $D$ are utility-maximising agents, the best response function for this closed game is given by:_

$$\mathtt{argmax}_{G}(\mathbb{E}_{y\in p}(d(y,D(G(y))))\times\mathtt{argmax}_{ D}(-\mathbb{E}_{y\in p}(d(y,D(G(y)))))$$ _where we use the notation $\mathbb{E}_{y\in p}$ to indicate the expectation (over the real numbers) where $y$ is distributed according to $p\in\mathcal{D}(Y)$. Thus we can see that the game reaches an equilibrium when the discriminator $D$ can always invert the generator $G$, and the generator cannot choose any strategy to change this. Implementing $G$ and $D$ as neural networks yields the generative adversarial architecture of Goodfellow et al. [13] which is used to solve a wide range of NLP tasks, see [14] for a survey. In Section 3.4.2, we will see how this architecture can be used for question answering._

In the remainder of this chapter, we will work interchangeably in the category of families of stochastic lenses $\mathbf{Fam}(\mathbf{Lens}(\mathbf{Prob}))$ or in $\mathbf{Game}(\mathbf{Prob})$. The only difference between these categories is that the latter has morphisms equipped with a best response function and a predefined way of composing them. As we will see, this definition of best response is not suited to formalising repeated games and the category of families of stochastic lenses gives a more flexible approach.

#### Markov decisions

We now study Markov decision processes (MDP) [15] as parametrized stochastic lenses. These are central in reinforcement learning, they model a situation in which a single agent makes decisions in a stochastic environment with the aim of maximising its expected long-term reward. An MDP is simply an MRP 3.2.7 parametrised by a set of actions.

**Definition 3.3.14** (Mdp).: _A Markov decision process with states in $X$ and actions in $A$ is given by the following data:_

1. _a transition_ $T:A\times X\rightarrow\mathcal{D}(X)$__
2. _a reward function_ $R:A\times X\rightarrow\mathcal{D}(\mathbb{R})$__
3. _a discount factor_ $\gamma\in[0,1)$__

A _policy_ is a function $\pi:X\rightarrow\mathcal{D}(Y)$ which represents a strategy for the agent: it yields a distribution over the actions $\pi(x)\in\mathcal{D}(Y)$ for each state $x\in X$. Given a policy $\pi\in\Pi=X\rightarrow\mathcal{D}(Y)$, the MDP induces an MRP which runs through the state space $X$ by choosing actions according to $\pi$ and collecting rewards. Thus, we can formalise an MDP as a family of MRPs parametrized by the policies $\Pi$, i.e. a morphism $P_{\pi}:(X,\mathbb{R})\rightarrow(X,\mathbb{R})$ in $\mathbf{Fam}(\mathbf{Lens}(\mathbf{Prob}))$, given by the following composition:

(3.20) The aim of the agent is to maximise its expected discounted reward. Given a policy $\pi$, the MRP $P_{\pi}$ induces a value function $v_{\pi}=\mathtt{value}(P_{\pi}):X\to\mathbb{R}$, as defined in Section 3.2. Again, we have that the _Bellman expectation equation_ holds:

$$\tikzfig{eq:Bellman 

#### Repeated games

The definition of MDP given above captures a _single_ agent interacting in a fixed environment with no agency. In real-world situations however, the environment consists itself in a collection of agents which also make choices so as to maximise their expected reward.

In order to allow many agents interacting in an environment, we break up the definition of MDPs above, and isolate the part that is making decisions from the _environment_ part. We pack the transition $T$, reward $R$ and discount factor $\gamma$ into one lens called environment and given by:

$$E=[T,R_{\gamma}]:(X\times A,\mathbb{R})\rightarrow(X,\mathbb{R})$$

where $R_{\gamma}:X\times A\times\mathbb{R}\rightarrow\mathbb{R}$ is defined by

$$R_{\gamma}(x,a,r)=R(x,a)+\gamma r$$

This allows to isolate the decision part, seen as an open game of the following type:

$$D:(X,1)\rightarrow(A,\mathbb{R})$$

which represents an agent turning states in $X$ into actions in $A$ and receiving rewards in $\mathbb{R}$. Explicitly we have the following definition.

**Definition 3.3.16** (Decision process).: _A decision process $D$ with state space $X$, action space $A$ and discount factor $\gamma$ is a utility maximising agent $D:(X,1)\rightarrow(A,\mathbb{R})$_

Composing $D$ with the environment $E$ as in the following diagram, we get back precisely the definition of MDP.

(3.22)

We can now consider a situation in which many decision processes interact in an environment.

Stochastic games, a.k.a Markov games, were introduced by Shapley in the 1950s [23]. They can be seen as a generalisation of MDPs, even though they appeared before the work of Bellman [1].

**Definition 3.3.17** (Stochastic game).: _A stochastic game is given by the following data:_

1. _A number_ $k$ _of players, a set of states_ $X$ _and a discount factor_ $\gamma$_,_
2. _a set of actions_ $A_{i}$ _for each player_ $i\in\{0,\ldots,k-1\}$_,_
3. _a transition function_ $T:X\times A_{0}\times\cdots\times A_{k}\rightarrow\mathcal{D}(X)$_,__._
4. _a reward function_ $R:X\times A_{0}\times\cdots\times A_{k}\to\mathbb{R}^{k}$_._

The game is played in stages. At each stage, every player observes the current state in $X$ and chooses an action in $A_{i}$, then "Nature" changes the state of the game using transition $T$ and every player is rewarded according to $R$. It is easy express this repeated game as a parallel composition of decision processes $D_{i}$ followed by the environment $[T,R_{\gamma}]$ in **Game**. As an example, we give the diagram for a two-player zero-sum stochastic game.

(3.23)

In this case, one can see directly from the diagram, that the zero-sum stochastic game induces an MDP with action set $\Pi_{0}\times\Pi_{1}$ given by pairs of policies from players $0$ and $1$. A consequence of this is that one can prove the Shapley equations [10], the analogue of the Bellman equation of MDPs, for determining the equilibria of the game.

Note that stochastic games only allow players to make moves in parallel, i.e. at every stage the move of player $i$ is independent of the other players' moves. The generality provided by this compositional approach allows to consider repeated stochastic games in which moves are made in sequence, as in the following example.

**Example 3.3.18** (Wittgenstein's builders).: _[_111_]_ _Consider a builder and an apprentice at work on the building site. The builder gives orders to his apprentice, who needs to implement them by acting on the state of the building site. In order to model this language game we start by fixing a grammar $G$ for orders, e.g. the regular grammar defined by the following labelled graph:_

_This defines a language for orders $\mathcal{L}(G)$ given by the paths $s_{0}\to o$ in the graph above. The builder observes the state of the building site $S$ and produces an order in $\mathcal{L}(G)$, we can model it as a channel $\pi_{B}:S\to\mathcal{DL}(G)$. We assume that the builder has a project $P$, i.e. a subset of the possible configurations of the building site that he finds satisfactory $P\subseteq S$. We can model these preferences with a utility function $u_{P}:S\to\mathbb{R}$, which computes the distance between the current state of the building site and the desired states in $P$. The builder wants to get the project done as soon as possible and he discounts the expected future rewards by a discount factor $\gamma\in[0,1)$. This data defines a stochastic lens given by the following composition:_

_The apprentice receives an order in $\mathcal{L}(G)$ and uses it to modify the state of the building site $S$. We can model this as a probabilistic channel $\pi_{A}:\mathcal{L}(G)\times S\to\mathcal{D}(S)$. This data defines the following stochastic lens:_

_We assume that the apprentice is satisfied when the builder is, i.e. the utilities of the builder are fed directly into the apprentice. This defines a repeated game, with strategy profiles given by pairs $(\pi_{B},\pi_{A})$, given by the following diagram:_

_This example can be extended and elaborated in different directions. For example, the policy for the apprentice $\pi_{A}$ could be modeled as a functor $F:G\to\mathbf{Set}$ with $F(s_{0})=1$ and $F(o)=S\to\mathcal{D}(S)$ so that grammatical orders in $\mathcal{L}(G)$ are mapped to channels that change the configuration of the building site. Another aspect is the builder's strategy $\pi_{B}:S\to\mathcal{L}(G,o)$ which could be modeled as a generation process from a probabilistic context-free grammar. Also the choice of state space $S$ is interesting, it could be a discrete minecraft-like space, or a continuous space in which words like "cut" have a more precise meaning._ 

### 3.4 Examples

#### Bayesian pragmatics

In this section we study the _Rational Speech Acts_ model of pragmatic reasoning [11, 12, 13, 14]. The idea, based on Grice's conversational implicatures [10], is to model speaker and listener as rational agents who choose words attempting to be informative in context. Implementing this idea involves the interaction of game theory and Bayesian inference. While this model has been criticised on the ground of attributing excessive rationality to human speakers [10], it has received support by psycholinguistic experiments on children and adults [11] and has been applied successfully to a referential expression generation task [13].

Consider a collaborative game between speaker and listener. There are some objects or _referents_ in $R$ lying on the table. The _speaker_ utters a word in $W$ referring to one of the objects. The _listener_ has to guess which object the word refers to. We define this reference game by the following diagram in $\mathbf{Game(Prob)}$.

(3.24)

Where $p$ is a given prior over the referents (encoding the probability that an object $r\in R$ would be referred to) and $\Delta(r,r^{\prime})=1$ if $r=r^{\prime}$ and $\Delta(r,r^{\prime})=0$ otherwise. The strategies for the speaker and listener are given by:

$$P_{0}=R\to\mathcal{D}(W)\qquad P_{1}=W\to\mathcal{D}(R)$$

The speaker is modeled by a utility-maximising agent with strategies $\pi_{0}:R\to\mathcal{D}(W)$ and best response in context $[p\in\mathcal{D}(R\times W),l:R\times W\to\mathbb{B}]$ given by the $\pi:R\to\mathcal{D}(W)$ in the argmax of $\mathbb{E}(l\circ(\pi\otimes\mathtt{id}_{R})\circ p)$. Similarly for the listener with the roles of $R$ and $W$ interchanged. Composing speaker and listener according to (3.24) we obtain a closed game for which the best response is a predicate over the strategy profiles $(\pi_{0}:R\to\mathcal{D}(W),\pi_{1}:W\to\mathcal{D}(R))$ indicating the subset of Nash equilibria.

$$\mathtt{argmax}_{\pi_{0},\pi_{1}}(\mathbb{E}(\Delta\circ((\pi_{1}\circ\pi_{0} )\otimes\mathtt{id}_{R})\circ\mathtt{copy}\circ p)$$ (3.25)

If we assume that the listener uses Bayesian inference to recover the speaker's intended referent, then we are in a Nash equilibrium.

**Proposition 3.4.1**.: _If $\pi_{1}:W\to\mathcal{D}(R)$ is a Bayesian inverse of $\pi_{0}:R\to\mathcal{D}(W)$ along $p\in\mathcal{D}(R)$ then $(\pi_{0},\pi_{1})$ is a Nash equilibrium for (3.24)._Proof.: Since $\pi_{1}$ is a Bayesian inverse of $\pi_{0}$ along $p$, Equation (3.2) implies the following equality:

$$\begin{array}{c}\includegraphics[width=142.

 Note that the experiment of Frank and Goodman involved three referents (a blue square, a blue circle and a green square) and four words (blue, green, square and circle). The sets $R(w)$ and $W(r)$ were calculated by hand, and computing the Bayesian inverse of $\pi_{0}$ in this case was an easy task. However, as the number of possible referents and words grows, Bayesian inversion quickly becomes computationally intractable without some underlying compositional structure mediating it.

#### Adversarial question answering

In this section we define a game modelling an interaction between a teacher and a student. The teacher poses questions that the student tries to answer. We assume that the student is incentivised to answer questions correctly, whereas the teacher is incentivised to ask hard questions, resulting in an _adversarial_ question answering game (QA). For simplicity, we work in a deterministic setting, i.e. we work in the category of in . We first give a syntactic definition of QA as a diagram, we then instantiate the definition with respect to monoidal grammars and functorial models, which allows us to compute the Nash equilibria for the game.

Let us fix three sets $C$, $Q$, $A$ for corpora (i.e. lists of facts), questions and answers respectively. Let $U$ be a set of utilities, which can be taken to be $\mathbb{R}$ or $\mathbb{B}$. A _teacher_ is a utility-maximising player where each strategy represents a function turning facts from the corpus into pairs of questions and answers. A _student_ is a utility-maximising player where each strategy represents a way of turning questions into answers. A _marker_ is a strategically trivial open game with trivial play function and a coplay function defined as where $d:A\times A\to U$ is a given metric on $A$. Finally, we model a _corpus_ as a strategically trivial open game with play function given by $\pi_{f}(*)=f\in C$. All these open games are composed to obtain a _question answering game_ in the following way.

(3.26)

Intuitively, the teacher produces a question from the corpus and gives it to the student who uses his strategy to answer. The marker will receive the correct answer from the teacher together with the answer that the student produced, and output two utilities. The utility of the teacher will be the distance between the student's answer and the correct answer; the utility of the student will be the exact opposite of this quantity. In this sense, question answering is a zero-sum game.

We now instantiate the game defined above with respect to a pregroup grammar $G=(B,V,D,s)$ with a fixed question type $z\in B$. The strategies of the student are given by relational models with $\sigma(z)=1$, so that given a question $q:u\to z$, $\sigma(q)\in\mathcal{P}(1)=\mathbb{B}$ is the student's answer. In practice, the student may only have a subset of models available to him so we set $\Sigma_{\mathcal{S}}\subseteq\{\sigma:G\to\mathbf{Rel}:\;\sigma(z)=1\}$.

 We assume that the teacher has the particularly simple role of picking a question-answer pair from a set of possible ones, i.e. we take the corpus $C$ to be a list of question-answer pairs $(q,a)$ for $q:u\to z$ and $a\in A$. For simplicity, we assume $q$ is a yes/no question and $a$ is a boolean answer, i.e. $Q=\mathcal{L}(G,z)$ and $A=\mathbb{B}$. The strategies of the teacher are given by indices $\Sigma_{\mathcal{T}}=\{\,0,1,\ldots n\,\}$, so that the play function $\pi_{\mathcal{T}}:\Sigma_{\mathcal{T}}\times(Q\times A)^{*}\to Q\times A$ picks the question-answer pair indicated by the index. The marker will compare the teacher's answer $a$ with the student's answer $\sigma(q)\in\mathbb{B}$ using the metric $d:A\times A\to\mathbb{B}::(a_{0},a_{1})\mapsto(a_{0}=a_{1})$ and output boolean utilities in $U=\mathbb{B}$. Plugging these open games as in (3.26), we can compute the set of equilibria by composing the equilibrium functions of its components.

$$E_{\mathcal{G}}=\{(j,\sigma)\in\Sigma_{\mathcal{T}}\times\Sigma_{\mathcal{S}} :\,j\in\underset{i\in\Sigma_{\mathcal{T}}}{\operatorname{argmax}}\,a_{i} \neq\sigma(q_{i})\wedge\sigma\in\underset{\sigma\in\Sigma_{\mathcal{S}}}{ \operatorname{argmax}}(a_{j}=\sigma(q_{j}))\}$$

Therefore, in a Nash equilibrium, the teacher will ask the question that the student, even with his best guess, is going to answer in the worst way. The student, on the other hand, is going to answer as correctly as possible.

We analyse the possible outcomes of this game.

1. There is a pair $(q_{i},a_{i})$ in $C$ that the student cannot answer correctly, i.e. $\forall\sigma\in\Sigma_{\mathcal{S}}:\,\sigma(q_{i})\neq a_{i}$. Then $i$ is a winning strategy for the teacher and $(i,\sigma)$ is a Nash equilibrium, for any choice of strategy $\sigma$ for the student. If no such pair exists, then we fall into one of the following cases.
2. The corpus is consistent -- i.e. $\exists\sigma:G\to\mathbf{Rel}$ such that $\forall i\cdot\sigma(q_{i})=a_{i}$ -- and the student has access to the model $\sigma$ that answers all the possible questions correctly. Then, the strategy profile $(j,\sigma)$ is a Nash equilibrium and a winning strategy for the student for any choice $j$ of the teacher.
3. For any choice $i$ of the teacher, the student has a model $\sigma_{i}$ that answers $q_{i}$ correctly. And viceversa, for any strategy $\sigma$ of the student there is a choice $j$ of the teacher such that $\sigma(q_{j})\neq a_{j}$. Then the set $E_{\mathcal{G}}$ is empty, there is no Nash equilibrium.

To illustrate the last case, consider a situation where the corpus $C=\{\,(q_{0},a_{0}),(q_{1},a_{1})\,\}$ has only two elements and the student has only two models $\Sigma_{\mathcal{S}}=\{\,\sigma_{0},\sigma_{1}\,\}$ such that $\sigma_{i}(q_{i})=a_{i}$ for $i\in\{\,0,1\,\}$ but $\sigma_{0}(q_{1})\neq a_{1}$ and $\sigma_{1}(q_{0})\neq a_{0}$. Then we're in a _matching pennies_ scenario, both the teacher and the student have no incentive to choose any one of their strategies and there is no Nash equilibrium. This problem can be ruled out if we allowed the players in the game to have _mixed strategies_, which can be achieved with minor modifications of the open game formalism [14].

#### Word sense disambiguation

Word sense disambiguation (WSD) is the task of choosing the correct sense of a word in the context of a sentence. WSD has been argued to be an AI-complete task in the sense that it can be used to simulate other NLP task [15]. In [16], Tripodi and Navigli use methods from evolutionary game theory to obtain state-of-the-art results in the WSD task. The idea is to model WSD as a collaborative game between words where strategies are word senses. In their model, the interactions between words are weighted by how close the words are in a piece of text. In this section, we propose a compositional alternative, where the interaction between words is mediated by the grammatical structure of the sentence they occur in. Concretely, we show that how to build a functor $J:G_{W}\rightarrow\mathbf{Game}$ given a functorial model $F:G_{V}\rightarrow\mathbf{Prob}$ where $G_{W}$ is a grammar for words and $G_{V}$ a grammar for word-senses. Given a sentence $u\in\mathcal{L}(G_{V})$, the functor $J$ constructs a collaborative game where the Nash equilibrium is given by a choice of sense for each word in $u$ that maximises the score of the sentence $u$ in $F$.

We work with a _dependency grammar_$G\subseteq(B+V)\times B^{*}$ where $B$ is a set of basic types and $V$ a set of words, see Definition 1.5.15. Recall from Proposition 1.5.21, that dependency relations are acyclic, i.e. we can always turn the dependency graph into a tree as in the following example:

This means that any sentence parsed with a dependency grammar induces a directed acyclic graph of dependencies. We may represent these parses in the free monoidal category $\mathbf{MC}(\tilde{G})$ where $\tilde{G}=B^{*}\gets V\to B$ is the signature with boxes labelled by words $v\in V$ with inputs given by the symbols that depend on $v$ and a single output given by the symbol on which $v$ depends, as shown in Proposition 1.5.21.

Taking dependency grammars seriously, it is sensible to interpret them directly in the category $\mathbf{Prob}$ of conditional distributions. Indeed, a functor $F:\tilde{G}\rightarrow\mathbf{Prob}$ is defined on objects by a choice of feature set $F(x)$ for every symbol $x\in B$ and on words $v:y_{1}y_{2}\ldots y_{n}\to x$ by a conditional distribution $F(v):F(y_{1})\times F(y_{2})\ldots F(y_{n})\rightarrow\mathcal{D}(F(x))$ indicating the probability that word $v$ has a particular feature given that the words it depends on have particular features. Thus a parsed sentence is sent to a _Bayesian network_ where the independency constraints of the network are induced by the dependency structure of the sentence. One may prove formally that functors $\tilde{G}\rightarrow\mathbf{Prob}$ induce Bayesian networks using the work of Fong [13].

We are now ready to describe the WSD procedure. Fix a set $W$ of words and $V$ of word-senses with a dependency grammar $G_{V}$ for senses and a relation $\Sigma\subseteq W\times V$, assigning to each word $w\in W$ the set of its senses $\Sigma(w)\subseteq V$. Composing $G_{V}$ with $\Sigma$, we get a grammar for words $G_{W}$. Assume we are given a functorial model $F:G_{V}\rightarrow\mathbf{Prob}$ with $F(s)=2$, i.e. for any grammatical sentence $g:u\to s$, its image $F(g)\in\mathcal{D}(2)=[0,1]$ quantifies how likely it is that the sentence is true. We use $F$ to define a functor $J:G_{W}\rightarrow\mathbf{Game}(\mathbf{Prob})$ such that the Nash equilibrium of the image of any grammatical sentence is an assignement of each word to a sense maximising the overall score of the sentence. On objects $J$ is defined by $J(b)=(F(b),2)$ for any $b\in B$. Given a word $w:y_{1}\ldots y_{n}\to x$ in $G_{W}$ its image under $J$ is given by an open game $J(w):(F(y_{1})\times F(y_{2})\ldots F(y_{n}),2^{n})\to(F(x),2)$ with strategy set $\Sigma(w)$ (i.e. strategies for word $w\in W$ are given by its senses $v\in\Sigma(w)\subseteq V$) defined for every strategy $v\in\Sigma(w)$ by the following lens:

The best response function in context $[p,k]$ is given by:

$$B_{J(w,t)}(k)=\operatorname{\mathtt{argmax}}_{v\in\Sigma(w)}(\mathbb{E}(p;J(w )(v);k))$$

Then given a grammatical sentence $g\in\mathbf{MC}(G_{W})$ we get a closed game $J(g):1\to 1$ with equilibrium given by:

$$B_{J(g)}=\operatorname{\mathtt{argmax}}_{v_{i}\in\Sigma(w_{i})}(F(g[w_{i}:=v_ {i}]))$$

where $u[w_{i}:=v_{i}]$ denotes the sentence obtained by replacing each word $w_{i}\in W$ with its sense $v_{i}\in\Sigma(w_{i})\subseteq V$. Computing this $\operatorname{\mathtt{argmax}}$ corresponds precisely to choosing a sense for each word such that the probability that the sentence is true is maximised.

**Example 3.4.4**.: _As an example take the following dependency grammar $G$ with $\tilde{G}$ given by the following morphisms:_

$$\text{Bob}:1\to n\:,\:\text{draws}=n\otimes n\to s\:,\:a:1\to d\:,\: \text{card}:d\to n\:,\:\text{diagram}:d\to n$$ (3.27)

_The relation $\Sigma\subseteq W\times V$ between words and senses is given by:_

$$\Sigma(\text{Bob})=\{\text{Bob Coecke},\:\text{Bob Ciaffone}\}\quad\Sigma( \text{draws})=\{\text{draws (pull)},\:\text{draws (picture)}\}$$

_and $\Sigma(x)=\{\,x\,\}$ for $x\in\{\text{card},\:\text{diagram},\:a\}$. The functor $F:G_{V}\to\mathbf{Prob}$ is defined on objects by $F(d)=1$ (i.e. determinants are discarded), $F(s)=2$ and $F(n)=\{\text{Bob Coecke},\:\text{Bob Ciaffone},\:\text{card},\:\text{diagram}\}$ and on arrows by:_

$$F(x)(y)=\begin{cases}1&x=y\\ 0&\text{otherwise}\end{cases}.$$

_for $x\in V\setminus\{\text{draws (pull)},\:\text{draws (picture)}\}$. The image of the two possible senses of "draw" are given by the following table:_

\begin{tabular}{|c|c|c|c|} \hline _subject_ & _object_ & _draws (picture)_ & _draws (pull)_ \\ \hline _Bob Coecke_ & _card_ & $0.1$ & $0.3$ \\ \hline _Bob Ciaffone_ & _card_ & $0.1$ & $0.9$ \\ \hline _Bob Coecke_ & _diagram_ & $0.9$ & $0.2$ \\ \hline _Bob Ciaffone_ & _diagram_ & $0.1$ & $0.1$ \\ \hline \end{tabular}

 _Note that a number in $[0,1]$ is sufficient to specify a distribution in $\mathcal{D}(2)$. We get a corresponding functor $J:G_{W}\rightarrow\mathbf{Game}(\mathbf{Prob})$ which maps "Bob draws a diagram" as follows:_

_$$\begin{array}{c}\includegraphics[width=142.26378pt]{figs/Bob_draw_diagram_} \end{array}\quad\mapsto\quad\begin{array}{c}\includegraphics[width=142.26378pt]{figs/Bob_draw_diagram_} \end{array}$$_

_Composing the channels according to the structure of the diagram we get a distribution in $\mathcal{D}(2)$ parametrized over the choice of sense for each word. According to the table above, the expectation of this distribution is maximised when the strategy of the word "Bob" is the sense "Bob Coecke" and the strategy of "draws" is the sense "draws (picture)"._ 

## References

* [AD19] AbadiMartin and PlotkinGordon D. "A Simple Differentiable Programming Language". In: _Proceedings of the ACM on Programming Languages_ (Dec. 2019). doi: 10.1145/3371106.
* [Abr12] Samson Abramsky. _No-Cloning In Categorical Quantum Mechanics_. Mar. 2012. arXiv: 0910.2401 [quant-ph].
* [AC07] Samson Abramsky and Bob Coecke. "A Categorical Semantics of Quantum Protocols". In: _arXiv:quant-ph/0402130_ (Mar. 2007). arXiv: quant-ph/0402130.
* [AC08] Samson Abramsky and Bob Coecke. "Categorical Quantum Mechanics". In: _arXiv:0808.1023 [quant-ph]_ (Aug. 2008). arXiv: 0808.1023 [quant-ph].
* [AJ95] Samson Abramsky and Achim Jung. "Domain Theory". In: _Handbook of Logic in Computer Science (Vol. 3): Semantic Structures_. USA: Oxford University Press, Inc., Jan. 1995, pp. 1-168.
* [AT10] Samson Abramsky and Nikos Tzevelekos. "Introduction to Categories and Categorical Logic". In: _arXiv:1102.1313 [cs, math]_ 813 (2010), pp. 3-94. doi: 10.1007/978-3-642-12821-9_1. arXiv: 1102.1313 [cs, math].
* [AR18] Takanori Adachi and Yoshihiro Ryu. "A Category of Probability Spaces". In: _arXiv:1611.03630 [math]_ (Oct. 2018). arXiv: 1611.03630 [math].
* [ALM07] Dorit Aharonov, Zeph Landau, and Johann Makowsky. "The Quantum FFT Can Be Classically Simulated". In: _arXiv:quant-ph/0611156_ (Mar. 2007). arXiv: quant-ph/0611156.
* [Ajd35] K. Ajdukiewiz. "Die Syntaktische Konnexitat". In: _Studia Philosophica_ (1935), pp. 1-27.
* [ACL19] Afra Alishahi, Grzegorz Chrupala, and Tal Linzen. "Analyzing and Interpreting Neural Networks for NLP: A Report on the First BlackboxNLP Workshop". In: _arXiv:1904.04063 [cs, stat]_ (Apr. 2019). arXiv: 1904.04063 [cs, stat].
* [AMY16] Noga Alon, Shay Moran, and Amir Yehudayoff. "Sign Rank versus VC Dimension". In: _arXiv:1503.07648 [math]_ (July 2016). arXiv: 1503.07648 [math].
* [Ane12] Irving H. Anellis. "How Peircean Was the "Fregean' Revolution" in Logic?" In: _arXiv:1201.0353 [math]_ (Jan. 2012). arXiv: 1201.0353 [math].

* [AL10] Itai Arad and Zeph Landau. "Quantum Computation and the Evaluation of Tensor Networks". In: _arXiv:0805.0040 [quant-ph]_ (Feb. 2010). arXiv: 0805.0040 [quant-ph].
* [AFZ14] Yoav Artzi, Nicholas Fitzgerald, and Luke Zettlemoyer. "Semantic Parsing with Combinatory Categorial Grammars". en-us. In: _Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing: Tutorial Abstracts_. Oct. 2014.
* [Ask19] John Ole Askedal. _Peirce and Valency Grammar_. en. De Gruyter Mouton, May 2019. Chap. Signs of Humanity / L'homme et ses signes, pp. 1343-1348.
* [BCR18] John C. Baez, Brandon Coya, and Franciscus Rebro. "Props in Network Theory". In: _arXiv:1707.08321 [math-ph]_ (June 2018). arXiv: 1707.08321 [math-ph].
* [BE14] John C. Baez and Jason Erbele. "Categories in Control". In: _arXiv:1405.6881 [quant-ph]_ (May 2014). arXiv: 1405.6881 [quant-ph].
* [BP17] John C. Baez and Blake S. Pollard. "A Compositional Framework for Reaction Networks". In: _Reviews in Mathematical Physics_ 29.09 (Oct. 2017), p. 1750028. doi: 10.1142/S0129055X17500283. arXiv: 1704.02051.
* [BM02] J. F. Baget and M. L. Mugnier. "Extensions of Simple Conceptual Graphs: The Complexity of Rules and Constraints". In: _Journal of Artificial Intelligence Research_ 16 (June 2002), pp. 425-465. doi: 10.1613/jair.918. arXiv: 1106.1800.
* [BCB14] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. "Neural Machine Translation by Jointly Learning to Align and Translate". In: _arXiv e-prints_ 1409 (Sept. 2014), arXiv:1409.0473.
* [BKV18] Krzysztof Bar, Aleks Kissinger, and Jamie Vicary. "Globular: An Online Proof Assistant for Higher-Dimensional Rewriting". In: _Logical Methods in Computer Science ; Volume 14_ (2018), Issue 1, 18605974. doi: 10.23638/LMCS-14(1:8)2018. arXiv: 1612.01093.
* [Bar53] Yehoshua Bar-Hillel. "A Quasi-Arithmetical Notation for Syntactic Description". In: _Language_ 29.1 (1953), pp. 47-58. doi: 10.2307/410452.
* [BGG12] Chitta Baral, Marcos Alvarez Gonzalez, and Aaron Gottesman. "The Inverse Lambda Calculus Algorithm for Typed First Order Logic Lambda Calculus and Its Application to Translating English to FOL". en. In: _Correct Reasoning: Essays on Logic-Based AI in Honour of Vladimir Lifschitz_. Ed. by Esra Erdem, Joohyung Lee, Yuliya Lierler, and David Pearce. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2012, pp. 40-56. doi: 10.1007/978-3-642-30743-0_4.
* [BP83] Jon Barwise and John Perry. _Situations and Attitudes_. MIT Press, 1983.
* [Bel57] Richard Bellman. "A Markovian Decision Process". In: _Journal of Mathematics and Mechanics_ 6.5 (1957), pp. 679-684.
* [Ben+03] Yoshua Bengio, Rejean Ducharme, Pascal Vincent, and Christian Janvin. "A Neural Probabilistic Language Model". In: _The Journal of Machine Learning Research_ 3.null (Mar. 2003), pp. 1137-1155.

 * [BS18] Anton Benz and Jon Stevens. "Game-Theoretic Approaches to Pragmatics". In: _Annual Review of Linguistics_ 4.1 (2018), pp. 173-191. doi:10.1146/annurev-linguistics-011817-045641.
* [Ber+13] Jonathan Berant, Andrew Chou, Roy Frostig, and Percy Liang. "Semantic Parsing on Freebase from Question-Answer Pairs". In: _Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing_. Seattle, Washington, USA: Association for Computational Linguistics, Oct. 2013, pp. 1533-1544.
* [BLG16] Leon Bergen, Roger Levy, and Noah Goodman. "Pragmatic Reasoning through Semantic Inference". en. In: _Semantics and Pragmatics_ 9.0 (May 2016), EARLY ACCESS. doi:10.3765/sp.9.20.
* [BMT15] Jacob D. Biamonte, Jason Morton, and Jacob W. Turner. "Tensor Network Contractions for #SAT". In: _Journal of Statistical Physics_ 160.5 (Sept. 2015), pp. 1389-1404. doi:10.1007/s10955-015-1276-z. arXiv:1405.7375.
* [Bia+00] Anna Maria Bianucci, Alessio Micheli, Alessandro Sperduti, and Antonina Starita. "Application of Cascade Correlation Networks for Structures to Chemistry". en. In: _Applied Intelligence_ 12.1 (Jan. 2000), pp. 117-147. doi:10.1023/A:1008368105614.
* [BPV06] Aaron Bohannon, Benjamin C. Pierce, and Jeffrey A. Vaughan. "Relational Lenses: A Language for Updatable Views". In: _Proceedings of the Twenty-Fifth ACM SIGMOD-SIGACT-SIGART Symposium on Principles of Database Systems_. PODS '06. New York, NY, USA: Association for Computing Machinery, June 2006, pp. 338-347. doi:10.1145/1142351.1142399.
* [Bol+08] Kurt Bollacker, Colin Evans, Praveen Paritosh, Tim Sturge, and Jamie Taylor. "Freebase: A Collaboratively Created Graph Database for Structuring Human Knowledge". In: _Proceedings of the 2008 ACM SIGMOD International Conference on Management of Data_. SIGMOD '08. New York, NY, USA: Association for Computing Machinery, June 2008, pp. 1247-1250. doi:10.1145/1376616.1376746.
* [BHZ19] Joe Bolt, Jules Hedges, and Philipp Zahn. "Bayesian Open Games". In: _arXiv:1910.03656 [cs, math]_ (Oct. 2019). arXiv: 1910.03656 [cs, math].
* [Bon+16] Filippo Bonchi, Fabio Gadducci, Aleks Kissinger, Pawel Sobocinski, and Fabio Zanasi. "Rewriting modulo Symmetric Monoidal Structure". In: _Proceedings of the 31st Annual ACM/IEEE Symposium on Logic in Computer Science_ (July 2016), pp. 710-719. doi:10.1145/2933575.2935316. arXiv:1602.06771.
* [Bon+20] Filippo Bonchi, Fabio Gadducci, Aleks Kissinger, Pawel Sobocinski, and Fabio Zanasi. "String Diagram Rewrite Theory I: Rewriting with Frobenius Structure". In: _arXiv:2012.01847 [cs, math]_ (Dec. 2020). arXiv: 2012.01847 [cs, math].
* [Bon+21] Filippo Bonchi, Fabio Gadducci, Aleks Kissinger, Pawel Sobocinski, and Fabio Zanasi. "String Diagram Rewrite Theory II: Rewriting with Symmetric Monoidal Structure". In: _arXiv:2104.14686 [cs, math]_ (Apr. 2021). arXiv: 2104.14686 [cs, math].

 * [BPS17] Filippo Bonchi, Dusko Pavlovic, and Pawel Sobocinski. "Functorial Semantics for Relational Theories". In: _arXiv:1711.08699 [cs, math]_ (Nov. 2017). arXiv: 1711.08699 [cs, math].
* [BSS18] Filippo Bonchi, Jens Seeber, and Pawel Sobocinski. "Graphical Conjunctive Queries". In: _arXiv:1804.07626 [cs]_ (Apr. 2018). arXiv: 1804.07626 [cs].
* [BSZ14] Filippo Bonchi, Pawe$\backslash$l Sobocinski, and Fabio Zanasi. "A Categorical Semantics of Signal Flow Graphs". In: _International Conference on Concurrency Theory_. Springer, 2014, pp. 435-450.
* [BCW14] Antoine Bordes, Sumit Chopra, and Jason Weston. "Question Answering with Subgraph Embeddings". In: _Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)_. Doha, Qatar: Association for Computational Linguistics, Oct. 2014, pp. 615-620. doi: 10.3115/v1/D14-1067.
* Volume 2_. NIPS'13. Red Hook, NY, USA: Curran Associates Inc., Dec. 2013, pp. 2787-2795.
* [Bor+09] M. Bordewich, M. Freedman, L. Lovasz, and D. Welsh. "Approximate Counting and Quantum Computation". In: _arXiv:0908.2122 [cs]_ (Aug. 2009). arXiv: 0908.2122 [cs].
* [BPM15] Samuel R. Bowman, Christopher Potts, and Christopher D. Manning. "Recursive Neural Networks Can Learn Logical Semantics". In: _Proceedings of the 3rd Workshop on Continuous Vector Space Models and Their Compositionality_. Beijing, China: Association for Computational Linguistics, July 2015, pp. 12-21. doi: 10.18653/v1/W15-4002.
* [Bra+18] James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris Leary, Dougal Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-Milne, and Qiao Zhang. _JAX: composable transformations of Python+NumPy programs_. Version 0.2.5. 2018. url: http://github.com/google/jax.
* [BT00] Geraldine Brady and Todd H. Trimble. "A Categorical Interpretation of C.S. Peirce's Propositional Logic Alpha". en. In: _Journal of Pure and Applied Algebra_ 149.3 (June 2000), pp. 213-239. doi: 10.1016/S0022-4049(98)00179-0.
* [Bre+82] Joan Bresnan, Ronald M. Kaplan, Stanley Peters, and Annie Zaenen. "Cross-Serial Dependencies in Dutch". In: _Linguistic Inquiry_ 13.4 (1982), pp. 613-635.
* [Bro+20] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. "Language Models Are Few-Shot Learners". In: _arXiv:2005.14165 [cs]_ (July 2020). arXiv: 2005.14165 [cs].
* [Bul17] Andrei A. Bulatov. "A Dichotomy Theorem for Nonuniform CSPs". In: _arXiv:1703.03021 [cs]_ (2017). doi: 10.1109/FOCS.2017.37. arXiv: 1703.03021 [cs].
* [BM20] Samuele Buro and Isabella Mastroeni. "On the Semantic Equivalence of Language Syntax Formalisms". en. In: _Theoretical Computer Science_ 840 (Nov. 2020), pp. 234-248. doi: 10.1016/j.tcs.2020.08.022.
* [Bus07] Wojciech Buszkowski. "Type Logics and Pregroups". en. In: _Studia Logica_ 87.2 (Dec. 2007), pp. 145-169. doi: 10.1007/s11225-007-9083-4.
* [Bus16] Wojciech Buszkowski. "Syntactic Categories and Types: Ajdukiewicz and Modern Categorial Grammars". In: 2016. doi: 10.1163/9789004311763_004.
* [BM07] Wojciech Buszkowski and Katarzyna Moroz. "Pregroup Grammars and Context-Free Grammars". In: 2007.
* [CW18] Liwei Cai and William Yang Wang. "KBGAN: Adversarial Learning for Knowledge Graph Embeddings". In: _Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)_. New Orleans, Louisiana: Association for Computational Linguistics, June 2018, pp. 1470-1480. doi: 10.18653/v1/N18-1133.
* [Can06] R. Ferrer i Cancho. "Why Do Syntactic Links Not Cross?" en. In: _EPL (Europhysics Letters)_ 76.6 (Nov. 2006), p. 1228. doi: 10.1209/epl/i2006-10406-0.
* [CW87] A. Carboni and R. F. C. Walters. "Cartesian Bicategories I". en. In: _Journal of Pure and Applied Algebra_ 49.1 (Nov. 1987), pp. 11-32. doi: 10.1016/0022-4049(87)90121-6.
* [CL02] Claudia Casadio and Joachim Lambek. "A Tale of Four Grammars". en. In: _Studia Logica_ 71.3 (Aug. 2002), pp. 315-329. doi: 10.1023/A:1020564714107.
* FIDET "76_. Not Known: ACM Press, 1976, pp. 249-264. doi: 10.1145/800296.811515.
* [Cha+22] Jireh Yi-Le Chan, Khean Thye Bea, Steven Mun Hong Leow, Seuk Wai Phoong, and Wai Khuen Cheng. "State of the Art: A Review of Sentiment Analysis Based on Sequential Transfer Learning". In: _Artificial Intelligence Review_ (Apr. 2022). doi: 10.1007/s10462-022-10183-8.
* STOC '77_. Boulder, Colorado, United States: ACM Press, 1977, pp. 77-90. doi: 10.1145/800105.803397.
 * [Cha+09] Philippe Chaput, Vincent Danos, Prakash Panangaden, and Gordon Plotkin. "Approximating Markov Processes by Averaging". en. In: _Automata, Languages and Programming_. Ed. by Susanne Albers, Alberto Marchetti-Spaccamela, Yossi Matias, Sotiris Nikoletseas, and Wolfgang Thomas. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2009, pp. 127-138. doi: 10.1007/978-3-642-02930-1_11.
* [CK15] Jianpeng Cheng and Dimitri Kartsaklis. "Syntax-Aware Multi-Sense Word Embeddings for Deep Compositional Models of Meaning". In: _arXiv:1508.02354 [cs]_ (Aug. 2015). arXiv: 1508.02354 [cs].
* [CJ19] Kenta Cho and Bart Jacobs. "Disintegration and Bayesian Inversion via String Diagrams". In: _Mathematical Structures in Computer Science_ (Mar. 2019), pp. 1-34. doi: 10.1017/S0960129518000488. arXiv: 1709.00322.
* [Cho+15] Francois Chollet et al. _Keras_. 2015. url: https://github.com/fchollet/keras.
* [Cho56] Noam Chomsky. "Three Models for the Description of Language". In: _Journal of Symbolic Logic_ 23.1 (1956), pp. 71-72. doi: 10.2307/2964524.
* [Cho57] Noam Chomsky. _Syntactic Structures_. The Hague: Mouton and Co., 1957.
* [Chu32] Alonzo Church. "A Set of Postulates for the Foundation of Logic". In: _Annals of Mathematics_ 33.2 (1932), pp. 346-366. doi: 10.2307/1968337.
* [Chu36] Alonzo Church. "An Unsolvable Problem of Elementary Number Theory". In: _Journal of Symbolic Logic_ 1.2 (1936), pp. 73-74. doi: 10.2307/2268571.
* [Chu40] Alonzo Church. "A Formulation of the Simple Theory of Types". In: _The Journal of Symbolic Logic_ 5.2 (1940), pp. 56-68. doi: 10.2307/2266170.
* [CM15] Kevin Clark and Christopher D. Manning. "Entity-Centric Coreference Resolution with Model Stacking". In: _Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)_. Beijing, China: Association for Computational Linguistics, July 2015, pp. 1405-1415. doi: 10.3115/v1/P15-1136.
* [CM16] Kevin Clark and Christopher D. Manning. "Deep Reinforcement Learning for Mention-Ranking Coreference Models". In: _Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing_. Austin, Texas: Association for Computational Linguistics, Nov. 2016, pp. 2256-2262. doi: 10.18653/v1/D16-1245.
* [CCS08] Stephen Clark, Bob Coecke, and Mehrnoosh Sadrzadeh. "A Compositional Distributional Model of Meaning". In: _Proceedings of the Second Symposium on Quantum Interaction (QI-2008)_ (2008), pp. 133-140.
* [CCS10] Stephen Clark, Bob Coecke, and Mehrnoosh Sadrzadeh. "Mathematical Foundations for a Compositional Distributional Model of Meaning". In: _A Festschrift for Jim Lambek_. Ed. by J. van Benthem, M. Moortgat, and W. Buszkowski. Vol. 36. Linguistic Analysis. 2010, pp. 345-384. arXiv: 1003.4394.

 * [Cod70] E F Codd. "A Relational Model of Data for Large Shared Data Banks". en. In: 13.6 (1970), p. 11.
* [Coe20] Bob Coecke. "The Mathematics of Text Structure". In: _arXiv:1904.03478 [quant-ph]_ (Feb. 2020). arXiv: 1904.03478 [quant-ph].
* [Coe+18] Bob Coecke, Giovanni de Felice, Dan Marsden, and Alexis Toumi. "Towards Compositional Distributional Discourse Analysis". In: _Electronic Proceedings in Theoretical Computer Science_ 283 (Nov. 2018), pp. 1-12. doi:10.4204/EPTCS.283.1. arXiv: 1811.03277 [cs].
* [Coe+20] Bob Coecke, Giovanni de Felice, Konstantinos Meichanetzidis, and Alexis Toumi. "Foundations for Near-Term Quantum Natural Language Processing". In: _arXiv:2012.03755 [quant-ph]_ (Dec. 2020). arXiv: 2012.03755 [quant-ph].
* [Coe+22] Bob Coecke, Giovanni de Felice, Konstantinos Meichanetzidis, and Alexis Toumi. "How to Make Qubits Speak". In: _Quantum Computing in the Arts and Humanities: An Introduction to Core Concepts, Theory and Applications_. Ed. by Eduardo Reck Miranda. Cham: Springer International Publishing, 2022, pp. 277-297. doi:10.1007/978-3-030-95538-0_8.
* [CK17] Bob Coecke and Aleks Kissinger. _Picturing Quantum Processes: A First Course in Quantum Theory and Diagrammatic Reasoning_. Cambridge: Cambridge University Press, 2017. doi:10.1017/9781316219317.
* [Coe+19] Andy Coenen, Emily Reif, Ann Yuan, Been Kim, Adam Pearce, Fernanda Viegas, and Martin Wattenberg. "Visualizing and Measuring the Geometry of BERT". In: _arXiv:1906.02715 [cs, stat]_ (Oct. 2019). arXiv: 1906.02715 [cs, stat].
* [Cru+21] G. S. H. Cruttwell, Bruno Gavranovic, Neil Ghani, Paul Wilson, and Fabio Zanasi. "Categorical Foundations of Gradient-Based Learning". In: _arXiv:2103.01931 [cs, math]_ (Mar. 2021). arXiv: 2103.01931 [cs, math].
* [Cur61] H. B. Curry. "Some Logical Aspects of Grammatical Structure". In: _Structure Language and Its Mathematical Aspects,_ vol. XII. American Mathematical Society, 1961, pp. 56-68.
* CP 2002_. Ed. by Gerhard Goos, Juris Hartmanis, Jan van Leeuwen, and Pascal Van Hentenryck. Vol. 2470. Berlin, Heidelberg: Springer Berlin Heidelberg, 2002, pp. 310-326. doi:10.1007/3-540-46135-3_21.
* [Dav67a] Donald Davidson. "The Logical Form of Action Sentences". In: _The Logic of Decision and Action_. Ed. by Nicholas Rescher. University of Pittsburgh Press, 1967, pp. 81-95.
* [Dav67b] Donald Davidson. "Truth and Meaning". In: _Synthese_ 17.3 (1967), pp. 304-323.
* [dKM20] Niel de Beaudrap, Aleks Kissinger, and Konstantinos Meichanetzidis. "Tensor Network Rewriting Strategies for Satisfiability and Counting". In: _arXiv:2004.06455 [quant-ph]_ (Apr. 2020). arXiv: 2004.06455 [quant-ph].

 * [de +21] Giovanni de Felice, Elena Di Lavero, Mario Roman, and Alexis Toumi. "Functorial Language Games for Question Answering". In: _Electronic Proceedings in Theoretical Computer Science_ 333 (Feb. 2021), pp. 311-321. doi: 10.4204/EPTCS.333.21. arXiv: 2005.09439 [cs].
* [dMT20] Giovanni de Felice, Konstantinos Meichanetzidis, and Alexis Toumi. "Functorial Question Answering". In: _Electronic Proceedings in Theoretical Computer Science_ 323 (Sept. 2020), pp. 84-94. doi: 10.4204/EPTCS.323.6. arXiv: 1905.07408 [cs, math].
* [dTC21] Giovanni de Felice, Alexis Toumi, and Bob Coecke. "DisCoPy: Monoidal Categories in Python". In: _Electronic Proceedings in Theoretical Computer Science_ 333 (Feb. 2021), pp. 183-197. doi: 10.4204/EPTCS.333.13. arXiv: 2005.02975 [math].
* [De 47] Augustus De Morgan. _Formal Logic: Or, The Calculus of Inference, Necessary and Probable_. en. Taylor and Walton, 1847.
* [DBM15] Wim De Mulder, Steven Bethard, and Marie-Francine Moens. "A Survey on the Application of Recurrent Neural Networks to Statistical Language Modeling". en. In: _Computer Speech & Language_ 30.1 (Mar. 2015), pp. 61-98. doi: 10.1016/j.csl.2014.09.005.
* [DP05] Sylvain Degeilh and Anne Preller. "Efficiency of Pregroups and the French Noun Phrase". en. In: _Journal of Logic, Language and Information_ 14.4 (Oct. 2005), pp. 423-444. doi: 10.1007/s10849-005-1242-2.
* [Del19] Antonin Delpeuch. "Autonomization of Monoidal Categories". In: _arXiv:1411.3827 [cs, math]_ (June 2019). arXiv: 1411.3827 [cs, math].
* [DV19a] Antonin Delpeuch and Jamie Vicary. "Normalization for Planar String Diagrams and a Quadratic Equivalence Algorithm". In: _arXiv:1804.07832 [cs]_ (Sept. 2019). arXiv: 1804.07832 [cs].
* [DEB19] Samuel Desrosiers, Glen Evenbly, and Thomas Baker. "Survey of Tensor Networks". In: (2019), F68.006.
* [Dev+19] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. "BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding". In: _arXiv:1810.04805 [cs]_ (May 2019). arXiv: 1810.04805 [cs].
* [DdR22] Elena Di Lavero, Giovanni de Felice, and Mario Roman. _Monoidal Streams for Dataflow Programming_. Feb. 2022. doi: 10.48550/arXiv.2202.02061. arXiv: 2202.02061 [cs, math].
* [Don+14] Xin Dong, Evgeniy Gabrilovich, Geremy Heitz, Wilko Horn, Ni Lao, Kevin Murphy, Thomas Strohmann, Shaohua Sun, and Wei Zhang. "Knowledge Vault: A Web-Scale Approach to Probabilistic Knowledge Fusion". In: _Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_. KDD '14. New York, NY, USA: Association for Computing Machinery, Aug. 2014, pp. 601-610. doi: 10.1145/2623330.2623623.

 * [Dos+20] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby. "An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale". In: _arXiv:2010.11929 [cs]_ (Oct. 2020). arXiv: 2010.11929 [cs].
* [DV19b] Lawrence Dunn and Jamie Vicary. "Coherence for Frobenius Pseudomonoids and the Geometry of Linear Proofs". In: _arXiv:1601.05372 [cs]_ (2019). doi: 10.23638/LMCS-15(3:5)2019. arXiv: 1601.05372 [cs].
* [Ear70] Jay Earley. "An Efficient Context-Free Parsing Algorithm". In: _Communications of the ACM_ 13.2 (Feb. 1970), pp. 94-102. doi: 10.1145/362007.362035.
* [Edu+18] Sergey Edunov, Myle Ott, Michael Auli, and David Grangier. "Understanding Back-Translation at Scale". In: _Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing_. Brussels, Belgium: Association for Computational Linguistics, Oct. 2018, pp. 489-500. doi: 10.18653/v1/D18-1045.
* [EHL19] Stavros Efthymiou, Jack Hidary, and Stefan Leichenauer. "TensorNetwork for Machine Learning". In: _arXiv:1906.06329 [cond-mat, physics:physics, stat]_ (June 2019). arXiv: 1906.06329 [cond-mat, physics:physics, stat].
* [Ein16] Albert Einstein. "The Foundation of the General Theory of Relativity". en. In: _Annalen Phys._ 49.7 (1916), pp. 769-822. doi: 10.1002/andp.200590044.
* [Eis13] J. Eisert. "Entanglement and Tensor Network States". In: _arXiv:1308.3318 [cond-mat, physics:quant-ph]_ (Sept. 2013). arXiv: 1308.3318 [cond-mat, physics:quant-ph].
* [Ela06] Pradheep Elango. _Coreference Resolution: A Survey_. 2006.
* [Elm90] Jeffrey L. Elman. "Finding Structure in Time". en. In: _Cognitive Science_ 14.2 (1990), pp. 179-211. doi: 10.1207/s15516709cog1402_1.
* [Fat+20] Bahare Fatemi, Perouz Taslakian, David Vazquez, and David Poole. "Knowledge Hypergraphs: Prediction Beyond Binary Relations". In: _arXiv:1906.00137 [cs, stat]_ (July 2020). arXiv: 1906.00137 [cs, stat].
* [Fon13] Brendan Fong. "Causal Theories: A Categorical Perspective on Bayesian Networks". In: _arXiv:1301.6201 [math]_ (Jan. 2013). arXiv: 1301.6201 [math].
* [FJ19] Brendan Fong and Michael Johnson. "Lenses and Learners". In: _arXiv:1903.03671 [cs, math]_ (May 2019). arXiv: 1903.03671 [cs, math].
* [FS18a] Brendan Fong and David I. Spivak. "Graphical Regular Logic". In: _arXiv:1812.05765 [cs, math]_ (Dec. 2018). arXiv: 1812.05765 [cs, math].
* [FS18b] Brendan Fong and David I. Spivak. "Hypergraph Categories". In: _arXiv:1806.08304 [cs, math]_ (June 2018). arXiv: 1806.08304 [cs, math].
* [FST19] Brendan Fong, David I. Spivak, and Remy Tuyeras. "Backprop as Functor: A Compositional Perspective on Supervised Learning". In: _arXiv:1711.10455 [cs, math]_ (May 2019). arXiv: 1711.10455 [cs, math].

 * [Fow08] Timothy A. D. Fowler. "Efficiently Parsing with the Product-Free Lambek Calculus". In: _Proceedings of the 22nd International Conference on Computational Linguistics (Coling 2008)_. Manchester, UK: Coling 2008 Organizing Committee, Aug. 2008, pp. 217-224.
* [Fox76] Thomas Fox. "Coalgebras and Cartesian Categories". In: _Communications in Algebra_ 4.7 (Jan. 1976), pp. 665-667. doi: 10.1080/00927877608822127.
* [FG12] Michael C. Frank and Noah D. Goodman. "Predicting Pragmatic Reasoning in Language Games". en. In: _Science_ 336.6084 (May 2012), pp. 998-998. doi: 10.1126/science.1218633.
* [Fra09] Michael Franke. "Signal to Act: Game Theory in Pragmatics". In: (Jan. 2009).
* [FJ16] Michael Franke and Gerhard Jager. "Probabilistic Pragmatics, or Why Bayes' Rule Is Probably Important for Pragmatics". en. In: _Zeitschrift fur Sprachwissenschaft_ 35.1 (June 2016), pp. 3-44. doi: 10.1515/zfs-2016-0002.
* [FGS98] P. Frasconi, M. Gori, and A. Sperduti. "A General Framework for Adaptive Processing of Data Structures". In: _IEEE Transactions on Neural Networks_ 9.5 (Sept. 1998), pp. 768-786. doi: 10.1109/72.712151.
* [FLW00] Michael Freedman, Michael Larsen, and Zhenghan Wang. "A Modular Functor Which Is Universal for Quantum Computation". In: _arXiv:quant-ph/0001108_ (Feb. 2000). arXiv: quant-ph/0001108.
* [FKW02] Michael H. Freedman, Alexei Kitaev, and Zhenghan Wang. "Simulation of Topological Field Theories by Quantum Computers". In: _Communications in Mathematical Physics_ 227.3 (June 2002), pp. 587-603. doi: 10.1007/s002200200635. arXiv: quant-ph/0001071.
* [Fre14] Gottlob Frege. "Letter to Jourdain". In: _The Frege Reader_. Oxford: Blackwell Publishing, 1914, pp. 319-321.
* [Fri20] Tobias Fritz. "A Synthetic Approach to Markov Kernels, Conditional Independence and Theorems on Sufficient Statistics". In: _arXiv:1908.07021 [cs, math, stat]_ (Mar. 2020). arXiv: 1908.07021 [cs, math, stat].
* [Gai65] Haim Gaifman. "Dependency Systems and Phrase-Structure Systems". en. In: _Information and Control_ 8.3 (June 1965), pp. 304-337. doi: 10.1016/S0019-9958(65)90232-9.
* [GJ90] Michael R. Garey and David S. Johnson. _Computers and Intractability; A Guide to the Theory of NP-Completeness_. New York, NY, USA: W. H. Freeman & Co., 1990.
* [Gat+13] A. Gatt, R. van Gompel, K. van Deemter, and E. J. Krahmer. "Are We Bayesian Referring Expression Generators?" English. In: _Proceedings of the CogSci workshop on the production of referring expressions: bridging the gap between cognitive and computational approaches to reference (PRE-CogSci 2013)_ (2013), pp. 1-6.
* [GHC98] Niyu Ge, John Hale, and Eugene Charniak. "A Statistical Approach to Anaphora Resolution". In: _Sixth Workshop on Very Large Corpora_. 1998.

 * [GSC00] Felix A. Gers, Jurgen Schmidhuber, and Fred Cummins. "Learning to Forget: Continual Prediction with LSTM". In: _Neural Computation_ 12.10 (Oct. 2000), pp. 2451-2471. doi: 10.1162/089976600300015015.
* [Gha+18] Neil Ghani, Jules Hedges, Viktor Winschel, and Philipp Zahn. "Compositional game theory". In: _Proceedings of the 33rd Annual ACM/IEEE Symposium on Logic in Computer Science_. 2018, pp. 472-481. doi: 10.3982/ECTA6297.
* [Gha+19] Neil Ghani, Clemens Kupke, Alasdair Lambert, and Fredrik Nordvall Forsberg. "Compositional Game Theory with Mixed Strategies: Probabilistic Open Games Using a Distributive Law". English. In: _Applied Category Theory Conference 2019_. July 2019.
* [Gla+19] Ivan Glasser, Ryan Sweke, Nicola Pancotti, Jens Eisert, and J. Ignacio Cirac. "Expressive Power of Tensor-Network Factorizations for Probabilistic Modeling, with Applications from Hidden Markov Models to Quantum Machine Learning". In: _arXiv:1907.03741 [cond-mat, physics:quant-ph, stat]_ (Nov. 2019). arXiv: 1907.03741 [cond-mat, physics:quant-ph, stat].
* [Gog+77] J. A. Goguen, J. W. Thatcher, E. G. Wagner, and J. B. Wright. "Initial Algebra Semantics and Continuous Algebras". In: _Journal of the ACM_ 24.1 (Jan. 1977), pp. 68-95. doi: 10.1145/321992.321997.
* [GK96] C. Goller and A. Kuchler. "Learning Task-Dependent Distributed Representations by Backpropagation through Structure". In: _Proceedings of International Conference on Neural Networks (ICNN'96)_. Vol. 1. June 1996, 347-352 vol.1. doi: 10.1109/ICNN.1996.548916.
* [Goo+14] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. "Generative Adversarial Nets". In: _Advances in Neural Information Processing Systems 27_. Ed. by Z. Ghahramani, M. Welling, C. Cortes, N. D. Lawrence, and K. Q. Weinberger. Curran Associates, Inc., 2014, pp. 2672-2680.
* [GS13] Noah Goodman and Andreas Stuhlmuller. "Knowledge and Implicature: Modeling Language Understanding as Social Cognition". In: _Topics in cognitive science_ 5 (Jan. 2013), pp. 173-184. doi: 10.1111/tops.12007.
* [GS14] Alexander Gouberman and Markus Siegle. "Markov Reward Models and Markov Decision Processes in Discrete and Continuous Time: Performance Evaluation and Optimization". en. In: _Stochastic Model Checking. Rigorous Dependability Analysis Using Model Checking Techniques for Stochastic Systems: International Autumn School, ROCKS 2012, Vahrn, Italy, October 22-26, 2012, Advanced Lectures_. Ed. by Anne Remke and Marielle Stoelinga. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2014, pp. 156-241. doi: 10.1007/978-3-662-45489-3_6.
* [GK20] Johnnie Gray and Stefanos Kourtis. "Hyper-Optimized Tensor Network Contraction". In: _arXiv:2002.01935 [cond-mat, physics:physics, physics:quant-ph]_ (Feb. 2020). arXiv: 2002.01935 [cond-mat, physics:physics, physics:quant-ph].

 * [GS11] Edward Grefenstette and Mehrnoosh Sadrzadeh. "Experimental Support for a Categorical Compositional Distributional Model of Meaning". In: _The 2014 Conference on Empirical Methods on Natural Language Processing._ 2011, pp. 1394-1404. arXiv: 1106.4058.
* [Gre65] Sheila A. Greibach. "A New Normal-Form Theorem for Context-Free Phrase Structure Grammars". In: _Journal of the ACM_ 12.1 (Jan. 1965), pp. 42-52. doi: 10.1145/321250.321254.
* [Gri67] Herbert Paul Grice. "Logic and Conversation". In: _Studies in the Way of Words_. Ed. by Paul Grice. Harvard University Press, 1967, pp. 41-58.
* [HOD12] Sherzod Hakimov, Salih Atilay Oto, and Erdogan Dogdu. "Named Entity Recognition and Disambiguation Using Linked Data and Graph-Based Centrality Scoring". In: _Proceedings of the 4th International Workshop on Semantic Web Information Management_. SWIM '12. New York, NY, USA: Association for Computing Machinery, May 2012, pp. 1-7. doi: 10.1145/2237867.2237871.
* [HL79] Per-Kristian Halvorsen and William A. Ladusaw. "Montague's 'Universal Grammar': An Introduction for the Linguist". In: _Linguistics and Philosophy_ 3.2 (1979), pp. 185-223.
* [Har+20] Charles R. Harris, K. Jarrod Millman, Stefan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett, Allan Haldane, Jaime Fernandez del Rio, Mark Wiebe, Pearu Peterson, Pierre Gerard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer Abbasi, Christoph Gohlke, and Travis E. Oliphant. "Array programming with NumPy". In: _Nature_ 585.7825 (Sept. 2020), pp. 357-362. doi: 10.1038/s41586-020-2649-2.
* [HR76] W.s. Hatcher and T. Rus. "Context-Free Algebras". In: _Journal of Cybernetics_ 6.1-2 (Jan. 1976), pp. 65-77. doi: 10.1080/01969727608927525.
* Gesammelte Werke. Berlin Heidelberg: Springer-Verlag, 1935. doi: 10.1007/978-3-540-76807-4.
* [HS20] Nathan Haydon and Pawel Sobocinski. "Compositional Diagrammatic First-Order Logic". In: _11th International Conference on the Theory and Application of Diagrams (DIAGRAMS 2020)_. 2020. url: https://www.ioc.ee/~pawel/papers/peirce.pdf.
* [Hay64] David G. Hays. "Dependency Theory: A Formalism and Some Observations". In: _Language_ 40.4 (1964), pp. 511-525. doi: 10.2307/411934.
* [Hed17] Jules Hedges. "Coherence for Lenses and Open Games". In: _arXiv:1704.02230 [cs, math]_ (Sept. 2017). arXiv: 1704.02230 [cs, math].

 * [HL18] Jules Hedges and Martha Lewis. "Towards Functorial Language-Games". In: _Electronic Proceedings in Theoretical Computer Science_ 283 (Nov. 2018), pp. 89-102. doi: 10.4204/eptcs.283.7.
* [HV19] Chris Heunen and Jamie Vicary. _Categories for Quantum Theory: An Introduction_. Oxford University Press, 2019.
* [Hob78] Jerry R. Hobbs. "Resolving Pronoun References". en. In: _Lingua_ 44.4 (Apr. 1978), pp. 311-338. doi: 10.1016/0024-3841(78)90006-2.
* [HS97] Sepp Hochreiter and Jurgen Schmidhuber. "Long Short-Term Memory". In: _Neural computation_ 9 (Dec. 1997), pp. 1735-80. doi: 10.1162/neco.1997.9.8.1735.
* [Hon+20] Matthew Honnibal, Ines Montani, Sofie Van Landeghem, and Adriane Boyd. _spaCy: Industrial-strength Natural Language Processing in Python_. 2020. doi: 10.5281/zenodo.1212303.
* [HJ12] Roger A Horn and Charles R Johnson. _Matrix Analysis_. Cambridge University Press, 2012.
* [How60] Roland Howard. _Dynamic Programming and Markov Processes_. MIT press, Cambridge, 1960.
* [Imm87] Neil Immerman. "Languages That Capture Complexity Classes". In: _SIAM Journal of Computing_ 16 (1987), pp. 760-778.
* [JKZ18] Bart Jacobs, Aleks Kissinger, and Fabio Zanasi. "Causal Inference by String Diagram Surgery". In: _arXiv:1811.08338 [cs, math]_ (Nov. 2018). arXiv: 1811.08338 [cs, math].
* [JZ21] Theo M. V. Janssen and Thomas Ede Zimmermann. "Montague Semantics". In: _The Stanford Encyclopedia of Philosophy_. Ed. by Edward N. Zalta. Summer 2021. Metaphysics Research Lab, Stanford University, 2021.
* [JSV04] Mark Jerrum, Alistair Sinclair, and Eric Vigoda. "A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries". In: _Journal of the ACM_ 51.4 (July 2004), pp. 671-697. doi: 10.1145/1008731.1008738.
* [JRW12] Michael Johnson, Robert Rosebugh, and R. J. Wood. "Lenses, Fibrations and Universal Translations!". en. In: _Mathematical Structures in Computer Science_ 22.1 (Feb. 2012), pp. 25-42. doi: 10.1017/S0960129511000442.
* [Jos85] Aravind K. Joshi. "Tree Adjoining Grammars: How Much Context-Sensitivity Is Required to Provide Reasonable Structural Descriptions?" In: _Natural Language Parsing: Psychological, Computational, and Theoretical Perspectives_. Ed. by Arnold M. Zwicky, David R. Dowty, and Lauri Karttunen. Studies in Natural Language Processing. Cambridge University Press, 1985, pp. 206-250. doi: 10.1017/CBO9780511597855.007.
* [JS91] A. Joyal and R. Street. "The Geometry of Tensor Calculus, I". In: _Advances in Mathematics_ 88.1 (1991), pp. 55-112. doi: 10.1016/0001-8708(91)90003-p.

 * [Jum+21] John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Zidek, Anna Potapenko, Alex Bridgland, Clemens Meyer, Simon A. A. Kohl, Andrew J. Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen, David Reiman, Ellen Clancy, Michal Zielinski, Martin Steinegger, Michalina Pacholska, Tamas Berghammer, Sebastian Bodenstein, David Silver, Oriol Vinyals, Andrew W. Senior, Koray Kavukcuoglu, Pushmeet Kohli, and Demis Hassabis. "Highly Accurate Protein Structure Prediction with AlphaFold". In: _Nature_ 596.7873 (Aug. 2021), pp. 583-589. doi: 10.1038/s41586-021-03819-2.
* [JM08] Daniel Jurafsky and James Martin. _Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition_. Vol. 2. United States: Prentice Hall PTR, Feb. 2008.
* [KGB14] Nal Kalchbrenner, Edward Grefenstette, and Phil Blunsom. "A Convolutional Neural Network for Modelling Sentences". In: _Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_. Baltimore, Maryland: Association for Computational Linguistics, June 2014, pp. 655-665. doi: 10.3115/v1/P14-1062.
* [Kar+21] Dimitri Kartsaklis, Ian Fan, Richie Yeung, Anna Pearson, Robin Lorenz, Alexis Toumi, Giovanni de Felice, Konstantinos Meichanetzidis, Stephen Clark, and Bob Coecke. "Lambeq: An Efficient High-Level Python Library for Quantum NLP". In: _arXiv:2110.04236 [quant-ph]_ (Oct. 2021). arXiv: 2110.04236 [quant-ph].
* [Kea+16] Steven Kearnes, Kevin McCloskey, Marc Berndl, Vijay Pande, and Patrick Riley. "Molecular Graph Convolutions: Moving beyond Fingerprints". In: _Journal of Computer-Aided Molecular Design_ 30.8 (Aug. 2016), pp. 595-608. doi: 10.1007/s10822-016-9938-8.
* [Kv19] Aleks Kissinger and John van de Wetering. "PyZX: Large Scale Automated Diagrammatic Reasoning". In: _arXiv:1904.04735 [quant-ph]_ (Apr. 2019). arXiv: 1904.04735 [quant-ph].
* [Kv20] Aleks Kissinger and John van de Wetering. "Reducing T-Count with the ZX-Calculus". In: _Physical Review A_ 102.2 (Aug. 2020), p. 022406. doi: 10.1103/PhysRevA.102.022406. arXiv: 1903.10477.
* [KH25] H. A. Kramers and W. Heisenberg. "Uber die Streuung von Strahlung durch Atome". de. In: _Zeitschrift fur Physik_ 31.1 (Feb. 1925), pp. 681-708. doi: 10.1007/BF02980624.
* [KM14] Jayant Krishnamurthy and Tom M. Mitchell. "Joint Syntactic and Semantic Parsing with Combinatory Categorial Grammar". In: _Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_. Baltimore, Maryland: Association for Computational Linguistics, June 2014, pp. 1188-1198. doi: 10.3115/v1/P14-1112.
* [KSJ18] Marco Kuhlmann, Giorgio Satta, and Peter Jonsson. "On the Complexity of CCG Parsing". In: _Computational Linguistics_ 44.3 (Sept. 2018), pp. 447-482. doi: 10.1162/coli_a_00324.

 * [Kus06] Boris A. Kushner. "The Constructive Mathematics of A. A. Markov". In: _The American Mathematical Monthly_ 113.6 (2006), pp. 559-566. doi: 10.2307/27641983.
* [Lam86] J. Lambek. "Cartesian Closed Categories and Typed $\lambda$-Calculi". en. In: _Combinators and Functional Programming Languages_. Ed. by Guy Cousineau, Pierre-Louis Curien, and Bernard Robinet. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 1986, pp. 136-175. doi: 10.1007/3-540-17184-3_44.
* [Lam88] J. Lambek. "Categorical and Categorical Grammars". en. In: _Categorial Grammars and Natural Language Structures_. Ed. by Richard T. Oehrle, Emmon Bach, and Deirdre Wheeler. Studies in Linguistics and Philosophy. Dordrecht: Springer Netherlands, 1988, pp. 297-317. doi: 10.1007/978-94-015-6878-4_11.
* [Lam99a] J. Lambek. "Type Grammar Revisited". en. In: _Logical Aspects of Computational Linguistics_. Ed. by Alain Lecomte, Francois Lamarche, and Guy Perrier. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 1999, pp. 1-27. doi: 10.1007/3-540-48975-4_1.
* [LS86] J. Lambek and P. J. Scott. _Introduction to Higher Order Categorical Logic_. Vol. 7. USA: Cambridge University Press, 1986.
* [Lam08] Jim Lambek. _From Word to Sentence: A Computational Algebraic Approach to Grammar_. Open Access Publications. Polimetrica, 2008.
* [Lam58] Joachim Lambek. "The Mathematics of Sentence Structure". In: _The American Mathematical Monthly_ 65.3 (Mar. 1958), pp. 154-170. doi: 10.1080/00029890.1958.11989160.
* [Lam68] Joachim Lambek. "Deductive Systems and Categories". en. In: _Mathematical systems theory_ 2.4 (Dec. 1968), pp. 287-318. doi: 10.1007/BF01703261.
* [Lam99b] Joachim Lambek. "Deductive Systems and Categories in Linguistics". en. In: _Logic, Language and Reasoning: Essays in Honour of Dov Gabbay_. Ed. by Hans Jurgen Ohlbach and Uwe Reyle. Trends in Logic. Dordrecht: Springer Netherlands, 1999, pp. 279-294. doi: 10.1007/978-94-011-4574-9_12.
* [LF04] Shalom Lappin and C. Fox. "An Expressive First-Order Logic for Natural Language Semantics". en. In: _Institute of Philosophy_ (2004).
* [LHH20] Md Tahmid Rahman Laskar, Jimmy Xiangji Huang, and Enamul Hoque. "Contextualized Embeddings Based Transformer Encoder for Sentence Similarity Modeling in Answer Selection Task". In: _Proceedings of the 12th Language Resources and Evaluation Conference_. Marseille, France: European Language Resources Association, May 2020, pp. 5505-5514.
* [Law63] F: W. Lawvere. "Functorial Semantics of Algebraic Theories". PhD thesis. Columbia University, 1963.
* [Lee+17] Kenton Lee, Luheng He, Mike Lewis, and Luke Zettlemoyer. "End-to-End Neural Coreference Resolution". In: _Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing_. Copenhagen, Denmark: Association for Computational Linguistics, Sept. 2017, pp. 188-197. doi: 10.18653/v1/D17-1018.

 - A Large-Scale, Multilingual Knowledge Base Extracted from Wikipedia". In: _Semantic Web Journal_ 6 (Jan. 2014). doi: 10.3233/SW-140134.
* [Lew69] David K. Lewis. _Convention: A Philosophical Study_. Wiley-Blackwell, 1969.
* [Li+16] Jiwei Li, Will Monroe, Alan Ritter, Michel Galley, Jianfeng Gao, and Dan Jurafsky. "Deep Reinforcement Learning for Dialogue Generation". en. In: _arXiv:1606.01541 [cs]_ (Sept. 2016). arXiv: 1606.01541 [cs].
* [Li+17] Jiwei Li, Will Monroe, Tianlin Shi, Sebastien Jean, Alan Ritter, and Dan Jurafsky. "Adversarial Learning for Neural Dialogue Generation". In: _arXiv:1701.06547 [cs]_ (Sept. 2017). arXiv: 1701.06547 [cs].
* [LB02] Edward Loper and Steven Bird. _NLTK: The Natural Language Toolkit_. May 2002. doi: 10.48550/arXiv.cs/0205028. arXiv: cs/0205028.
* [Lor+21] Robin Lorenz, Anna Pearson, Konstantinos Meichanetzidis, Dimitri Kartsaklis, and Bob Coecke. "QNLP in Practice: Running Compositional Models of Meaning on a Quantum Computer". In: _arXiv:2102.12846 [quant-ph]_ (Feb. 2021). arXiv: 2102.12846 [quant-ph].
* [Ma+19] Yunpu Ma, Volker Tresp, Liming Zhao, and Yuyi Wang. "Variational Quantum Circuit Model for Knowledge Graphs Embedding". In: _arXiv:1903.00556 [quant-ph]_ (Feb. 2019). arXiv: 1903.00556 [quant-ph].
* [Mac71] S. Mac Lane. _Categories for the Working Mathematician_. Springer Verlag, 1971.
* [MS99] Christopher D. Manning and Hinrich Schutze. _Foundations of Statistical Natural Language Processing_. Cambridge, MA, USA: MIT Press, 1999.
* [Mar+15] Martin Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo, Zhifeng Chen, Craig Citro, Greg S. Corrado, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Ian Goodfellow, Andrew Harp, Geoffrey Irving, Michael Isard, Yangqing Jia, Rafal Jozefowicz, Lukasz Kaiser, Manjunath Kudlur, Josh Levenberg, Dandelion Mane, Rajat Monga, Sherry Moore, Derek Murray, Chris Olah, Mike Schuster, Jonathon Shlens, Benoit Steiner, Ilya Sutskever, Kunal Talwar, Paul Tucker, Vincent Vanhoucke, Vijay Vasudevan, Fernanda Viegas, Oriol Vinyals, Pete Warden, Martin Wattenberg, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng. _TensorFlow: Large-Scale Machine Learning on Heterogeneous Systems_. Software available from tensorflow.org. 2015. url: https://www.tensorflow.org/.
* [Mei+21] Konstantinos Meichanetzidis, Stefano Gogioso, Giovanni de Felice, Nicolo Chiappori, Alexis Toumi, and Bob Coecke. "Quantum Natural Language Processing on Near-Term Quantum Computers". In: _Electronic Proceedings in Theoretical Computer Science_ 340 (Sept. 2021), pp. 213-229. doi: 10.4204/EPTCS.340.11. arXiv: 2005.04147 [quant-ph].

 * [Mei+20] Konstantinos Meichanetzidis, Alexis Toumi, Giovanni de Felice, and Bob Coecke. "Grammar-Aware Question-Answering on Quantum Computers". In: _arXiv:2012.03756 [quant-ph]_ (Dec. 2020). arXiv: 2012.03756 [quant-ph].
* [Meu+17] Aaron Meurer, Christopher P. Smith, Mateusz Paprocki, Ondrej Certik, Sergey B. Kirpichev, Matthew Rocklin, AMiT Kumar, Sergiu Ivanov, Jason K. Moore, Sartaj Singh, Thilina Rathnayake, Sean Vig, Brian E. Granger, Richard P. Muller, Francesco Bonazzi, Harsh Gupta, Shivam Vats, Fredrik Johansson, Fabian Pedregosa, Matthew J. Curry, Andy R. Terrel, Stepan Roucka, Ashutosh Saboo, Isuru Fernando, Sumith Kulal, Robert Cimrman, and Anthony Scopatz. "SymPy: symbolic computing in Python". In: _PeerJ Computer Science_ 3 (Jan. 2017), e103. doi: 10.7717/peerj-cs.103.
* [MSS04] Alessio Micheli, Diego Sona, and Alessandro Sperduti. "Contextual Processing of Structured Data by Recursive Cascade Correlation". eng. In: _IEEE transactions on neural networks_ 15.6 (Nov. 2004), pp. 1396-1410. doi: 10.1109/TNN.2004.837783.
* [Mik+10] Tomas Mikolov, Martin Karafiat, Lukas Burget, Jan Cernocky, and Sanjeev Khudanpur. "Recurrent Neural Network Based Language Model". In: _Proceedings of the 11th Annual Conference of the International Speech Communication Association, INTERSPEECH 2010_. Vol. 2. Jan. 2010, pp. 1045-1048.
* [Mil56] George A. Miller. "The Magical Number Seven, plus or Minus Two: Some Limits on Our Capacity for Processing Information". In: _Psychological Review_ 63.2 (1956), pp. 81-97. doi: 10.1037/h0043158.
* [MP15] Will Monroe and Christopher Potts. "Learning in the Rational Speech Acts Model". In: _arXiv:1510.06807 [cs]_ (Oct. 2015). arXiv: 1510.06807 [cs].
* [Mon70a] Richard Montague. "English as a Formal Language". In: _Linguaggi Nella Societa e Nella Tecnica_. Ed. by Bruno Visentini. Edizioni di Communita, 1970, pp. 188-221.
* [Mon70b] Richard Montague. "Universal Grammar". en. In: _Theoria_ 36.3 (1970), pp. 373-398. doi: 10.1111/j.1755-2567.1970.tb00434.x.
* [Mon73] Richard Montague. "The Proper Treatment of Quantification in Ordinary English". In: _Approaches to Natural Language_. Ed. by K. J. J. Hintikka, J. Moravcsic, and P. Suppes. Dordrecht: Reidel, 1973, pp. 221-242.
* [Moo88] Michael Moortgat. _Categorial Investigations: Logical and Linguistic Aspects of the Lambek Calculus_. 9. Walter de Gruyter, 1988.
* [MR12a] Richard Moot and Christian Retore. "Lambek Calculus and Montague Grammar". en. In: _The Logic of Categorial Grammars: A Deductive Account of Natural Language Syntax and Semantics_. Ed. by Richard Moot and Christian Retore. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2012, pp. 65-99. doi: 10.1007/978-3-642-31555-8_3.

 * [MR12b] Richard Moot and Christian Retore. "The Multimodal Lambek Calculus". en. In: _The Logic of Categorial Grammars: A Deductive Account of Natural Language Syntax and Semantics_. Ed. by Richard Moot and Christian Retore. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2012, pp. 149-191. doi: 10.1007/978-3-642-31555-8_5.
* [MR12c] Richard Moot and Christian Retore. "The Non-Associative Lambek Calculus". en. In: _The Logic of Categorial Grammars: A Deductive Account of Natural Language Syntax and Semantics_. Ed. by Richard Moot and Christian Retore. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2012, pp. 101-147. doi: 10.1007/978-3-642-31555-8_4.
* [Mor11] Katarzyna Moroz. "A Savateev-Style Parsing Algorithm for Pregroup Grammars". en. In: _Formal Grammar_. Ed. by Philippe de Groote, Markus Egg, and Laura Kallmeyer. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2011, pp. 133-149. doi: 10.1007/978-3-642-20169-1_9.
* [Nav09] Roberto Navigli. "Word Sense Disambiguation: A Survey". In: _ACM Computing Surveys_ 41.2 (Feb. 2009), 10:1-10:69. doi: 10.1145/1459352.1459355.
* [NTK11] Maximilian Nickel, Volker Tresp, and Hans-Peter Kriegel. "A Three-Way Model for Collective Learning on Multi-Relational Data". In: _Proceedings of the 28th International Conference on International Conference on Machine Learning_. ICML'11. Madison, WI, USA: Omnipress, June 2011, pp. 809-816.
* [OGo19] Bryan O'Gorman. "Parameterization of Tensor Network Contraction". In: _arXiv:1906.00013 [quant-ph]_ (2019), 19 pages. doi: 10.4230/LIPIcs.TQC.2019.10. arXiv: 1906.00013 [quant-ph].
* [OBW88] Richard T. Oehrle, E. Bach, and Deirdre Wheeler, eds. _Categorial Grammars and Natural Language Structures_. en. Studies in Linguistics and Philosophy. Springer Netherlands, 1988. doi: 10.1007/978-94-015-6878-4.
* [OK19] Ilsang Ohn and Yongdai Kim. "Smooth Function Approximation by Deep Neural Networks with General Activation Functions". en. In: _Entropy_ 21.7 (July 2019), p. 627. doi: 10.3390/e21070627.
* [OMK19] Daniel W. Otter, Julian R. Medina, and Jugal K. Kalita. "A Survey of the Usages of Deep Learning in Natural Language Processing". In: _arXiv:1807.10854 [cs]_ (Dec. 2019). arXiv: 1807.10854 [cs].
* [Par76] Barbara Partee. _Montague Grammar_. en. Elsevier, 1976. doi: 10.1016/C2013-0-11289-5.
* [Pas+19] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala. "PyTorch: An Imperative Style, High-Performance Deep Learning Library". In: _Advances in Neural Information Processing Systems 32_. Ed. by H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alche-Buc, E. Fox, and R. Garnett. Curran Associates, Inc., 2019, pp. 8024-8035. url: http://papers.neurips.cc/paper/9015-pytorch-an-imperative-style-high-performance-deep-learning-library.pdf.
* [Pei65] C. S. Peirce. "On a New List of Categories". In: _Proceedings of the American Academy of Arts and Sciences_ 7 (1865), pp. 287-298. doi: 10.2307/20179567.
* [Pei97] Charles S. Peirce. "The Logic of Relatives". In: _The Monist_ 7.2 (1897), pp. 161-217.
* [Pei06] Charles Santiago Sanders Peirce. "Prolegomena to an Apology for Pragmaticism". In: _The Monist_ 16.4 (1906), pp. 492-546.
* [Pen71] Roger Penrose. "Applications of Negative Dimensional Tensors". en. 1971.
* [Pen93] M. Pentus. "Lambek Grammars Are Context Free". In: _[1993] Proceedings Eighth Annual IEEE Symposium on Logic in Computer Science_. June 1993, pp. 429-433. doi: 10.1109/LICS.1993.287565.
* [PV17] Vasily Pestun and Yiannis Vlassopoulos. "Tensor Network Language Model". In: _arXiv:1710.10248 [cond-mat, stat]_ (Oct. 2017). arXiv: 1710.10248 [cond-mat, stat].
* [PGW17] Matthew Pickering, Jeremy Gibbons, and Nicolas Wu. "Profunctor Optics: Modular Data Accessors". In: _The Art, Science, and Engineering of Programming_ 1.2 (Apr. 2017), p. 7. doi: 10.22152/programming-journal.org/2017/1/7. arXiv: 1703.10857.
* [Pop+20] Martin Popel, Marketa Tomkova, Jakub Tomek, Lukasz Kaiser, Jakob Uszkoreit, Ondrej Bojar, and Zdenek Zabokrtsky. "Transforming Machine Translation: A Deep Learning System Reaches News Translation Quality Comparable to Human Professionals". en. In: _Nature Communications_ 11.1 (Sept. 2020), p. 4381. doi: 10.1038/s41467-020-18073-9.
* [Pos47] Emil L. Post. "Recursive Unsolvability of a Problem of Thue". EN. In: _Journal of Symbolic Logic_ 12.1 (Mar. 1947), pp. 1-11.
* [PR97] John Power and Edmund Robinson. "Premonoidal Categories and Notions of Computation". In: _Mathematical Structures in Computer Science_ 7.5 (Oct. 1997), pp. 453-468. doi: 10.1017/S0960129597002375.
* [Pre07] Anne Preller. "Linear Processing with Pregroups". en. In: _Studia Logica_ 87.2-3 (Dec. 2007), pp. 171-197. doi: 10.1007/s11225-007-9087-0.
* [PL07] Anne Preller and Joachim Lambek. "Free Compact 2-Categories". en. In: _Mathematical Structures in Computer Science_ 17.02 (Apr. 2007), p. 309. doi: 10.1017/S0960129506005901.
* [Qi+20] Peng Qi, Yuhao Zhang, Yuhui Zhang, Jason Bolton, and Christopher D. Manning. "Stanza: A Python Natural Language Processing Toolkit for Many Human Languages". In: _Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations_. 2020.
* [Ren19] Jerome Renault. "A Tutorial on Zero-Sum Stochastic Games". May 2019.
* [Ret05] Christian Retore. _The Logic of Categorial Grammars: Lecture Notes_. en. Report. INRIA, Sept. 2005, p. 105.

 * [RL00] M. M. G. Ricci and T. Levi-Civita. "Methodes de calcul differentiel absolu et leurs applications". fr. In: _Mathematische Annalen_ 54.1 (Mar. 1900), pp. 125-201. doi: 10.1007/BF01454201.
* [Ril18a] Mitchell Riley. "Categories of Optics". In: _arXiv:1809.00738 [math]_ (Sept. 2018). arXiv: 1809.00738 [math].
* [Ril18b] Mitchell Riley. "Categories of Optics". In: _arXiv:1809.00738 [math]_ (Sept. 2018). arXiv: 1809.00738 [math].
* [Rob+19] Chase Roberts, Ashley Milsted, Martin Ganahl, Adam Zalcman, Bruce Fontaine, Yijian Zou, Jack Hidary, Guifre Vidal, and Stefan Leichenauer. _TensorNetwork: A Library for Physics and Machine Learning_. May 2019. doi: 10.48550/arXiv.1905.01330. arXiv: 1905.01330 [cond-mat, physics:hep-th, physics:physics, stat].
* [SCC13] Mehrnoosh Sadrzadeh, Stephen Clark, and Bob Coecke. "The Frobenius Anatomy of Word Meanings I: Subject and Object Relative Pronouns". In: _Journal of Logic and Computation_ 23.6 (Dec. 2013), pp. 1293-1317. doi: 10.1093/logcom/ext044. arXiv: 1404.5278.
* [SCC14] Mehrnoosh Sadrzadeh, Stephen Clark, and Bob Coecke. "The Frobenius Anatomy of Word Meanings II: Possessive Relative Pronouns". In: _Journal of Logic and Computation_ abs/1406.4690 (2014), exu027.
* [SRP91] Vijay A. Saraswat, Martin Rinard, and Prakash Panangaden. "The Semantic Foundations of Concurrent Constraint Programming". In: _Proceedings of the 18th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages_. POPL '91. New York, NY, USA: Association for Computing Machinery, Jan. 1991, pp. 333-352. doi: 10.1145/99583.99627.
* [Sav12] Yury Savateev. "Product-Free Lambek Calculus Is NP-Complete". en. In: _Annals of Pure and Applied Logic_. The Symposium on Logical Foundations of Computer Science 2009 163.7 (July 2012), pp. 775-788. doi: 10.1016/j.apal.2011.09.017.
* [Sch90] Schroder. _Vorlesungen uber die algebra der logik_. ger. Leipzig, B. G. Teubner, 1890.
* [SP97] M. Schuster and K.K. Paliwal. "Bidirectional Recurrent Neural Networks". In: _IEEE Transactions on Signal Processing_ 45.11 (Nov. 1997), pp. 2673-2681. doi: 10.1109/78.650093.
* [Sch98] Hinrich Schutze. "Automatic Word Sense Discrimination". In: _Computational Linguistics_ 24.1 (1998), pp. 97-123.
* [Sha53] L. S. Shapley. "Stochastic Games". en. In: _Proceedings of the National Academy of Sciences_ 39.10 (Oct. 1953), pp. 1095-1100. doi: 10.1073/pnas.39.10.1095.
* [STS20] Dan Shiebler, Alexis Toumi, and Mehrnoosh Sadrzadeh. _Incremental Monoidal Grammars_. Jan. 2020. doi: 10.48550/arXiv.2001.02296. arXiv: 2001.02296 [cs].
* [Siv+20] Seyon Sivarajah, Silas Dilkes, Alexander Cowtan, Will Simmons, Alec Edgington, and Ross Duncan. "T$|$ket$>$ : A Retargetable Compiler for NISQ Devices". en. In: _Quantum Science and Technology_ 6.1 (Nov. 2020).

 * [SJ07] Noah A. Smith and Mark Johnson. "Weighted and Probabilistic Context-Free Grammars Are Equally Expressive". In: _Computational Linguistics_ 33.4 (2007), pp. 477-491. doi: 10.1162/coli.2007.33.4.477.
* [Soc+13a] R. Socher, Alex Perelygin, J. Wu, Jason Chuang, Christopher D. Manning, A. Ng, and Christopher Potts. "Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank". In: _EMNLP_. 2013.
* Volume 1_. NIPS'13. Red Hook, NY, USA: Curran Associates Inc., Dec. 2013, pp. 926-934.
* [SW97] Karen Sparck Jones and Peter Willett, eds. _Readings in Information Retrieval_. San Francisco, CA, USA: Morgan Kaufmann Publishers Inc., 1997.
* [SS97] A. Sperduti and A. Starita. "Supervised Neural Networks for the Classification of Structures". In: _IEEE Transactions on Neural Networks_ 8.3 (May 1997), pp. 714-735. doi: 10.1109/72.572108.
* [Spi12] David I. Spivak. "Functorial Data Migration". en. In: _Information and Computation_ 217 (Aug. 2012), pp. 31-51. doi: 10.1016/j.ic.2012.05.001.
* [Sta04] Edward Stabler. "Varieties of Crossing Dependencies: Structure Dependence and Mild Context Sensitivity". In: _Cognitive Science_ 28 (Sept. 2004), pp. 699-720. doi: 10.1016/j.cogsci.2004.05.002.
* [Sta70] Robert C. Stalnaker. "Pragmatics". In: _Synthese_ 22.1-2 (1970), pp. 272-289. doi: 10.1007/bf00413603.
* [Sta79] Richard Statman. "The Typed $\lambda$-Calculus Is Not Elementary Recursive". en. In: _Theoretical Computer Science_ 9.1 (July 1979), pp. 73-81. doi: 10.1016/0304-3975(79)90007-0.
* [Ste87] Mark Steedman. "Combinatory Grammars and Parasitic Gaps". en. In: _Natural Language & Linguistic Theory_ 5.3 (Aug. 1987), pp. 403-439. doi: 10.1007/BF00134555.
* [Ste00] Mark Steedman. _The Syntactic Process_. Cambridge, MA, USA: MIT Press, 2000.
* [Ste19] Mark Steedman. _14. Combinatory Categorial Grammar_. en. De Gruyter Mouton, May 2019. Chap. Current Approaches to Syntax, pp. 389-420.
* [Str07] Lutz Strasburger. "What Is a Logic, and What Is a Proof?" en. In: _Logica Universalis_. Ed. by Jean-Yves Beziau. Basel: Birkhauser, 2007, pp. 135-152. doi: 10.1007/978-3-7643-8354-1_8.
* [Tar36] Alfred Tarski. "The Concept of Truth in Formalized Languages". In: _Logic, Semantics, Metamathematics_. Ed. by A. Tarski. Oxford University Press, 1936, pp. 152-278.
* [Tar41] Alfred Tarski. "On the Calculus of Relations". EN. In: _Journal of Symbolic Logic_ 6.3 (Sept. 1941), pp. 73-89.

 * [Tar43] Alfred Tarski. "The Semantic Conception of Truth and the Foundations of Semantics". In: _Philosophy and Phenomenological Research_ 4.3 (1943), pp. 341-376. doi: 10.2307/2102968.
* [Ter12] Kazushige Terui. "Semantic Evaluation, Intersection Types and Complexity of Simply Typed Lambda Calculus". In: _23rd International Conference on Rewriting Techniques and Applications (RTA'12)_. Ed. by Ashish Tiwari. Vol. 15. Leibniz International Proceedings in Informatics (LIPIcs). Dagstuhl, Germany: Schloss Dagstuhl-Leibniz-Zentrum fuer Informatik, 2012, pp. 323-338. doi: 10.4230/LIPIcs.RTA.2012.323.
* [Tes59] Lucien Tesniere. _Elements de Syntaxe Structurale_. Paris/FRA: Klincksiek, 1959.
* Decidability, Complexity, and Algorithms". en. PhD thesis. Oct. 2013. url: https://tel.archives-ouvertes.fr/tel-00925722.
* [TKG03] Domonkos Tikk, Laszlo T. Koczy, and Tamas D. Gedeon. "A Survey on Universal Approximation and Its Limits in Soft Computing Techniques". en. In: _International Journal of Approximate Reasoning_ 33.2 (June 2003), pp. 185-202. doi: 10.1016/S0888-613X(03)00021-5.
* [Tou22] Alexis Toumi. "Category Theory for Quantum Natural Language Processing". University of Oxford, 2022.
* [TdY22] Alexis Toumi, Giovanni de Felice, and Richie Yeung. _DisCoPy for the Quantum Computer Scientist_. May 2022. doi: 10.48550/arXiv.2205.05190. arXiv: 2205.05190 [quant-ph].
* [TK21] Alexis Toumi and Alex Koziell-Pipe. "Functorial Language Models". In: _arXiv:2103.14411 [cs, math]_ (Mar. 2021). arXiv: 2103.14411 [cs, math].
* [TYd21] Alexis Toumi, Richie Yeung, and Giovanni de Felice. "Diagrammatic Differentiation for Quantum Machine Learning". In: _Electronic Proceedings in Theoretical Computer Science_ 343 (Sept. 2021), pp. 132-144. doi: 10.4204/EPTCS.343.7. arXiv: 2103.07960 [quant-ph].
* [TM21] Alex Townsend-Teague and Konstantinos Meichanetzidis. "Classifying Complexity with the ZX-Calculus: Jones Polynomials and Potts Partition Functions". In: _arXiv:2103.06914 [quant-ph]_ (Mar. 2021). arXiv: 2103.06914 [quant-ph].
* [TN19] Rocco Tripodi and Roberto Navigli. "Game Theory Meets Embeddings: A Unified Framework for Word Sense Disambiguation". In: _Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)_. Hong Kong, China: Association for Computational Linguistics, Nov. 2019, pp. 88-99. doi: 10.18653/v1/D19-1009.
* [Tro+17] Theo Trouillon, Christopher R. Dance, Johannes Welbl, Sebastian Riedel, Eric Gaussier, and Guillaume Bouchard. "Knowledge Graph Completion via Complex Tensor Factorization". In: _The Journal of Machine Learning Research_ 18.1 (2017), pp. 4735-4772. eprint: arXiv:1702.06879.

 * [Tur37] A. M. Turing. "Computability and Lambda-Definability". In: _Journal of Symbolic Logic_ 2.4 (1937), pp. 153-163. doi: 10.2307/2268280.
* [TP10] Peter D. Turney and Patrick Pantel. "From Frequency to Meaning: Vector Space Models of Semantics". In: _Journal of Artificial Intelligence Research_ 37 (Feb. 2010), pp. 141-188. doi: 10.1613/jair.2934. arXiv: 1003.1141.
* [TN05] Karl Tuyls and Ann Nowe. "Evolutionary Game Theory and Multi-Agent Reinforcement Learning". en. In: _The Knowledge Engineering Review_ 20.1 (Mar. 2005), pp. 63-90. doi: 10.1017/S026988890500041X.
* [VKS19] VakarMatthijs, KammarOhad, and StatonSam. "A Domain Theory for Statistical Probabilistic Programming". In: _Proceedings of the ACM on Programming Languages_ (Jan. 2019). doi: 10.1145/3290349.
* [van87] Johan van Benthem. "Categorical Grammar and Lambda Calculus". en. In: _Mathematical Logic and Its Applications_. Ed. by Dimiter G. Skordev. Boston, MA: Springer US, 1987, pp. 39-60. doi: 10.1007/978-1-4613-0897-3_4.
* [van20] John van de Wetering. "ZX-Calculus for the Working Quantum Computer Scientist". In: _arXiv:2012.13966 [quant-ph]_ (Dec. 2020). arXiv: 2012.13966 [quant-ph].
* [Var82] Moshe Y. Vardi. "The Complexity of Relational Query Languages (Extended Abstract)". In: _Proceedings of the Fourteenth Annual ACM Symposium on Theory of Computing_. STOC '82. New York, NY, USA: Association for Computing Machinery, May 1982, pp. 137-146. doi: 10.1145/800070.802186.
* [Vas+17] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. "Attention Is All You Need". In: _arXiv:1706.03762 [cs]_ (Dec. 2017). arXiv: 1706.03762 [cs].
* [VW94] K. Vijay-Shanker and David J. Weir. "The Equivalence Of Four Extensions Of Context-Free Grammars". In: _Mathematical Systems Theory_ 27 (1994), pp. 27-511.
* [Von29] J. Von Neumann. "Zur Algebra Der Funktionaloperationen Und Theorie Der Normalen Operatoren". In: _Mathematische Annalen_ 102 (1929), pp. 370-427. doi: 10.1007/BF01782352.
* [Wal89a] R. F. C. Walters. "A Note on Context-Free Languages". en. In: _Journal of Pure and Applied Algebra_ 62.2 (Dec. 1989), pp. 199-203. doi: 10.1016/0022-4049(89)90151-5.
* [Wal89b] R. F. C. Walters. "The Free Category with Products on a Multigraph". en. In: _Journal of Pure and Applied Algebra_ 62.2 (Dec. 1989), pp. 205-210. doi: 10.1016/0022-4049(89)90152-7.
* [Wan+17] Q. Wang, Z. Mao, B. Wang, and L. Guo. "Knowledge Graph Embedding: A Survey of Approaches and Applications". In: _IEEE Transactions on Knowledge and Data Engineering_ 29.12 (Dec. 2017), pp. 2724-2743. doi: 10.1109/TKDE.2017.2754499.

 * [WSL19] William Yang Wang, Sameer Singh, and Jiwei Li. "Deep Adversarial Learning for NLP". In: _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Tutorials_. Minneapolis. Minnesota: Association for Computational Linguistics, June 2019, pp. 1-5. doi: 10.18653/v1/N19-5001.
* [Wil03] Edwin Williams. _Representation Theory_. en. MIT Press, 2003.
* [WZ21] Paul Wilson and Fabio Zanasi. "The Cost of Compositionality: A High-Performance Implementation of String Diagram Composition". In: _arXiv:2105.09257 [cs, math]_ (May 2021). arXiv: 2105.09257 [cs, math].
* [Wit53] Ludwig Wittgenstein. _Philosophical Investigations_. Oxford: Basil Blackwell, 1953.
* [Wu+20] Yongji Wu, Defu Lian, Yiheng Xu, Le Wu, and Enhong Chen. "Graph Convolutional Networks with Markov Random Field Reasoning for Social Spammer Detection". In: _Proceedings of the AAAI Conference on Artificial Intelligence_ 34.01 (Apr. 2020), pp. 1054-1061. doi: 10.1609/aaai.v34i01.5455.
* [XHW18] Wenhan Xiong, Thien Hoang, and William Yang Wang. "DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning". In: _arXiv:1707.06690 [cs]_ (July 2018). arXiv: 1707.06690 [cs].
* [Yan+15] Bishan Yang, Wen-tau Yih, Xiaodong He, Jianfeng Gao, and Li Deng. "Embedding Entities and Relations for Learning and Inference in Knowledge Bases". In: _arXiv:1412.6575 [cs]_ (Aug. 2015). arXiv: 1412.6575 [cs].
* [YK21] Richie Yeung and Dimitri Kartsaklis. "A CCG-Based Version of the DisCoCat Framework". In: _arXiv:2105.07720 [cs, math]_ (May 2021). arXiv: 2105.07720 [cs, math].
* [YNM17] Masashi Yoshikawa, Hiroshi Noji, and Yuji Matsumoto. "A* CCG Parsing with a Supertag and Dependency Factored Model". In: _Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_. Vancouver, Canada: Association for Computational Linguistics, July 2017, pp. 277-287. doi: 10.18653/v1/P17-1026.
* [Yos+19] Masashi Yoshikawa, Hiroshi Noji, Koji Mineshima, and Daisuke Bekki. "Automatic Generation of High Quality CCGbanks for Parser Domain Adaptation". In: _arXiv:1906.01834 [cs]_ (June 2019). arXiv: 1906.01834 [cs].
* [You67] Daniel H. Younger. "Recognition and Parsing of Context-Free Languages in Time N3". en. In: _Information and Control_ 10.2 (Feb. 1967), pp. 189-208. doi: 10.1016/S0019-9958(67)80007-X.
* [ZC16] William Zeng and Bob Coecke. "Quantum Algorithms for Compositional Natural Language Processing". In: _Electronic Proceedings in Theoretical Computer Science_ 221 (Aug. 2016), pp. 67-75. doi: 10.4204/EPTCS.221.8. arXiv: 1608.01406.
* [Zha+19] Lipeng Zhang, Peng Zhang, Xindian Ma, Shuqin Gu, Zhan Su, and Dawei Song. "A Generalized Language Model in Tensor Space". In: _arXiv:1901.11167 [cs]_ (Jan. 2019). arXiv: 1901.11167 [cs].

 * [Zho+21] Jie Zhou, Ganqu Cui, Shengding Hu, Zhengyan Zhang, Cheng Yang, Zhiyuan Liu, Lifeng Wang, Changcheng Li, and Maosong Sun. _Graph Neural Networks: A Review of Methods and Applications._ Oct. 2021. arXiv: 1812.08434 [cs, stat].
* [Zho+17] Qingyu Zhou, Nan Yang, Furu Wei, Chuanqi Tan, Hangbo Bao, and Ming Zhou. "Neural Question Generation from Text: A Preliminary Study". In: _arXiv:1704.01792 [cs]_ (Apr. 2017). arXiv: 1704.01792 [cs].

 