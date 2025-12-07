from huggingface_hub import login
login()

from huggingface_hub import HfApi
api = HfApi()
api.upload_folder(
    folder_path='./content/output/model-best',
    repo_id="ArielUW/hacknationNER",
    commit_message=f"updated to a slightly better version")


"""python -m spacy package ./content/output/model-best ./models/hacknationNER-v-1-2 --create-meta --build wheel --name hacknationNER --version 1.2"""