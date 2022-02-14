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

    salary_list = ["min_salary", "max_salary", "date_posted"]
    jobs_dict = {
        "min_salary": jobs_min,
        "max_salary": jobs_max,
        "date_posted": jobs_date_posted
    }

    for salary_option in salary_list:
        sort_by(jobs, salary_option)
        assert jobs == jobs_dict[salary_option]
