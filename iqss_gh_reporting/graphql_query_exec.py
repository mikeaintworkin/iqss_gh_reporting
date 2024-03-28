
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
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
        # TODO: add more sophisticated error handling See: #50

        self._auth_token_val = auth_token_val
        self._query = gql(query_dict["query_str"])
        self._query_vars = query_dict["query_vars"]
        self._next_page_start = query_dict["next_page_start"]
        self._next_page_exists = query_dict["next_page_exists"]
        self._url = query_dict["url"]
        self._results_json = None
        self._results_dict = {}
        self.record_count=0
        self.page_count=0
        self._fetch_items()

    def _get_value_by_path(self, data, path):
        # This is really inefficent to do.
        value = data
        for key in path:
            value = value[key]
            x = 1
        return value

    def _fetch_one_set_of_pages(self, start_with=None, ):
        # input: self._auth_token_val
        # i/o: self._query_vars
        # input: self._query
        # i/o: self.record_count

        headers = {"Authorization": "Bearer " + self._auth_token_val}
        transport = AIOHTTPTransport(url=self._url, headers=headers)
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Update the query variables for pagination
        # The first time throught this must be None.
        # After that it will be the cursor starting place for this set of pages
        # startsWith Key is assumed to exist, and whatever value it had is overwritten
        self._query_vars['startWith'] = start_with

        # Execute the query
        # gql will raise an exception when it encounters a GraphQL error.
        # e.g something not found will return an exception
        try:
            data = client.execute(document=self._query, variable_values=self._query_vars)
            self.record_count  += 1

        except Exception as e:  # Catching all exceptions. Change this to more specific exceptions if needed.
            print(f"Exception: {e}")
            return {}

        self._results_dict.update(data)

    def _fetch_items(self):
        # for each page of results, get the data and add it to the results_dict
        counter = 0
        start_with = None
        while True:
            self._fetch_one_set_of_pages( start_with)

            self.page_count += 1

            if self._get_value_by_path(self._results_dict, self._next_page_exists):
                start_with = self._get_value_by_path(self._results_dict, self._next_page_start)
            else:
                break

            # print(f"Records Retrieved: {counter}. Retrieve more? {has_next_page}")

        self.results_json = json.dumps(self._results_dict, indent=4)
        return self.results_json

    def save_result_to_file(self, file_path: str = None, output_file_name: str = 'output.json'):
        outfile = file_path + "/" + output_file_name
        print(f"Saving result to file:\n{outfile}")
        if self._results_dict is None:
            raise ValueError("No result to write")

        with open(outfile, 'w') as file:
            json.dump(self._results_dict, file, indent=4)

    def print_results(self):
        if self._results_dict is None:
            raise ValueError("No result to write")
        print(f" results: \n ---- \n {json.dumps(self._results_dict, indent=4)} \n ---- \n")


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
