import json

def transform_data(data):
    transformed_data = []
    for record in data['annotations']:
        if record and isinstance(record, list) and len(record) == 2:
            text, entity_data = record
            if 'entities' in entity_data:
                entities = entity_data["entities"]
                transformed_entities = []

                for entity in entities:
                    start, end, label = entity
                    transformed_entities.append([start, end, label])

                transformed_data.append([text, {"entities": transformed_entities}])
            else:
                print(f'Pominięto rekord bez "entities": {record}')
        else:
            print(f'Pominięto nieprawidłowy rekord: {record}')
    return transformed_data

def main(data_to_transform):
    with open(data_to_transform, 'r', encoding='utf-8') as file:
        data_to_transform = json.load(file)

    transformed_annotations = transform_data(data_to_transform)
    print(transformed_annotations)

    output_file_path = './content/data_transformed.json'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(transformed_annotations, file, ensure_ascii=False, indent=4)

    print(f'Transformacja zakończona. Wynik zapisano w pliku: {output_file_path}')

if __name__=="__main__":
    main("content/annotations.json")