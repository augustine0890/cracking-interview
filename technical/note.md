# Technical Interview
**Things you should know**
- Variables
- Classes, Objects, and OOP
- Conditionals, Loops
- Arrays and ArrayLists
- Strings

**Syllabus**
- Fundamental data structures
    - Node
    - Linked Lists
    - Doubly Linked Lists
    - Queues
    - Stacks
- Algorithmic complexity and asymptotic notation
- Complex data structures
    - Trees
    - Heaps
    - Graphs
- Sorting algorithms: Bubble Sort, Merge Sort, and Quicksort
- Dijkstra's Algorithm
- Common interview questions

## Data Structures
- Data structures are the way we are able to store and retrieve data.
- The essential building blocks that we used to organize all of our digital information.
- Choosing the right data structure allows us to use the algorithms we want and keeps our code running smoothly.

## Java Topics
- Type casting is the process of converting a value of one primitive data types to another primitive data type.
```text
Byte --> Short --> Int --> Long --> Float --> Double
```
- `Dictionary` is the abstract parent class of `Hashtable`, a data structure that stores key-value pairs.
- `Hashtable` does not allow any `null` key or value likes `HashMap` does.
- An _interface_ is a collection of abstract methods which lay out the required behavior of any class that implements it.
- `Hashtable` is the only subclass of `Dictionary` and `Hashtable` implements `Map`.
- The `Dictionary` class has now become somewhat obsolete in the wake of the more versatile and applicable `Map` interface.
### Nodes
- The data contained within a node can be variety of types. It could be an integer, string, decimal, an array or nothing (`null`).
- The link or links within the node are sometimes referred to as _pointers_. If the links are `null`, it denotes that you have reached the end of the particular node.
- The nodes can be orphaned if there are no existing links to them.
- The `data` helps to store information, and `next` is a link to other Nodes for easier traversal.

## Linear Data Structure
### Linked List
- The list is comprises a series of nodes
- The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
- Can be unidirectional or bidirectional
- Are a basic data structure, and form the basis for many other data structures
- Have a single head node, which serves as the first node in the list
- Require some maintenance in order to add or remove nodes
- The methods we used are an example and depend on the exact use case and/or programming language being used