from typing import List

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from .utils import load_videos_embedding
    
videos = load_videos_embedding()

def algo_recommendations(user_data: dict, top_n: int = 3) -> List[str]:
    """Рекомендации видео на основе данных пользователя cos sim"""
    

    watched_videos = set(user_data.get("watched_videos", []))
    liked_categories = set(user_data.get("liked_categories", []))

    available_videos = []
    watched_embeddings = []
    category_embeddings = {category: [] for category in liked_categories}

    for video in videos:
        if video.category in liked_categories:
            category_embeddings[video.category].append(video.embedding)

        if video.video_id in watched_videos:
            watched_embeddings.append(video.embedding)
        else:
            available_videos.append(video)

    user_embedding = np.zeros(3)

    if watched_embeddings:
        user_embedding += np.vstack(watched_embeddings).mean(axis=0)

    for embeddings in category_embeddings.values():
        if embeddings:
            user_embedding += np.vstack(embeddings).mean(axis=0)

    user_embedding = user_embedding.reshape(1, -1)

    if not available_videos:
        return []

    available_embeddings = np.vstack([v.embedding for v in available_videos])
    similarities = cosine_similarity(user_embedding, available_embeddings)[0]

    for video, similarity in zip(available_videos, similarities):
        video.similarity = similarity

    available_videos.sort(key=lambda x: x.similarity, reverse=True)

    if available_videos:    
        return [video.video_id for video in available_videos[:top_n]]
    else:
        return []

def get_recommendations(
    watched_videos: List[str], liked_categories: List[str]
) -> List[str]:
    """
    Функция для получения рекомендаций на основе предпочтений пользователя

    Args:
        watched_videos: Список просмотренных видео
        liked_categories: Список понравившихся категорий

    Returns:
        Список рекомендованных видео
    """

    return algo_recommendations(
        {"watched_videos": watched_videos, "liked_categories": liked_categories}
    )
