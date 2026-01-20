from pydantic import BaseModel, Field
from typing import List


class RecommendationRequest(BaseModel):
    user_id: int = Field(..., description="Уникальный идентификатор пользователя")
    watched_videos: List[str] = Field(default=[], description="Список просмотренных видео")
    liked_categories: List[str] = Field(default=[], description="Список понравившихся категорий")
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 123,
                "watched_videos": ["v1", "v2"],
                "liked_categories": ["adventure", "education"]
            }
        }


class RecommendationResponse(BaseModel):
    user_id: int = Field(..., description="Уникальный идентификатор пользователя")
    recommendations: List[str] = Field(..., description="Список рекомендованных видео")
    algorithm_version: str = Field(..., description="Версия алгоритма рекомендаций")
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 123,
                "recommendations": ["v3", "v4", "v5"],
                "algorithm_version": "1.0"
            }
        }