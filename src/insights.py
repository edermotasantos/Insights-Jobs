from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_job_types_list = []
    for job_types_row in jobs_list:
        if not job_types_row["job_type"] in unique_job_types_list:
            unique_job_types_list.append(job_types_row["job_type"])
    return unique_job_types_list


def filter_by_job_type(jobs, job_type):
    jobs_dict_list = jobs
    job_type_str = job_type
    filtered_by_job_type = []
    for job_type_row in jobs_dict_list:
        if job_type_row["job_type"] == job_type_str:
            filtered_by_job_type.append(job_type_row)
    return filtered_by_job_type


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries_list = []
    for industries_types_row in jobs_list:
        if not industries_types_row[
          "industry"] in unique_industries_list and industries_types_row[
              "industry"] != "":
            unique_industries_list.append(industries_types_row["industry"])
    return unique_industries_list


def filter_by_industry(jobs, industry):
    jobs_dict_list = jobs
    industry_str = industry
    filtered_by_industry_list = []
    for industry_row in jobs_dict_list:
        if industry_row["industry"] == industry_str:
            filtered_by_industry_list.append(industry_row)
    return filtered_by_industry_list


def get_max_salary(path):
    jobs_list = read(path)
    salary_list = []
    max_salary = 0
    for max_salary_row in jobs_list:
        if not max_salary_row[
          "max_salary"] in salary_list and max_salary_row[
              "max_salary"].isdigit():
            value_num = int(max_salary_row["max_salary"])
            salary_list.append(value_num)
    max_salary = max(salary_list)
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    salary_list = []
    min_salary = 0
    for min_salary_row in jobs_list:
        if not min_salary_row[
          "min_salary"] in salary_list and min_salary_row[
              "min_salary"].isdigit():
            value_num = int(min_salary_row["min_salary"])
            salary_list.append(value_num)
    min_salary = min(salary_list)
    return min_salary


def matches_salary_range(job, salary):
    job_dict = job
    salary_int = salary
    if("max_salary" not in job_dict or "min_salary" not in job_dict):
        raise ValueError(
            "Job dictionary must contain the keys min_salary and max_salary")
    if (type(job_dict["min_salary"]) is not int or
            type(job_dict["max_salary"]) is not int):
        raise ValueError(
            "Job dictionary must contain the keys"
            "min_salary and max_salary with valid values")
    if (job_dict["min_salary"] > job_dict["max_salary"]):
        raise ValueError(
            "The value of the min_salary key"
            "cannot be greater than that of the max_salary key")
    if (type(salary_int) is not int):
        raise ValueError("The salary_int parameter must be a valid value")
    min_salary = job_dict["min_salary"]
    max_salary = job_dict["max_salary"]
    salary_range = min_salary <= salary_int <= max_salary
    return salary_range


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
