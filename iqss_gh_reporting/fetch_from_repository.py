
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import parse
import json


class GraphQLFetcher:
    # ==============================================================================================================
    # Run a query and return the results
    # The query is packaged with the variables that are needed to run the query
    # ==============================================================================================================
    def __init__(self, auth_token_val: str = None, query_dict: dict = None):
        # This is what the query_dict looks like:
        # It theoretically contains everything that this function will need in order to run the query
        # The information is specific to the query that is being run
        # query_dict = {
        #     "query_str": query_string,
        #     "has_next_page_path": ["repository", "pullRequests", "pageInfo", "hasNextPage"],
        #     "start_with_path": ["repository", "pullRequests", "pageInfo", "endCursor"],
        #     "query_vars": {
        #         "loginOrg": "IQSS",
        #         "repo": "dataverse",
        #         "firstFew": 100
        #         "startWith": ""
        #     }
        # }
        
        # TODO: add a check to make sure that the vars_in are correct for the query
        self._start_with_path = query_dict["start_with_path"]
        self._has_next_page_path = query_dict["has_next_page_path"]
        self._query = parse(query_dict["query_str"])
        self._query_input_params = query_dict["query_vars"]
        self._auth_token_val = auth_token_val
        self._results_json = None
        self._results_dict = {}
        self._fetch_items()

    def _get_value_by_path(self, data, path):
        value = data
        for key in path:
            value = value[key]
        return value

    def _fetch_items(self):
        has_next_page = True
        headers = {"Authorization": "Bearer " + self._auth_token_val}
        transport = AIOHTTPTransport(url='https://api.github.com/graphql', headers=headers)
        client = Client(transport=transport)

        # for each page of results, get the data and add it to the results_dict
        counter = 0
        while has_next_page:
            data = client.execute(self._query, variable_values=self._query_input_params)
            counter += 1
            self._results_dict.update(data)
            has_next_page = self._get_value_by_path(data, self._has_next_page_path)
            self._query_input_params["startWith"] = self._get_value_by_path(data, self._start_with_path)
            print(f"Records Retrieved: {counter}. Retrieve more? {has_next_page}")

        self.results_json = json.dumps(self._results_dict, indent=4)
        return self.results_json

    def save_result_to_file(self):
        print(f"Saving result to file:")
        if self._results_dict is None:
            raise ValueError("No result to write")

        with open('output.json', 'w') as file:
            json.dump(self._results_dict, file, indent=4)

    @property
    def json(self):
        return self._results_json

    @property
    def dict(self):
        return self._results_dict

    # def load_query(self):
    #     with open(self._query_file) as file:
    #         return gql(file.read())
    #
    # precond: file_path is a valid path to a file
    #        : The data looks like this:
    #          #has_next_page_path = ["organization", "projectV2", "items", "pageInfo", "hasNextPage"]
    # def read_variable_from_file(self, variable_name):
    #     with open(self._query_file, 'r') as file:
    #         for line in file:
    #             if line.startswith('#' + variable_name):
    #                 path_str = line.split('=')[1].strip()
    #                 variable_val = json.loads(path_str)
    #                 return variable_val
    #     return None
