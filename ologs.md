

# Ologs: A Categorical Framework for Knowledge Representation

David I. Spivak

Department of Mathematics, University of California, Berkeley, CA 94720-3895, USA spivak@math.berkeley.edu

Robert E. Kent

Department of Mathematics, University of California, Berkeley, CA 94720-3895, USA robert.kent@math.berkeley.edu

###### Abstract.

In this paper we introduce the olog, or ontology log, a category-theoretic model for knowledge representation (KR). Grounded in formal mathematics, ologs can be rigorously formulated and cross-compared in ways that other KR models (such as semantic networks) cannot. An olog is similar to a relational database schema; in fact an olog can serve as a data repository if desired. Unlike database schemas, which are generally difficult to create or modify, ologs are designed to be user-friendly enough that authoring or re-configuring an olog is a matter of course rather than a difficult chore. It is hoped that learning to author ologs is much simpler than learning a database definition language, despite their similarity. We describe ologs carefully and illustrate with many examples. As an application we show that any primitive recursive function can be described by an olog. We also show that ologs can be aligned or connected together into a larger network using functors. The various methods of information flow and institutions can then be used to integrate local and global world-views. We finish by providing several different avenues for future research.

This project was supported by Office of Naval Research grant: N000141010841 and a generous contribution by Clark Barwick, Jacob Lurie, and the Massachusetts Institute of Technology Department of Mathematics.

based on a branch of mathematics called category theory. An olog is roughly a category that models a given real-world situation.

The main advantages of authoring an olog rather than writing a prose description of a subject are that

* an olog gives a precise formulation of a conceptual world-view,
* an olog can be formulaically converted into a database schema,
* an olog can be extended as new information is obtained,
* an olog written by one author can be easily and precisely referenced by others,
* an olog can be input into a computer and "meaningfully stored", and
* different ologs can be compared by functors, which in turn generate automatic terminology translation systems.

The main disadvantage to using ologs over prose, aside from taking more space on the page, is that writing a good olog demands a clarity of thought that ordinary writing or conversation can more easily elide. However, the contemplation required to write a good olog about a subject may have unexpected benefits as well.

A category is a mathematical structure that appears much like a directed graph: it consists of objects (often drawn as nodes or dots, but here drawn as boxes) and arrows between them. The feature of categories that distinguishes them from graphs is the ability to declare an equivalence relation on the set of paths. A functor is a mapping from one category to another that preserves the structure (i.e. the nodes, the arrows, and the equivalences). If one views a category as a kind of language (as we shall in this paper) then a functor would act as a kind of translating dictionary between languages. There are many good references on category theory, including [LS], [Sic], [Pie], [BW1], [Awo], and [Mac]; the first and second are suited for general audiences, the third and fourth are suited for computer scientists, and the fifth and sixth are suited for mathematicians (in each class the first reference is easier than the second).

A basic olog, defined in Section 2, is a category in which the objects and arrows have been labeled by English-language phrases that indicate their intended meaning. The objects represent types of things, the arrows represent functional relationships (also known as aspects, attributes, or observables), and the commutative diagrams represent facts. Here is a simple olog about an amino acid called arginine ([W]):

(1)

$D$$ The idea of representing information in a graph is not new. For example the Resource Descriptive Framework (RDF) is a system for doing just that [CM]. The key difference between a category and a graph is the consideration of paths, and that two paths from $A$ to $B$ may be declared identical in a category (see [11]). For example, we can further declare that in Diagram (1), the diagram

(2)

