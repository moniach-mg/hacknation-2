import spacy
import json
from loguru import logger
import sys

def map_tokens():
    substitutes={}
    with open("./content/annotations.json", "r") as file:
        data = json.load(file)
    classes = data['classes']
    for c in classes:
        substitutes[c]=f"{{{c.lower()}}}"
    print(substitutes)
    return substitutes

def anonymize(source, nlp):
    with open(source, "r") as f:
        content = f.read()
    doc = nlp(content)
    substitutes = map_tokens()
    for ent in doc.ents:
        #this should've been done much better, but im too sleepy!
        print(ent.text,substitutes[ent.label_])
        content = content.replace(ent.text,substitutes[ent.label_])
    print(content)
    return content

def main(source,type,model,output=None):
    if source.endswith(".txt"):        
        if type=="local":
            nlp = spacy.load(model)
            text = anonymize(source, nlp)
        elif type=="remote":
            try:
                nlp = spacy.load(model)
            except Exception as e:
                print(e)
                logger.warning("There is  problem loading your model to SpaCy. Perhaps you forgot to download it? Use pip install https://huggingface.co/ArielUW/pl_hacknationner/resolve/main/pl_hacknationner-any-py3-none-any.whl or see more on: https://huggingface.co/docs/hub/spacy")
            text = anonymize(source, nlp)
        else:
            logger.warning(f"Unexpected model type.Please make sure to type either 'local' or 'remote' as the second argument.")
        if output:
            try:
                with open(output, 'w') as file:
                    file.write(text)
            except:
                logger.warning(f"There's something wrong with your output path. Sorry, I'm too sleepy to handle it better 😭")

    else:
        logger.warning(f"Unexpected file extension: {source}. Please provide an input as a .txt file.")

if __name__ == "__main__":
    print(len(sys.argv))
    output = None if len(sys.argv) < 5 else sys.argv[4]
    main(sys.argv[1],sys.argv[2],sys.argv[3],output)
    #python3 anonymizer.py content/test.txt remote pl_hacknationNER