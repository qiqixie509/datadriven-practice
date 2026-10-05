def actor_genre_box_office(movies: list[dict], actors: list[dict], mapping: list[dict], genre: str, min_rating: float) -> dict:
  filtered_movies = {
      m["movie_id"] for m in movies
      if m["genre"] == genre and m["rating"] >= min_rating
    }
  box_office_by_movie = {
    m["movie_id"]: m["box_office"] for m in movies
    if m["movie_id"] in filtered_movies
    }
  actor_id_by_name = {a["actor_id"]: a["name"] for a in actors}
  # print(box_office_by_movie)
  # print(mapping)
  result: dict = {}
  for m in mapping:
    movie_id = m["movie_id"]
    actor_id = m["actor_id"]
    if movie_id in box_office_by_movie :
      actor_name = actor_id_by_name.get(actor_id)
      if actor_name is None:
        continue
      result[actor_name] = result.get(actor_name, 0) + box_office_by_movie[movie_id] 
  
  return result
