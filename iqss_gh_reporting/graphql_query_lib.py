from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import os
import json


def query_get_one_pr_malformed():
    # =================================================================
    # get the associated issue information: number, labels, title for a single pull request
    # =================================================================
    # return values. These are hardcoded by you when you create the query.
    #
    # "query_str": query_string
    # "has_next_page_path": This is the check for the next page of data formatted specifically for this query
    # "start_with_path": This is the path for the next page of data formatted specifically for this query
    #  "query_vars": These are the variables that are required internally for the query to run
    #       "loginOrg": "IQSS"
    #       "repo": "dataverse"
    #       "number": 1234 - Pull request number. Required.
    #       "firstFew": 100 - count of prs per page.  Required. Leave as 100.
    #       "startWith" - An interim variable that is used to store the cursor. Required. set to ""
    #
    # Expected results of this query:
    #
    # ---------------------------------------------------------------
    query_string = \
    """
    query ($loginOrg: String!, $repo: String!, $firstFew: Int!, $startWith: String, $number: Int!) {
        repository(followRenames:false, owner: $loginOrg, name: $repo) {
                pullRequest (number: $number) {
                    closingIssuesReferences(first: $firstFew, after: $startWith) {
                        totalCount
                        pageInfo {
                            hasNextPage
                            hasPreviousPage
                            endCursor
                            startCursor
                        }
                        nodes {
                           # ...issueFields - malformed on purpose so that the query will fail
                            ...issueField
                        }

                    }
                }
        }
    }
        """
    query_string = query_string + fragment_issue_fields_on_issue()
    qry = {
        "query_str": query_string,
        "has_next_page_path": ["repository", "pullRequest", "closingIssuesReferences", "pageInfo", "hasNextPage"],
        "start_with_path": ["repository", "pullRequest", "closingIssuesReferences", "pageInfo", "endCursor"],
        "query_vars": {
            "loginOrg": "IQSS",
            "repo": "dataverse",
            "number": '',
            "firstFew": 100,
            "startWith": ""
            }
        }
    return qry

def query_get_one_pr():
    # =================================================================
    # get the associated issue information: number, labels, title for a single pull request
    # =================================================================
    # return values. These are hardcoded by you when you create the query.
    #
    # "query_str": query_string
    # "has_next_page_path": This is the check for the next page of data formatted specifically for this query
    # "start_with_path": This is the path for the next page of data formatted specifically for this query
    #  "query_vars": These are the variables that are required internally for the query to run
    #       "loginOrg": "IQSS"
    #       "repo": "dataverse"
    #       "number": 1234 - Pull request number. Required.
    #       "firstFew": 100 - count of prs per page.  Required. Leave as 100.
    #       "startWith" - An interim variable that is used to store the cursor. Required. set to ""
    #
    # Expected results of this query:
    #
    # ---------------------------------------------------------------
    query_string = \
    """
    query ($loginOrg: String!, $repo: String!, $firstFew: Int!, $startWith: String, $number: Int!) {
        repository(followRenames:false, owner: $loginOrg, name: $repo) {
                pullRequest (number: $number) {
                    closingIssuesReferences(first: $firstFew, after: $startWith) {
                        totalCount
                        pageInfo {
                            hasNextPage
                            hasPreviousPage
                            endCursor
                            startCursor
                        }
                        nodes {
                            ...issueFields
                        }

                    }
                }
        }
    }
        """
    query_string = query_string + fragment_issue_fields_on_issue()
    qry = {
        "query_str": query_string,
        "has_next_page_path": ["repository", "pullRequest", "closingIssuesReferences", "pageInfo", "hasNextPage"],
        "start_with_path": ["repository", "pullRequest", "closingIssuesReferences", "pageInfo", "endCursor"],
        "query_vars": {
            "loginOrg": "IQSS",
            "repo": "dataverse",
            "number": '',
            "firstFew": 100,
            "startWith": ""
            }
        }
    return qry


def query_get_all_prs():
    # =================================================================
    # get a list of all prs for a given repository
    # =================================================================
    # "query_str": query_string
    # "has_next_page_path": This is the check for the next page of data formatted specifically for this query
    # "start_with_path": This is the path for the next page of data formatted specifically for this query
    #  "query_vars": These are the variables that are required internally for the query to run
    #       "loginOrg": "IQSS",
    #       "repo": "dataverse",
    #       "firstFew": 100,
    #       "startWith" - this is not used initially it's an interim variable that is used to store the cursor
    #
    # ---------------------------------------------------------------
    query_string = \
    """
    query ($loginOrg: String!, $repo: String!, $firstFew: Int, $startWith: String) {
        repository(followRenames:false, owner: $loginOrg, name: $repo) {
                id
                name
                url
                owner {
                    login
                }
                pullRequests (first: $firstFew, after: $startWith) {
                    totalCount
                    pageInfo {
                        hasNextPage
                        hasPreviousPage
                        endCursor
                        startCursor
                    }
                    nodes {
                        ...prFields
                    }
                }
        }
    }
        """
    query_string = query_string + fragment_pr_fields_on_pullrequest()
    qry = {
        "query_str": query_string,
        "has_next_page_path": ["repository", "pullRequests", "pageInfo", "hasNextPage"],
        "start_with_path": ["repository", "pullRequests", "pageInfo", "endCursor"],
        "query_vars": {
            "loginOrg": "IQSS",
            "repo": "dataverse",
            "firstFew": 100,
            "startWith": ""
            }
        }
    return qry

def fragment_pr_fields_on_pullrequest():
    # =================================================================
    # this is a query fragment used within other queries
    # =================================================================

    fragment_string = \
    """
    fragment prFields on PullRequest {
       repository {
            name
        }
        title
        number
        id
        url
        closed
        closedAt
        labels (first: 10) {
          totalCount
            nodes {
                name
            }
        }
        closingIssuesReferences (first: 20){
            totalCount
            nodes {
                number
                }

        }
    }
    """
    return fragment_string

def fragment_issue_fields_on_issue():
    # =================================================================
    # this is a query fragment used within other queries
    # =================================================================

    fragment_string = \
    """
    fragment issueFields on Issue {
        repository {
            name
        }
        title
        number
        id
        url
        closed
        closedAt
        labels (first: 100) {
          totalCount
            nodes {
                name
            }
        }
    }
    """
    return fragment_string


queries = {
    # -----------------------------------------------------------------
    # This is a global dictionary of the queries that are available.
    # Each query comes along with a data structure.
    # These are all required values.
    # The top level keys are defined within the query itself and the paired calling code GraphQLFetcher knows
    #  how to use them.  e.g. from fetch_from_repository import GraphQLFetcher
    # The query_vars entries are the external variables that are required to be set correctly for the query to run
    # here is an example:
    #     qry = {
    #     "query_str": query_string,
    #     "has_next_page_path": ["repository", "pullRequests", "pageInfo", "hasNextPage"],
    #     "start_with_path": ["repository", "pullRequests", "pageInfo", "endCursor"],
    #     "query_vars": {
    #         "loginOrg": "IQSS",
    #         "repo": "dataverse",
    #         "firstFew": 100,
    #         "startWith": ""
    #     }
    # }
    # -----------------------------------------------------------------
    'query_get_one_pr': query_get_one_pr,
    'query_get_all_prs': query_get_all_prs,
    'query_get_one_pr_malformed': query_get_one_pr_malformed

}