# Customizable SpaCy NER anonymizer for Polish

This is a customizable anonymizer based on fine-tuned SpaCy NER model, created for a Hacknation 2025 challange from NASK ("Dane bez twarzy").

## How to use it?

To run the script using a remote model (for example downloaded from HuggingFace), use:

python3 anonymizer.py /path/to/your/source/file.txt remote modelname /path/to/your/output/file.txt

The recommended model, trained specifically for this challange, can be downloaded with:

pip install https://huggingface.co/ArielUW/pl_hacknationner/resolve/main/pl_hacknationner-any-py3-none-any.whl

To run the script using your own local model, use:

python3 anonymizer.py /path/to/your/source/file.txt local /your/path/to/your/model/directory /path/to/your/output/file.txt

In both cases path to output file is optional. When output parameter is not provided, the script simply prints out the anonymized text in the terminal. Additionally, main() function always reutrns a string containing the anonymized text.

## Anonymization classes

This script and the accompanying model have been created to anonymize various personal and sensitive data. Spans of text containing this information is covered with placeholders listed below (curly brackets appear in text as literal characters). Some placeholders are self-explanatory.
* {date-of-birth}
* {city}
* {surname}
* {relative}
* {username}
* {street}
* {adress}
* {bank-account}
* {secret}: string of characters that is likely to be a password, passcode etc.
* {sexual-orientation}
* {name}
* {ethnicity}
* {phone}
* {age}
* {sex}
* {credit-card-number}
* {country}
* {email}
* {religion}
* {school-name}
* {job-title}
* {address}
* {pesel}
* {date}
* {company}
* {health}: names of diesieses and states related to body, such as hypertension or pregnancy
* {document-number}
* {political-view}: words related to political views and believes, such as liberal, conservative.

Attention: those classes are recognised based on a probabilistic approach. Some data may not be properly anonymized, and some anonymizations may be false positives. Subjective and complex notions such as {health} or {political-view} are the most likely to be miscategorized. Additionally, some information may still be deductible from context even if part of the information is covered. It is also possible that some similar classes, such as {date-of-birth} and a more general {date} are likely to get mixed up.

## Models

To use models stored on HuggingFace (including the default model), be sure to create an account on HuggingFace. Use your personal token the first time you log in. Be midful that the default option is to save your personal token as git credential (you can opt out). More info: https://huggingface.co/docs/huggingface_hub/guides/cli#hf-auth-login

To use your local model, upload it in local ./models folder. You can also train your own model using and [text](training.py). To provide training data, use https://arunmozhi.in/ner-annotator/ annotation tool, export annotations as json file and use [data_preprocessing.py](data_preprocessing.py) script to prepare it for further transformations. When training, you can use [confing file](content/config.cfg) sored in ./content.

## Customization and training
To customize classes and provide your own training data, substitute the content/annotations.json file with your own data in the same format. The pipeline uses classes from this file do determine the expected results of the anonymization process – if your annotations are stored somewhere else, make sure to modify the anonymizer.py script to reflect that. Annotation file is used by the substitute_tokens() function.