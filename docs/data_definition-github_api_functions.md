## Get issues associated with a single PR.

input:
- URL to an item of type PR

output:
- **A list of** issue objects as defined in the graphql schema
- For **each Issue**
   - Required:
     - URL as unique id
     - title
     - labels as a comma separated list of strings enclosed in quotes
     - state
     - **list of** project objects as defined in the graphql schema
     - For **each project**
       - Required
         - project URL as unique id
         - values of of all fields defined within that project
           - The intent of this is to make sure things like the OG Queue will be returned. See: [Decision table for comparing contents of Backlog and Sprint](https://docs.google.com/spreadsheets/d/1nOwITq9rITgg2T-RCvKB8YqtN1kSENekY0DNcIB7rF8/edit?usp=sharing)




re things like the OG Queue will be returned. See: Decision table for comparing contents of Backlog and Sprint

## Get issue by URL
input: 
- URL to an item of type Issue

output: 
- An issue object as defined in the graphql schema
- For each Issue
   - Required: 
     - URL as unique id
     - title
     - labels
     - state
     - list of project objects as defined in the graphql schema
     - For each project
       - Required
         - project URL as unique id
         - values of all fields defined within that project
           - The intent of this is to make sure things like the OG Queue will be returned. See: [Decision table for comparing contents of Backlog and Sprint](https://docs.google.com/spreadsheets/d/1nOwITq9rITgg2T-RCvKB8YqtN1kSENekY0DNcIB7rF8/edit?usp=sharing)
           
               

