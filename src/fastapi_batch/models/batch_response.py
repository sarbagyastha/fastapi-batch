from pydantic import BaseModel

from fastapi_batch.models.batch_model import Keyed, ResponseBatchModel


class BatchResponse(BaseModel):
    responses: Keyed[ResponseBatchModel]
