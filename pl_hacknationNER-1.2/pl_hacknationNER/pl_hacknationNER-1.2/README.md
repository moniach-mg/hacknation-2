second round of training

| Feature | Description |
| --- | --- |
| **Name** | `pl_hacknationNER` |
| **Version** | `1.2` |
| **spaCy** | `>=3.8.3,<3.9.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `apache-2.0` |
| **Author** | [Ariel]() |

### Label Scheme

<details>

<summary>View label scheme (23 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `ADDRESS`, `AGE`, `BANK-ACCOUNT`, `CITY`, `COMPANY`, `DATE`, `DOCUMENT-NUMBER`, `EMAIL`, `ETHNICITY`, `HEALTH`, `JOB-TITLE`, `NAME`, `PESEL`, `PHONE`, `POLITICAL-VIEW`, `RELATIVE`, `RELIGION`, `SCHOOL-NAME`, `SECRET`, `SEX`, `SEXUAL-ORIENTATION`, `SURNAME`, `USERNAME` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 69.83 |
| `ENTS_P` | 76.78 |
| `ENTS_R` | 64.03 |
| `TOK2VEC_LOSS` | 58885.11 |
| `NER_LOSS` | 17819.95 |