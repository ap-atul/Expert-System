## Expert System 
Generic expert system to generate rules and create relation between entries and knowledge base.

### Rule
Currently adding following operations

* AND : +
* OR : |
* NOT : !

### Thought process
- Json format file that can clearly define a structure to parse.
- Getting Atom nodes from rule created from the Json file.
- Using this Atom nodes to ask queries.
- Logical Implication

    | p | q | p => q|
    | --- | --- | --- |
    | T | T | T |
    | T | F | F |
    | F | T | T |
    | F | F | T |
 
- Each rule Atom is query to the user, the answer is base on input.
- Since answer can be conditional, binary, negate, and unknowns.
- Finally the Atom gets evaluated to either True or False.
- Rest is just evaluation of rule ( T + F | F | T).
- Finally answer is either True or False.