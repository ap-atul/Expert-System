## Expert System 
* Generic expert system to generate rules and create relation between entries and knowledge base.
* Implemented using Forward Chaining and Backward chaining.
* Require to input well-formatted json files that correspond to the example in ```data``` folder
* The clauses should relate to the Knowledge base or it won't make any sense when run.
* Parsers are built to parse the json file and create objects on runtime.

### Description
* The Rule is a string that can be compared.
* Knowledge is formed up of multiple rules
* Knowledge Base is formed up of multiple knowledge
* Clause is a set of questions
* Clause has 3 attributes clause, negative, positive
* For each clause, the knowledge base is searched, percent higher than Min Match is outputted
* The constants can be changed from ```utils/constants.py```
* Check out the examples ```data/```

### Thought process
* Json format file that can clearly define a structure to parse.
* Reading the json file and building the Knowledge Base and the Clause Base.
* The user input for each clause is converted to Knowledge Base.
* Both Knowledge bases are compared and max percent matched is outputted.
* There may be multiple matches, we could display details with percentage.
* Finally answer is either True or False.

   
* Knowledge base syntax
```json
{
  "target": [
    {
      "name": "Kidney disease",
      "rules": {
        "1": "head aches",
        "2": "vomiting",
        "3": "body ache",
        "4": "no sleep"
      }
    },
    {
      "name": "Some target",
      "rules": {
        "1": "rule1",
        "2": "rule2"
      }
    }
  ]
}
```


* Clause base syntax
```json
{
  "1": {
    "question": "State your symptoms?",
    "answer": {
      "positive": "Yes, you are positive for ",
      "negative": "We don't see any signs of "
    }
  },
  "2": {
    "question": "question/statement",
    "answer": {
      "positive": "positive statement with potential to add target at end",
      "negative": "negative statement, target will be added at end"
    }
  }
}
```

----------------------------------
### Example
```
Chankya >>> State your symptoms?
You >>> no sleep, head aches
[DEBUG]  Target :: Kidney disease --->  Matched :: 50.0
[DEBUG]  Target :: Lung disease --->  Matched :: 50.0
[DEBUG]  Target :: Heart disease --->  Matched :: 0.0

[INFO]  Yes, you are positive for Kidney disease 50.0 % sure
[INFO]  Hope that you are satisfied with your answers !
```