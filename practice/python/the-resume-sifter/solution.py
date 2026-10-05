def filter_new_resumes(urls: list[str], existing_ids: set[str]) -> list[list[str]]:
  result = []
  for url in urls:
    # get firstname_lastname_id
    slug = url.rsplit("/", 1)[-1]
    # separate firstname_lastname and id
    name, id = slug.rsplit('_', 1)
    if id not in existing_ids:
      result.append([name, id])
  return result
