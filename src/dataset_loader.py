import ir_datasets
from ranx import Qrels

class DatasetLoader:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.dataset = ir_datasets.load(dataset_name)
        self.docs = {d.doc_id: d.text for d in self.dataset.docs_iter()}
        self.queries = {q.query_id: q.text for q in self.dataset.queries_iter()}
        self.qrels = Qrels.from_ir_datasets(dataset_name) # use ranx to load qrels in dict format

    def get_docs(self):
        return list(self.docs)

    def get_queries(self):
        return list(self.queries)

    def get_qrels(self):
        return self.qrels

    def get_all(self):
        return self.docs, self.queries, self.qrels

    def print_info(self):
        # inspect data to check that it loaded correctly
        print(f'DATASET: {self.dataset_name}')
        print(f'DOCS ({len(self.docs)}): {list(self.docs.items())[0]} \n')
        print(f'QUERIES ({len(self.queries)}): {list(self.queries.items())[0]} \n')
        print(f'QRELS ({len(self.qrels)}): {list(self.qrels.to_dict().items())[0]} \n')