_commutes_, i.e. that the two paths $A$$\xrightarrow{\text{\raisebox{-1.0pt}{\includegraphics[]{fig/Rf_R that are meaningful to others and easily extendable. We will begin in Section 2 by laying out the basics: types as objects, aspects as arrows, and facts as commutative diagrams. In Section 3, we will explain how to attach "instance" data to an olog and hence realize ologs as database schemas. In Section 4, we will discuss meaningful constraints betweeen ologs that allow us to develop a higher-dimensional web of information called an information system, and we will discuss how the various parts of such a system interact via information channels. In Sections 5 and 6, we will extend the olog definition language to include "layouts" and "groupings", which make for more expressive ologs; we will also describe two applications, one which explicates the computation of the factorial function, and the other which defines a notion from pure mathematics (that of pseudo-metric spaces). Finally, in Section 7, we will discuss some possible directions for future research.

For the remainder of the present section, we will explain how ologs relate to existing ideas in the field of knowledge representation.

### The semantic advantage of ologs: modularity

The difference between ologs and prose is modularity: small conceptual pieces can form large ideas, and these pieces work best when they are reusable. The same phenomenon is true throughout computer science and mathematics. In programming languages, modularity brings not only vast efficiency to the writing of programs but enables an "abstraction barrier" that keeps the ideas clean. In mathematics, the most powerful results are often simple lemmas that are reusable in a wide variety of circumstances.

Web pages that consist of prose writing are often referred to as _information silos_. The idea is that a silo is a "big tube of stuff" which is not organized in any real way. Links between web pages provide some structure, but such a link does not carry with it a precise method to correlate the information within the two pages. Similarly in science, one author may reference another paper, but such a reference carries very little structure -- it just points to a silo.

Ologs can be connected with links which are much richer than the link between two silos could possibly be. Individual concepts and connections within one olog can be "functorially aligned" with concepts and connections in another. A functor creates a precise connection between the work of one author and the work of another so that the precise nature of the comparison is not left to the reader's imagination but explicitly specified. The ability to incorporate mathematical precision into the sharing of ideas is a central feature of ologs.

### Relation to other models

There are many languages for knowledge representation (KR). For example, there are database languages such as SQL, ontology languages such as RDF and OWL, the language of Semantic Nets, and others (see [Bor]). One may ask what makes the olog concept different or better than the others.

The first response is that ologs are closely related to the above ideas. Indeed, all of these KR models can be "categorified" (i.e. phrased in the language of category theory) and related by functors, so that many of the ideas align and can be transferred between the different systems. In fact, as we will make clear in Section 3, ologs are almost identical to the categorical model of databases presented in [Spi2].

However, ologs have advantages over many existing KR models. The first advantage arises from the notion of commutative diagrams (which allow us to equate different paths through the domain, see Section 2.3) and of limits and colimits (which allow us to lay out and group things, see Sections 5 and 6). The additional expressivity of ologs give them a certain semantic clarity and interoperability that cannot be achieved with graphs and networks in the usual sense. The second advantage arises from the notion of olog morphisms, which allow the definition of meaningful constraints between ologs. With this in hand, we can integrate a set of similar ologs into a single information system, and go on to define information fusion. This will be discussed further Section 4.

In the remainder of this section we will provide a few more details on the relationship between ologs and each of the above KR models: databases, RDF/OWL, and semantic nets. The reader who does not know or care much about other systems of knowledge representation can skip to Section 1.4.

#### 1.3.1. Ologs and Databases

A database is a system of tables, each table of which consists of a header of columns and a set of rows. A table represents a type of thing $T$, each column represents an attribute of $T$, and each row represents an example of $T$. An attribute is itself a "type of thing", so each column of a table points to another table.

The relationship between ologs and databases is that every box $B$ in an olog represents a type of thing and every arrow $B\to X$ emanating from $B$ represents an attribute of $B$ (whose results are of type $X$). Thus the boxes and arrows in an olog correspond to tables and their columns in a database. The rows of each table in a database will correspond to "instances" of each type in an olog. Again, this will be made more clear in Section 3 or one can see [20] or [14].

The point is that every olog can serve as a database schema, and the schemas represented by ologs range from simple (just objects and arrows) to complex (including commutative diagrams, products, sums, etc.). However, whereas database schemas are often prescriptive ("you must put your data into this format!"), ologs are usually descriptive ("this is how I see things"). One can think of an olog as an interface between people and databases: an olog is human readable, but it is also easily converted to a database schema upon which powerful applications can be put to work. Of course, if one is to use an olog as a database schema, it will become prescriptive. However, since the intention of each object and arrow is well-documented (as its label), schema evolution would be straightforward. Moreover, the categorical structure of ologs allows for _functorial data migration_ by which one can transfer the instance data from an older schema to the current one (see [20]).

#### 1.3.2. Ologs and RDF / OWL

In [20], the first author explained how a categorical database can be converted into an RDF triple store using the Grothendieck construction. The main difference between a categorical database schema (or an olog) and an RDF schema is that one cannot specify commutativity in an RDF schema. Thus one cannot express things like "the woman parent of a person $x$ is the mother of $x$." Without this expressivity, it is hard to enforce much rigor, and thus RDF data tends to be too loose for many applications.

OWL schemas, on the other hand, can express many more constraints on classes and properties. We have not yet explored the connection, nor compared the expressive power, of ologs and OWL. However, they are significantly different systems, most obviously in that OWL relies on logic where ologs rely on category theory.

#### 1.3.3. Semantic Nets

On the surface, ologs look the most like semantic networks, or concept webs, but there are important differences between the two notions. First, arrows in a semantic network need not indicate functions; they can be relations. So there could be an arrow $\ulcorner$a father$\urcorner$has$\urcorner$a child$\urcorner$ in a semantic network, but not in an olog (see Section 2.2.3 for how the same idea is expressible in an olog). There is a nice category of sets and relations, often denoted **Rel**, but this category is harder to reason about than is the ordinary category of sets and functions (often denoted **Set**). Thus, as mentioned above, semantic networks are categorifiable (using **Rel**), but this underlying formalism does not appear to play a part in the study or use of semantic networks. However, some attempt to integrate category theory and neural nets has been made, see [HC].

Moreover, commutative diagrams and other expressive abilities held by ologs are not generally part of the semantic network concept (see [Sow1]). For these reasons, semantic networks tend to be brittle: minor changes can have devastating effects. For example, if two semantic networks are somehow synced up and then one is changed, the linkage must be revised or may be altogether broken. Such a disaster is often avoided if one uses categories: because different paths can be equivalent, one can simply add new ideas (types and aspects) without changing the semantic meaning of what was already there. As section 4.4 demonstates with an extended example, conceptual graphs, which are a popular formalism for semantics nets, can be linearized to ologs, thereby gaining in precision and expressibility.

### Acknowledgements

#### 1.4.1. David Spivak's acknowledgments

I would like to thank Mathieu Anel and Henrik Forssell for many pleasant and quite useful conversations. I would also like to thank Micha Breakstone for his help on understanding the relationship between ologs and linguistics. Finally I would like to thank Dave Balaban for helpful suggestions on this document itself.

#### 1.4.2. Robert Kent's acknowledgments

I would like to thank the participants in the Standard Upper Ontology working group for many interesting, spirited, rewarding and enlightening discussions about knowledge representation in general and ontologies in particular; I especially want to thank Leo Obrst, Marco Schorlemmer and John Sowa from that group. I want to thank Jon Barwise for leading the development of the theory of information flow. I want to thank Joseph Goguen for leading the development of the theory of institutions, and for pointing out the common approach to knowledge representation used by both the Information Flow Framework and the theory of institutions.

## 2. Types, aspects, and facts

In this section we will explain basic ologs, which involve types, aspects, and facts. A basic olog is a category in which each object and arrow has been labeled by text; throughout this paper we will assume that text to be written in English.

The purpose of this section is to show how one can convert a real-world situation into an olog. It is probably impossible to explain this process precisely in words. Instead, we will explain mainly by example. We will give "rules of good practice" that lead to good ologs. While these rules are not strictly necessary, they help to ensure that the olog is properly formulated. As the Dalai Lama says, "Learn the rules so you know how to break them properly." 

### Types

A type is an abstract concept, a distinction the author has made. We represent each type as a box containing a _singular indefinite noun phrase_. Each of the following four boxes is a type:

(3) $$\begin{array}{|c|}\hline\mbox{a man}&\framebox{an automobile}\\ \hline\end{array}$$

a pair $(a,w)$, where $w$ is a woman and $a$ is an automobile

a pair $(a,w)$ where $w$ is a woman and $a$ is a blue automobile owned by $w$

Each of the four boxes in (3) represents a type of thing, a whole class of things, and the label on that box is what one should call _each example_ of that class. Thus $\ulcorner$a man$\urcorner$ does not represent a single man, but the set of men, each example of which is called "a man"1. Similarly, the bottom right-hand box in (3) represents an abstract type of thing, which probably has more than a million examples, but the label on the box indicates a common name for each such example.

Footnote 1: In other words, types in ologs are intentional, rather than extensional — the label on a type describes its intention. The extension of a type will be captured by _instance data_; see Section 3 .

Typographical problems emerge when writing a text-box in a line of text, e.g. the text-box [a man] seems out of place here, and the more in-line text-boxes one has in a given paragraph, the worse it gets. To remedy this, we will denote types which occur in a line of text with corner-symbols, e.g. we will write $\ulcorner$a man$\urcorner$instead of a man.

#### 2.1.1. Types with compound structures

Many types have compound structures; i.e. they are composed of smaller units. Examples include

(4) $$\begin{array}{|c|}\hline\mbox{a man and}\\ \mbox{a woman}&\framebox{a food $f$ and a child $c$ such that $c$ ate all of $f$}\\ \hline\end{array}\qquad\framebox{a triple $(p,a,j)$ where $p$ is a paper, $a$ is an author of $p$, and $j$ is a journal in which $p$ was published}\\ \hline\end{array}$$

It is good practice to declare the variables in a "compound type", as we did in the last two cases of (4). In other words, it is preferable to replace the first box above with something like

$$\framebox{a man $m$ and}\\ \framebox{a woman $w$}\qquad\mbox{or}\qquad\framebox{a pair $(m,w)$ where $m$ is a man and $w$ is a woman}\\ \hline\end{array}$$

so that the variables $(m,w)$ are clear.

#### Rules of good practice

A type is presented as a text box. The text in that box should

1. begin with the word "a" or "an";
2. refer to a distinction made and recognizable by the author;
3. refer to a distinction for which instances can be documented;
4. not end in a punctuation mark;5. declare all variables in a compound structure.

The first, second, and third rules ensure that the class of things represented by each box appears to the author as a well-defined set; see Section 3 for more details. The fourth and fifth rules encourage good "readability" of arrows, as will be discussed next in Section 2.2.

We will not always follow the rules of good practice throughout this document. We think of these rules being followed "in the background" but that we have "nick-named" various boxes. So "Steve" may stand as a nickname for "a thing classified as Steve" and "arginine" as a nickname for "a molecule of arginine".

### Aspects

An aspect of a thing $x$ is a way of viewing it, a particular way in which $x$ can be regarded or measured. For example, a woman can be regarded as a person; hence "being a person" is an aspect of a woman. A man has a height (say, taken in inches), so "having a height (in inches)" is an aspect of a man. In an olog, an aspect of $A$ is represented by an arrow $A\to B$, where $B$ is the set of possible "answers" or results of the measurement. For example when observing the height of a man, the set of possible results is the set of integers, or perhaps the set of integers between 20 and 120.

(5)

(6)

has as height (in inches) an integer between 20 and 120

We will formalize the notion of aspect by saying that aspects are functional relationships.2 Suppose we wish to say that a thing classified as $X$ has an aspect $f$ whose result set is $Y$. This means there is a functional relationship called $f$ between $X$ and $Y$, which can be denoted $f\colon X\to Y$. We call $X$ the _domain of definition_ for the aspect $f$, and we call $Y$ the _set of result values_ for $f$. For example, a man has a height in inches whose result is an integer, and we could denote this by $h\colon M\to\mathbf{Int}$. Here, $M$ is the domain of definition for height and $\mathbf{Int}$ is the set of result values.

Footnote 2: In type theory, what we here call aspects are called _functions_. Since our types are not fixed sets (see Section 3), we preferred a term that was less formal.

A set may always be drawn as a blob with dots in it. If $X$ and $Y$ are two sets, then a _a function from $X$ to $Y$_, denoted $f\colon X\to Y$ can be presented by drawing arrows from dots in blob $X$ to dots in blob $Y$. There are two rules:

1. each arrow must emanate _from_ a dot in $X$ and point _to_ a dot in $Y$;
2. each dot in $X$ must have precisely _one_ arrow emanating from it.

Given an element $x\in X$, the arrow emanating from it points to some element $y\in Y$, which we call _the image of $x$ under $f$_ and denote $f(x)=y$.

Again, in an olog, an aspect of a thing $X$ is drawn as a labeled arrow pointing from $X$ to a "set of result values." Let us concentrate briefly on the arrow in (5). The domain of definition is the set of women (a set with perhaps 3 billion elements); the set of result values is the set of persons (a set with perhaps 6 billion elements). We can imagine drawing an arrow from each dot in the "woman" set to a unique dot in the "person" set. No woman points to two different people, nor to zero people -- each woman is exactly one person -- so the rules for a functional relationship are satisfied. Let us now concentrate briefly on the arrow in (6). The domain of definition is the set of men, the set of result values is the set of integers $\{20,21,22,\ldots,119,120\}$. We can imagine drawing an arrow from each dot in the "man" set to a single dot in the "integer" set. No man points to two different heights, nor can a man have no height: each man has exactly one height. Note however that two different men can point to the same height.

#### 2.2.1. Invalid aspects

We tried above to clarify what it is that makes an aspect "valid", namely that it must be a "functional relationship." In this subsection we will present two arrows which on their face may appear to be aspects, but which on closer inspection are not functional (and hence are not valid as aspects).

Consider the following two arrows:

(7*) $$\begin{array}{c}\mbox{a person}\\ \end{array}\begin{array}{c}\mbox{has}\\ \end{array}\begin{array}{c}\mbox{a child}\\ \end{array}$$

(8*) $$\begin{array}{c}\mbox{a mechanical pencil}\\ \end{array}\begin{array}{c}\mbox{uses}\\ \end{array}\begin{array}{c}\mbox{a piece of lead}\\ \end{array}$$

A person may have no children or may have more than one child, so the first arrow is invalid: it is not functional because it does not satisfy rule (2) above. Similarly, if we drew an arrow from each mechanical pencil to each piece of lead it uses, it would not satisfy rule (2) above. Thus neither of these is a valid aspect.

Of course, in keeping with Warning 1.0.1, the above arrows may not be wrong but simply reflect that the author has a strange world-view or a strange vocabulary. Maybe the author believes that every mechanical pencil uses exactly one piece of lead. If this is so, then $\ulcorner$ a mechanical pencil$\ulcorner\xrightarrow{\mbox{uses}}\ulcorner$ a piece of lead$\urcorner$ is indeed a valid aspect! Similarly, suppose the author meant to say that each person _was once_ a child, or that a person has an inner child. Since every person has one and only one inner child (according to the author), the map $\ulcorner$ a person$\urcorner\xrightarrow{\mbox{has as inner child}}\ulcorner$ a child$\urcorner$ is a valid aspect. We cannot fault the author for such a view, but note that we have changed the name of the label to make its intention more explicit.

#### 2.2.2. Reading aspects and paths as English phrases

Each arrow (aspect) $X\xrightarrow{f}Y$ can be read by first reading the label on its source box (domain of definition) $X$, then the label on the arrow $f$, and finally the label on its target box (set of result values) $Y$. For example, the arrow

(9) $$\begin{array}{c}\mbox{has as first author}\\ \end{array}\begin{array}{c}\mbox{a person}\\ \end{array}$$

is read "a book has as first author a person", a valid English sentence.

Sometimes the label on an arrow can be shortened or dropped altogether if it is obvious from context. We will discuss this more in Section 2.3 but here is a common example from the way we write ologs.

(10)

Neither arrow is readable by the protocol given above (e.g. "a pair $(x,y)$ where $x$ and $y$ are integers $x$ an integer" is not an English sentence), and yet it is obvious what each map means. For example, given the pair $(8,11)$ which belongs in box $A$, application of arrow $x$ would yield $8$ in box $B$. The label $x$ can be thought of as a nickname for the full name "yields, via the value of $x$," and similarly for $y$. We do not generally use the full name for fear that the olog would become cluttered with text.

One can also read paths through an olog by inserting the word "which" after each intermediate box. For example the following olog has two paths of length $3$ (counting arrows in a chain):

(11)

$$\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{\xy(0,0)*{ \xy(0,0)*{\xy( The set $R$ represents those sequences $(a_{1},a_{2},\ldots,a_{n})$ that are so-related. In an olog, we represent this as follows

For example,

Whereas $A_{1}\times A_{2}\times A_{3}$ includes all possible triples $(p,a,j)$ where $a$ is a person, $p$ is a paper, and $j$ is a journal, it is obvious that not all such triples are found in $R$. Thus $R$ represents a proper subset of $A_{1}\times A_{2}\times A_{3}$.

#### Rules of good practice

An aspect is presented as a labeled arrow, pointing from a source box to a target box. The arrow text should

1. begin with a verb;
2. yield an English sentence, when the source-box text followed by the arrow text followed by the target-box text is read;
3. refer to a functional dependence: each instance of the source type should give rise to a specific instance of the target type;

### Facts

In this section we will discuss facts and their relationship to "path equivalences." It is such path equivalences, which exist in categories but do not exist in graphs, that make category theory so powerful. See [Spi3] for details.

 Given an olog, the author may want to declare that two paths are equivalent. For example consider the two paths from $A$ to $C$ in the olog

(12) $$\begin{array}{c}\includegraphics[width=142.26378pt]{a.eps}\end{array}$$

We know as English speakers that a woman parent is called a mother, so these two paths $A\to C$ should be equivalent. A more mathematical way to say this is that the triangle in Olog (12) _commutes_.

A _commutative diagram_ is a graph with some declared path equivalences. In the example above we concisely say "a woman parent is equivalent to a mother." We declare this by defining the diagonal map in (12) to be _the composition_ of the horizontal map and the vertical map.

We generally prefer to indicate a commutative diagram by drawing a check-mark, $\check{\check{\check{\check{\check{\check{\check{\check{\check{\check{\check{\check{\check{ \check{\check{\check _Example 2.3.2_.: How would one record a fact like "a truck weighs more than a car"? We suggest something like this:

where both top and bottom commute. This olog exemplifies the fact that simple sentences sometimes contain large amounts of information. While the long map may seem to suffice to convey the idea "a truck weighs more than a car," the path equivalences (declared by check-marks) serve to ground the idea in more basic types. These other types tend to be useful for other purposes, both within the olog and when connecting it to others.

#### 2.3.3. Specific facts at the olog level

Another fact one might wish to record is that "John Doe's weight is 150 lbs." This is established by declaring that the following diagram commutes:

(13)

If one only had the top line, it would be less obvious how to connect its information with that of other ologs. (See Section 4 for more on connecting different ologs).

Note that the top line in Diagram (13) might also be considered as existing at the "data level" rather than at the "olog level." In other words, one could see John Doe as an "instance" of ${}^{\neg}$a person${}^{\neg}$, rather than as a type in and of itself, and similarly see 150 as an instance of ${}^{\neg}$a real number${}^{\neg}$. This idea of an olog having a "data level" is the subject of the Section 3.

_Rules of good practice_ 2.3.4.: A fact is the declaration that two paths (having the same source and target) in an olog are equivalent. Such a fact is either presented as a checkmark between the two paths (if such a check-mark is unambiguous) or by an equation. Every such equivalence should be declared; i.e. no fact should be considered too obvious to declare.

 

## 3. Instances

The reader at this point hopefully sees an oog as a kind of "concept map," and it is one, albeit a concept map with a formal structure (implicitly coming from category theory) and specific rules of good practice. In this section we will show that one can also load an olog with data. Each type can be assigned a set of instances, each aspect will map the instances of one type to instances of the other, and each fact will equate two such mappings. We give examples of these ideas in Section 3.1.

In Section 3.2, we will show that in fact every olog can also serve as the layout for a database. In other words, given an olog one can immediately generate a _database schema_, i.e. a system of tables, in any reasonable data definition language such as that of SQL. The tables in this database will be in one-to-one correspondence with the types in the olog. The columns of a given table will be the aspects of the corresponding type, i.e. the arrows whose source is that type. Commutative diagrams in the olog will give constraints on the data.

In fact, this idea is the basic thesis in [10], even though the word olog does not appear in that paper. There it was explained that a category $\mathcal{C}$ naturally can be viewed as a database schema and that a functor $I\colon\mathcal{C}\to\mathbf{Set}$, where $\mathbf{Set}$ is the category of sets, is a database state. Since an olog is a drawing of a category, it is also a drawing of a database schema. The current section is about the "states" of an olog, i.e. the kinds of data that can be captured by it.

### Instances of types, aspects, and facts

Recall from Section 2 that basic ologs consist of types, displayed as boxes; aspects, displayed as arrows; and facts, displayed as equations or check-marks. In this section we discuss the instances of these three basic constructions. The rules of good practice (2.1.1, 2.2.1, and 2.3.4) were specifically designed to simplify the process of finding instances.

#### 3.1.1. Instances of types

According to Rules 2.1.1, each box in an olog contains text which should refer to **a distinction made and recognizable by the author for which instances can be documented.** For example if my olog contains a box

(14) $$\begin{array}{|l|}\hline\text{a pair }(p,c)\text{ where }p\\ \text{is a person, }c\text{ is a cat,}\\ \text{and }p\text{ has petted }c\end{array}$$

then I must have some concept of when this situation occurs. Every time I witness a new person-cat petting, I document it. Whether this is done in my mind, in a ledger notebook, or on a computer does not matter; however using a computer would probably be the most self-explanatory. Imagine a computer program in which one can create ologs. Clicking a text box in an olog results in it "opening up" to show a list of documented instances of that type. If one is reading the CBS news olog and clicks on the box "an episode of 60 Minutes", he or she should see a list of all episodes of the TV show "60 Minutes." If we wish to document a new person-cat petting incident we click on the box in (14) and add this new instance.

#### 3.1.2. Instances of aspects

According to Rules 2.2.1, each arrow in an olog should be labeled with text that refers to a functional relationship between the source box and the target box. A functional relationship $f\colon A\to B$ between finite sets $A$ and $B$ can always be written as a 2-column table: the first column is filled with theinstances of type $A$ and the second column is filled with their $f$-values, which are instances of type $B$.

For example, consider the aspect

(15) $$\framebox{a moon}\xrightarrow{\mathrm{orbits}}\framebox{a planet}$$

We can document some instances of this relationship using the following table:

(16) $$\begin{array}{|c||c|}\hline\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\ Abel, and Chelsey), the two paths to $\ulcorner$a woman$\urcorner$ give the same answers. Indeed, for Cain the two paths are:

1. [label=()]
2. Cain $\mapsto$ (Eve, Adam) $\mapsto$ Eve;
3. Cain $\mapsto$ Eve;

and these answers agree. If one changed any instance of the word "Eve" to the word "Steve" in one of the tables in (17), some pair of paths would fail to agree. Thus the "fact" that the diagram in (12) commutes ensures that there is some internal consistency between the meaning of parents and the meaning of mother, and this consistency must be born out at the instance level.

All of this will be formalized in Section 3.2.2.

### The relationship between ologs and databases

Recall from Section 3.1.1 that we can imagine creating an olog on a computer. The user creates boxes, arrows, and compositions, hence creating a category $\mathcal{C}$. Each text-box $x$ in the olog can be "clicked" by the computer mouse, an action which allows the user to "view the contents" of $x$. The result will be a set of things, which we might call $I(x)\in\mathbf{Set}$, whose elements are things of type $x$. So clicking on the box $\ulcorner$a man$\urcorner$ one sees $I(\ulcorner$a man$\urcorner)$, the set of everything the author has documented as being a man. For each aspect $f\colon x\to y$ of $x$, the user can see a function from the set $I(x)$ to $I(y)$, perhaps as a 2-column table as in (17).

The type $x$ may have many aspects, which we can put together into a single multi-column table. Its columns are the aspects of $x$, and its rows are the elements of $I(x)$. Consider the following olog, taken from [10] where it was presented as a database schema.

(18)

The type $\ulcorner$Employee$\urcorner$ has four aspects, namely manager (valued in $\ulcorner$Employee$\urcorner$), works in (valued in $\ulcorner$department$\urcorner$), and first name and last name (valued in $\ulcorner$string$\urcorner$). As a database, each type together with its aspects form a multi-column table, as in the following example.

_Example 3.2.1_.: We can convert Olog (18) into a database schema. Each box represents a table, each arrow out of a box represents a column of that table. Here is an example state of that database.

 (19) 
 Note that every arrow $f\colon x\to y$ of Olog (18) is represented in Database (19) as a column of table $x$, and that every cell in that column can be found in the Id column of table $y$. For example, every cell in the "works in" column of table **employee** can be found in the Id column of table **department**.

The point is that ologs can be drawn to represent a world-view (as in Section 2), but they can also store data. Rules 1,2, and 3 in 2.1.1 align the construction of an olog with the ability to document instances for each of its types.

#### 3.2.2. Instance data as a set-valued functor

Let $\mathcal{C}$ be an olog. Section 3 so far has described instances of types, aspects, and facts and how all of these come together into a set of interconnected tables. The assignment of a set of instances to each type and a function to each aspect in $\mathcal{C}$, such that the declared facts hold, is called an assignment of _instance data_ for $\mathcal{C}$. More precisely, instance data on $\mathcal{C}$ is a functor $\mathcal{C}\to\mathbf{Set}$, as in Definition 3.2.3.

**Definition 3.2.3**.: Let $\mathcal{C}$ be a category (olog) with underlying graph $|\mathcal{C}|$, and let $\mathbf{Set}$ denote the category of sets. An _instance of $\mathcal{C}$_ (or _an assignment of instance data for $\mathcal{C}$_) is a functor $I\colon\mathcal{C}\to\mathbf{Set}$. That is, it consists of

* a set $I(x)$ for each object (type) $x$ in $\mathcal{C}$,
* a function $I(f)\colon I(x)\to I(y)$ for each arrow (aspect) $f\colon x\to y$ in $\mathcal{C}$, and
* for each fact (path-equivalence or equation) 3 Footnote 3: If we let $f=f_{1}\,;f_{2}\,;\,\cdots\,;f_{n}=f^{\prime}_{1}\,;f^{\prime}_{2}\,;\,\cdots\,; f^{\prime}_{m}$

declared in $\mathcal{C}$, an equality of functions

$$I(f_{1})\,;I(f_{2})\,;\,\cdots\,;I(f_{n})=I(f^{\prime}_{1})\,;I(f^{\prime}_{2 })\,;\,\cdots\,;I(f^{\prime}_{m}).$$

For more on this viewpoint of categories and functors, the reader can consult [20].

## 4. Communication between ologs

The world is inherently heterogeneous. Different individuals 4 in the world naturally have different world-views -- each individual has its own perspective on the world. The conceptual knowledge (information resources) of an individual represents its world-view, and is encoded in an ontology log, or olog, containing the concepts, relations, and observations that are important to that individual. An olog is a formal specification of an individual's world-view in a language representing the concepts and relationships used by that individual. In addition to the formulation of an expressive language, a specification needs to contain axioms (facts) that constrain the possible interpretations of that language.

Since the ologs of different individuals are encoded in different languages, the important need to merge disparate ologs into a more general representation is difficult, time-consuming and expensive. The solution is to develop appropriate communication between individuals to allow interoperability of their ologs. Communication can occur between individuals when there is some commonality between their world-views. It is this commonality that allows one individual to benefit from the knowledge and experience of another. In this section we will discuss how to formulate these channels of communication, thereby describing a generalized and practical technique for merging ologs.

The mathematical concept that makes it all work is that of a functor. A functor is a mapping from one category to another that preserves all the declared structure. Whereas in Definition 3.2.3 we defined a functor from an olog to $\mathbf{Set}$, here we will be discussing functors from one olog to another.

Suppose we have two ologs, $\mathcal{C}$ and $\mathcal{D}$, that represent the world-views of two individuals. A functor $F\colon\mathcal{C}\to\mathcal{D}$ is basically a way of matching each type (box) of $\mathcal{C}$ to a type of $\mathcal{D}$, and each aspect (arrow) in $\mathcal{C}$ to an aspect (or path of aspects) in $\mathcal{D}$. Once ologs are aligned in this way, communication can occur: the two individuals know what each other is talking about. In fact, mathematically we can show that instance data held in $\mathcal{C}$ can be transformed (in coherent ways) to instance data held in $\mathcal{D}$, and vice versa (see [20]). In simple terms, once individuals understand each other in a certain domain (be it social, mathematical, etc.), they can communicate their views about it.

While the basic idea is not hard, the details can be a bit technical. This section is written in a more formal and logical style, and is decidedly more difficult than the others. For this section only, we assume the reader is familiar with the notion of fibered categories, colimits in the category $\mathbf{Cat}$ of categories, etc. We return to our more informal style in Section 5, where we discuss how an individual can author a more expressive olog.

### Categories and their presentations

We never defined categories in this paper, but we defined ologs and said that the two notions amounted to the same thing. Thus, we implied that a category consists of the following: a set of objects, a set of arrows (each pointing from one object to another), and a congruence relation on paths.5 This differs from the standard definition of categories (see [19]), which replaces our congruence relation with a composition rule and associativity law (obtained by taking the categorical quotient). One could say that an olog is a presentation of a category by generators (objects and arrows) and relations (path congruences). Any category can be resolved and presented in such a way, which we will call a specification. Likewise any functor can be resolved and presented as a morphism between specifications. 6

Footnote 6: We take an agnostic approach to foundations here. With the presentation form, we show how categories and functors are definable in terms of sets and functions, indicating how category theoretic concepts could be defined in terms of set theory. However, we fully understand that **Set**, the category of sets and functions, is but one example of a topos, indicating how set theoretic concepts could be defined in terms of category theory.

In fact, this presentation form for categories (and the analogous one for functors) is preferable for our work on communication between ologs, because it separates the strictly graphical part of an olog (its types and aspects, regarded as the olog language) from the propositional part (its facts, regarded as the olog formalism). This presentation form is standard in the institutions [GB] and information flow [BS] communities, since it separates the mechanism of flow from the content of flow; in this case the formal content. Our work here applies the general theories of institutions and information flow to the specific logical system that underlies categories and functors,7 demonstrating how this logical system can be used for knowledge representation. Using the presentation forms for categories and functors, we show how communication between individuals is effected by the flow of information along channels.

Footnote 7: For the expert, this refers to the sketch logical system Sk, in its various manifestations.

### The architecture underlying information systems

We think of a community of people, businesses, etc. in terms of the ologs of each individual participant together with the information channels that connect them. These channels are functors between ologs, which allow communication to occur. The heterogeneity of multiple differing world-views connected through such links can lead to a flexibility and robustness of interaction. For example, heterogeneity allows for multiple schemas to be employed in the design of database systems in particular, and multiple languages to be employed in the design of knowledge representation systems in general.

For any olog, consider the underlying graph of types and aspects. We regard this graph as being the language of the olog, 8 with the facts of the olog being a subset of all the possible assertions that one can make within this language. Any two ologs with the same underlying graph of types and aspects have the same language, and since the facts of each olog are expressed in the same language, they can be "understood" by each other without translation. As such, we think of the collection of all ologs with the same language (underlying graph) as forming a homogeneous _context_, with the ologs ordered in a specialization-generalization hierarchy.

Footnote 8: Section 4.4 indicates how natural languages can be encoded into ologs.

Whereas an olog represents (the world-view of) a single individual, an information system (of ologs) represents a community of separate, independent and distributed individuals. Here we consider an information system to be a diagram of ologs of some shape **I**; that is, a collection of ologs and constraints indexed by a base category **I**. The parts of the system represent either the ologs of the various individuals in the system or common grounds needed for communication between the individuals. Each part of the system specifies its world-view as facts expressed in terms of its language. The system is heterogeneous, since each part has a separate language for the expression of its world-view. The morphisms between the parts are the alignment (constraint) links defining the common grounds.

 As will be made clear in a moment, there is an underlying distributed system consisting of the language (underlying graph) for each component part of the information system and a translation (graph morphism) for each alignment link. We can think of this distributed system as an underlying system of languages linked by translating dictionaries. This distributed system determines an information channel with core language (graph) and component translation links (graph morphisms) along which the specifications of each component part can flow to the core. We can think of this core as a universal language for the whole system and the channel as a translation mechanism from parts to whole. At the core, the direct flow of the component specifications are joined together (unioned) and allowed to interact through entailment. The result of this interaction can then be distributed back to the component parts, thereby allowing the separate parts of an information system to interoperate.

In this section, we will make all this clear and rigorous. As mentioned above, we will work with category presentations (here called _specifications_) rather than categories. We will discuss the homogeneous contexts called fibers in detail and give the axioms of satisfaction. We will then discuss how morphisms between graphs (the translating dictionaries between the ologs) allow for direct and inverse information flow between these homogeneous fiber contexts. Finally, we discuss specifications (also known as _theories_) and the lattice of theories construction for ontologies.

In Section 4.3 we will discuss how the information in ologs can be aligned by the use of common grounds. This alignment will result in the creation of _information systems_, which are systems of ologs connected together along functors. We will discuss how to take the information contained in each olog of a heterogeneous system and integrate it all into a single whole, called the fusion olog. Finally we will discuss how the consequence of bringing all this information together, and allowing it to interact, can be transferred back to each part of the system (individual olog) as a set of local facts entailed by remote ologs, allowing for a kind of interoperability between ologs. In Section 4.4 we will discuss conceptual graphs and their relationship to ologs.

#### 4.2.1. Fibers

A graph $G$ contains types as nodes and aspects as edges. The graphs underlying an olog is considered its _language_. Any category $\mathcal{C}$ has an underlying graph $|\mathcal{C}|$. In particular, $|\textbf{Set}|$ is the graph underlying the category of sets and functions. Olog (12) has an underlying graph containing the three types ${}^{\ulcorner}$person${}^{\urcorner}$, person-pair${}^{\urcorner}$ and ${}^{\urcorner}$woman${}^{\urcorner}$ and the three aspects 'has a parent', 'woman' and 'has as mother'. Olog (17) has an underlying graph containing the three types ${}^{\ulcorner}$employee${}^{\urcorner}$, ${}^{\ulcorner}$department${}^{\urcorner}$, and ${}^{\urcorner}$string${}^{\urcorner}$ and the six aspects 'manager', 'works in', 'secretary', 'name', 'first name' and 'last name'. Let $\textbf{eqn}(G)$ denote the set of all facts (equations) that are possible to express using the types and aspects of $G$. A $G$-specification is a set $E\subseteq\textbf{eqn}(G)$ consisting of some of the facts expressible in $G$. The singleton set with the one fact that "the female parent of a person is his/her mother" is a specification for the graph of Olog (12). The set with the two facts that "the manager has the same department as any employee" and "the secretary of a department is an employee in that department" is a specification for the graph of Olog (17). Let $\textbf{spec}(G)$ denote the collection of all $G$-specifications ordered by inclusion $E_{1}\subseteq E_{2}$.

 

#### 4.2.2. Satisfaction

It will be useful here to define an instance of a graph $G$, instead of an instance of a category $\mathcal{C}$. An instance of a graph populates the graph by assigning instance data to it. An instance of a graph $G$ is a graph morphism $D\colon G\to|\mathbf{Set}|$ mapping each type $x$ in $G$ to a set $D(x)$ of instances and mapping each aspect $e\colon x\to y$ in $G$ to an instance function $D(e)\colon D(x)\to D(y)$. Using database terminology, we also call $D$ a key diagram, since it gives the set of row identifiers (primary keys) of tables and the cell contents defined by key maps.

A key diagram $D\colon G\to|\mathbf{Set}|$ satisfies (is a model of) a $G$-fact $\epsilon\in\boldsymbol{eqn}(G)$ (see Definition 3.2.3), symbolized $D\models_{G}\epsilon$, when we have an equality of functions $D^{*}(\epsilon_{0})=D^{*}(\epsilon_{1})$. We also say that $\epsilon$ (holds in) is true when interpreted in $D$. An identity $(f=_{G}f)\colon i\to j$ holds in all key diagrams (hence, is a tautology), and vice-versa for any set $A\in|\mathbf{Set}|$ a constant key diagram $\Delta(A)\colon G\to|\mathbf{Set}|$ satisfies any fact $\epsilon\in\boldsymbol{eqn}(G)$. A key diagram $D\colon G\to|\mathbf{Set}|$ satisfies (is a model of) a $G$-specification $E$, symbolized $D\models_{G}E$, when it satisfies every fact in the specification. For any graph $G$, a $G$-specification $E$ entails a $G$-fact $\epsilon$, denoted by $E\vdash_{G}\epsilon$, when any model of the specification satisfies the fact. The consequence $E^{\bullet}$ of a $G$-specification $E$ is the set of all entailed equations. The consequence operator $(-)^{\bullet}$ is a closure operator, and the consequence of a specification is a congruence. For any $G$-specification $E$, entailment satisfies the following axioms.

(20) $$\begin{array}{rl}\text{(basic)}&\text{If $E$ contains the equation $e$, then $E$ entails $e$.}\\ \text{(reflexive)}&\text{$E$ entails the equations $(f=_{G}f)\colon i\to j$ for any path $f\colon i\to j$.}\\ \text{(symmetric)}&\text{If $E$ entails the equation $(f_{1}=_{G}f_{2})\colon i\to j$, then $E$ entails the equation $(f_{2}=_{G}f_{1})\colon i\to j$.}\\ \text{(transitive)}&\text{If $E$ entails the two equations $(f_{1}=_{G}f_{2})\colon i\to j$ and $(f_{2}=_{G}f_{3})\colon i\to j$,}\\ \text{then $E$ entails the equation $(f_{1}=_{G}f_{3})\colon i\to j$.}\\ \text{(compositional)}&\text{If $E$ entails the two equations $(f_{1}=_{G}f_{2})\colon i\to j$ and $(g_{1}=_{G}g_{2})\colon j\to k$,}\\ \text{then $E$ entails the equation $(f_{1}\,;\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\conceptual intent of a key diagram $D$, implicit in satisfaction, is the closed specification $\mbox{\boldmath{{int}}}(D)$ consisting of all facts satisfied by the key diagram. Hence, $D\models_{G}E$ iff $E\subseteq\mbox{\boldmath{{int}}}(D)$ iff $\mbox{\boldmath{{int}}}(D)\leq_{G}E$.11

Footnote 11: This is the first step in the algebraization of Tarski’s “semantic definition of truth” [Ken4].

#### 4.2.3. Elementary flow

A graph morphism $H\colon G_{1}\to G_{2}$ maps the types and aspects of $G_{1}$ to the types and aspects of $G_{2}$. Graph morphisms are the translations between ologs. A functor $\mathcal{F}\colon\mathcal{C}_{1}\to\mathcal{C}_{2}$ has an underlying graph morphism $|\mathcal{F}|\colon|\mathcal{C}_{1}|\to|\mathcal{C}_{2}|$. For any graph morphism $H\colon G_{1}\to G_{2}$, there is a fact function $\mbox{\boldmath{{eqn}}}(H)\colon\mbox{\boldmath{{eqn}}}(G_{1})\to\mbox{ \boldmath{{eqn}}}(G_{2})$ that maps a $G_{1}$-equation ($f_{1}=_{G_{1}}f_{1}^{\prime}$)$\colon i_{1}\to j_{1}$ to the $G_{2}$-equation ($H^{*}(f_{1})=_{G_{2}}H^{*}(f_{1}^{\prime})$)$\colon H(i_{1})\to H(j_{1})$, and a key diagram functor $\mbox{\boldmath{{dgm}}}(H)\colon\mbox{\boldmath{{dgm}}}(G_{2})\to\mbox{ \boldmath{{dgm}}}(G_{1})$ that maps a key diagram $D_{2}\colon G_{2}\to|\mbox{\boldmath{{Set}}}|$ to the key diagram $H\circ D_{2}\colon G_{2}\to|\mbox{\boldmath{{Set}}}|$.12 The fact function is the fundamental unit of information (formal) flow for ologs, and the key diagram functor is the fundamental unit of semantic flow for ologs.13 Formal flow is adjoint to semantic flow -- satisfaction is invariant under flow: $\mbox{\boldmath{{dgm}}}(H)(D_{2})\models_{G_{1}}\epsilon_{1}$ iff $D_{2}\models_{G_{2}}\mbox{\boldmath{{eqn}}}(H)(\epsilon_{1})$ for any graph morphism $H\colon G_{1}\to G_{2}$, source fact $\epsilon_{1}$ and target diagram $D_{2}$. Specifications can be moved along graph morphisms by extending the fact (equation) function. For any graph morphism $H\colon G_{1}\to G_{2}$, define the _direct flow_ operator $\mbox{\boldmath{{dir}}}(H)=\wp\mbox{\boldmath{{eqn}}}(H):\mbox{\boldmath{{ spec}}}(G_{1})\to\mbox{\boldmath{{spec}}}(G_{2})$14 and the _inverse flow_ operator $\mbox{\boldmath{{inv}}}(H)=\mbox{\boldmath{{eqn}}}(H)^{-1}((\cdot)^{\bullet}) :\mbox{\boldmath{{spec}}}(G_{2})\to\mbox{\boldmath{{spec}}}(G_{1})$. Direct and inverse flow are adjoint monotonic functions $\langle\mbox{\boldmath{{dir}}}(H)\dash{{inv}}(H)\rangle\colon\mbox{\boldmath{{ fbr}}}(G_{1})\to\mbox{\boldmath{{fbr}}}(G_{2})$ w.r.t. fiber order: $\mbox{\boldmath{{dir}}}(H)(E_{1})\geq_{G_{2}}E_{2}$ iff $E_{1}\geq_{G_{1}}\mbox{\boldmath{{inv}}}(H)(E_{2})$. For any graph morphism $H\colon G_{1}\to G_{2}$, any $G_{1}$-specification $E_{1}$, and any $G_{2}$-specification $E_{2}$, entailment satisfies the following axioms.

Footnote 12: The composition of graph morphisms is written in diagrammatic order.

Footnote 13: This is so, at the abstraction of institutions [Ken3].

Footnote 14: The symbol $\wp$ denotes the power-set operator.

\begin{tabular}{l l} (direct flow) & If $E_{1}$ entails the equation ($f=_{G_{1}}f^{\prime}$)$\colon i\to $\mathcal{F}\colon\boldsymbol{spec}(\mathcal{C}_{1})\to\boldsymbol{spec}( \mathcal{C}_{2})$. Hence, the presentation form for a functor does exactly what the functor does. The fibered category of specifications $\boldsymbol{Spec}$ has specifications as objects and specification morphisms as morphisms. Thus, it is defined in terms of information flow. There is an underlying graph functor $\boldsymbol{gph}\colon\boldsymbol{Spec}\to\boldsymbol{Gph}$ from specifications to graphs $\langle G,E\rangle\mapsto G$. The subcategory over any fixed graph $G$ is the fiber $\boldsymbol{fbr}(G)$; because of the opposite orientation, we say that "the category of specifications points downward in the concept lattice". Throughout this section we identify ologs with specifications and olog morphisms with specification morphisms.

#### 4.2.5. The lattice of theories construction

Sowa's "lattice of theories" construction (LOT) describes a modular framework for ontologies [12]. The Olog formalism follows the approach to LOT described in [10].15 In the Olog formalism, LOT is locally represented by the entailment preorders $\boldsymbol{spec}(G)$, and globally represented by the category of specifications $\boldsymbol{Spec}$. We follow the discussion in section 6.5 "Theories, Models and the World" of Sowa [12]. From each olog (specification) in the "lattice of theories", the entailment ordering defines paths to the more generalized ologs above and the more specialized ologs below. Sowa defines four ways for moving along paths from one olog to another: contraction, expansion, revision and analogy.

Footnote 15: The IFF term ‘theory’ is replaced by the Olog term ‘specification’ or ‘olog’.

**Contraction:**: Any olog can be contracted or reduced to a smaller, simpler olog, moving upward in the preorder $\boldsymbol{spec}(G)$, by deleting one or more facts.
**Expansion:**: Any olog can be expanded, moving downward in the preorder $\boldsymbol{spec}(G)$, by adding one or more facts.
**Revision:**: A revision step is composite, moving crosswise in the preorder $\boldsymbol{spec}(G)$; it uses a contraction step to discard irrelevant details, followed by an expansion step to added new facts.
**Analogy:**: Unlike contraction and expansion, which move to nearby ologs in an entailment preorder $\boldsymbol{spec}(G)$, analogy moves to an olog in a remote entailment preorder in the category $\boldsymbol{Spec}$ via the flow along an underlying graph morphism $H\colon G_{1}\to G_{2}$ by systematically renaming the types and aspects that appear in the facts: any olog $E_{1}$ in $\boldsymbol{spec}(G_{1})$ is moved (by systematic renaming) to the olog $\boldsymbol{dir}(H)(E_{1})$ in $\boldsymbol{spec}(G_{2})$.

According to Sowa, the various methods used in nonmonotonic logic and the operators for belief revision correspond to movement through the lattice of theories.

### Alignment and integration of information systems

#### 4.3.1. Common ground

Given the world-views of two individuals, as represented by ologs $\mathcal{S}_{1}=\langle G_{1},E_{1}\rangle$ and $\mathcal{S}_{2}=\langle G_{2},E_{2}\rangle$, there is little hope that one of them completely contains the other (even after allowing for renaming of types and aspects), and there is correspondingly little chance of finding a meaningful olog morphism between the two. Instead, in order to communicate the two individuals could attempt to find a common ground, a third olog $\mathcal{S}=\langle G,E\rangle$ and meaningful morphisms16 $H_{1}\colon\mathcal{S}\to\mathcal{S}_{1}$ and $H_{2}\colon\mathcal{S}\to\mathcal{S}_{2}$.17 This connection is a $1$-dimensional knowledge network $\mathcal{S}_{1}\xleftarrow{H_{1}}\mathcal{S}\xrightarrow{H_{2}}\mathcal{S}_{2}$ of shape $\bullet\leftarrow\bullet\to\bullet$ called a span (in $\mathbf{Spec}$), where each node is an olog and each edge is a morphism between ologs. The requirements of this span are that $\textbf{{dir}}(H_{1})(E)\geq_{G_{1}}E_{1}$ and $\textbf{{dir}}(H_{2})(E)\geq_{G_{2}}E_{2}$, two requirements involving local flow. Equivalently, that $E\geq_{G}\textbf{{inv}}(H_{1})(E_{1})\vee_{G}\textbf{{inv}}(H_{2})(E_{2})$. The latter precise expression can be rendered in natural language as "the world-view of the common ground is contained in the combined world-views of the two individuals". The various local direct/inverse flows allow world-views to be compared. Such a common ground can be expanded and improved over time. The basic idea is that one individual can attempt to explain a new idea (type, aspect or fact) to another in terms of the common ground. Then the other individual can either interpret this idea as they already have, learn from it (i.e. freely add it to their olog), or reject it. We view an olog morphism $H_{1}\colon\mathcal{S}_{1}\to\mathcal{S}_{2}$ as an atomic constraint (alignment) link between $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$.18 We view a common ground span $\mathcal{S}_{1}\xleftarrow{H_{1}}\mathcal{S}\xrightarrow{H_{2}}\mathcal{S}_{2}$ as a molecular constraint between $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, which is weakest when $\mathcal{S}=\emptyset$ and strongest when $\mathcal{S}_{1}=\mathcal{S}=\mathcal{S}_{2}$.

Footnote 17: A common ground olog is also called a reference ontology in knowledge representation.

Footnote 18: This is so, at the abstraction of institutions [Ken3].

#### 4.3.2. Systems of ologs

In the general case, more than two individuals will share a common ground. For example, companies that do business together may have a common-ground olog as part of a legal contract; or, the various participants at a conference will have some common understanding of the topic of that conference. In fact, for any finite set of ologs $\mathbb{X}=\{\mathcal{S}_{1},\mathcal{S}_{2},\ldots,\mathcal{S}_{n}\}$, there should be a common ground world-view (even if empty), say $\mathcal{S}_{\mathbb{X}}$. If $\mathbb{Y}\subseteq\mathbb{X}$ is a subset, then there should be a map $\mathcal{S}_{\mathbb{X}}\to\mathcal{S}_{\mathbb{Y}}$ because any common understanding held by the individuals in $\mathbb{X}$ is held by the individuals in $\mathbb{Y}$. For example, the triangular-shaped diagram

(21)

represents three individuals $\{1,2,3\}$, their ologs $\{\mathcal{S}_{1},\mathcal{S}_{2},\mathcal{S}_{3}\}$, their pair-wise commonality ologs $\{\mathcal{S}_{12},\mathcal{S}_{13},\mathcal{S}_{23}\}$, and their three-way commonality olog $\mathcal{S}_{123}$. This diagram, which stands for the interaction between individuals $\{1,2,3\}$, does not stand alone, but is part of an intricate web of other ologs and alignment constraints. In particular, individuals $1$ and $3$ may be part of some different interacting group, say of individuals $\{1,3,6,7\}$, and hence the right edge of the diagram would be part of some tetrahedron-shaped diagram with vertices $\{1,3,6,7\}$. If we take the point-of-view that "a collection of ologs representing the world-views of various individuals" is a system, then we can think of the ologs as being the types of that system, the morphisms connecting the ologs as being the aspects of that system, with the shape of a system being its underlying graph. In essence, we can apply ologs to themselves. In the system represented by diagram (21), there are seven types $\{\mathcal{S}_{1},\mathcal{S}_{2},\mathcal{S}_{3},\mathcal{S}_{12},\mathcal{S}_{ 13},\mathcal{S}_{23},\mathcal{S}_{123}\}$ and nine aspects $\{\cdots,\mathcal{S}_{123}\rightarrow\mathcal{S}_{13},\dots\}$, and the shape looks like this

In addition, we can introduce certain facts to represent the meaning of that system and then enforce those facts.

A _distributed system_ is a diagram (functor) $\mathcal{G}\colon\mathbf{I}\rightarrow\mathbf{G}\mathbf{ph}$ of shape $\mathbf{I}$ within the ambient category $\mathbf{G}\mathbf{ph}$. As such, it consists of an indexed family $\{G_{n}\mid n\in\mathbf{I}\}$ of graphs together with an indexed family $\{G_{e}\colon G_{n}\to G_{m}\mid(e\colon n\to m)\in\mathbf{I}\}$ of graph morphisms. Let $\mathbf{Dist}(\mathbf{I})$ denote the collection of distributed systems of shape $\mathbf{I}$. An _information system_ is a diagram $\mathcal{S}\colon\mathbf{I}\rightarrow\mathbf{Spec}$ of shape $\mathbf{I}$ within the ambient category $\mathbf{Spec}$. As such, it consists of an indexed family $\{\mathcal{S}_{n}=\langle G_{n},E_{n}\rangle\mid n\in\mathbf{I}\}$ of ologs together with an indexed family $\{\mathcal{S}_{e}\colon\mathcal{S}_{n}\rightarrow\mathcal{S}_{m}\mid(e\colon n \to m)\in\mathbf{I}\}$ of olog morphisms. Some of these ologs might represent the world-views of various individuals, whereas others could be common grounds; also included might be portals between individual ologs and common grounds, as in the CG example of Section 4.4. Let $\mathbf{Info}(\mathbf{I})$ denote the collection of information systems of shape $\mathbf{I}$. An information system $\mathcal{S}$ with component ologs $\mathcal{S}_{n}=\langle G_{n},E_{n}\rangle$ has an underlying distributed system $\mathcal{G}$ of the same shape with component graphs $G_{n}$ for $n\in\mathbf{I}$. For any distributed system $\mathcal{G}$, let $\boldsymbol{info_{1}}(\mathcal{G})$ denote the collection of information systems over $\mathcal{G}$ of shape $\mathbf{I}$. There is a pointwise entailment order $\mathcal{S}\leq^{\mathbf{I}}_{\mathcal{G}}\mathcal{S}^{\prime}$ on $\boldsymbol{info_{1}}(\mathcal{G})$ when component ologs satisfy the same entailment ordering $E_{n}\leq_{G_{n}}E^{\prime}_{n}$ for $n\in\mathbf{I}$, and by taking the coproduct there is a pointwise entailment order on $\mathbf{Info}(\mathbf{I})=\coprod_{\mathcal{G}\in\mathbf{Dist}(\mathbf{I})} \boldsymbol{info_{1}}(\mathcal{G})$. A constant distributed system $\Delta(G)\in\mathbf{Dist}(\mathbf{I})$ is a distributed system $\Delta(G)\colon\mathbf{I}\rightarrow\mathbf{G}\mathbf{ph}$ with the same language $G$ for any index $n\in\mathbf{I}$. Any constant distributed system defines join and meet monotonic functions $\bigvee^{\mathbf{I}}_{G},\bigwedge^{\mathbf{I}}_{G}:\boldsymbol{info_{1}}( \Delta(G))\rightarrow\boldsymbol{fbr}(G)$ mapping an information system $\mathcal{S}\in\boldsymbol{info_{1}}(\Delta(G))$ to the join and meet ologs $\bigvee\mathcal{S}=\bigcup_{n\in\mathbf{I}}E_{n}$ and $\bigwedge\mathcal{S}=\bigcap_{n\in\mathbf{I}}E_{n}$ in $\boldsymbol{fbr}(G)$. The join monotonic function is adjoint to the constant monotonic function $\Delta^{\mathbf{I}}_{G}:\boldsymbol{fbr}(G)\rightarrow\boldsymbol{info_{1}}( \Delta(G))$ that distributes an olog $\mathcal{S}^{\prime}\in\boldsymbol{fbr}(G)$ to the various locations $n\in\mathbf{I}$ forming a constant information system $\Delta(\mathcal{S}^{\prime})\in\boldsymbol{info_{1}}(\Delta(G))$, since $\bigvee\mathcal{S}\geq_{G}\mathcal{S}^{ defined by $\textbf{{dir}}_{\textbf{1}}(\theta)(\mathcal{S})_{n}=\textbf{{dir}}(\theta_{n})(E_{n})$ for $n\in\textbf{I}$.19 An inverse flow operator $\textbf{{inv}}_{\textbf{1}}(\theta):\textbf{{info}}_{\textbf{1}}(\mathcal{G}^{ \prime})\rightarrow\textbf{{info}}_{\textbf{1}}(\mathcal{G})$ can similarly be defined. Direct and inverse flow are adjoint monotonic functions $\langle\textbf{{dir}}_{\textbf{1}}(\theta)\dashv\textbf{{inv}}_{\textbf{1}}( \theta)\rangle:\textbf{{info}}_{\textbf{1}}(\mathcal{G})\rightarrow\textbf{{info }}_{\textbf{1}}(\mathcal{G}^{\prime})$, since $\textbf{{dir}}_{\textbf{1}}(\theta)(\mathcal{S})\geq^{\textbf{I}}_{\mathcal{G }^{\prime}}\mathcal{S}^{\prime}$ iff $\mathcal{S}\geq^{\textbf{I}}_{\mathcal{G}}\textbf{{inv}}_{\textbf{1}}(\theta) (\mathcal{S}^{\prime})$. An information system morphism $\theta\colon\mathcal{S}\Rightarrow\mathcal{S}^{\prime}$ in $\textbf{{Info}}(\textbf{I})$ consists of a collection $\{\theta_{n}\colon\mathcal{S}_{n}\rightarrow\mathcal{S}^{\prime}_{n}\mid n \in\textbf{I}\}$ of component olog morphisms, which are systematically coordinated and preserve alignment in the sense that they satisfy the naturality conditions $\mathcal{S}_{e}\circ\theta_{m}=\theta_{n}\circ\mathcal{S}^{\prime}_{e}$ for any indexing link $e\colon n\to m$ in **I**; equivalently, $\theta$ is a morphism between the underlying distributed systems $\theta\colon\mathcal{G}\Rightarrow\mathcal{G}^{\prime}$ and the direct flow of $\mathcal{S}$ is at least as general as $\mathcal{S}^{\prime}$: $\textbf{{dir}}_{\textbf{1}}(\theta)(\mathcal{S})\geq^{\textbf{I}}_{\mathcal{G }^{\prime}}\mathcal{S}^{\prime}$. The ordering $\mathcal{S}\geq^{\textbf{I}}_{\mathcal{G}}\mathcal{S}^{\prime}$ is an information system morphism $\theta\colon\mathcal{S}\Rightarrow\mathcal{S}^{\prime}$ with identity component translations $\theta_{n}=\textbf{{id}}_{G_{n}}$ for each index $n\in\textbf{I}$.

Footnote 19: Well-defined, since $\textbf{{dir}}(G^{\prime}_{e})(\textbf{{dir}}(\theta_{n})(E_{n}))=\textbf{{dir }}(\theta_{m})(\textbf{{dir}}(G_{e})(E_{n}))\geq_{m}\textbf{{dir}}(\theta_{m}) (E_{m})$.

#### 4.3.4. Channels

We continue with our systems point-of-view. Since we have represented the whole system as a diagram $\mathcal{S}$ of parts (ologs) $\mathcal{S}_{n}$ with part-part relations (alignment constraints) $\mathcal{S}_{n}\rightarrow\mathcal{S}_{m}$, we also want to represent the whole system as an olog $\mathcal{C}$ with part-whole relations $\mathcal{S}_{n}\rightarrow\mathcal{C}$.20 An _information channel_$\langle\gamma\colon\mathcal{M}\Rightarrow\Delta(C),C\rangle$ consists of an indexed family $\{\gamma_{n}\colon G_{n}\to C\mid n\in\textbf{I}\}$ of graph morphisms called flow links with a common target graph $C$ called the core of the channel. A channel $\langle\gamma,C\rangle$ covers a distributed system $\mathcal{G}$ of shape **I** when the part-whole relationships respect the alignment constraints (are consistent with the part-part relationships): $\gamma_{n}=G_{e}\circ\gamma_{m}$ for each indexing morphism $e\colon n\to m$ in **I**. A covering channel is a distributed system morphism $\gamma\colon\mathcal{G}\Rightarrow\Delta(C)$ in $\textbf{Dist}(\textbf{I})$ from distributed system $\mathcal{G}$ to constant distributed system $\Delta(C)\colon\textbf{I}\rightarrow\textbf{{Gph}}$. Such a channel defines a direct flow operator $\textbf{{dir}}_{\textbf{I}}(\gamma):\textbf{{info}}_{\textbf{1}}(\mathcal{G}) \rightarrow\textbf{ $\boldsymbol{dir}_{(\mathbf{I},\mathcal{G})}=\boldsymbol{dir_{\mathbf{I}}}(\iota) \cdot\vee_{\hat{\mathcal{G}}}^{\mathbf{I}}:\boldsymbol{info_{\mathbf{I}}}( \mathcal{G})\rightarrow\boldsymbol{fbr}(\widehat{\mathcal{G}})$. Direct system flow has two steps: (i) direct (fixed shape) system flow of an information system along the optimal channel ($\mathbf{Dist}(\mathbf{I})$-morphism) $\iota\colon\mathcal{G}\Rightarrow\Delta(\widehat{\mathcal{G}})$ and (ii) lattice join combining the contributions of the parts into a whole. In the opposite direction, there is an _inverse system flow_ monotonic function (see Figure 1) $\boldsymbol{inv}_{(\mathbf{I},\mathcal{G})}=\Delta_{\mathcal{G}}^{\mathbf{I}} \cdot\boldsymbol{inv_{\mathbf{I}}}(\iota)\colon\boldsymbol{fbr}(\widehat{ \mathcal{G}})\rightarrow\boldsymbol{info_{\mathbf{I}}}(\mathcal{G})$. Inverse system flow has two steps: (i) mapping an olog with core language $\widehat{\mathcal{G}}$ to a constant information system over $\Delta(\widehat{\mathcal{G}})$ with shape $\mathbf{I}$ by distributing the olog to the locations $n\in\mathbf{I}$, and (ii) inverse (fixed shape) system flow of this constant information system back along the optimal channel $\iota\colon\mathcal{G}\Rightarrow\Delta(\widehat{\mathcal{G}})$. Direct system flow is adjoint to inverse system flow $\langle\boldsymbol{dir}_{(\mathbf{I},\mathcal{G})}\dashv\boldsymbol{inv}_{( \mathbf{I},\mathcal{G})}\rangle\colon\boldsymbol{info_{\mathbf{I}}}(\mathcal{G })\rightarrow\boldsymbol{fbr}(\widehat{\mathcal{G}})$, since the composition components are adjoint. For any distributed system $\mathcal{G}\in\mathbf{Dist}(\mathbf{I})$ with optimal core $\widehat{\mathcal{G}}=\coprod\mathcal{G}$, any information system $\mathcal{S}\in\boldsymbol{info_{\mathbf{I}}}(\mathcal{G})$, and any olog $\widehat{\mathcal{S}}\in\boldsymbol{fbr}(\widehat{\mathcal{G}})$, entailment satisfies the following axioms.

\begin{tabular}{l l} (direct flow) & If $E_{n}$ entails the equation $(f=_{\mathcal{G}n}f^{\prime})\colon\iota\to j$, then $\boldsymbol{dir}_{(\mathbf{I},\mathcal{G})}(\mathcal{S})$ entails \\  & the equation $(\iota_{n}^{*}(f)=_{\mathcal{G}}\iota_{n}^{*}(f^{\prime}))\colon\iota_{n}(i) \rightarrow\iota_{n}(j)$ for any $n\in\mathbf{I}$. \\ (inverse flow) & If $\widehat{\mathcal{S}}$ entails the equation $(\iota_{n}^{*}(f)=_{\mathcal{G}}\iota_{n}^{*}(f^{\prime}))\colon\iota_{n}(i) \rightarrow\iota_{n}(j)$, then $\boldsymbol{inv}_{(\mathbf{I},\mathcal{G})}(\widehat{\mathcal{S}})_{n}$ entails the equation $(f=_{\mathcal{G}n}f^{\prime})\colon i\to j$ for any $n\in\mathbf{I}$. \\ \end{tabular}

These are converted to inference rules in Table 1. Information flow can be used to compute the fusion olog for an information system and to define the consequence of an information system. Fusion is direct system flow, and consequence is the composition of direct and inverse system flow. Let $\mathcal{S}\in\boldsymbol{info_{\mathbf{I}}}(\mathcal{G})$ be any information system. The fusion $\coprod\mathcal{S}=\boldsymbol{dir}_{(\mathbf{I},\mathcal{G})}(\mathcal{S})= \langle\coprod\mathcal{G},\bigvee_{n\in\mathbf{I}}\boldsymbol{dir}(\iota_{n} )(E_{n})\rangle\in\boldsymbol{fbr}(\widehat{\mathcal{G}})$ is an olog that represents the whole system in a centralized fashion [Ken2],[Ken3]. The consequence $\mathcal{S}_{(\mathbf{I},\mathcal{G})}^{\bullet}=\boldsymbol{inv}_{(\mathbf{ I},\mathcal{G})}(\boldsymbol{dir}_{(\mathbf{I},\mathcal{G})}(\mathcal{S}))= \boldsymbol{inv}_{(\mathbf{I},\mathcal{G})}(\coprod\mathcal{S})=\{\boldsymbol{ inv}(\iota_{n})(\coprod\mathcal{S})\mid n\in\ entailment order $\preceq$ on $\mathbf{Info}(\mathbf{I})$ is defined by $\mathcal{S}_{1}\preceq\mathcal{S}_{2}$ when $\mathcal{S}_{1}^{\bullet}\leq\mathcal{S}_{2}^{\bullet}$; equivalently, $\mathcal{S}_{1}^{\bullet}\leq\mathcal{S}_{2}$. Pointwise order is stronger than system entailment order: $\mathcal{S}_{1}\leq\mathcal{S}_{2}$ implies $\mathcal{S}_{1}\preceq\mathcal{S}_{2}$. This is a specialization-generalization order. Any information system $\mathcal{S}$ is entailment equivalent to its consequence $\mathcal{S}\cong\mathcal{S}^{\bullet}$. An information system $\mathcal{S}$ is closed when it is equal to its consequence $\mathcal{S}=\mathcal{S}^{\bullet}$.

The whole effect of taking the system consequence may be greater than the sum of its parts, in the sense that $\mathcal{S}_{n}\geq_{n}\mathcal{S}_{n}^{\bullet_{n}}\geq_{n}\bigvee_{m}\textbf {inv}(\iota_{n})(\textbf{dir}(\iota_{m})(\mathcal{S}_{m}))\geq_{n}\mathcal{S}_ {n}^{\bullet}$ for any $n\in\mathbf{I}$, since separate parts may have a productive interaction at the channel core. A final part of an information system is a part with no non-trivial constraint links from it. (The graphical subsystem beneath) nonfinal parts are necessary for the alignment of information systems, resulting in the equivalencing of types and aspects through quotienting. However, because of the covering condition $\iota_{n}=G_{e}\circ\iota_{m}$ and the entailment order $\textbf{dir}(G_{e})(E_{n})\geq_{m}E_{m}$ for constraint links $\mathcal{S}_{e}\colon\mathcal{S}_{n}\to\mathcal{S}_{m}$, only the fact(ual) content of final parts of information systems are necessary to compute the system fusion and consequence.

#### 4.3.6. General examples

Here are some examples of system fusion/consequence.

* An information system $\mathcal{S}$ with a constant underlying distributed system, $G_{i}=G$ for all $n\in\mathbf{I}$, gathers together all the component parts of the information system and forms their consequence. It has identity flow links $\{\mathit{t}_{n}=\mathit{id}_{G}\colon G\to G=\coprod\mathcal{G}\mid n\in \mathbf{I}\}$, component join fusion $\coprod\mathcal{S}=\bigvee_{n\in\mathbf{I}}\mathcal{S}_{n}=\langle G,\bigcup_{ n\in\mathbf{I}}E_{n}\rangle$, and constant system consequence $\mathcal{S}_{n}^{\blacklozenge}=\bigvee_{n^{\prime}\in\mathbf{I}}\mathcal{S} _{n^{\prime}}\big{)}^{\star}$ for all $n\in\mathbf{I}$.
* A discrete information system $\mathcal{S}=\{\mathcal{S}_{n}=\langle G_{n},E_{n}\rangle\mid n\in\mathbf{I}\}$ with no constraint links $G_{e}\colon\mathcal{S}_{n}\to\mathcal{S}_{m}$ for $n\neq m$, has coproduct injection flow links $\iota_{n}\colon G_{n}\to+_{n\in\mathbf{I}}G_{n}$, non-restricting fusion, and inverse flow projecting back to individual component consequence $\mathcal{S}_{n}^{\blacklozenge}=\mathcal{S}_{n}^{\blacklozenge}$ for all $n\in\mathbf{I}$. No alignment (constraint) links means no interaction.
* An information system $\mathcal{S}=\{\mathcal{S}_{1}\stackrel{{ H_{1}}}{{\longleftarrow}} \mathcal{S}\stackrel{{ H_{2}}}{{\longrightarrow}}\mathcal{S}_{2}\}$ consisting of a single common ground $\mathcal{S}=\langle G,E\rangle$ between two component ologs $\mathcal{S}_{1}=\langle G_{1},E_{1}\rangle$ and $\mathcal{S}_{2}=\langle G_{2},E_{2}\rangle$, with underlying distributed system (span) $\mathcal{G}=\{G_{1}\stackrel{{ H_{1}}}{{\longleftarrow}}G\stackrel{{ H_{2}}}{{\longrightarrow}}G_{2}\}$, has pushout injection flow links $G_{1}\stackrel{{\iota_{1}}}{{\longrightarrow}}\coprod\mathcal{G }\stackrel{{\iota_{2}}}{{\longleftarrow}}G_{2}$, direct image union fusion $\coprod\mathcal{S}=\langle\coprod\mathcal{G},\mathit{\mathit{\mathit{\mathit{ \mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{ \mathit{\mathit{\mathitmathit{     \mathitmathitmathitmathitmathitmathit{        \mathit{   \mathitmathit{     \mathitmathit{    \mathitmathit{    \mathitmathit{    \mathitmathit{    \mathitmathit{    \mathit{ \mathitmathit{    \mathit{ \mathitmathit{    \mathitmathit{    \mathit{ \mathitmathit{   \mathitmathit{   \mathitmathit{    \mathit{ \mathitmathit{    \mathit{  \mathitmathit{   \mathitmathit{   \mathit{  \mathitmathit{   \mathitmathit{   \mathitmathit{   \mathit{  \mathitmathit{    \mathit{  \mathitmathit{   \mathitmathit{   \mathit{  \mathitmathit{    \mathit{  \mathitmathit{   \mathit{   \mathitmathit{   \mathit{   \mathit{  \mathitmathit{    \mathit{  \mathitmathit{    \mathit{  \mathitmathit{    \mathit{  \mathit{   \mathit{   \mathit{   \mathit{   \mathit{    \mathit{   \mathit{   \mathit{    \mathit{   \mathit{   \mathit{    \mathit{   \mathit{     \mathit{  \mathit{     \mathit{    \mathit{ \mathit{      \mathit{ \mathit{      \mathit{ \mathit{       \mathit{ \mathit{      \mathit{ \mathit{      \mathit{ \mathit{    \mathit{   \mathit{    \mathit{   \mathit{    \mathit{   \mathit{    \mathit{   \mathit{    \mathit{   \mathit{    \mathit{    \mathit{   \mathit{    \mathit{   \mathit{    \mathit{   \mathit{ roles 'agent', 'instrument' and 'destination'.

(23)

(24)

(inst)

Bus

However, the case relations that semantically describe the thematic roles should be viewed as functional in nature; that is, for any instance of the action of a sentence's verb there is a unique entity described by a noun phrase of the sentence. When this semantics is respected, the translation to thematic roles becomes a process of "linearization", which is best described abstractly as: (1) the identification of relation types with entity types, (2) the translation of a sorted multiarity relation to a span of functions, one function for each role, and (3) the functional interpretation of thematic roles.

The Olog formalism, which also represents DBS and NLP, is a version of equational logic. Both the Olog and CG formalisms were designed as graphical representations. However, the CG formalism is binary and relational, whereas the Olog formalism is unary and functional. The CG formalism is binary since it has two kinds of type, concepts and relations; it is relational in the way it interprets edges. The Olog formalism is unary since it has only one kind of type, the abstract concept; it is functional in the way it interprets aspects (edges). However, much of the semantics of the CG formalism can be transformed to the Olog formalism by the process of linearization23, thereby gaining in efficiency and conciseness. For example, conceptual graph (22) can be linearized to the olog graph24

Footnote 23: The linearization process works for any binary/relational knowledge representation, such as CGs, entity-relationship data modelling [JRW], relational database systems [Ken5] or the Information Flow Framework [IFF1]. In the entity-relationship data modelling, $n$-ary relationship links are replaced by $n$-ary spans of aspects and attributes are included as types.

(25)

Since olog aspects are interpreted functionally, the functional nature of thematic roles is respected. In this manner, the olog formalism could be used to replace the CG representation of ontologies. For example, a community (acting as an individual) could build its ontology $\mathcal{C}$ from ground up by aligning it with some top-level reference ontology $\mathcal{T}$ (such as in the appendix of [Sow2]), thereby importing some formal semantics from $\mathcal{T}$. The following fragment demonstrates how this works.

Assume that ontology $\mathcal{T}$ contains the concept of "spatial process" as represented by the general concept type ${}^{\neg}$Spatial-Process${}^{\neg}$ with aspects ${}^{\neg}$Spatial-Process${}^{\neg}$${}^{\neg}$Agent${}^{\neg}$, ${}^{\neg}$Spatial-Process${}^{\neg}$${}^{\neg}$${}^{\neg}$Vehicle${}^{\neg}$ and ${}^{\neg}$Spatial-Process${}^{\neg}$${}^{\neg}$${}^{\neg}$${}^{\neg}$Location${}^{\neg}$. At some stage assume that the community ontology $\mathcal{C}$ has specified the concept type orderings ${}^{\neg}$${}^{\neg}$${}^{\neg}$${}^{\neg}$Agent${}^{\neg}$, ${}^{\neg}$Bus${}^{\neg}$$\leq$${}^{\neg}$Vehicle${}^{\neg}$ and ${}^{\neg}$City${}^{\neg}$$\leq$${}^{\neg}$Location${}^{\neg}$ with corresponding injective aspects ${}^{\neg}$Person${}^{\neg}$${}^{\neg}$${}^{\text{is}}$, ${}^{\neg}$Agent${}^{\neg}$, ${}^{\neg}$Bus${}^{\neg}$${}^{\neg}$${}^{\text{is}}$${}^{\neg}$Vehicle${}^{\neg}$ and ${}^{\top}$City${}^{\top}\xrightarrow{\text{is}}{\rightarrow}{}^{\top}$Location${}^{\top}$. At the next stage it could define a concept type ${}^{\top}$C${}^{\top}$ with aspects ${}^{\top}$C${}^{\top}\xrightarrow{\text{person}}{}^{\top}$Person${}^{\top}$, ${}^{\top}$C${}^{\top}\xrightarrow{\text{bus}}{}^{\top}$Bus${}^{\top}$ and ${}^{\top}$C${}^{\top}\xrightarrow{\text{city}}{}^{\top}$City${}^{\top}$, and link it with the reference ontology concept ${}^{\top}$Spatial-Process${}^{\top}$ by specifying a connecting aspect ${}^{\top}$C${}^{\top}\xrightarrow{\text{process}}{}^{\top}$Spatial-Process${}^{\top}$and asserting the facts 'person ; is = process ; agent', 'bus ; is = process ; vehicle' and 'city ; is = process ; location'.25 In the more expressive ologs with joins (Section 5), the process concept of "going to city by bus" can then be defined as the pullback of the "spatial process" concept: here, the concept type ${}^{\top}$Go${}^{\top}$ with aspects ${}^{\top}$Go${}^{\top}\xrightarrow{\text{person}}{}^{\top}$Person${}^{\top}$, ${}^{\top}$Go${}^{\top}\xrightarrow{\text{bus}}{}^{\top}$Bus${}^{\top}$ and ${}^{\top}$Go${}^{\top}\xrightarrow{\text{city}}{}^{\top}$City${}^{\top}$ is pulled back along the above injective aspects, resulting in the injective aspect ${}^{\top}$Go${}^{\top}\xrightarrow{\text{is}}{}^{\top}$Spatial-Process${}^{\top}$ with corresponding concept type ordering ${}^{\top}$Go${}^{\top}\leq{}^{\top}$Spatial-Process${}^{\top}$. As a result, the concept ${}^{\top}$C${}^{\top}$ has the new mediating aspect C $\xrightarrow{\text{going}}$ Go, which satisfies the fact 'going ; is = process'. In this manner the community ontology $\mathcal{C}$ has been enlarged.

Footnote 25: The symbol ‘;’ denotes concatenation or formal composition.

$\mathcal{C}$

$\mathcal{P}$

We assume that community ontology $\mathcal{C}$ and reference ontology $\mathcal{T}$ are combined into a portal ontology $\mathcal{P}$ with portal link $\mathcal{C}\xrightarrow{P}\mathcal{P}$ and alignment link $\mathcal{T}\xrightarrow{A}\mathcal{P}$. If some other ontology $\mathcal{C}^{\prime}$ is built up and aligned in the same fashion, then $\mathcal{T}$ is being used as a common ground, and we have a 'W'-shaped information system

(25)

with portals $\mathcal{P}$ and $\mathcal{P}^{\prime}$ being the final parts. This 'W'-shaped information system uses the sketch institution Sk for ologs. It can be compared to the 'W'-shaped information system in [12], which uses the information flow IF institution for (local) logics.

## 5. More expressive ologs I

In this section and the next (5 and 6) we will introduce limits and colimits within the context of ologs. These will allow authors to build ologs that are quite expressive. For example we can declare one type to be the union or intersection of other types. We do not assume mathematical knowledge beyond that of sets and functions, which were loosely defined in Section 2.2. However, the reader may benefit by consulting a reference on category theory, such as [Awo].

The basic ologs discussed in previous sections are based on the mathematical notion of categories, whereas the olog presentation language we will discuss in this section and the next are based on _general sketches_ (see [Mak]). The difference is in what can be expressed: in basic ologs we can declare types, aspects, and facts, whereas in general ologs we can express ideas like products and sums, as we will see below.

We will begin by discussing layouts, which will be represented categorically by "finite limits". As usual, the english terminology (layout) is not precise enough to express the notion we mean it to express (limit). Intuitively, a limit can be thought of as a system: it is a collection of units, each of a specific type, such that these units have compatible aspects. These will include types like ${}^{\neg}$a man and a woman with the same last name${}^{\neg}$. In Section 6 we will discuss groupings, which will be represented by colimits. These will include types like ${}^{\neg}$a thing that is either a pear or a watermelon${}^{\neg}$.

### Layouts

A dictionary might define the word _layout_ as something like "a structured arrangement of items within certain limits; a plan for such arrangement." In other words, we can lay out or specify the need for a set of parts, each of a given type, such that the parts fit together well. This idea roughly corresponds to the notion of limits in category theory, especially limits in the category of sets. Given a diagram of sets and functions, its limit is the set of ways to accordingly choose one element from each. For example, we could have a type ${}^{\neg}$a car and a driver${}^{\neg}$, which category-theoretically is a product, but which we are calling a "layout" -- a compound type whose parts are "laid out." Of course, the term layout is insufficient to express the precise meaning of limits, but it will have to do for now. To understand limits, one really only need understand pullbacks and products. These will be the subjects of Sections 5.2 and 5.3, or one can see [Awo] for more details.

### Pullbacks

Given three objects and two arrows arranged as to the left, the pullback is the commutative square to the right:

We write $A=B\times_{D}C$ and say "$A$ is the pullback of $B$ and $C$ over $D$." The question is, what does it signify? We will begin with some examples and then give a precise definition.

_Example 5.2.1_.: We will now give four examples to motivate the definition of pullback. In the first example, (26), both $B$ and $C$ will be subtypes of $D$, and in such cases the pullback will be their intersection. In the next two examples (27 and 28), only $B$ will be a subtype of $D$, and in such cases the pullback will be the "corresponding subtype of $C$" (as should make sense upon inspection). In the last example (29), neither $B$ nor $C$ will be a subtype of $D$. In each line below, the pullback of the diagram to the left is the diagram to the right. The reader should think of the left-hand olog as a kind of problem to which the new box $A$ in the right-hand olog is a solution.

 (26)

(26)

(27)

(28)

(29)

(29)

(30,0)

(31,0)

(32,0)

(33,0)

(34,0)

(35,0)

(36,0)

(37,0)

(38,0)
 See Example 5.2.3 for a justification of these, in light of Definition 5.2.2.

The following is the definition of pullbacks in the category of sets. For an olog, the instance data are given by sets (at least in this paper, see Section 3), so this definition suffices for now. See [Awo] for more details on pullbacks.

**Definition 5.2.2**.: Let $B,C,$ and $D$ be sets, and let $f\colon B\to D$ and $g\colon C\to D$ be functions. The _pullback_ of $B\xrightarrow{f}D\stackrel{{ g}}{{\leftarrow}}C$, denoted $B\times_{D}C$, is defined to be the set

$$B\times_{D}C:=\{(b,c)\mid b\in B,c\in C,\text{ and }f(b)=g(c)\}$$

together with the obvious maps $B\times_{D}C\to B$ and $B\times_{D}C\to C$, which send an element $(b,c)$ to $b$ and to $c$, respectively. In other words, the pullback of $B\xrightarrow{f}D\stackrel{{ g}}{{\leftarrow}}C$ is a commutative square

_Example 5.2.3_.: In Example 5.2.1 we gave four examples of pullbacks. For each, we will consider $B\xrightarrow{f}D\stackrel{{ g}}{{\leftarrow}}C$ to be sets and functions as in Definition 5.2.2 and explain how the set $A$ follows that definition, i.e. how its label fits with the set $B\times_{D}C=\{(b,c)\mid b\in B,c\in C,\text{ and }f(b)=g(c)\}$.

In the case of (26), the set $B\times_{D}C$ should consist of pairs $(w,l)$ where $w$ is a wealthy customer, $l$ is a loyal customer, and $w$ is equal to $l$ (as customers). But if $w$ and $l$ are the same customer then $(w,l)$ is just a customer that is both wealthy and loyal, not two different customers. In other words, an instance of the pullback is a customer that is both loyal and wealthy, so the label of $A$ fits.

In the case of (27), the set $B\times_{D}C$ should consist of pairs $(p,b)$ where $p$ is a person, $b$ is the color blue, and the favorite color of $p$ is equal to $b$ (as colors). In other words, it is a person whose favorite color is blue, so the label of $A$ fits. If desired, one could instead label $A$ with $\ulcorner$ a pair $(p,b)$ where $p$ is a person, $b$ is blue, and the favorite color of $p$ is $b\urcorner$.

In the case of (28), the set $B\times_{D}C$ should consist of pairs $(d,w)$ where $d$ is a dog, $w$ is a woman, and the owner of $d$ is equal to $w$ (as people). In other words, it is a dog whose owner is a woman, so the label of $A$ fits. If desired, one could instead label $A$ with $\ulcorner$ a pair $(d,w)$ where $d$ is a dog, $w$ is a woman, and the owner of $d$ is $w\urcorner$.

In the case of (29), the set $B\times_{D}C$ should consist of pairs $(f,s)$ where $f$ is a piece of furniture, $s$ is a space in our house, and the width of $f$ is equal to the width of $s$. This is fits perfectly with the label of $A$.

#### 5.2.4. Using pullbacks to classify

To distinguish between two things, one must find a common aspect of the two things for which they have differing results. For example, a pen is different from a pencil in that they both use some material to write (a common aspect), but the two materials they use are different. Thus the material which a writing implement uses is an aspect of writing implements, and this aspect serves to segregate or classify them. We can think of three such writing-materials: graphite, ink, and pigment-wax. For each, we will make a layout in the olog below:

$$\begin{array}{|c|c|}\hline\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\ The category-theoretic fact described above says that since $A=B\times_{D}C$ and $C=D\times_{F}E$, it follows that $A=B\times_{F}E$. That is, we can decuce the definition "a cellphone that has a bad battery is defined as a cellphone that has a battery which remains charged for less than one hour." In other words, $A=B\times_{F}E$.

### Products

Given a set of types (boxes) in an olog, one can select one instance from each. All the ways of doing just that comprise what is called the product of these types. For example, if $A=\ulcorner$a number between $1$ and $10\urcorner$ and $B=\ulcorner$a letter between x and z$\urcorner$, the product includes a total of $30$ elements, including $(4,z)$. We are ready for the definition.

**Definition 5.3.1**.: Given sets $A,B$, their _product_, denoted $A\times B$, is the set

$$A\times B=\{(a,b)\mid a\in A\text{ and }b\in B\}.$$

There are two obvious _projection maps_$A\times B\to A$ and $A\times B\to B$, sending the pair $(a,b)$ to $a$ and to $b$ respectively.

_Example 5.3.2_.: In Example 5.2.1, (29) we presented the idea of a piece of furniture that was the same width as a space in the house. What if we say that $\ulcorner$a nice furniture placement$\ulcorner$ is any space that is between $1$ and $8$ inches bigger than a piece of furniture? We can use a combination of products and pullbacks to create the appropriate type.

$$\begin{array}{|c|c|}\hline\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\ 

#### 5.3.3. Products of more (or fewer) types

The product of two sets $A$ and $B$ was defined in 5.3.1. One may also take the product of three sets $A,B,C$ in a similar way, so the elements are triples $(a,b,c)$ where $a\in A,b\in B$, and $c\in C$. In fact this idea holds for any number of sets. It even makes sense to take the product of one set (just $A$) or no sets! The product of one set is itself, and the product of no sets is the singleton set $\{*\}$. For more on this, see Section 5.5 or [Mac].

### Declaring an injective aspect

A function is called _injective_ if different inputs always yield different outputs. For example the function that doubles every integer $(x\mapsto 2x)$ is injective, whereas the function that squares every integer $(x\mapsto x^{2})$ is not because $3^{2}=(-3)^{2}$. An example of an injective aspect is $\ulcorner$a woman$\urcorner\xrightarrow{\text{is}}\urcorner$a person$\urcorner$ because different women are always different as people. An example of a non-injective aspect is $\ulcorner$a person$\urcorner\xrightarrow{\text{has as father}}\urcorner$a person$\urcorner$ because different people may have the same father.

The easiest way to indicate that an aspect is injective is to use a "hook arrow" as in $f\colon A\hookrightarrow B$, instead of a regular arrow $f\colon A\to B$, to denote it. For example, the first map is injective (and specified as such with a hook-arrow), but the second is not in the olog:

$$\boxed{\text{a person}}\subset\xrightarrow{\text{has}}\under{\text{a personality}}\xrightarrow{\text{can be classified}}$$

The author of this olog believes that no two people can have precisely the same personality (though they may have the same personality type).

We include injective aspects in this section because it turns out that injectivity can also be specified by pullbacks. See [nL1] for details.

### Singletons types

A singleton set is a set with one element; it can be considered the "empty product." In other words if we denote $A^{n}=A\times A\times\cdots A$ (where $A$ is written $n$ times), then $A^{0}$ is the empty product and is a singleton set. One can specify that a certain type has only one instance by annotating it with $A=\{*\}$ in the olog. For example the olog

$$\boxed{\text{God}}\xrightarrow{\text{is}}\under{\text{a good thing}}$$

says that the author considers $\ulcorner\text{God}\urcorner$ to be single. As a more concrete example, the intersection of $\{x\in\mathbb{R}\mid x\geq 0\}$ and $\{y\in\mathbb{R}\mid x\leq 0\}$ is a singleton set, as expressed in the olog

$$\boxed{\text{a real number }z}\under{\text{such that }z\geq 0}\under{\text{and }z\leq 0}\under{\text{is}} \under{\text{a real number }x\geq 0}\under{\text{a real number }x\geq 0}$$

$$\boxed{\text{is}}\under{\text{a real number }y}\under{\text{such that }y\leq 0}\under{\text{is}} \under{\text{a real number }}$$

$$\boxed{\text{is}}\under{\text{a real number }y}\under{\text{such that }y\leq 0}\under{\text{is}} \under{\text{a real number }}$$

$$\boxed{\text{is}}\under{\text{a real number }y}\under{\text{such that }y\leq 0}\under{\text{is}} \under{\text{a real number }}$$

$$\boxed{\text{is}}\under{\text{a real number }y}\under{\text{such that }y\leq 0}\under{\text{is}} \under{\text{a real number }}$$

$$\boxed{\text{is}}\under{\text{a real number }y}\under{\text{such that }y\leq 0}\under{\text{is}} \under{\text{a real number }y}\under{\text{a real numberThe fact that $A=B\times_{D}C$ and $A=\{*\}$ are declared indicates that there is only one possible instance of a real number that is in both $B$ and $C$.

### The universal property of layouts

We cannot do the notion of universal properties justice in this paper, but the basic idea is as follows. Suppose that $\mathcal{D}$ is an olog, that $D_{1},D_{2}$ are types in it, and that $D=D_{1}\times D_{2}$ (together with its projection maps $p_{1}\colon D\to D_{1}$ and $p_{2}\colon D\to D_{2}$) is their product.

(30)

The so-called universal property of products should be thought of as "an existence and uniqueness" claim in $\mathcal{D}$. Namely, for any type $X$ with maps $f\colon X\to D_{1}$ and $g\colon X\to D_{2}$, there is exactly one possible map $m\colon X\to D$ such that the facts $f=m;p_{1}$ and $g=m;p_{2}$ hold.

(31)

This may sound esoteric, but consider the following example.

The following olog is similar to the one in Example 5.3.2

Here the only unlabeled map is the horizontal one $B\to D$; how can we get away with leaving it unlabeled? How does a piece of furniture and a space in the house yield a pair of numbers? The answer is that $B$ has a map to $D_{1}$ (the path across the top) and a map to $D_{2}$ (the path across the bottom), and hence the universal property of products gives a unique arrow $B\to D$ such that the two facts indicated by checkmarks hold. (In terms of (30) and (31) we are using $X=B$.) In other words, there is exactly one way to take a piece of furniture and a space in the house and yield a pair of numbers if we enforce that the first number is the width in inches of the piece of furniture and the second number is the width in inches of the space in the house.

At this point we hope it is clear that the universal property of products is a useful and constructive one. We will not describe the other universal properties (either for pullbacks, singletons, or any colimits); as mentioned above they can be found in [Awo].

## 6. More expressive ologs II

In this section we will describe various colimits, which are in some sense dual to limits. Whereas limits allow one to "lay out" a team consisting of many different interacting or non-interacting parts, colimits allow one to "group" different types together. For example, whereas the product of ${}^{\sqcap}$a number between $1$ and $10$${}^{\sqcap}$ and ${}^{\sqcap}$a letter between x and z${}^{\sqcap}$ has 30 elements (such as $(3,y)$), the coproduct of these two types has 13 elements (including 4). Just as "layout" is a too weak a word to capture the essence of limits, "grouping" is too weak a word to capture the essence of colimits, but it will have to do.

We will start by describing coproducts or "disjoint unions" in Section 6.1. Then we will describe pushouts in Section 6.2, wherein one can declare some elements in a union to be equivalent to others. There is a category-theoretic duality between coproducts and products and between pushouts and pullbacks. It extends to a duality between surjections and injections and a duality between empty types and singleton types, the subject of Sections 6.3 and 6.4. The interested reader can see [Awo] for details.

### Coproducts

Coproducts are also called "disjoint unions." If $A$ and $B$ are sets with no members in common, then the coproduct of $A$ and $B$ is their union. However, if they have elements in common, one must include both copies in $A\amalg B$ and differentiate between them. Here is a definition.

**Definition 6.1.1**.: Given sets $A$ and $B$, their _coproduct_, denoted $A\amalg B$, is the set

$$A\amalg B=\{(a,``A")\mid a\in A\}\cup\{(b,``B")\mid b\in B\}.$$

There are two obvious _inclusion maps_$A\to A\amalg B$ and $B\to A\amalg B$, sending $a$ to $(a,``A")$ and $b$ to $(b,``B")$, respectively.

If $A$ and $B$ have no elements in common, then the one can drop the "$A$" and "$B$" labels without changing the set $A\amalg B$ in a substantial way. Here are two examples that should make the coproduct idea clear.

_Example 6.1.2_.: In the following olog the types $A$ and $B$ are disjoint, so the coproduct $C=A\amalg B$ is just the union.

[a person] is[a person or a cat] is[a cat] is[a cat] _Example 6.1.3_.: In the following oog, $A$ and $B$ are not disjoint, so care must be taken to differentiate common elements.

$$\begin{array}{|c|c|}\hline\par\ (32)

$$\begin{array}{|c|c|c|}\hline\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\ the function which subtracts $1$ from every integer ($x\mapsto x-1$) is surjective, because every integer has a successor; whereas the function that doubles every integer ($x\mapsto 2x$) is not surjective because odd numbers are not mapped to. The aspect is $\ulcorner$ a published paper$\ulcorner$$\underline{\text{was published in}}$$\ulcorner$$ Consider the olog

(34)

Some people own more than one computer, and some computers are owned by more than one person. Some computers are not owned by a person, and some people do not own a computer. The purpose of this section is to show how to use ologs to capture ideas such as "a person who owns a computer" and "a computer that is owned by a person". These are called the images of $p$ and $c$ respectively.

Every aspect has an image, and these are quite important for human understanding. For example the image of the map $\ulcorner$a person$\ulcorner$$\xrightarrow{\text{has as father}}\ulcorner$a person$\ulcorner$ is the type $\ulcorner$a father$\urcorner$. In other words, a father is defined to be a person $x$ for which there is some other person $y$ such that $x$ is the father of $y$.

The image of a function $f\colon A\to B$ is a commutative diagram (fact)

where $f_{s}$ is surjective and $f_{i}$ is injective (see Sections 6.3 and 5.4). We indicate that a type is the image of a map $f$ by annotating it with $\mathbf{Im}(f)$, as in the following olog:

$$\xy(0,0)*{A}="a";(0,0)*{B}="a";(0,0)*{A}="a";(0,0)*{B}="a";(0,0)*{A}="a";(0,0)*{B }="a";(0,0)*{A}="a";(0,0)*{B}="a";(0,0)*{A}="a";(0,0)*{B}="a";(0,0)*{A}="a";(0,0)*{B }="a";(0,0)*{B}="a";(0,0)*{A}="a";(0,0)*{B}="a";(0,0)*{B}="a";(0,0)*{A}="a";(0,0)*{B }="a";(0,0)*{B}="a";(0,0)*{B}="a 

### Application: Primitive recursion

We have already seen how ologs can be used to express a conceptual understanding of a situation (all the ologs thus far exemplify this idea). In this section we hope to convince the reader that ologs are also able to express certain computations. In particular we will show by example that primitive recursive functions (like factorial or fibonacci) can be expressed by ologs. In this way, we can to put computation and knowledge representation together into the same framework. It would be quite valuable to strengthen this connection by showing that Ologs (or an extension thereof) can express any recursive function (i.e. simulate Turing machines). This is an open research possibility.

_Example 6.6.1_.: In this example we will present an olog that can represent the "Factorial function," often denoted $n\mapsto n!$, where for example the factorial of $4$ is $24$. Recall that a _natural number_ is any nonnegative whole number: $0,1,2,3,4,\ldots$.

$$\begin{array}{|cccc|}&&f(n)=n!\\ \hline\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span \omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit \span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\span\omit\spanThe above olog defines the factorial function $(f)$ in terms of itself, which is the hallmark of primitive recursion. Note, however, that this same olog can compute many things besides the factorial function. That is, nothing about the olog says that the instances of ${}^{\neg}$Zero${}^{\neg}$ is the set $\{0\}$, that $\omega$ sends $0$ to $1$, that $d$ is the decrement function, or that $m$ is multiplication -- changing any of these will change $f$ as a function. For example, the same olog can be used to compute "triangle numbers" (e.g. f(4)=1+2+3+4=10) by simply changing the instances of $\omega$ and $m$ in the obvious ways (use $\omega=0,m=+$ rather than $\omega=1,m=*$)). For a radical departure, fix any forest (set of graphical trees) $F$, let $E={}^{\neg}$zero${}^{\neg}$ represent its set of roots, $A$ the other nodes, $\omega$ the constant $0$ function, $d$ the parent function, and $m$ sending $(p,d(p))$ to $f(d(p))+1$. Then for each tree in $F$ and each node $n$ in that tree, the function $f$ will send $n$ to its height on the tree.

Primitive recursion is a powerful technique for deriving new functions from the repetition of others using a kind of "while loop." The general form of primitive recursive functions can be found in [BBJ], and it is not hard to imitate Example 6.6.1 for the general case.

### Application: defining mathematical concepts

In this subsection we hope to convince the reader that many mathematical concepts can be defined byogs. This should not seem like much of a stretch: ologs describe relationships between sets, so we rely on the maxim that all of mathematics can be formulated within set theory. To make the idea explicit, however, we will recall the definition of pseudo-metric space (in 6.7.1) and then provide an olog with the same content (in 35).

**Definition 6.7.1**.: Let $\mathbb{R}_{\geq 0}$ denote the set of non-negative real numbers. A _pseudo-metric space_ is a pair $(X,\delta)$ where $X$ is a set and $\delta\colon X\times X\to\mathbb{R}_{\geq 0}$ is a function with the following properties for all elements $x,y,z\in X$:

1. $\delta(x,x)=0$;
2. $\delta(x,y)=\delta(y,x)$; and
3. $\delta(x,z)\leq\delta(x,y)+\delta(y,z)$.

 (35)

$$\begin{array}{|l|}\hline\frac{d_{0};y=d_{1};y}{s;y=\mathrm{id}_{7}}\ \ 

## 7. Further directions

Ologs are basically categories which have text labels to explain their intended semantic. As such there are many directions to explore ranging from quite theoretical to quite practical. Here we consider three main classes: extending the theory of ologs, studying communication with ologs, and implementing ologs in the real world.

### Extending the theory of ologs

In this paper we began by discussing basic ologs, which are rich enough to capture the semantic of many situations. In Sections 5 and 6 we added more expressivity to ologs to allow one to encode ideas such as intersections, unions, and images. However, ologs could be even more expressive. One could add "function types" (also known as exponentials); add a "subobject classifier type," which could allow for negation and complements as well as power-sets; or even add fixed sets (like the set of Strings) to the language of ologs. This is not too hard (using sketches, see [12]); the reason we did not include them in this paper was more because of space than any other reason.

Another generalization would be to allow the instances of an olog to take values in a category other than $\mathbf{Set}$. For example, one could have an instance-space rather than an instance-set, e.g. it is clear that the instances of the type $\ulcorner$ a point on the unit circle$\ulcorner$ constitute a topological space. One could similarly argue that the instances of the type $\ulcorner$ a human invention$\ulcorner$ have a topology or metric as well (e.g. as an invention, the cellphone is closer to the telephone than it is to artificial flavoring). Instance data on an olog $\mathcal{C}$ corresponds to a functor $\mathcal{C}\to\mathbf{Set}$ in this paper, but it is quite easy to replace $\mathbf{Set}$ with a different category such as $\mathbf{Top}$ (the category of topological spaces), and this may have interesting uses in data modeling.

In Section 6.7, we explicitly showed that pseudo-metric spaces (and we stated further that metric spaces) can be presented by ologs. It would be interesting to see if theorems could also be proven entirely within the context of ologs. If so, a teacher could first sketch a mathematical proof as a small or sparse olog $\mathcal{C}$, and then use a functor $\mathcal{C}\to\mathcal{D}$ to rigorously "zoom in" on that proof so that the sketch becomes a full-fledged proof (as the maps in $\mathcal{C}$ are factored into understandable units in $\mathcal{D}$).

If ologs are to be viable venues in which to discuss results in mathematics, then they should be capable of describing all recursion, not just primitive recursion (as in Section 6.6). We do not yet have an understanding for how this can be done. If recursion can be fully defined with the ologs described above, it would be interesting to see it written out; if not, it would be interesting to understand what basic idea could be gracefully added to ologs so that recursion becomes expressible.

In a different direction, one could test the expressive power of ologs by defining simple games, like Tic Tac Toe or Chess, using ologs. It would be impressive to define a vocabulary for writing games and a program which could automatically convert an olog-defined game into a playable computer game. This would show that the same theory that we have seen express ideas about fatherhood and factorials can also be used to invent games and program computers.

### Studying communication with ologs

As discussed in Section 4, ologs can be connected by functors into networks that are not just 2-way, but $n$-way. These communication networks should be studied: what kinds of information can pass,how reliable is it, how quickly can it spread, etc. This may be applicable in fields from economics to psychology to sociology. Such research may use results from established mathematics such as Network Coding Theory (see [YLC]).

In [SA], we study how two or more entities (described as ologs) can communicate new ideas (not just new instance data) to each other. It would be interesting to see how well this "communication protocol" works in practice, and whether it can be theoretically automated. Furthermore, this communication protocol and any theoretical automation of it should be implemented on a computer to see if different database schemas can be meaningfully integrated with minimal human assistance.

It may be possible to train children to create ologs about their interests or about a given lesson. These ologs would show how the child actually perceives something, which would probably be fascinating. By our experience and that of people we have taught, the process of building an olog usually leads to a clarification of the concepts involved. Moreover, a class project to connect the ologs of different students and between the students and the teacher, may have excellent pedagogical benefits.

Finally, it may be interesting to study "local truth" vs. "global truth" in a network of ologs. Functorial connections between ologs can allow for translation of ideas between members of a group, but there may be ideas which do not extend globally, just as a Mobius band does not admit a global orientation. That is, given three parties on the Mobius band, any pair can agree on a compass orientation, but there is no choice that the three can simultaneously agree on. Similarly, whether or not it is possible to construct a global language which extends all the existing local ones could be determined if these local languages and their connections were entered into a computer olog system.

### Implementing ologs in the real world

Once ologs are implemented on computers, and once people learn how to author good ologs, much is possible. One advantage comes in searching the information space. Currently when we search for a concept (say in Google or on our hard drive), we can only describe the concept in words and hope that those words are found in a document describing the concept. That is, search is always text-based. Better would be if the concept is meaningfully interconnected in a web of concepts (an olog) that could be navigated in a meaningful (as opposed to text-based) way.

Indeed, this is the semantic web vision: When internet data is machine-readable, search becomes much more powerful. Currently, we rely on RDF scrapers that scour web pages for $\langle$subject, predicate, object$\rangle$ sentences and store them in RDF format, as though each such sentence is a fact. Since people are inputting their data as prose text, this may be the best available method for now; however, it is quite inaccurate (e.g. often 15% of the facts are wrong, a number which can lead to degeneration of deductive reasoning - see [MBCH]). If ideas could be put on the internet such that they compatibly made sense to both human and computer, it would give a huge boost to the semantic web. We believe that ologs can serve as such a human-computer interface.

While it is often assumed that because we all speak the same language we all must mean the same things by it, this is simply not true. The age-old question about whether "blue for me" is the same as "blue for you" is applicable to every single word and idiom in our language. There is no easy way to sync up different people's perceptions. If communication is to be efficient, agreements must be fairly explicit and precise, and this precision demands a rigor that is simply unavailable in English prose. It is available in a network of ologs (as described in Section 4).

For example, the laws of the United States are hopelessly complex. Residents of the US are required to obey the laws. However, unlike the rules of the Scholastic Aptitude Test (SAT), which take 10 minutes for the proctor to read aloud, the laws of the US are never really expressed -- the most important among them are hopefully picked up by cultural osmosis. If an olog was created which had enough detail that laws could be written in that format, then a woman could research for herself whether her landlord was required to fix her refrigerator or whether this was her responsibility. It may prove that the olog of laws is internally inconsistent, i.e. that it is impossible for a person to satisfy all the laws -- such an analysis, if performed, could fundamentally change our outlook on the legal system.

The same goes for science; information written up in articles is much less accessible than information that is entered into an ontology. However, the dream of a single universal ontology is untenable ([Min]). Instead we must allow each lab or institute to create its own ontology, and then require citations to be functorial olog connections, rather than mere silo-to-silo pointers. Thus, a network of ologs should be created to represent the understanding of the modern scientific community as a multi-faceted whole.

Another impetus for a scientist to write an olog about the study at hand is that, once an olog is made, it can be instantly converted to a database schema which the scientist can use to input all the data pertaining to this study. Indeed, if some data did not fit within this schema, then the olog must have been insufficient to begin with and should be modified to fully describe the experiment. If scientists work this way, then the separation between them and database modelers can be reduced or eliminated (the scientist assumes the database modeling role with little additional burden). Moreover, if functorial connections are established between the ologs of different labs, then data can be meaningfully shared along those connections, and ideas written in the language of one lab's olog can be translated automatically into the language of the other's. The speed and accuracy of scientific research should improve.

## References

* [Awo] S. Awodey. _Category Theory_. Second edition. Oxford Logic Guides, 52. Oxford University Press, Oxford (2010).
* [BBJ] G.S. Boolos, J.P. Burgess, R.C. Jeffrey. _Computability and Logic_. Fifth edition. Cambridge University Press, Cambridge (2007).
* [BW1] M. Barr, C. Wells. _Category Theory for Computing Science_. Prentice Hall International Series in Computer Science. Prentice Hall International, New York (1990).
* [BW2] M. Barr, C. Wells. _Toposes, Triples and Theories_. Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], 278. Springer-Verlag, New York (1985).
* [BS] J. Barwise and J. Seligman. _Information Flow: The Logic of Distributed Systems_. Cambridge University Press, Cambridge (1997).
* [Bor] A. Borgida. "Knowledge representation meets databases -- a view of the symbiosis --". 20th International Workshop on Description Logics (2007).
* [CM] M. Chein, M-L Mugnier. _Graph-based Knowledge Representation and Reasoning: Computational Foundations of Conceptual Graphs_. Advanced Information and Knowledge Processing Series, Springer London, 427 pages (2008).
* [Coq]_The Coq proof assistant_. (2011). Available online: http://coq.inria.fr/.

 * [GW] B. Ganter, R. Wille. _Formal Concept Analysis: Mathematical Foundations_. Springer, New York (1999).
* [Gog1] J. Goguen. "A categorical manifesto". Math. Struc. Comp. Sci. 1: 49-67 (1991).
* [Gog2] J. Goguen. "Information integration in institutions". Draft paper for the Jon Barwise memorial volume edited by Larry Moss (2006).
* [GB] J. Goguen, R. Burstall. "Institutions: Abstract model theory for specification and programming". J. Assoc. Comp. Mach. vol. 39, pp. 95-146 (1992).
* [HC] M.J. Healy and T.P. Cavdell. "Neural networks, knowledge and cognition: A mathematical semantic model based upon category theory," UNM Technical Report EECE-TR-04-020, DSpaceUNM, University of New Mexico (2004).
* [IFF1]_The Information Flow Framework (IFF)_. Available online: http://suo.ieee.org/IFF/.
* [IFF2] "The IFF approach to the lattice of theories". Available online: http://suo.ieee.org/IFF/work-in-progress/LOT/lattice-of-theories.pdf.
* [JRW] M. Johnson, R. Rosebrugh, and R. Wood. "Entity Relationship Attribute Designs and Sketches". Theory and Application of Categories 10, 3, 94-112 (2002).
* [Ken1] R.E. Kent. "The IFF foundation for ontological knowledge organization". Cataloging & Classification Quarterly, special issue: _Knowledge Organization and Classification in International Information Retrieval_ (2003).
* [Ken2] R.E. Kent. "Semantic integration in the Information Flow Framework". In: Kalfoglou, Y., Schorlemmer, M., Sheth, A., Staab, S., Uschold, M. (eds.) _Semantic Interoperability and Integration_. Dagstuhl Seminar Proceedings, vol. 04391, Dagstuhl Research Online Publication Server (2005).
* [Ken3] R.E. Kent. "System consequence". In: Rudolph, S., Dau, F., Kuznetsov, S. (eds.) The Proceedings of the 17th International Conference on Conceptual Structures: _Conceptual Structures: Leveraging Semantic Technologies_. LNCS 5662. Springer-Verlag Berlin, Heidelberg (2009). Slides for ICCS2009 presentation located online: http://www.hse.ru/data/708/792/1224/system-consequence_Robert_E_Kent.pdf.
* [Ken4] R.E. Kent. "The architecture of truth". Unpublished manuscript (2010) to appear online at: http://arxiv.org/.
* [Ken5] R.E. Kent. "Database semantics". Unpublished manuscript (2011) to appear online at: http://arxiv.org/.
* [LS] F.W. Lawvere, S.H. Schanuel. _Conceptual Mathematics. A First Introduction to Categories_. Second edition. Cambridge University Press, Cambridge (2009).
* [Mac] S. Mac Lane. _Categories for the Working Mathematician_. Second edition. Graduate Texts in Mathematics, 5. Springer-Verlag, New York (1998).
* [Mak] M. Makkai. "Generalized sketches as a framework for completeness theorems. I,II,III". J. Pure Appl. Algebra 115 (1997), no. 1.
* [Min] G.W. Mineau. "Sharing knowledge: Starting with the integration of vocabularies". _Lecture Notes in Computer Science_, Vol 754 (1993), pp. 34-45. Springer.
* [MBCH] T.M. Mitchell, J. Betteridge, A. Carlson, E. Hruschka. "Populating the semantic web by macro-reading internet text". _Lecture Notes in Computer Science_, Vol. 5823 (2009), pp. 998-1002. Springer.
* [nL1] nLab contributors. "Monomorphism". nLab. Available online: http://ncatlab.org/nlab/show/monomorphism.
* [nL2] nLab contributors. "Epimorphism". nLab. Available online: http://ncatlab.org/nlab/show/epimorphism.
* [Pie] B.C. Pierce. _Basic Category Theory for Computer Scientists_. MIT Press (1991).
* [Sic] G. Sica. "What is category theory?". Polimetrica S.a.s. Milan, Italy (2006).
* [Sow1] J. Sowa. "Semantic Networks". Available online: http://www.jfsowa.com/pubs/semnet.htm.
* [Sow2] J. Sowa. _Knowledge Representation: Logical, Philosophical, and Computational Foundations_. Brooks/Cole (2000).
* [Spi1] D.I. Spivak. "Higher dimensional models of networks" (2009). Available online: http://arxiv.org/pdf/0909.4314.
* [Spi2] D.I. Spivak. "Functorial data migration" (2010). Available online: http://arxiv.org/abs/1009.1166.
* [Spi3] D.I. Spiv * [SA] D.I. Spivak, M. Anel. "Communication protocol". In preparation.
* [TBG] A. Tarlecki, R. Burstall, J. Goguen. "Some fundamental algebraic tools for the semantics of computation, part 3: Indexed categories". Th. Comp. Sci. vol. 91, pp. 239-264. Elsevier (1991).
* [W] Wikipedia contributors. "Amino acid" Wikipedia, The Free Encyclopedia. 30 Sep. 2010. Web. 30 Sep. 2010. Available online: http://en.wikipedia.org/wiki/Amino_acid.
* [YLC] R. Yeung, S-Y Li, N. Cai. "Network coding theory" _Foundations and trends in communications and information theory._ now Publishers Inc., Boston (2006).

 