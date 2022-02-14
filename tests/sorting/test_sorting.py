from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"date_posted": "2020-05-05", "max_salary": 8000, "min_salary": 10},
        {"date_posted": "2020-01-01", "max_salary": 10, "min_salary": 100},
        {"date_posted": "2020-03-03", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2020-12-01", "max_salary": 15000, "min_salary": 1},
        {"date_posted": "2020-11-12", "max_salary": 1500, "min_salary": 2},
        {"date_posted": "2020-10-12", "max_salary": 4000, "min_salary": 11},
    ]

    jobs_min = [
        {"date_posted": "2020-12-01", "max_salary": 15000, "min_salary": 1},
        {"date_posted": "2020-11-12", "max_salary": 1500, "min_salary": 2},
        {"date_posted": "2020-05-05", "max_salary": 8000, "min_salary": 10},
        {"date_posted": "2020-10-12", "max_salary": 4000, "min_salary": 11},
        {"date_posted": "2020-01-01", "max_salary": 10, "min_salary": 100},
        {"date_posted": "2020-03-03", "max_salary": 10000, "min_salary": 200},
    ]

    jobs_max = [
        {"date_posted": "2020-12-01", "max_salary": 15000, "min_salary": 1},
        {"date_posted": "2020-03-03", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2020-05-05", "max_salary": 8000, "min_salary": 10},
        {"date_posted": "2020-10-12", "max_salary": 4000, "min_salary": 11},
        {"date_posted": "2020-11-12", "max_salary": 1500, "min_salary": 2},
        {"date_posted": "2020-01-01", "max_salary": 10, "min_salary": 100},
    ]

    jobs_date_posted = [
        {"date_posted": "2020-12-01", "max_salary": 15000, "min_salary": 1},
        {"date_posted": "2020-11-12", "max_salary": 1500, "min_salary": 2},
        {"date_posted": "2020-10-12", "max_salary": 4000, "min_salary": 11},
        {"date_posted": "2020-05-05", "max_salary": 8000, "min_salary": 10},
        {"date_posted": "2020-03-03", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2020-01-01", "max_salary": 10, "min_salary": 100},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == jobs_min
    sort_by(jobs, "max_salary")
    assert jobs == jobs_max
    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_posted
