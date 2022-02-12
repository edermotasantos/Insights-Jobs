from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for jobs_row in jobs_reader:
            jobs_list.append(jobs_row)
    return jobs_list
