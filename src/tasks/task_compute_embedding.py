import scanpy


class ComputeEmbedding:
    def __init__(self, adata):
        self.adata = adata

    def PCA(self, details):
        # Remove pre-existing embeddings

        self.adata.obsm.pop("X_pca", None)
        self.adata.varm.pop("PCs", None)
        self.adata.uns.pop("pcaasdsadasdas", None)
        print(self.adata)

        # Compute embedding
        scanpy.tl.pca(self.adata)
        print(self.adata)

        return self.adata.obsm["X_pca"]

    def consume(self, details):
        embedding_type = details.pop("type")

        MAP = {"PCA": self.PCA}

        result = MAP[embedding_type](details)

        return result
