from typing import Dict
from selenium import webdriver
from utils import login_linkedin, get_job_info_from_browser

import json

def get_job_from_linkedin(username : str, 
                          password : str, 
                          keyword : str, 
                          location : str = "United States", 
                          experience : str = None
                          ) -> str:
    """
    Pull Job posting from linkedin by searching based on keyword and location.

    Args:
        username:
            Linkedin username.
        password:
            Linkedin password.
        keyword:
            keyword that feed into Linkedin search engine. This can include experience level, field of 
            expertise, company name. 
        location:
            Location of job. This takes inputs ranging from zipcode, city, country. 
        experience:
            six levels of job exerpeince: Internship,Entry level,Associate,Mid-Senior level,Director,Executive.
            TODO: infer the job level given by year of working experience. 

    Returns:
        A json serialized response that contains up to 7 job ID corresponding to the detail information of
        the job posting. 
        {job title: ... , salary: ... , company size: ..., job description: ...}
    """

    # Install Chrome Driver as the browser.
    browser = webdriver.Chrome()
    # Use the browser to log in to linkedin.
    login_linkedin(browser, username, password)
    # Retrive information from Linkedin.
    jobInfo = get_job_info_from_browser(browser, keyword, location, experience)
    # Serialize job information and return it.
    return json.dumps(jobInfo)

