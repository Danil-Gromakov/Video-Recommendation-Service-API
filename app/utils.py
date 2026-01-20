import os
import csv
import json
import numpy as np
from dataclasses import dataclass
from typing import List

    

@dataclass
class Video:
    video_id: str
    title: str
    category: str
    embedding: np.ndarray
    similarity: float = 0.0



def parse_embedding(embedding_str: str) -> np.ndarray:
    try:
        embedding_str = json.loads(embedding_str)
        embedding_list = json.loads(embedding_str)
    except json.JSONDecodeError:
        embedding_list = json.loads(embedding_str)
    return np.array(embedding_list)


# TODO: Заменить на запрос в БД, это тестовая демонстрация, 
def load_videos_embedding() -> List[Video]:
    """Чтение данные видео"""
    videos = []
    filepath = "../videos_data.csv" if os.getenv("DEV") else "videos_data.csv"
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            embedding = parse_embedding(row["embedding"])
            video = Video(
                video_id=row["video_id"],
                title=row["title"],
                category=row["category"],
                embedding=embedding,
            )
            videos.append(video)
    return videos
