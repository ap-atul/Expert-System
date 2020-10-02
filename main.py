from engine.inference import Inference

knowledgeBaseFile = "./data/knowledge.json"
clauseBaseFile = "./data/clause.json"

inferenceEngine = Inference()
inferenceEngine.startEngine(knowledgeBaseFile,
                            clauseBaseFile,
                            verbose=True,
                            method="backward")
