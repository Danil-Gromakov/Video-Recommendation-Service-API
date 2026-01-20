from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.models import RecommendationRequest, RecommendationResponse
from app.recommender import get_recommendations

app = FastAPI(
    title="Recommendation Service API",
    description="Сервис для получения рекомендаций видео",
    version="1.0.0"
)


@app.get("/health")
async def health_check():
    """
    Health check endpoint для мониторинга состояния сервиса
    """
    return {"status": "ok"}


@app.post("/recommend", response_model=RecommendationResponse)
async def recommend(request: RecommendationRequest):
    """
    Эндпоинт для получения рекомендаций видео
    """
    
    try:
        # Получаем рекомендации с использованием алгоритма
        recommendations = get_recommendations(
            watched_videos=request.watched_videos,
            liked_categories=request.liked_categories
        )
        
        # Формируем ответ
        response = RecommendationResponse(
            user_id=request.user_id,
            recommendations=recommendations,
            algorithm_version="1.0"
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка при формировании рекомендаций: {str(e)}"
        )


# Middleware для обработки ошибок
@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)}
    )

